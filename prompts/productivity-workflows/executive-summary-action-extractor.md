---
title: "Executive Summary & Action Item Extractor"
category: "productivity-workflows"
tags: ["productivity", "summarization", "executive-summary", "action-items", "notes"]
description: "Distills lengthy reports, transcripts, or email threads into high-impact bulleted briefings with clear ownership."
model_tested: ["Claude 3.5 Sonnet", "GPT-4o", "Gemini 2.0"]
version: "1.0"
---

# Executive Summary & Action Item Extractor

## 🎯 Overview
Turns wall-of-text documents, email chains, and reports into a 30-second executive briefing with a clear Who/What/When action matrix.

## 📋 Prompt
```text
You are a Chief of Staff to an executive. Read the source text provided below and distill it into a high-signal briefing.

Format your output strictly using this structure:

1. 🎯 TL;DR (Maximum 3 sentences):
   - What happened, why it matters, and the primary conclusion.

2. 🔑 Key Takeaways & Strategic Decisions:
   - 3 to 5 bullet points capturing the core facts or decisions reached.

3. ⚠️ Risks & Blockers:
   - Any identified red flags, open questions, or dependencies.

4. 📋 Action Items Matrix:
   | Action Item | Owner | Priority (High / Med / Low) | Deadline / Status |
   | :--- | :--- | :--- | :--- |
   | [Task] | [Person / Team] | [Priority] | [Date or TBD] |

Source Text:
"""
{{SOURCE_TEXT}}
"""
```

## 🧩 Variables & Placeholders
| Variable | Description | Example |
| :--- | :--- | :--- |
| `{{SOURCE_TEXT}}` | The long text, transcript, or document | `Paste the email thread, meeting transcript, or project update here` |
