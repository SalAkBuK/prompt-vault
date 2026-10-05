---
title: "High-Converting Landing Page Copy (PAS Framework)"
category: "writing-copywriting"
tags: ["copywriting", "landing-page", "conversion", "sales", "pas-formula"]
description: "Generates high-converting hero sections, value propositions, and CTA copy using the Problem-Agitate-Solve framework."
model_tested: ["Claude 3.5 Sonnet", "GPT-4o"]
version: "1.0"
---

# High-Converting Landing Page Copy (PAS Framework)

## 🎯 Overview
Constructs persuasive, benefit-driven SaaS or product landing page copy that hooks readers, speaks directly to their deep pain points, and compels them to convert.

## 📋 Prompt
```text
You are a world-class direct response copywriter specializing in B2B SaaS and high-ticket digital products.

Using the PAS (Problem - Agitate - Solution) framework, write landing page copy for the following product:
- Product Name: {{PRODUCT_NAME}}
- Target Audience: {{AUDIENCE}}
- Core Problem Solved: {{CORE_PROBLEM}}
- Unique Value Proposition (UVP): {{UVP}}

Please generate the following structured sections:
1. 💥 Hero Section:
   - Compelling H1 (under 10 words, benefit-driven, no buzzwords)
   - Supporting Subheadline (clarifying what it is, who it is for, and the payoff)
   - Primary Call To Action (action-oriented button text)
   - Social Proof / Trust Badge micro-copy
2. 🔥 The Pain (Problem & Agitation):
   - 3 bullet points showing deep empathy with their current painful status quo
   - The hidden cost of doing nothing
3. ✨ The Transformation (Solution):
   - 3 distinct feature-to-benefit translations ("Feature X -> so you can achieve Outcome Y without Friction Z")
4. 🛡️ Risk Reversal:
   - Guarantees, free tier reassurance, or objection handling snippet
5. 🚀 Final CTA Section:
   - Urgency or closure headline + secondary CTA
```

## 🧩 Variables & Placeholders
| Variable | Description | Example |
| :--- | :--- | :--- |
| `{{PRODUCT_NAME}}` | The name of your product or service | `PulseMetrics` |
| `{{AUDIENCE}}` | The exact niche or ideal customer profile | `Bootstrapped SaaS founders with 10k-100k MRR` |
| `{{CORE_PROBLEM}}` | What keeps them awake at night | `Drowning in customer churn without knowing why users leave` |
| `{{UVP}}` | How your tool solves it uniquely | `Predicts churn 14 days before cancellation using AI event patterns` |
