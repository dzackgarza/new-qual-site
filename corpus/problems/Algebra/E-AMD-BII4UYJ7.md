---
schema: qual/card@1
id: E-AMD-BII4UYJ7
kind: problem
title: Prime ideals are primary
classification:
  areas:
  - algebra
  topics:
  - Primary Decomposition
  - Prime Ideals
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that every prime ideal is primary.
:::

::: {.solution}
Let \(\mathfrak p\) be a prime ideal. If
\[
ab\in\mathfrak p,
\]
then primality gives
\[
a\in\mathfrak p\quad\text{or}\quad b\in\mathfrak p.
\]
In the second case \(b^1\in\mathfrak p\). Thus whenever \(ab\in\mathfrak p\), either \(a\in\mathfrak p\) or \(b^n\in\mathfrak p\) for some \(n\ge1\), which is exactly the definition of a primary ideal.

Therefore every prime ideal is primary.
:::
