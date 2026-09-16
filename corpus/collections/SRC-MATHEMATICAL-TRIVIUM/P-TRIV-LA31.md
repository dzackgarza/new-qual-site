---
schema: qual/card@1
id: P-TRIV-LA31
kind: problem
title: Exponentials of the infinitesimal rotation generators of $SO(3)$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 31, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: problem
Define the matrix exponential $e ^ { A }$ of a matrix A as follows: $e ^ { A } \ = \ \sum _ { n = 0 } ^ { \infty } { \frac { A ^ { n } } { n ! } }$ Consider the following matrices

$$
M _ { x } = { \left[ \begin{array} { l l l } { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { - 1 } \\ { 0 } & { 1 } & { 0 } \end{array} \right] } , M _ { y } = { \left[ \begin{array} { l l l } { 0 } & { 0 } & { 1 } \\ { 0 } & { 0 } & { 0 } \\ { - 1 } & { 0 } & { 0 } \end{array} \right] } , M _ { z } = { \left[ \begin{array} { l l l } { 0 } & { - 1 } & { 0 } \\ { 1 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } \end{array} \right] } .\tag{7}
$$

(a) Write $\mathrm { T r } M _ { i } , M _ { i } ^ { T } , i = x , y , z$

(b) Calculate $e ^ { \theta M _ { x } } , e ^ { \theta M _ { y } } , e ^ { \theta M _ { z } }$ , where $\theta \in [ 0 , 2 \pi )$

(c) Give a geometrical interpretation of the transformations $e ^ { \theta M _ { i } } , i = x , y , z$ acting on the vectors in $\mathbb { R } ^ { 3 }$
:::
