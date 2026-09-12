---
schema: qual/card@1
id: P-UCLARA14S-01
kind: problem
title: Layer-cake formula for the L1 distance
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
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Spring 2014 section.
---

::: {.problem}
Let $(X,\mathcal A,\mu)$ be a $\sigma$-finite measure space.
For $t\in\mathbb R$, let $e_t$ be the characteristic function of $(t,\infty)$.
Prove that for measurable $f,g:X\to\mathbb R$,
\[
\|f-g\|_{L^1(X)}=\int_{\mathbb R}\|e_t\circ f-e_t\circ g\|_{L^1(X)}\,dt.
\]
:::
