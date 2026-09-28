---
schema: qual/card@1
id: P-CASP07D
kind: problem
title: "Counting roots of z^n + z^{-m} = w in a disk via Rouché's theorem"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $n$ and $m$ be positive integers.
Fix $w$ with $|w| \leq 1$ and consider the equation $$z^n + \frac{1}{z^m} = w.$$ How many roots (counting multiplicities) are there in $B(0, 2)$?
:::

::: {.solution}
Multiplying the equation by $z^m$ gives
\[
P(z)=z^{n+m}-wz^m+1=0.
\]
Since $P(0)=1$, this introduces no spurious zero at the origin.

On $|z|=2$,
\[
|-wz^m+1|
\le |w|2^m+1
\le 2^m+1
<2^{m+n}
=|z^{m+n}|,
\]
because $m,n\ge1$. Rouché's theorem therefore shows that $P$ and
$z^{m+n}$ have the same number of zeros in $B(0,2)$, counted with
multiplicity. Hence the original equation has exactly
\[
\boxed{m+n}
\]
roots in $B(0,2)$.
:::
