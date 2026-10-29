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
Recall that $a$ is a zero of multiplicity $n$ when $f(z)=(z-a)^ng(z)$ with $g$ holomorphic near $a$ and $g(a)\neq0$.

::: pf

::: pf-step
If $a$ is a zero of multiplicity $n$, then $f^{(k)}(a)=0$ for $k\le n-1$ and $f^{(n)}(a)\neq0$.

::: pf-proof
Write $f(z) = (z-a)^n h(z)$ with $h$ holomorphic near $a$ and $h(a)\neq0$, and expand $h(z)=\sum_{j\ge0}d_j(z-a)^j$ with $d_0=h(a)$.
Then $f(z)=\sum_{j\geq0}d_j(z-a)^{j+n}$, and by uniqueness of power series coefficients, $c_k=0$ for $k\le n-1$ and $c_n=d_0\neq0$.
That is, $f^{(k)}(a)=0$ for $k\le n-1$ and $f^{(n)}(a)=n!\,h(a)\neq0$.
:::

:::

::: pf-step
If $f^{(k)}(a)=0$ for $k\le n-1$ and $f^{(n)}(a)\ne0$, then $a$ is a zero of multiplicity $n$.

::: pf-proof
The hypothesis says $c_k=0$ for $k\le n-1$ and $c_n\ne0$. Then
$$
f(z) = \sum_{k\geq n} c_k (z-a)^k = (z-a)^n g(z),
\qquad
g(z)\coloneqq\sum_{k\geq n} c_k (z-a)^{k-n},
$$
where $g$ is holomorphic on $\DD_r(a)$ with $g(a) = c_n \neq 0$.
:::

:::

:::

:::
