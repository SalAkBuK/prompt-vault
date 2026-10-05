---
title: "Frontier Reference Benchmark Website Builder"
category: "creative-web-design"
tags: ["creative-web-design", "benchmark", "reference-analysis", "website-generation", "autonomous-design", "subagent-review", "interaction-design"]
description: "A complete benchmark-driven website building prompt combining reference quality matching, anti-cliché constraints, signature mechanics, typography tuning, and autonomous subagent scoring."
version: "1.0"
---

# Frontier Reference Benchmark Website Builder

## 🎯 Overview
Directs an AI agent to build an original website anchored to the technical and creative caliber of a reference site. Incorporates first-pass quality matching, post-v1 anti-cliché suppression, signature structural interaction, typography improvement, and iterative subagent scoring until the quality threshold is satisfied.

## 📋 Prompt
```text
Analyze [REFERENCE WEBSITE] and build me a website for [TOPIC / BRAND / IDEA] that reaches a similar level of quality and execution, but do not copy it (!!).

If [TOPIC / BRAND / IDEA] is left blank, choose any topic yourself and make the website unique.

Keep going until the result reaches that level.

After the first complete version:

No [UNWANTED DESIGN PATTERN], [UNWANTED DESIGN PATTERN], [UNWANTED DESIGN PATTERN] or [UNWANTED DESIGN PATTERN].

Add [SIGNATURE INTERACTION / STRUCTURAL IDEA].

Use [FONT / TYPEFACE] if it improves the design.

Rate your result using independent subagents. The score has to be above [QUALITY THRESHOLD — e.g. 80%].

If it falls below that level, improve it and review it again.

Then [PUBLISH / DEPLOY / CREATE ARTIFACT / LEAVE READY FOR REVIEW].
```

## 🧩 Variables & Placeholders
| Variable | Description | Example |
| :--- | :--- | :--- |
| `[REFERENCE WEBSITE]` | Quality benchmark reference URL | `igloo.inc` |
| `[TOPIC / BRAND / IDEA]` | Project concept or leave blank for agent choice | `Leave blank` |
| `[UNWANTED DESIGN PATTERN]` | Specific visual clichés to suppress after v1 | `"01/03" counters`, `eyebrow labels`, `monospace text`, `long thin lines` |
| `[SIGNATURE INTERACTION / STRUCTURAL IDEA]` | One memorable mechanical or transition idea | `An infinite scroll: a final section that morphs smoothly back into the opening scene` |
| `[FONT / TYPEFACE]` | Recommended typeface family | `Inter Variable or Geist` |
| `[QUALITY THRESHOLD — e.g. 80%]` | Target evaluation score for subagents | `80%` |
| `[PUBLISH / DEPLOY / CREATE ARTIFACT / LEAVE READY FOR REVIEW]` | Delivery action | `Publish it as an artifact` |

## 💡 Example

```text
Analyze igloo.inc and build me a website which looks like something similar, at least at that level, but don't copy it(!!)

Keep going until it reaches that level.

Rate your result using independant subagents, score has to be above 80%.

Choose any topic for the website, make it look unique.

No "01/03" counters, eyebrow labels, monospace text or long thin lines.

Add an infinite scroll: a final section that morphs smoothly back into the opening scene. Then publish it as an artifact.

Using Inter Variable or Geist here would have made the entire thing 10x better.
```
