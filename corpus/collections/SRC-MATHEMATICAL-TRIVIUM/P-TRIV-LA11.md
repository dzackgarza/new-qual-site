---
schema: qual/card@1
id: P-TRIV-LA11
kind: problem
title: Vandermonde determinant
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 11, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: problem
Consider the Vandermonde matrix

$$
V ( x _ { 1 } , . . . , x _ { n } ) = \left[ \begin{array} { c c c c c } { { 1 } } & { { 1 } } & { { 1 } } & { { . . . } } & { { 1 } } \\ { { x _ { 1 } } } & { { x _ { 2 } } } & { { x _ { 3 } } } & { { . . . } } & { { x _ { n } } } \\ { { x _ { 1 } ^ { 2 } } } & { { x _ { 2 } ^ { 2 } } } & { { x _ { 3 } ^ { 2 } } } & { { . . . } } & { { x _ { n } ^ { 2 } } } \\ { { \vdots } } & { { \vdots } } & { { \vdots } } & { { \ddots } } & { { \vdots } } \\ { { x _ { 1 } ^ { n - 1 } } } & { { x _ { 2 } ^ { n - 1 } } } & { { x _ { 3 } ^ { n - 1 } } } & { { . . . } } & { { x _ { n } ^ { n - 1 } } } \end{array} \right] .\tag{4}
$$

(a) Calculate det $V ( x _ { 1 } , . . . , x _ { n } )$

(b) Show that det $V ( x _ { 1 } , . . . , x _ { n } ) = 0$ if and only if $x _ { i } = x _ { j }$ for some $i \neq j$
:::
