---
schema: qual/card@1
id: P-UCLARA14F-04
kind: problem
title: Cosine series with $\sum(1+n^2)|c_n|^2<\infty$ form an algebra
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
  note: Transcribed from the retained UCLA Analysis Qualifying Exam Solutions compendium, Fall 2014 section; the official exam PDF is image-only.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retranscribed the font-garbled statement in LaTeX from Problem 4 on page 1 of the official analysis-14F.pdf exam, checked against the Fall 2014 section of UCLA_Solutions.pdf.
---

::: {.problem}
Given $f \in L^2([0,\pi])$, we say that $f \in \mathcal{G}$ if $f$ admits a representation of the form
\[
f(x) = \sum_{n=0}^{\infty} c_n \cos(nx) \quad \text{with} \quad \sum_{n=0}^{\infty} (1+n^2)|c_n|^2 < \infty.
\]
Show that if $f \in \mathcal{G}$ and $g \in \mathcal{G}$ then $fg \in \mathcal{G}$.
:::
