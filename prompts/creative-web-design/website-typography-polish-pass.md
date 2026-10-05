---
title: "Website Typography Polish Pass"
category: "creative-web-design"
tags: ["creative-web-design", "typography", "design-polish", "visual-hierarchy", "refinement", "ui-typography"]
description: "Stage 4 (Final Polish): Elevates perceived visual quality by replacing generic fonts with an intentional typographic system retuned across hierarchy, tracking, and sizing."
model_tested: ["Claude 3.5 Sonnet", "GPT-4o"]
version: "1.0"
---

# Website Typography Polish Pass

## 🎯 Overview
Use this during the final polish stage when the site's visual concept and interactions are strong, but the typography is lowering perceived quality. Rather than a superficial font swap, it directs a holistic retuning of weights, tracking, line heights, and hierarchy.

## 📋 Prompt
```text
Replace the current typography with **[FONT / TYPEFACE]** and retune the type system around it.

Do not merely swap the font file.

Reconsider:

- font weights
- tracking
- line-height
- hierarchy
- sizing
- responsive behavior
- relationships between display and body text

The typography should feel intentional within the current design rather than added on top of it.

Preserve the site's existing visual concept and interaction system unless typography requires a small supporting adjustment.
```

## 🧩 Variables & Placeholders
| Variable | Description | Example |
| :--- | :--- | :--- |
| `[FONT / TYPEFACE]` | Primary typeface or pairing to introduce | `Instrument Serif for headlines and Plus Jakarta Sans for body` |

## 💡 Example
### Input
```text
Replace the current typography with Cormorant Garamond display paired with Inter body, and retune the type system around it.
```

### Expected Output
Refined CSS typography rules with fluid clamp sizing, proportional line-heights, letter-spacing adjustments for uppercase tracking, and balanced contrast between headlines and body copy.
