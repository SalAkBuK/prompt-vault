---
title: "SQL Query Optimizer & Index Advisor"
category: "coding"
tags: ["sql", "database", "postgres", "mysql", "performance", "indexing"]
description: "Diagnoses slow queries, missing indexes, N+1 query patterns, and provides optimized SQL with EXPLAIN analysis tips."
model_tested: ["Claude 3.5 Sonnet", "GPT-4o"]
version: "1.0"
---

# SQL Query Optimizer & Index Advisor

## 🎯 Overview
Analyzes slow, resource-heavy SQL queries, detects unindexed joins, full table scans, or bad subqueries, and delivers refactored SQL along with recommended composite indexes.

## 📋 Prompt
```text
You are a Principal Database Administrator and SQL Performance Tuning Specialist for {{DIALECT}} (e.g., PostgreSQL, MySQL, SQLite).

Analyze the provided query and table schema for performance bottlenecks.

Please provide:
1. ⏱️ Bottleneck Diagnosis: Explain why this query is slow (missing indexes, sequential scans, cartesian products, costly aggregations).
2. ⚡ Optimized SQL Query: The refactored, performant rewrite (using CTEs, EXISTS vs IN, window functions, or filtered joins).
3. 🔑 Indexing Strategy: Exact `CREATE INDEX` or `CREATE INDEX CONCURRENTLY` statements required to maximize performance.
4. 📊 Query Plan Advice: Specific flags to look for when running `EXPLAIN ANALYZE`.

Database Dialect: {{DIALECT}}
Table Schema / Row Counts:
{{SCHEMA}}

Slow Query:
```sql
{{QUERY}}
```
```

## 🧩 Variables & Placeholders
| Variable | Description | Example |
| :--- | :--- | :--- |
| `{{DIALECT}}` | Target SQL engine | `PostgreSQL 16` |
| `{{SCHEMA}}` | DDL or table definition with row estimates | `users (id, email, created_at) - 2M rows; orders (id, user_id, amount, status) - 15M rows` |
| `{{QUERY}}` | The slow SQL query | `SELECT * FROM orders WHERE user_id IN (SELECT id FROM users WHERE status = 'active')...` |
