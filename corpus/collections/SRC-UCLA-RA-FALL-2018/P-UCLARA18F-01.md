---
schema: qual/card@1
id: P-UCLARA18F-01
kind: problem
title: $L^1$ convergence from almost everywhere convergence with weighted $L^1$ and $L^2$ bounds
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 1. Let $\{f_n\}$ be a sequence of real-valued Lebesgue measurable functions on $\mathbb R$, and let $f$ be another such function. Assume that

1. $f_n\to f$ Lebesgue almost everywhere;
2. $\displaystyle \int_{\mathbb R}|x|\,|f_n(x)|\,dx\le100$ for all $n$;
3. $\displaystyle \int_{\mathbb R}|f_n(x)|^2\,dx\le100$ for all $n$.

Prove that $f_n\in L^1$ for all $n$, that $f\in L^1$, and that
\[
\|f_n-f\|_{L^1}\to0.
\]
Also show that neither assumption 2 nor assumption 3 can be omitted while making these deductions.
:::
