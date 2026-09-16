---
schema: qual/card@1
id: P-TIE-F09-13
kind: problem
title: Entire functions omitting an open set are constant; Parseval's identity and Liouville's theorem
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2009, question 13.
---

::: {.problem}
Let $f ( z )$ be entire and assume values of $f ( z )$ lie outside a bounded open set Ω. Show without using Picard’s theorems that $f ( z )$ is a constant.

(1) Assume $f ( z ) = \sum _ { n = 0 } ^ { \infty } c _ { n } z ^ { n }$ converges in $| z | < R$ . Show that for $r < R ,$

$$
\frac { 1 } { 2 \pi } \int _ { 0 } ^ { 2 \pi } | f ( r e ^ { i \theta } ) | ^ { 2 } d \theta = \sum _ { n = 0 } ^ { \infty } | c _ { n } | ^ { 2 } r ^ { 2 n } .
$$

(2) Deduce Liouville’s theorem from (1).
:::
