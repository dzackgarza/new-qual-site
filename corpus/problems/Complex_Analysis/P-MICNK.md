---
schema: qual/card@1
id: P-MICNK
kind: problem
title: $az^n+z+1$ has a root in $|z|\le 2$
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
  - Polynomials
relations: []
review: draft
---

::: {.problem}
Let $a\in \CC$ and $n\geq 2$.
Show that the following polynomial has at least one root in $\abs{z} \leq 2$:
\[
f(z) = az^n + z + 1
.\]
:::

::: {.solution}
First suppose
\[
|a|<2^{-n}.
\]
On $|z|=2$,
\[
|az^n|=|a|2^n<1\le |z+1|.
\]
Rouché's theorem therefore shows that $az^n+z+1$ and $z+1$ have the same number of zeros in $|z|<2$, namely one.

Now suppose $|a|\ge2^{-n}$. Then $a\neq0$. Let $z_1,\ldots,z_n$ be the roots of $f$, counted with multiplicity. Vieta's formula gives
\[
\left|\prod_{k=1}^n z_k\right|={1\over|a|}\le2^n.
\]
If every root satisfied $|z_k|>2$, their product would have modulus strictly greater than $2^n$, a contradiction. Hence at least one root lies in $|z|\le2$.
:::
