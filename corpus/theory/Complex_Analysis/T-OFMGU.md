---
schema: qual/card@1
id: T-OFMGU
kind: theorem
title: Identity theorem, with a two-variable version
classification:
  areas:
  - complex-analysis
  topics:
  - Identity Theorem
  - Zeros
relations: []
review: draft
---

::: {.theorem}
Let $\Omega\subseteq\CC$ be a connected open set and let $S\subseteq\Omega$ have a [[D-TFSPT|limit point]] in $\Omega$.

(i) If $f$ and $g$ are [[D-V6UQJ|analytic]] on $\Omega$ and $f(z)=g(z)$ for all $z\in S$, then $f(z)=g(z)$ for all $z\in\Omega$.

(ii) If $F\colon\Omega\times\Omega\to\CC$ is holomorphic in each variable separately and $F(z,w)=0$ for all $z,w\in S$, then $F(z,w)=0$ for all $z,w\in\Omega$.
:::

::: {.proof}
For (i), the zeros of the analytic function $f-g$ have a limit point in the connected open set $\Omega$, so $f-g\equiv0$.
For (ii), fix $w\in S$; the function $z\mapsto F(z,w)$ is holomorphic on $\Omega$ and vanishes on $S$, so by (i) it vanishes on $\Omega$.
Now fix $z\in\Omega$; the function $w\mapsto F(z,w)$ is holomorphic on $\Omega$ and vanishes on $S$, so by (i) it vanishes on $\Omega$.
:::
