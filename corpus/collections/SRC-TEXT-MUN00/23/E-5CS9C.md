---
schema: qual/card@1
id: E-5CS9C
kind: problem
title: Connectedness of $\RR^\omega$ in the uniform topology
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Determine whether or not $\mathbb{R}^\omega$ is connected in the uniform topology.
:::

::: {.solution}
The uniform metric is $\bar\rho(\mathbf x,\mathbf y)=\sup_n\min\{\abs{x_n-y_n},1\}$. Let $\mathcal B$ be the set of bounded sequences.

<1>1. If $\bar\rho(\mathbf x,\mathbf y)<\frac12$, then $\mathbf x$ is bounded if and only if $\mathbf y$ is bounded.

::: {.proof}
$\bar\rho(\mathbf x,\mathbf y)<\frac12$ forces $\abs{x_n-y_n}<\frac12$ for every $n$, so $\sup_n\abs{y_n}\le\sup_n\abs{x_n}+\frac12$ and symmetrically.
:::

<1>2. $\mathcal B$ is open and closed in the uniform topology, and $\mathcal B\ne\varnothing,\RR^\omega$.

::: {.proof}
By step <1>1, the ball $B_{\bar\rho}(\mathbf x,\frac12)$ lies in $\mathcal B$ when $\mathbf x\in\mathcal B$ and in $\RR^\omega-\mathcal B$ when $\mathbf x\notin\mathcal B$, so both sets are open.
$\mathbf 0\in\mathcal B$ and $(1,2,3,\ldots)\notin\mathcal B$.
:::

<1>3. Q.E.D.

::: {.proof}
By step <1>2, $\mathcal B$ and its complement separate $\RR^\omega$, so $\RR^\omega$ is $\boxed{\text{not connected}}$ in the uniform topology.
:::
:::
