---
schema: qual/card@1
id: P-UCLARA15F-11
kind: problem
title: Phragmén--Lindelöf principle for subharmonic functions in the quadrant
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
  note: Retranscribed the font-garbled statement in LaTeX from Problem 11 on page 2 of the official analysis-15F.pdf exam, checked against the Fall 2015 section of UCLA_Solutions.pdf.
---

::: {.problem}
Let $\Omega = \{(x,y) \in \mathbb{R}^2 ; x > 0, y > 0\}$ and let $u$ be subharmonic in $\Omega$, continuous in $\overline{\Omega}$, such that
\[
u(x,y) \leq |x + iy|,
\]
for large $(x,y) \in \Omega$. Assume that
\[
u(x,0) \leq ax, \quad u(0,y) \leq by, \quad x, y \geq 0,
\]
for some $a, b > 0$. Show that
\[
u(x,y) \leq ax + by, \quad (x,y) \in \Omega.
\]
:::
