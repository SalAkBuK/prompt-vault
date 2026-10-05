---
title: "Reference Benchmark Website Builder"
category: "creative-web-design"
tags: ["creative-web-design", "reference-analysis", "benchmark", "website-generation", "autonomous-design", "visual-quality", "agentic-iteration"]
description: "Stage 1 (Initial Build): Analyzes an exceptional reference website and builds an original website targeting the same creative and technical benchmark without copying."
version: "1.0"
---

# Reference Benchmark Website Builder

## 🎯 Overview
Use this as a first-pass / initial-build prompt when you find an exceptional reference website and want the AI agent to build an original site matching that creative and technical caliber. It establishes high ambition and autonomous self-evaluation without cloning the reference.

## 📋 Prompt
```text
Analyze **[REFERENCE WEBSITE / URL]** and build me a website for **[TOPIC / BRAND / IDEA]** which looks like something similar in terms of quality and execution, at least at that level, but don't copy it (!!).

Keep going until it reaches that level.

Rate your result using independent subagents. The score has to be above **[QUALITY THRESHOLD — e.g. 80%]**.

The website itself should be original. Do not copy the reference's exact composition, assets, branding, text, or concept.

Topic: [YOUR TOPIC]

—or, if I leave the topic blank—

Choose any topic for the website and make it look unique.
```

## 🧩 Variables & Placeholders
| Variable | Description | Example |
| :--- | :--- | :--- |
| `[REFERENCE WEBSITE / URL]` | URL or name of the benchmark site setting the bar | `https://stripe.com/press` or `Linear.app` |
| `[TOPIC / BRAND / IDEA]` | Your project topic, brand, or concept | `Artisan coffee roastery with sensory interactive guides` |
| `[QUALITY THRESHOLD — e.g. 80%]` | Target benchmark score for subagent critique | `85%` |
| `[YOUR TOPIC]` | Explicit topic fallback or specific brief | `Interactive portfolio for an architectural photographer` |

## 💡 Example
### Input
```text
Analyze https://chronicles.luxury and build me a website for a boutique kinetic sculpture studio which looks like something similar in terms of quality and execution, at least at that level, but don't copy it (!!).
```

### Expected Output
An original, high-fidelity site architecture, art direction system, and bespoke layout matching the reference's polish, pacing, and interaction fidelity while maintaining completely distinct identity, assets, and storytelling.
