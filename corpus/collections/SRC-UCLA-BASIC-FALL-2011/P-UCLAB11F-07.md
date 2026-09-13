---
schema: qual/card@1
id: P-UCLAB11F-07
kind: problem
title: Lower semicontinuity of matrix rank
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 7 of the retained UCLA Basic Examination, Fall 2011.
---

::: {.problem}
Problem 7. Let $f:\mathbb R\to M_{n\times n}$ be continuous, where $M_{n\times n}$ is the space of $n\times n$ matrices. Show that
\[
g(t)=\operatorname{rank}(f(t))
\]
is lower semicontinuous: if $t_k\to t$, then
\[
g(t)\le \liminf_{k\to\infty}g(t_k).
\]
Is $g$ always continuous?
:::
