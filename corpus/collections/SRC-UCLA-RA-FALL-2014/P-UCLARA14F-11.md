---
schema: qual/card@1
id: P-UCLARA14F-11
kind: problem
title: Harnack inequality for nonnegative harmonic functions
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
  note: Retranscribed the font-garbled statement in LaTeX from Problem 11 of the Fall 2014 section, page 74 of UCLA_Solutions.pdf, with its checked-in extraction.
---

::: {.problem}
Let $\Omega \subseteq \mathbb{C}$ be open, bounded, and simply connected. Let $u$ be harmonic in $\Omega$ and assume that $u \geq 0$. Show the following: for each compact set $K \subseteq \Omega$, there exists a constant $C_K > 0$ such that
\[
\sup_{x \in K} u(x) \leq C_K \inf_{x \in K} u(x).
\]
:::
