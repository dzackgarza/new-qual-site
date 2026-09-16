---
schema: qual/card@1
id: P-AZOFF-E08
kind: problem
title: Entire functions with $f(z)/z^n\to0$ are polynomials of degree less than $n$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Liouville, FTA, and power series, Problem 8, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md. Flash separates the limit arrow and $z\to\infty$ from the displayed quotient; the card recombines those extracted pieces without changing the mathematical statement.
---

::: problem
Suppose $f$ is entire and, for some integer $n\ge1$,
\[
\lim_{z\to\infty}\frac{f(z)}{z^n}=0.
\]
Prove that $f$ is a polynomial of degree at most $n-1$.
:::
