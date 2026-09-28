---
schema: qual/card@1
id: P-WESRA16-B2
kind: problem
title: '$L^\\infty$ convergence on finite-measure support implies convergence of integrals'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Group B, problem B2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md. Flash drops the convergence arrows in the final sentence; the $L^\infty$ hypothesis and two displayed integrals determine the intended convergence.
---

::: {.problem}
Let $X\subset\mathbb R^d$ be measurable with $\lambda(X)<\infty$.
Let $g,f_n$ be measurable with supports contained in $X$.
Prove that if
\[
f_n\to g\quad\text{in }L^\infty,
\]
then
\[
\int_{\mathbb R^d}f_n\to\int_{\mathbb R^d}g.
\]
:::
