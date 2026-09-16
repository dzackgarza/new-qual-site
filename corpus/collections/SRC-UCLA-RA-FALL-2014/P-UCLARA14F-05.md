---
schema: qual/card@1
id: P-UCLARA14F-05
kind: problem
title: Density of a pushforward under a nonsingular continuous map
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
  note: Retranscribed the font-garbled statement in LaTeX from Problem 5 of the Fall 2014 section, page 71 of UCLA_Solutions.pdf, with its checked-in extraction.
---

::: {.problem}
Let $\phi : [0,1] \to [0,1]$ be continuous and let $d\mu$ be a Borel probability measure on $[0,1]$. Suppose $\mu(\phi^{-1}(E)) = 0$ for every Borel set $E \subseteq [0,1]$ with $\mu(E) = 0$. Show that there is a Borel measurable function $w : [0,1] \to [0,\infty)$ so that
\[
\int f \circ \phi(x)\,d\mu(x) = \int f(y) w(y)\,d\mu(y)
\]
for all continuous $f : [0,1] \to \mathbb{R}$.
:::
