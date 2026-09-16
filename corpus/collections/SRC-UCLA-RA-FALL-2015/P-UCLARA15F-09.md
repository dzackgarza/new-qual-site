---
schema: qual/card@1
id: P-UCLARA15F-09
kind: problem
title: Normal families in a Gaussian-weighted $L^2$ space of entire functions
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
  note: Retranscribed the font-garbled statement in LaTeX from Problem 9 on page 2 of the official analysis-15F.pdf exam, checked against the Fall 2015 section of UCLA_Solutions.pdf.
---

::: {.problem}
Let $(f_j)$ be a sequence of entire functions such that, writing $z = x + iy$, we have
\[
\iint_{\mathbb{C}} |f_j(z)|^2 e^{-|z|^2}\,dx\,dy \leq C, \quad j = 1, 2, \ldots,
\]
for some constant $C > 0$. Show that there exists a subsequence $(f_{j_k})$ and an entire function $f$ such that we have
\[
\iint_{\mathbb{C}} |f_{j_k}(z) - f(z)|^2 e^{-2|z|^2}\,dx\,dy \to 0, \quad k \to \infty.
\]
:::
