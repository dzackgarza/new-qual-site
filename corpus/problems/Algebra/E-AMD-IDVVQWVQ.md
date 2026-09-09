---
schema: qual/card@1
id: E-AMD-IDVVQWVQ
kind: problem
title: Every prime ideal is radical
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09

---

::: {.exercise}
Show that every prime ideal is radical.
:::

::: solution
Let $\mathfrak p$ be a prime ideal of a commutative ring $R$. The inclusion
\[
\mathfrak p\subseteq\sqrt{\mathfrak p}
\]
is immediate.

Conversely, let $x\in\sqrt{\mathfrak p}$. Then $x^n\in\mathfrak p$ for some $n\ge1$. Since
\[
x^n=x\,x^{n-1}\in\mathfrak p
\]
and $\mathfrak p$ is prime, either $x\in\mathfrak p$ or $x^{n-1}\in\mathfrak p$. Repeating this argument finitely many times gives $x\in\mathfrak p$. Hence
\[
\sqrt{\mathfrak p}\subseteq\mathfrak p.
\]
Therefore
\[
\sqrt{\mathfrak p}=\mathfrak p,
\]
so every prime ideal is radical.
:::
