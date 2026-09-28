---
schema: qual/card@1
id: P-UCLAB02W-08
kind: problem
title: Rank bounds for a composition of linear maps
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 8 of the official UCLA Basic Examination, Winter 2002 PDF. The source asks for the upper bound by the maximum of the two ranks, not the sharper standard bound by their minimum.
---

::: {.problem}
Let $T:V\to W$ and $S:W\to X$ be linear maps between finite-dimensional real vector spaces.
Prove that
\[
\operatorname{rank}(T)+\operatorname{rank}(S)-\dim W
\leq
\operatorname{rank}(S\circ T)
\leq
\max\{\operatorname{rank}(T),\operatorname{rank}(S)\}.
\]

Here the rank of a linear transformation is the dimension of its image.
:::
