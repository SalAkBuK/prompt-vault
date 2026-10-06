#!/usr/bin/env python3
"""
Prompt Vault CLI
Zero-dependency utility to browse, search, create, copy, and catalog prompts.
"""

import sys
import os
import re
import argparse
import subprocess
from pathlib import Path

# Fix Windows console encoding for Unicode emojis
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

BASE_DIR = Path(__file__).parent.resolve()
PROMPTS_DIR = BASE_DIR / "prompts"
TEMPLATE_FILE = BASE_DIR / "template.md"
CATALOG_FILE = BASE_DIR / "CATALOG.md"


def parse_frontmatter(file_content: str) -> tuple[dict, str]:
    """Extract YAML-like frontmatter and body from markdown content."""
    meta = {}
    body = file_content
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", file_content, re.DOTALL)
    if match:
        raw_meta = match.group(1)
        body = match.group(2)
        for line in raw_meta.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if ":" in line:
                key, val = line.split(":", 1)
                key = key.strip()
                val = val.strip()
                # Remove inline comment if present
                if " #" in val and not (val.startswith('"') or val.startswith("'")):
                    val = val.split(" #", 1)[0].strip()
                # Parse lists: ["a", "b"]
                if val.startswith("[") and val.endswith("]"):
                    items = [
                        item.strip().strip('"').strip("'")
                        for item in val[1:-1].split(",")
                        if item.strip()
                    ]
                    meta[key] = items
                else:
                    meta[key] = val.strip('"').strip("'")
    return meta, body


def get_all_prompts() -> list[dict]:
    """Retrieve metadata and paths for all prompt files."""
    prompts = []
    if not PROMPTS_DIR.exists():
        return prompts

    for md_path in PROMPTS_DIR.rglob("*.md"):
        if md_path.name.startswith("."):
            continue
        try:
            content = md_path.read_text(encoding="utf-8")
        except Exception:
            continue

        meta, body = parse_frontmatter(content)
        category = md_path.parent.name
        rel_path = md_path.relative_to(BASE_DIR).as_posix()
        images = meta.get("images", [])
        if isinstance(images, str):
            if images.startswith("[") and images.endswith("]"):
                images = [x.strip().strip('"').strip("'") for x in images[1:-1].split(",") if x.strip()]
            else:
                images = [images] if images.strip() else []
        elif not isinstance(images, list):
            images = []
        if not images and meta.get("image"):
            images = [meta["image"]]
        image = images[0] if images else meta.get("image", "")

        prompts.append({
            "path": md_path,
            "rel_path": rel_path,
            "category": meta.get("category", category),
            "title": meta.get("title", md_path.stem.replace("-", " ").title()),
            "tags": meta.get("tags", []),
            "description": meta.get("description", ""),
            "version": meta.get("version", "1.0"),
            "video": meta.get("video", ""),
            "image": image,
            "images": images,
            "body": body,
            "content": content,
        })
    prompts.sort(key=lambda x: (x["category"], x["title"]))
    return prompts


def extract_section(body: str, header_pattern: str) -> str:
    """Extract content under a level 2 header matching header_pattern, stopping before next level 1 or 2 header."""
    pattern = rf"##\s*{header_pattern}\s*\n(.*?)(?=\n#{{1,2}}\s+|$)"
    match = re.search(pattern, body, re.DOTALL)
    return match.group(1).strip() if match else ""


def extract_fenced_code(text: str) -> str:
    """Extract the first fenced code block from markdown text, or return empty string."""
    match = re.search(r"```(?:\w+)?\s*\n(.*?)\n```", text, re.DOTALL)
    return match.group(1).strip() if match else ""


def extract_prompt_code(body: str) -> str:
    """Extract code block under ## 📋 Prompt, or fallback to sensible text."""
    prompt_section = extract_section(body, r"📋\s*Prompt")
    target = prompt_section if prompt_section else body

    # Look for fenced code block ```text ... ``` or ``` ... ```
    code = extract_fenced_code(target)
    if code:
        return code
    return target.strip()


