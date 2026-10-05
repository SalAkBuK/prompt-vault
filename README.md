# ⚡ Prompt Vault

> A clean, battle-tested personal repository for storing, categorizing, searching, and 1-click copying your AI prompts across ChatGPT, Claude, Gemini, Midjourney, and Flux.

[![Prompts Count](https://img.shields.io/badge/Prompts-8-blue.svg)](#-master-prompt-catalog)
[![Categories](https://img.shields.io/badge/Categories-2-brightgreen.svg)](#-categories)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🌟 Why This Repo?

- 📁 **Organized by Category**: No more lost prompts across random notes or messy chat history.
- ⚡ **Zero-Dependency CLI (`vault.py`)**: Search, create, and copy prompts directly to your system clipboard from terminal.
- 🌐 **Interactive Web Gallery (`index.html`)**: Instant dark-mode browser dashboard with live filtering, tag search, and 1-click copy.
- 📋 **Standardized Template**: Consistent structure with tags, variables (`{{INPUT}}`), and versioning.
- 🔄 **Auto-Updating Catalog**: Run one command to regenerate the master table of contents and JSON catalog.

---

## 📁 Repository Structure

```text
delightful-curie/
├── index.html                   # 🌐 Visual browser dashboard with 1-click copy
├── vault.py                     # ⚡ Zero-dependency Python CLI
├── template.md                  # 📄 Reusable prompt template
├── CATALOG.md                   # 📚 Auto-generated master prompt catalog
├── prompts.json                 # 💾 JSON dump for tools & web UI
└── prompts/                     # 📂 Categorized prompt storage
    ├── creative-web-design/     # Reference benchmarks, anti-cliché cleanup, interactions, typography
    └── video-production/        # Programmatic launch films, motion timing, audio drops
```

---

## 🚀 Quick Start (CLI Guide)

The built-in `vault.py` works out of the box with Python 3.8+ (no `pip install` required).

### 1. Browse All Prompts
```bash
python vault.py list
```

### 2. Search by Keyword or Tag
```bash
python vault.py search "creative web"
python vault.py search "typography"
python vault.py search "launch film"
```

### 3. Copy Prompt Directly to Clipboard
Finds the prompt by name or keyword, extracts the prompt block, and copies it straight to your clipboard:
```bash
python vault.py copy "signature interaction"
python vault.py copy "anti-cliche"
python vault.py copy "launch film"
```
*(Now simply press `Ctrl + V` into ChatGPT, Claude, or your LLM interface!)*

### 4. Create a New Prompt from Template
```bash
python vault.py new creative-web-design "Bespoke Portfolio Animator"
```
This generates a formatted file under `prompts/<category>/<slug>.md`.

### 5. Rebuild Catalogs & Web Data
After adding or editing any prompts, run:
```bash
python vault.py build
```
This automatically updates `CATALOG.md` and `prompts.json`.

---

## 🌐 Visual Web Dashboard

Want a visual interface? 

1. Double-click or open **[`index.html`](file:///index.html)** in any browser.
2. Filter by category pills, type keywords into live search, and hit **📋 Copy** on any prompt card.

---

## 🧭 Categories & Prompts

| Category | Description | Prompts |
| :--- | :--- | :--- |
| **`creative-web-design`** | Benchmarks, anti-cliché review, signature mechanics, typography | [Frontier Reference Benchmark](prompts/creative-web-design/frontier-reference-benchmark-website-builder.md), [Reference Benchmark](prompts/creative-web-design/reference-benchmark-website-builder.md), [Anti-Cliché Review](prompts/creative-web-design/anti-cliche-website-design-review.md), [Signature Interaction](prompts/creative-web-design/signature-website-interaction-designer.md), [Typography Polish](prompts/creative-web-design/website-typography-polish-pass.md), [Cinematic Scroll](prompts/creative-web-design/cinematic-scroll-image-sequence.md), [Scroll-Driven Image Sequence](prompts/creative-web-design/scroll-driven-image-sequence-website.md) |
| **`video-production`** | Launch films, motion design, audio drops, QA stills | [Programmatic Product Launch Film](prompts/video-production/programmatic-product-launch-film.md) |

For the full detailed index, see **[`CATALOG.md`](file:///CATALOG.md)**.

---

## 📝 How to Add Your Own Prompts

1. Run:
   ```bash
   python vault.py new <category-name> "<Your Prompt Title>"
   ```
2. Open the created file in your editor (e.g. in `prompts/<category-name>/...md`).
3. Fill in:
   - Frontmatter tags & description
   - The prompt text inside the fenced code block
   - Any variables (`{{VARIABLE_NAME}}`)
4. Rebuild the catalog:
   ```bash
   python vault.py build
   ```
5. Commit and push:
   ```bash
   git add .
   git commit -m "Add new prompt: <Your Prompt Title>"
   git push
   ```

---

## 📄 License
MIT License. Free to use, adapt, and share.
