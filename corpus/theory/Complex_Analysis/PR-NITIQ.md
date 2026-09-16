---
schema: qual/card@1
id: PR-NITIQ
kind: proposition
title: Well-definedness of pole order
classification:
  areas:
  - complex-analysis
  topics:
  - Poles
relations: []
review: draft
---

::: {.proposition}
Let $f$ be [[D-E7A5W|holomorphic]] on a punctured disc $D_r(z_0)\sm\ts{z_0}$ and have a [[D-R4BDD|pole]] at $z_0$, so that $\abs{f(z)}\to\infty$ as $z\to z_0$.
Then there exist a least integer $n\ge1$ and a function $h$ holomorphic on a neighborhood of $z_0$ such that
$$
f(z)=(z-z_0)^{-n}h(z)
$$
near $z_0$, $z\neq z_0$.
For this $n$, the function $h$ is unique and $h(z_0)\neq0$; the integer $n$ is the [[D-R4BDD|order]] of the pole.
:::

::: {.proof}
Since $\abs{f}\to\infty$, there is $0<\rho\le r$ with $f\neq0$ on $D_\rho(z_0)\sm\ts{z_0}$.
The function $g\coloneqq1/f$ is holomorphic and bounded there, so by Riemann's removable singularity theorem it extends holomorphically to $D_\rho(z_0)$ with $g(z_0)=0$.
The extension is not identically zero, so its [[D-65VIK|zero]] at $z_0$ has a finite order $n\ge1$: $g(z)=(z-z_0)^nk(z)$ with $k$ holomorphic and nonvanishing on a neighborhood of $z_0$.
Then $h\coloneqq1/k$ is holomorphic near $z_0$, $h(z_0)\neq0$, and $f(z)=(z-z_0)^{-n}h(z)$.

If also $f(z)=(z-z_0)^{-m}\tilde h(z)$ with $\tilde h$ holomorphic near $z_0$ and $m<n$, then $\tilde h(z)=(z-z_0)^{m-n}h(z)$ for $z\neq z_0$, and $\abs{\tilde h(z)}\to\infty$ as $z\to z_0$ because $h(z_0)\neq0$; this contradicts continuity of $\tilde h$.
So $n$ is least, and $h=(z-z_0)^nf$ is determined off $z_0$, hence everywhere by continuity.
:::