def copy_to_clipboard(text: str) -> bool:
    """Copy text to clipboard cross-platform without external packages."""
    if sys.platform == "win32":
        try:
            # clip.exe expects utf-16le or local encoding on Windows
            p = subprocess.Popen(["clip"], stdin=subprocess.PIPE, shell=True)
            p.communicate(input=text.encode("utf-16le"))
            return p.returncode == 0
        except Exception:
            pass

        try:
            cmd = ["powershell", "-NoProfile", "-Command", "$input | Set-Clipboard"]
            p = subprocess.Popen(cmd, stdin=subprocess.PIPE, text=True, encoding="utf-8")
            p.communicate(input=text)
            return p.returncode == 0
        except Exception:
            return False
    elif sys.platform == "darwin":
        try:
            p = subprocess.Popen(["pbcopy"], stdin=subprocess.PIPE, text=True, encoding="utf-8")
            p.communicate(input=text)
            return p.returncode == 0
        except Exception:
            return False
    else:
        # Linux xclip / xsel
        for tool in [["xclip", "-selection", "clipboard"], ["xsel", "--clipboard", "--input"]]:
            try:
                p = subprocess.Popen(tool, stdin=subprocess.PIPE, text=True, encoding="utf-8")
                p.communicate(input=text)
                if p.returncode == 0:
                    return True
            except Exception:
                continue
    return False


def cmd_list(args):
    """List all prompts grouped by category."""
    prompts = get_all_prompts()
    if not prompts:
        print("No prompts found in 'prompts/' directory.")
        return

    categories = {}
    for p in prompts:
        categories.setdefault(p["category"], []).append(p)

    print(f"\n📂 PROMPT VAULT ({len(prompts)} total prompts in {len(categories)} categories)\n" + "=" * 60)
    for cat, items in categories.items():
        print(f"\n📁 [{cat.upper()}] ({len(items)} prompts)")
        for item in items:
            tags = ", ".join(item["tags"]) if isinstance(item["tags"], list) else str(item["tags"])
            tag_str = f" [{tags}]" if tags else ""
            print(f"  • {item['title']}{tag_str}")
            print(f"    Path: {item['rel_path']}")
            if item["description"]:
                print(f"    Info: {item['description']}")
    print("\n" + "=" * 60 + "\nTip: Run `python vault.py copy <name>` to copy prompt directly to clipboard!\n")


def cmd_search(args):
    """Search prompts by keyword."""
    query = args.query.lower().strip()
    prompts = get_all_prompts()
    matches = []
    query_tokens = [t for t in re.split(r"[\s\-_]+", query) if t]

    for p in prompts:
        tags_str = " ".join(p["tags"]).lower() if isinstance(p["tags"], list) else str(p["tags"]).lower()
        searchable = f"{p['title'].lower()} {p['category'].lower()} {tags_str} {p['description'].lower()} {p['content'].lower()}"
        searchable_norm = searchable.replace("-", " ")
        if query in searchable or query in searchable_norm or (query_tokens and all(t in searchable_norm for t in query_tokens)):
            matches.append(p)

    if not matches:
        print(f"No prompts found matching '{args.query}'.")
        return

    print(f"\n🔍 Search Results for '{args.query}' ({len(matches)} found):\n" + "-" * 60)
    for p in matches:
        tags = ", ".join(p["tags"]) if isinstance(p["tags"], list) else str(p["tags"])
        print(f"\n• {p['title']} [{p['category']}]")
        print(f"  Tags: {tags}")
        print(f"  Path: {p['rel_path']}")
        if p["description"]:
            print(f"  Desc: {p['description']}")
    print("\n" + "-" * 60)


def cmd_new(args):
    """Create a new prompt from template."""
    category = args.category.strip().lower().replace(" ", "-")
    title = args.title.strip()
    slug = re.sub(r"[^\w\-_]", "", title.lower().replace(" ", "-"))

    cat_dir = PROMPTS_DIR / category
    cat_dir.mkdir(parents=True, exist_ok=True)
    target_path = cat_dir / f"{slug}.md"

    if target_path.exists():
        print(f"❌ Error: File already exists at {target_path}")
        return

    template_content = ""
    if TEMPLATE_FILE.exists():
        template_content = TEMPLATE_FILE.read_text(encoding="utf-8")
        template_content = template_content.replace('"Prompt Title Here"', f'"{title}"')
        template_content = template_content.replace('# Prompt Title Here', f'# {title}')
        template_content = template_content.replace('category: "coding"', f'category: "{category}"')
    else:
        template_content = f"""---
title: "{title}"
category: "{category}"
tags: []
description: "Brief description of this prompt."
version: "1.0"
---

# {title}

## 🎯 Overview
Describe what this prompt does.

## 📋 Prompt
```text
Enter your prompt here...
```

## 🧩 Variables & Placeholders
| Variable | Description | Example |
| :--- | :--- | :--- |
| `{{{{INPUT}}}}` | Input data | `Example` |
"""

    target_path.write_text(template_content, encoding="utf-8")
    rel_path = target_path.relative_to(BASE_DIR).as_posix()
    print(f"✅ Created new prompt: {title}")
    print(f"📄 File: {rel_path}")
    print(f"💡 Edit your new prompt now, then run `python vault.py build` to update the catalog!")


