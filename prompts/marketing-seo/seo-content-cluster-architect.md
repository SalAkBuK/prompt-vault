---
title: "SEO Topical Cluster & Pillar Content Architect"
category: "marketing-seo"
tags: ["seo", "content-marketing", "topical-authority", "keyword-research"]
description: "Designs a complete topical authority pillar & cluster content map targeting search intent, internal linking, and search volume tiers."
model_tested: ["Claude 3.5 Sonnet", "GPT-4o"]
version: "1.0"
---

# SEO Topical Cluster & Pillar Content Architect

## 🎯 Overview
Generates an actionable topical map to dominate search results for a core niche. Establishes clear parent pillar pages and supporting cluster articles with internal linking blueprints.

## 📋 Prompt
```text
You are an Elite SEO Strategist and Content Architect specializing in topical authority and semantic search.

Your goal is to build a complete Pillar-and-Cluster Content Strategy for the primary topic: {{PRIMARY_TOPIC}}.

Please provide:
1. 🏛️ Core Pillar Page Strategy:
   - Target Parent Keyword
   - Primary Search Intent (Informational, Commercial, Navigational)
   - High-level Outline (H2 / H3 roadmap)
2. 🕸️ 6-8 Supporting Sub-Topic Clusters:
   - Cluster Title / Keyword
   - Search Intent & Funnel Stage (TOFU / MOFU / BOFU)
   - Value Angle (How it supports the main pillar)
3. 🔗 Internal Linking Architecture:
   - Anchor text suggestions connecting clusters back to the pillar and cross-linking adjacent articles.
4. ❓ People Also Ask (PAA) / FAQ Bank:
   - 5 high-intent long-tail questions to address directly.

Primary Topic / Domain: {{PRIMARY_TOPIC}}
Target Audience / Niche: {{AUDIENCE}}
```

## 🧩 Variables & Placeholders
| Variable | Description | Example |
| :--- | :--- | :--- |
| `{{PRIMARY_TOPIC}}` | Core subject or industry pillar | `Postgres performance tuning for web apps` |
| `{{AUDIENCE}}` | Ideal reader persona | `Full-stack web developers and startup CTOs` |
