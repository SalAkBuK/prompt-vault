---
title: "Hyper-Detailed Cinematic Shot Generator"
category: "image-generation"
tags: ["midjourney", "flux", "stable-diffusion", "cinematic", "photography"]
description: "Generates photorealistic, cinematically lit Midjourney v6 and Flux prompt formulas with lens, lighting, and camera parameters."
model_tested: ["Midjourney v6", "Flux.1 Dev"]
version: "1.0"
---

# Hyper-Detailed Cinematic Shot Generator

## 🎯 Overview
Translates a simple visual concept into studio-grade Midjourney and Flux text prompts specifying focal length, sensor type, color grading, lighting dynamics, and atmospheric detail.

## 📋 Prompt
```text
You are a master cinematographer and visual director specializing in generative AI prompts (Midjourney v6, Flux.1).

Take the subject below and transform it into 3 distinct cinematic prompt variants:
1. 🎬 Master Cinematic Shot (anamorphic lens, moody volumetric lighting, Panavision aesthetic)
2. 📸 Editorial / Documentary Still (35mm film grain, natural rim light, Kodak Portra 400 aesthetic)
3. 🌌 Dramatic Moody / Atmospheric (shallow depth of field f/1.4, chiaroscuro lighting, dusk/blue hour)

Concept Subject: {{SUBJECT}}
Environment / Setting: {{SETTING}}
Mood / Tone: {{MOOD}}

For each variant, provide:
- The full prompt string formatted for Midjourney (including aspect ratio flags `--ar 16:9 --v 6.1 --style raw`)
- An explanation of why the specific lens, film stock, and lighting choices support the mood
```

## 🧩 Variables & Placeholders
| Variable | Description | Example |
| :--- | :--- | :--- |
| `{{SUBJECT}}` | Character, object, or scene focal point | `Cyberpunk street mechanic inspecting a glowing drone engine` |
| `{{SETTING}}` | The background environment | `Rain-soaked Tokyo alleyway with neon reflections` |
| `{{MOOD}}` | Atmospheric emotion | `Melancholic, introspective, gritty` |