def find_best_match(query: str, prompts: list[dict]) -> dict | None:
    """Find prompt by exact path, title, substring, or token matching."""
    query_clean = query.strip().lower()
    if not query_clean:
        return None

    # 1. Exact rel_path or stem match
    for p in prompts:
        if query_clean in (p["rel_path"].lower(), p["path"].name.lower(), p["path"].stem.lower()):
            return p

    # 2. Exact title match
    for p in prompts:
        if query_clean == p["title"].lower():
            return p

    # 3. Substring in title or filename
    for p in prompts:
        if query_clean in p["title"].lower() or query_clean in p["path"].stem.lower():
            return p

    # 4. Token subset match (all words in query exist in title + path + tags)
    query_tokens = [t for t in re.split(r"\s+", query_clean) if t]
    best_candidate = None
    best_score = 0

    for p in prompts:
        tags_str = " ".join(p["tags"]).lower() if isinstance(p["tags"], list) else ""
        combined = f"{p['title'].lower()} {p['path'].stem.lower()} {tags_str}"
        matches = sum(1 for t in query_tokens if t in combined)
        if matches == len(query_tokens):
            return p  # All tokens matched
        if matches > best_score:
            best_score = matches
            best_candidate = p

    if best_score > 0 and (best_score / len(query_tokens)) >= 0.5:
        return best_candidate

    return None


def cmd_copy(args):
    """Extract prompt text (or example if --example specified) and copy it to clipboard."""
    prompts = get_all_prompts()
    p = find_best_match(args.target, prompts)
    if not p:
        print(f"❌ Could not find a prompt matching '{args.target}'. Try `python vault.py list` or `search`.")
        return

    is_example = getattr(args, "example", False)
    if is_example:
        example_sec = extract_section(p["body"], r"💡\s*Example")
        target_text = extract_fenced_code(example_sec) or example_sec
        label = "Example"
    else:
        target_text = extract_prompt_code(p["body"])
        label = "Prompt"

    if not target_text:
        print(f"⚠️ No {label.lower()} found for '{p['title']}'.")
        return

    copied = copy_to_clipboard(target_text)

    print(f"\n📋 Selected {label}: {p['title']} ({p['rel_path']})")
    print("-" * 50)
    print(target_text[:300] + ("\n... [truncated for display]" if len(target_text) > 300 else ""))
    print("-" * 50)

    if copied:
        print(f"✨ SUCCESS: {label} text copied to your clipboard! Ready to paste.")
    else:
        print("⚠️ Notice: Could not access system clipboard automatically. Copy the text displayed above.")


def cmd_view(args):
    """View full prompt markdown."""
    prompts = get_all_prompts()
    p = find_best_match(args.target, prompts)
    if not p:
        print(f"❌ Could not find a prompt matching '{args.target}'.")
        return

    print(f"\n=== {p['title']} [{p['rel_path']}] ===\n")
    print(p["content"])


