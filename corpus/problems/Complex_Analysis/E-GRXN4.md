---
schema: qual/card@1
id: E-GRXN4
kind: problem
title: Sums and products of poles and essential singularities
classification:
  areas:
  - complex-analysis
  topics:
  - Poles
  - Essential Singularities
  - Laurent Series
  - Counterexamples
relations: []
review: draft
---

::: {.exercise}
Determine whether each statement is true, proving it or giving a counterexample.

(a) If $f,g$ have a pole at $a$, then $f+g$ has a pole at $a$.

(b) If $f,g$ have a pole at $a$, then $fg$ has a pole at $a$.

(c) If $f$ has an essential singularity at $z_0$ and $g$ has a pole at $z_0$, then $z_0$ is an essential singularity for $f+g$.

(d) If $f$ has a pole of order $N$ at $z_0$ then $f^2$ has a pole of order $2N$ at $z_0$.
:::

::: {.solution}

::: pf

::: pf-step
(a) is $\boxed{\text{false}}$.

::: pf-proof
The functions $f(z)={1\over z-a}$ and $g(z)=-{1\over z-a}$ have simple poles at $a$, but $f+g=0$.
:::

:::

::: pf-step
(b) is $\boxed{\text{true}}$.

::: pf-proof
If $f$ and $g$ have poles of orders $m$ and $n$, write $f(z)=(z-a)^{-m}u(z)$ and $g(z)=(z-a)^{-n}v(z)$ with $u,v$ holomorphic near $a$ and $u(a),v(a)\neq0$.
Then $fg=(z-a)^{-(m+n)}uv$ with $u(a)v(a)\neq0$, a pole of order $m+n$.
:::

:::

::: pf-step
(c) is $\boxed{\text{true}}$.

::: pf-proof
If $g$ has a pole of order $N$ at $z_0$, its Laurent series at $z_0$ has no terms of degree below $-N$.
The Laurent series of $f$ at $z_0$ has infinitely many nonzero terms of negative degree, so infinitely many of degree below $-N$, and these are also terms of the Laurent series of $f+g$.
Hence $z_0$ is an essential singularity of $f+g$.
:::

:::

::: pf-step
(d) is $\boxed{\text{true}}$.

::: pf-proof
Write $f(z)=(z-z_0)^{-N}u(z)$ with $u$ holomorphic near $z_0$ and $u(z_0)\neq0$.
Then $f^2=(z-z_0)^{-2N}u^2$ with $u(z_0)^2\neq0$, a pole of order $2N$.
:::

:::

:::

:::
