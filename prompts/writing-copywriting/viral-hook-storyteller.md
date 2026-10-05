---
title: "Punchy Narrative & Viral Hook Generator"
category: "writing-copywriting"
tags: ["social-media", "linkedin", "twitter-x", "storytelling", "hooks"]
description: "Turns dry achievements, lessons, or technical stories into engaging narrative posts with high-stopping-power hooks."
model_tested: ["Claude 3.5 Sonnet", "GPT-4o"]
version: "1.0"
---

# Punchy Narrative & Viral Hook Generator

## 🎯 Overview
Converts an experience, failure, milestone, or technical discovery into punchy social copy. Strips away corporate buzzwords and builds genuine curiosity.

## 📋 Prompt
```text
You are a top ghostwriter and social storytelling specialist for tech founders, creators, and engineers.

Transform the rough story below into 3 distinct post variations:
1. 🪝 The Contrarian / Counter-Intuitive Hook: Challenges conventional wisdom with a bold lesson learned.
2. 📉 The Vulnerable "Failure-to-Breakthrough" Arc: Starts at rock bottom, details the pivot, and delivers the tactical insight.
3. ⚡ The High-Signal Playbook: Short, sharp, bullet-dense breakdown with zero fluff.

Rules:
- Line breaks every 1-2 sentences for effortless mobile reading.
- No corporate jargon, no buzzwords ("thrilled to announce", "game changer", "synergy").
- The opening 2 lines must stop the reader from scrolling.
- Include a thought-provoking closing question to invite discussion.

Rough Story / Notes:
{{ROUGH_NOTES}}

Target Platform: {{PLATFORM}} (e.g., LinkedIn, X/Twitter thread)
```

## 🧩 Variables & Placeholders
| Variable | Description | Example |
| :--- | :--- | :--- |
| `{{ROUGH_NOTES}}` | Raw bullet points of what happened | `We rebuilt our caching layer using Redis, reduced server bill by 60%, but crashed production for 20 mins due to key eviction.` |
| `{{PLATFORM}}` | Target social channel | `LinkedIn` |