def cmd_build(args=None):
    """Rebuild CATALOG.md, prompts.json, and sync index.html embedded data."""
    prompts = get_all_prompts()
    categories = {}
    for p in prompts:
        categories.setdefault(p["category"], []).append(p)

    lines = [
        "# 📚 Master Prompt Catalog",
        "",
        f"> Auto-generated index of all **{len(prompts)} prompts** across **{len(categories)} categories**.",
        "> Update anytime with `python vault.py build`.",
        "",
        "## 🧭 Quick Jump",
        "",
    ]

    if categories:
        for cat in sorted(categories.keys()):
            count = len(categories[cat])
            display_name = cat.replace("-", " ").title()
            anchor = cat.lower().replace(" ", "-")
            lines.append(f"- [{display_name}](#{anchor}) `({count})`")
    else:
        lines.append("*(No prompts in vault yet. Run `python vault.py new <category> \"<Title>\"` to add your first prompt!)*")

    lines.append("")
    lines.append("---")
    lines.append("")

    for cat in sorted(categories.keys()):
        items = categories[cat]
        display_name = cat.replace("-", " ").title()
        lines.append(f"## {display_name}")
        lines.append("")
        lines.append("| Title | Tags | File |")
        lines.append("| :--- | :--- | :--- |")

        for item in items:
            title = item["title"]
            rel_link = f"[{item['path'].name}]({item['rel_path']})"
            tags = " ".join([f"`{t}`" for t in item["tags"]]) if isinstance(item["tags"], list) else f"`{item['tags']}`"
            lines.append(f"| **{title}**<br>*{item['description']}* | {tags or '-'} | {rel_link} |")

        lines.append("")

    catalog_text = "\n".join(lines)
    CATALOG_FILE.write_text(catalog_text, encoding="utf-8")

    # Build rich JSON catalog for web UI / programmatic use
    import json
    json_path = BASE_DIR / "prompts.json"
    clean_prompts = []
    for p in prompts:
        body = p["body"]
        prompt_sec = extract_section(body, r"📋\s*Prompt")
        prompt_code = extract_fenced_code(prompt_sec) if prompt_sec else ""
        if not prompt_code:
            prompt_code = extract_fenced_code(body) or body.strip()

        example_sec = extract_section(body, r"💡\s*Example")
        example_code = extract_fenced_code(example_sec) if example_sec else ""

        overview = extract_section(body, r"🎯\s*Overview") or p["description"]
        variables = extract_section(body, r"🧩\s*Variables & Placeholders")

        clean_prompts.append({
            "slug": p["path"].stem,
            "title": p["title"],
            "category": p["category"],
            "tags": p["tags"],
            "description": p["description"],
            "version": p["version"],
            "overview": overview,
            "prompt": prompt_code,
            "variables": variables,
            "example": example_sec,
            "example_code": example_code,
            "video": p.get("video", ""),
            "image": p.get("image", ""),
            "images": p.get("images", ([p["image"]] if p.get("image") else [])),
            "rel_path": p["rel_path"],
        })

    json_str = json.dumps(clean_prompts, indent=2, ensure_ascii=False)
    json_path.write_text(json_str, encoding="utf-8")

    # Also update embedded dataset in index.html if it exists
    index_path = BASE_DIR / "index.html"
    if index_path.exists():
        index_content = index_path.read_text(encoding="utf-8")
        # Escape < and > so strings containing </script> in prompts do not break HTML tokenizer
        safe_embedded_json = json_str.replace("<", "\\u003c").replace(">", "\\u003e")
        start_tag = '<script id="prompts-data" type="application/json">'
        end_tag = '</script>\n\n  <script>'
        start_pos = index_content.find(start_tag)
        end_pos = index_content.find(end_tag)
        if start_pos != -1 and end_pos != -1:
            new_index = (
                index_content[:start_pos + len(start_tag)]
                + "\n"
                + safe_embedded_json
                + "\n  "
                + index_content[end_pos:]
            )
            index_path.write_text(new_index, encoding="utf-8")

    print(f"✅ Generated {CATALOG_FILE.name} and {json_path.name} with {len(prompts)} prompts across {len(categories)} categories.")



