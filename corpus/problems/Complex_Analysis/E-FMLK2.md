---
schema: qual/card@1
id: E-FMLK2
kind: problem
title: A zero of multiplicity $n$ is a point where $f,\ldots,f^{(n-1)}$ vanish and $f^{(n)}$
  does not
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros
  - Power Series
  - Holomorphic Functions
relations: []
review: draft
---

::: {.exercise}
Show that if $f$ is holomorphic in $\DD_r(a)$ and $a$ is a zero of $f$ of multiplicity $n$, then $f^{(k)}(a) = 0$ for $k\leq n-1$ and $f^{(n)}(a) \neq 0$.
Show that this is an iff.

:::

::: {.solution}
Write $f(z) = \sum_{k\geq 0} c_k (z-a)^k$ on $\DD_r(a)$, where $c_k = f^{(k)}(a)/k!$.
Recall that $a$ is a zero of multiplicity $m$ when $f(z)=(z-a)^mg(z)$ with $g$ holomorphic near $a$ and $g(a)\neq0$.

$\impliedby$:
Suppose $f^{(k)}(a)=0$ for $k\le m-1$ and $f^{(m)}(a)\ne0$, so $c_k=0$ for $k\le m-1$ and $c_m\ne0$.
Then
\[
f(z) = \sum_{k\geq m} c_k (z-a)^k = (z-a)^m \sum_{k\geq m} c_k (z-a)^{k-m} \da (z-a)^m g(z)
,\]
where $g$ is holomorphic on $\DD_r(a)$ with $g(a) = c_m \neq 0$, making $a$ a zero of $f$ of multiplicity $m$.

$\implies$:
If $a$ is a zero of multiplicity $m$, write $f(z) = (z-a)^m h(z)$ with $h$ holomorphic near $a$ and $h(a)\neq0$, and expand $h(z)=\sum_{j\ge0}d_j(z-a)^j$ with $d_0=h(a)$.
Then $f(z)=\sum_{j\geq0}d_j(z-a)^{j+m}$, and by uniqueness of power series coefficients, $c_k=0$ for $k\le m-1$ and $c_m=d_0\neq0$.
That is, $f^{(k)}(a)=0$ for $k\le m-1$ and $f^{(m)}(a)=m!\,h(a)\neq0$.
:::
