---
schema: qual/card@1
id: P-6PMCN
kind: problem
title: Laurent series of $\frac{1}{z}+\frac{1}{z^2-1}$ on the largest annuli of validity
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Poles
  - Principal Parts
relations: []
review: draft
---

::: {.problem}
Let $\displaystyle f(z) = \frac{1}{z} + \frac{1}{z^2 -1}$.
Find all the Laurent series of $f$ and describe the largest annuli in which these series are valid.
:::

::: {.solution}
The singularities are at $-1,0,1$, so the maximal annuli centered at $0$ are
\[
0<|z|<1
\qquad\text{and}\qquad
|z|>1.
\]

For $0<|z|<1$,
\[
\frac1{z^2-1}=-\frac1{1-z^2}=-\sum_{n=0}^\infty z^{2n},
\]
and hence
\[
\boxed{
f(z)=\frac1z-\sum_{n=0}^\infty z^{2n}
=\frac1z-1-z^2-z^4-\cdots,
\qquad 0<|z|<1.}
\]

For $|z|>1$,
\[
\frac1{z^2-1}
=\frac1{z^2}\frac1{1-z^{-2}}
=\sum_{n=0}^\infty z^{-2n-2},
\]
so
\[
\boxed{
f(z)=\frac1z+\sum_{n=0}^\infty z^{-2n-2}
=\frac1z+\frac1{z^2}+\frac1{z^4}+\frac1{z^6}+\cdots,
\qquad |z|>1.}
\]
These are all Laurent expansions about $0$ on maximal annuli of analyticity.
:::