def cmd_serve(args):
    """Start local server with web GUI and auto-saving API."""
    import http.server
    import socketserver
    import urllib.parse
    import json

    port = getattr(args, "port", 3000) or 3000

    class VaultHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *a, **kw):
            super().__init__(*a, directory=str(BASE_DIR), **kw)

        def do_POST(self):
            parsed = urllib.parse.urlparse(self.path)
            if parsed.path == "/api/save-prompt":
                content_len = int(self.headers.get("Content-Length", 0))
                post_data = self.rfile.read(content_len)
                try:
                    payload = json.loads(post_data.decode("utf-8"))
                    category = payload.get("category", "general").strip().lower().replace(" ", "-")
                    title = payload.get("title", "").strip()
                    if not title:
                        raise ValueError("Title is required")

                    slug = payload.get("slug") or re.sub(r"[^\w\-_]", "", title.lower().replace(" ", "-"))
                    cat_dir = PROMPTS_DIR / category
                    cat_dir.mkdir(parents=True, exist_ok=True)
                    target_path = cat_dir / f"{slug}.md"

                    tags = payload.get("tags", [])
                    if isinstance(tags, str):
                        tags = [t.strip() for t in tags.split(",") if t.strip()]

                    description = payload.get("description", "").strip()
                    prompt_text = payload.get("prompt", "").strip()
                    example_text = payload.get("example", "").strip()
                    video = payload.get("video", "").strip()
                    images = payload.get("images", [])
                    if isinstance(images, str):
                        images = [t.strip() for t in images.split(",") if t.strip()]
                    elif not isinstance(images, list):
                        images = []
                    image = payload.get("image", "").strip()
                    if not image and images:
                        image = images[0]
                    if not images and image:
                        images = [image]

                    frontmatter_lines = [
                        "---",
                        f'title: "{title}"',
                        f'category: "{category}"',
                        f'tags: {json.dumps(tags)}',
                        f'description: "{description}"',
                        'version: "1.0"',
                    ]
                    if video:
                        frontmatter_lines.append(f'video: "{video}"')
                    if images:
                        frontmatter_lines.append(f'images: {json.dumps(images)}')
                    if image:
                        frontmatter_lines.append(f'image: "{image}"')
                    frontmatter_lines.append("---\n")

                    body_sections = [
                        f"# {title}\n",
                        "## 🎯 Overview\n" + (description or "Overview of this prompt.") + "\n",
                        "## 📋 Prompt\n```text\n" + prompt_text + "\n```\n",
                    ]
                    if example_text:
                        body_sections.append("## 💡 Example\n" + example_text + "\n")

                    full_md = "\n".join(frontmatter_lines) + "\n".join(body_sections)
                    target_path.write_text(full_md, encoding="utf-8")

                    # Rebuild catalogs
                    cmd_build()

                    self.send_response(200)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps({"success": True, "slug": slug, "path": target_path.as_posix()}).encode("utf-8"))
                except Exception as err:
                    self.send_response(400)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps({"success": False, "error": str(err)}).encode("utf-8"))
            elif parsed.path in ("/api/upload-media", "/api/upload-video", "/api/upload-image"):
                try:
                    content_len = int(self.headers.get("Content-Length", 0))
                    filename = self.headers.get("X-File-Name", "reference-media")
                    filename = re.sub(r"[^\w\-_.]", "_", filename)
                    media_dir = BASE_DIR / "media"
                    media_dir.mkdir(parents=True, exist_ok=True)
                    dest = media_dir / filename
                    with open(dest, "wb") as f:
                        f.write(self.rfile.read(content_len))
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps({"success": True, "url": f"media/{filename}"}).encode("utf-8"))
                except Exception as err:
                    self.send_response(400)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps({"success": False, "error": str(err)}).encode("utf-8"))
            else:
                self.send_response(404)
                self.end_headers()

    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", port), VaultHTTPRequestHandler) as httpd:
        print(f"\n⚡ Prompt Vault Studio running at http://localhost:{port}")
        print("✨ Add prompts and video references via GUI with auto-save to disk!")
        print("Press Ctrl+C to stop.\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")


def main():
    parser = argparse.ArgumentParser(description="Prompt Vault CLI - Manage, search, and copy your AI prompts.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # list
    subparsers.add_parser("list", help="List all prompts grouped by category")

    # search
    search_parser = subparsers.add_parser("search", help="Search prompts by keyword or tag")
    search_parser.add_argument("query", help="Search keyword")

    # new
    new_parser = subparsers.add_parser("new", help="Create a new prompt file")
    new_parser.add_argument("category", help="Category folder (e.g., coding, writing, image-generation)")
    new_parser.add_argument("title", help="Prompt title")

    # copy
    copy_parser = subparsers.add_parser("copy", help="Copy a prompt directly to your clipboard")
    copy_parser.add_argument("target", help="Prompt title, keyword, or filename")
    copy_parser.add_argument("--example", "-e", action="store_true", help="Copy the real-world example instead of the template prompt")

    # view
    view_parser = subparsers.add_parser("view", help="Print full prompt markdown to terminal")
    view_parser.add_argument("target", help="Prompt title or filename")

    # build
    subparsers.add_parser("build", help="Rebuild CATALOG.md table of contents and prompts.json")

    # serve
    serve_parser = subparsers.add_parser("serve", help="Start local web studio with GUI and auto-saving API")
    serve_parser.add_argument("--port", "-p", type=int, default=3000, help="Port to run on (default: 3000)")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    cmd_map = {
        "list": cmd_list,
        "search": cmd_search,
        "new": cmd_new,
        "copy": cmd_copy,
        "view": cmd_view,
        "build": cmd_build,
        "serve": cmd_serve,
    }

    cmd_map[args.command](args)


if __name__ == "__main__":
    main()
