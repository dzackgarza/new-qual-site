---
schema: qual/card@1
id: P-UCLARA14F-10
kind: problem
title: Completeness of the Fock space of entire functions
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
  note: Retranscribed the font-garbled statement in LaTeX from Problem 10 of the Fall 2014 section, page 73 of UCLA_Solutions.pdf, with its checked-in extraction.
---

::: {.problem}
Let us introduce a vector space $\mathcal{B}$ as follows.
\[
\mathcal{B} = \left\{ u : \mathbb{C} \to \mathbb{C} : u \text{ is holomorphic and } \iint_{\mathbb{C}} |u(x+iy)|^2 e^{-(x^2+y^2)}\,dx\,dy < \infty \right\}.
\]
Show that $\mathcal{B}$ becomes a *complete* vector space when equipped with the norm
\[
\|u\|^2 = \iint_{\mathbb{C}} |u(x+iy)|^2 e^{-(x^2+y^2)}\,dx\,dy.
\]
:::
