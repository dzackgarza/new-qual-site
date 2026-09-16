---
schema: qual/card@1
id: D-R4BDD
kind: definition
title: Poles via reciprocals
classification:
  areas:
  - complex-analysis
  topics:
  - Poles
  - Singularities
relations:
- kind: variant-of
  target: D-AUD6K
review: draft
---

::: {.definition}
Let $f$ be [[D-E7A5W|holomorphic]] on a punctured disc $D_r(z_0)\setminus\{z_0\}$.
The point $z_0$ is a \dfn{pole} of $f$ if there is $0<\rho\le r$ such that $f$ has no zeros on $D_\rho(z_0)\setminus\{z_0\}$ and $g\coloneqq1/f$, extended by $g(z_0)\coloneqq0$, is holomorphic on $D_\rho(z_0)$.
The \dfn{order} of the pole is the least integer $n\ge1$ for which there is a function $h$ holomorphic on a neighborhood of $z_0$ with
$$
f(z)=(z-z_0)^{-n}h(z)
$$
for $z\neq z_0$ near $z_0$.
A pole of order $1$ is a \dfn{simple pole}.
:::

::: {.proposition}
Let $f$ be holomorphic on $D_r(z_0)\setminus\{z_0\}$.

(i) $z_0$ is a pole of $f$ if and only if $\abs{f(z)}\to\infty$ as $z\to z_0$.

(ii) If $z_0$ is a pole, its order exists and equals the order of $z_0$ as a [[D-65VIK|zero]] of $1/f$; for this $n$ the function $h$ satisfies $h(z_0)\neq0$.
In particular the definition agrees with [[D-AUD6K]].
:::

::: {.proof}
(i) This is the last assertion of the proposition on [[D-AUD6K]], whose condition (b) is the present definition.

(ii) Since $g=1/f$ is holomorphic near $z_0$, not identically zero, and $g(z_0)=0$, it has a zero of some order $n\ge1$: $g(z)=(z-z_0)^nk(z)$ with $k(z_0)\neq0$, and $h_0\coloneqq1/k$ is holomorphic near $z_0$ with $f(z)=(z-z_0)^{-n}h_0(z)$ and $h_0(z_0)\neq0$.
If $f(z)=(z-z_0)^{-m}h(z)$ with $h$ holomorphic near $z_0$ and $m<n$, then $h(z)=(z-z_0)^{m-n}h_0(z)$ for $z\neq z_0$, which is unbounded near $z_0$, a contradiction.
So $n$ is the least such integer.
:::
