---
schema: qual/card@1
id: P-BKF99-2
kind: problem
title: Nested closed sets of vanishing diameter in a complete metric space intersect
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $E_1,E_2,\ldots$ be nonempty closed subsets of a complete metric space $(X,d)$ such that
\[
E_{n+1}\subseteq E_n
\]
for every positive integer $n$, and
\[
\lim_{n\to\infty}\operatorname{diam}(E_n)=0,
\qquad
\operatorname{diam}(E)=\sup\{d(x,y):x,y\in E\}.
\]
Prove that
\[
\bigcap_{n=1}^{\infty}E_n\ne\varnothing.
\]
:::
