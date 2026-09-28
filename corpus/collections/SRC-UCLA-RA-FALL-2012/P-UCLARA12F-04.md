---
schema: qual/card@1
id: P-UCLARA12F-04
kind: problem
title: Supremum growth of Fourier partial sums
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Fall 2012 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Fix $f\in C(\mathbb T)$, where $\mathbb T=\mathbb R/(2\pi\mathbb Z)$, and let $s_n$ denote the $n$th partial sum of the Fourier series of $f$.
Prove that
\[
\lim_{n\to\infty}\frac{\|s_n\|_{L^\infty(\mathbb T)}}{\log n}=0.
\]
:::
