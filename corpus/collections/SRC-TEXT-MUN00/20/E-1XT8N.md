---
schema: qual/card@1
id: E-1XT8N
kind: problem
title: Continuity of the affine map in the uniform topology
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Consider the map $h: \mathbb{R}^\omega \to \mathbb{R}^\omega$ defined in Exercise 8 of §19; give $\mathbb{R}^\omega$ the uniform topology.
Under what conditions on the numbers $a_i$ and $b_i$ is $h$ continuous?
a homeomorphism?
:::

::: {.solution}
Here $h(\mathbf x)=(a_ix_i+b_i)_{i\ge1}$ with $a_i>0$, as in [[E-AWEWJ]], and the uniform topology is given by $\bar\rho(\mathbf x,\mathbf y)=\sup_i\min\{\abs{x_i-y_i},1\}$.

<1>1. Translation $\mathbf x\mapsto\mathbf x+\mathbf b$ is an isometry of $(\mathbb R^\omega,\bar\rho)$, so $h$ is continuous, or a homeomorphism, if and only if $\mathbf x\mapsto(a_ix_i)_i$ is.

::: {.proof}
$\min\{\abs{(x_i+b_i)-(y_i+b_i)},1\}=\min\{\abs{x_i-y_i},1\}$ for every $i$.
:::

<1>2. $h$ is continuous if and only if $\boxed{\sup_i a_i<\infty}$.

::: {.proof}
Suppose $M=\sup_ia_i<\infty$, and let $0<\varepsilon\le1$.
If $\bar\rho(\mathbf x,\mathbf y)<\min\{\varepsilon/M,1\}$, then $\abs{x_i-y_i}<\varepsilon/M$ for every $i$, so $\abs{a_ix_i-a_iy_i}<\varepsilon$ and $\bar\rho(h\mathbf x,h\mathbf y)\le\varepsilon$.

Suppose $(a_i)$ is unbounded, and let $\delta\in(0,1)$.
Choose $k$ with $a_k>1/\delta$, and let $\mathbf y$ have $k$-th coordinate $\delta/2$ and all other coordinates $0$.
Then $\bar\rho(\mathbf y,\mathbf 0)=\delta/2<\delta$, but the $k$-th coordinates of $h\mathbf y$ and $h\mathbf 0$ differ by $a_k\delta/2>\frac12$, so $\bar\rho(h\mathbf y,h\mathbf 0)>\frac12$.
Hence $h$ is not continuous at $\mathbf 0$.
:::

<1>3. $h$ is a homeomorphism if and only if $\boxed{\sup_ia_i<\infty\text{ and }\inf_ia_i>0}$.

::: {.proof}
Since every $a_i>0$, $h$ is bijective with inverse $h^{-1}(\mathbf y)=\bigl((y_i-b_i)/a_i\bigr)_i$, a map of the same form with coefficients $1/a_i$.
By step <1>2, $h$ is continuous if and only if $\sup_ia_i<\infty$, and $h^{-1}$ is continuous if and only if $\sup_i(1/a_i)<\infty$, that is, $\inf_ia_i>0$.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>2 and <1>3 give the two conditions; by step <1>1 neither depends on $(b_i)$.
:::
:::
