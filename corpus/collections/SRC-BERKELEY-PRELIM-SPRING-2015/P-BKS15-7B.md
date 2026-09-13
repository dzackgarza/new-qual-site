---
schema: qual/card@1
id: P-BKS15-7B
kind: problem
title: Low-rank approximation of the exponential kernel matrix
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
  note: Checked against the vendored UC Berkeley Spring 2015 Graduate Preliminary Examination.
---

::: {.problem}
Fix $N\ge1$.
Let $s_1,\ldots,s_N,t_1,\ldots,t_N$ be $2N$ complex numbers of magnitude at most $1$, and let $A$ be the $N\times N$ matrix
\[
A_{ij}=\exp(t_is_j).
\]
Show that $A$ can be approximated by matrices of small rank in the following sense: for every $m\ge1$, the matrix $B$ with entries
\[
B_{ij}=\sum_{n=0}^{m-1}\frac{(t_is_j)^n}{n!}
\]
satisfies
\[
|A_{ij}-B_{ij}|\le\frac2{m!}
\]
for all $i,j$, and has rank at most $m$.
:::
