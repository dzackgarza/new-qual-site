---
schema: qual/card@1
id: E-ALB7C
kind: problem
title: A pole of order $n$ of $f$ is a pole of order $n+k$ of $f^{(k)}$
classification:
  areas:
  - complex-analysis
  topics:
  - Poles
  - Laurent Series
  - Principal Parts
relations: []
review: draft
---

::: {.exercise}
Show that if $z_0$ is a pole of order $n$ of $f$, then it is a pole of order $n+k$ for $f^{(k)}$.

:::

::: {.solution}
Without loss of generality suppose $z_0=0$ is the pole.
On a punctured disk about $0$, write the Laurent series $f(z) = \sum_{j\geq -n} c_j z^j$ with $c_{-n}\neq0$.
Differentiating term by term,
\[
f^{(k)}(z) = \sum_{j\geq -n} j(j-1)\cdots(j-k+1)\, c_j z^{j-k}
.\]
The most negative power that occurs is $z^{-n-k}$, with coefficient
\[
(-n)(-n-1)\cdots(-n-k+1)\,c_{-n}=(-1)^k n(n+1)\cdots(n+k-1)\,c_{-n}\neq0
,\]
so $0$ is a pole of order $n+k$ of $f^{(k)}$.
:::
