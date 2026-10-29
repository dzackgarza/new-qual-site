---
schema: qual/card@1
id: T-YKOLU
kind: theorem
title: Lebesgue density theorem
slogan: 'Almost every point of a measurable set is a point of density $1$.'
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Measure Theory
relations: []
review: draft
---

::: {.theorem}
Let $m$ be Lebesgue measure on $\RR^d$ and let $E\subseteq\RR^d$ be Lebesgue measurable.
Then for almost every $x\in E$,
$$
\lim_{r\to 0}\frac{m(E\cap B(x,r))}{m(B(x,r))} = 1.
$$
It follows from the [[T-S3C3S|Lebesgue differentiation theorem]] applied to the indicator function of $E\cap B(0,R)$ for each $R\in\NN$ [@SS05, chap. 3].
:::
