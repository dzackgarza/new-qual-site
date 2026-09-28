---
schema: qual/card@1
id: P-UCLARA15F-02
kind: problem
title: Almost everywhere convergence of $\sum_n\int_n^{n+n^{-a}}|f(x+y)|\,dy$ for $f\in L^p$
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the retained UCLA Analysis Qualifying Exam Solutions compendium, Fall 2015 section; the official exam PDF is image-only.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retranscribed the font-garbled statement in LaTeX from Problem 2 on page 1 of the official analysis-15F.pdf exam, checked against the Fall 2015 section of UCLA_Solutions.pdf.
---

::: {.problem}
Let $f \in L^p(\mathbb{R})$, $1 < p < \infty$, and let $a \in \mathbb{R}$ be such that $a > 1 - \frac{1}{p}$. Show that the series
\[
\sum_{n=1}^{\infty} \int_n^{n+n^{-a}} |f(x+y)|\,dy
\]
converges for almost all $x \in \mathbb{R}$.
:::
