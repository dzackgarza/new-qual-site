---
schema: qual/card@1
id: E-ALB7C
kind: exercise
title: "Poles of derivatives"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Poles of derivatives"}
Show that if $z_0$ is a pole of order $n$ of $f$, then it is a pole of order $n+k$ for $f^{(k)}$.

:::

:::{.solution}
Without loss of generality suppose $z_0=0$ is the pole.
Write $f(z) = \sum_{k\geq -N} c_k z^k$, then
\[
f(z) = \sum_{1\leq j \leq N} c_j z^{-j} + \sum_{k\geq 0} c_k z^k \\
\implies
f'(z) = \sum_{2 \leq j \leq N+1} -j c_j z^{-j-1} + \sum_{k\geq 1}k c_k z^{k-1}
,\]
making $0$ a pole of order $N+1$.
:::
