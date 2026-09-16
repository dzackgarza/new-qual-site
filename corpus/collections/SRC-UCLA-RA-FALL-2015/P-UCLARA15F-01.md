---
schema: qual/card@1
id: P-UCLARA15F-01
kind: problem
title: Locally uniform convergence of $f*g_n$ for bounded $g_n\to0$ almost everywhere
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
  note: Retranscribed the font-garbled statement in LaTeX from Problem 1 on page 1 of the official analysis-15F.pdf exam, checked against the Fall 2015 section of UCLA_Solutions.pdf.
---

::: {.problem}
Let $g_n$ be a sequence of measurable functions on $\mathbb{R}^d$, such that $|g_n(x)| \leq 1$ for all $x$, and assume that $g_n \to 0$ almost everywhere. Let $f \in L^1(\mathbb{R}^d)$. Show that the sequence
\[
f * g_n(x) = \int f(x-y) g_n(y)\,dy \to 0
\]
uniformly on each compact subset of $\mathbb{R}^d$, as $n \to \infty$.
:::
