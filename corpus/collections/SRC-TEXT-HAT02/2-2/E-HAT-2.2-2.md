---
schema: qual/card@1
id: E-HAT-2.2-2
kind: problem
title: Map of $S^{2n}$ has fixed point or antipodal point; $\mathbb{RP}^{2n}$ maps have fixed points
classification:
  areas:
  - topology
  topics:
  - Degree
  - Fixed Point Theorems
  - Projective Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Given a map $f: S^{2n} \to S^{2n}$, show that there is some point $x \in S^{2n}$ with either $f(x) = x$ or $f(x) = -x$.
Deduce that every map $\mathbb{RP}^{2n} \to \mathbb{RP}^{2n}$ has a fixed point.
Construct maps $\mathbb{RP}^{2n-1} \to \mathbb{RP}^{2n-1}$ without fixed points from linear transformations $\mathbb{R}^{2n} \to \mathbb{R}^{2n}$ without eigenvectors.
:::

::: {.solution}
**Goal.** Show every map $f: S^{2n} \to S^{2n}$ has a fixed point or an antipodal point; deduce every map $\RP^{2n} \to \RP^{2n}$ has a fixed point; and construct fixed-point-free maps of $\RP^{2n-1}$.

::: pf

::: {.pf-step #s1}
Every map $f: S^{2n} \to S^{2n}$ has $f(x) = x$ or $f(x) = -x$ for some $x$.

::: pf-proof

::: {.pf-step #s1-1}
If $f(x) \neq x$ for all $x$, then $f$ has no fixed point, so $\deg f = (-1)^{2n+1} = -1$.

::: pf-proof
a fixed-point-free map of $S^m$ has degree $(-1)^{m+1}$ (the antipodal map $x \mapsto -x$ has degree $(-1)^{m+1}$, and any fixed-point-free map is homotopic to it).
:::

:::

::: pf-step
If also $f(x) \neq -x$ for all $x$, then $-f$ has no fixed point, so $\deg(-f) = -1$.

::: pf-proof
$-f$ is fixed-point-free, so by step [](#s1-1){.pf-ref} its degree is $(-1)^{2n+1} = -1$.
:::

:::

::: {.pf-step #s1-3}
But $\deg(-f) = (-1)^{2n+1}\deg f = -\deg f = -(-1) = 1$, contradiction.

::: pf-proof
the antipodal map has degree $(-1)^{2n+1} = -1$, and $\deg(-f) = \deg(\text{antipodal} \circ f) = (-1)^{2n+1}\deg f = -\deg f$.
:::

:::

::: pf-step
Hence $f(x) = x$ or $f(x) = -x$ for some $x$.

::: pf-proof
Step [](#s1-3){.pf-ref} contradicts the assumption that neither holds.
:::

:::

:::

:::

::: {.pf-step #s2}
Every map $\RP^{2n} \to \RP^{2n}$ has a fixed point.

::: pf-proof

::: pf-step
A map $g: \RP^{2n} \to \RP^{2n}$ lifts to a map $\tilde g: S^{2n} \to S^{2n}$.

::: pf-proof
$\RP^{2n}$ has universal cover $S^{2n}$; since $\pi_1(\RP^{2n}) = \ZZ/2$ and $g_*$ maps $\ZZ/2$ into itself, the lift exists (the induced map on $\pi_1$ is either identity or zero, both compatible with the covering).
:::

:::

::: pf-step
By step [](#s1){.pf-ref}, $\tilde g(x) = x$ or $\tilde g(x) = -x$ for some $x$.

::: pf-proof
apply step [](#s1){.pf-ref} to $\tilde g$.
:::

:::

::: pf-step
In either case $g([x]) = [x]$.

::: pf-proof
$[x] = [-x]$ in $\RP^{2n}$, and $g([x]) = [\tilde g(x)] = [x]$ or $[-x] = [x]$.
:::

:::

:::

:::

::: {.pf-step #s3}
Fixed-point-free maps of $\RP^{2n-1}$.

::: pf-proof

::: pf-step
A linear map $T: \RR^{2n} \to \RR^{2n}$ without real eigenvectors induces a map $\RP^{2n-1} \to \RP^{2n-1}$.

::: pf-proof
$T$ sends lines to lines (it is linear), and no line is fixed because a fixed line would be an eigenspace, i.e. an eigenvector.
:::

:::

::: pf-step
Example: $T(x_1, \dots, x_{2n}) = (-x_2, x_1, -x_4, x_3, \dots, -x_{2n}, x_{2n-1})$, a block rotation by $90^\circ$ in each coordinate pair.

::: pf-proof
$T$ has no real eigenvectors (its eigenvalues are $\pm i$), so the induced map on $\RP^{2n-1}$ has no fixed point.
:::

:::

:::

:::

::: pf-qed
Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, and [](#s3){.pf-ref} are the three requested statements.
:::

:::

:::
