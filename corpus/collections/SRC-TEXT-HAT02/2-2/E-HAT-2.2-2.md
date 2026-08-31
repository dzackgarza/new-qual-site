---
schema: qual/card@1
id: E-HAT-2.2-2
kind: exercise
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

Given a map $f: S^{2n} \to S^{2n}$, show that there is some point $x \in S^{2n}$ with either $f(x) = x$ or $f(x) = -x$.
Deduce that every map $\mathbb{RP}^{2n} \to \mathbb{RP}^{2n}$ has a fixed point.
Construct maps $\mathbb{RP}^{2n-1} \to \mathbb{RP}^{2n-1}$ without fixed points from linear transformations $\mathbb{R}^{2n} \to \mathbb{R}^{2n}$ without eigenvectors.

::: {.solution}
**Goal.** Show every map $f: S^{2n} \to S^{2n}$ has a fixed point or an antipodal point; deduce every map $\RP^{2n} \to \RP^{2n}$ has a fixed point; and construct fixed-point-free maps of $\RP^{2n-1}$.

<1>1. Every map $f: S^{2n} \to S^{2n}$ has $f(x) = x$ or $f(x) = -x$ for some $x$.
<2>1. If $f(x) \neq x$ for all $x$, then $f$ has no fixed point, so $\deg f = (-1)^{2n+1} = -1$.
::: {.proof}
a fixed-point-free map of $S^m$ has degree $(-1)^{m+1}$ (the antipodal map $x \mapsto -x$ has degree $(-1)^{m+1}$, and any fixed-point-free map is homotopic to it).
:::
<2>2. If also $f(x) \neq -x$ for all $x$, then $-f$ has no fixed point, so $\deg(-f) = -1$.
::: {.proof}
$-f$ is fixed-point-free, so by <1>2.1 its degree is $(-1)^{2n+1} = -1$.
:::
<2>3. But $\deg(-f) = (-1)^{2n+1}\deg f = -\deg f = -(-1) = 1$, contradiction.
::: {.proof}
the antipodal map has degree $(-1)^{2n+1} = -1$, and $\deg(-f) = \deg(\text{antipodal} \circ f) = (-1)^{2n+1}\deg f = -\deg f$.
:::
<2>4. Hence $f(x) = x$ or $f(x) = -x$ for some $x$.
::: {.proof}
<1>2.3 contradicts the assumption that neither holds.
:::

<1>2. Every map $\RP^{2n} \to \RP^{2n}$ has a fixed point.
<2>1. A map $g: \RP^{2n} \to \RP^{2n}$ lifts to a map $\tilde g: S^{2n} \to S^{2n}$.
::: {.proof}
$\RP^{2n}$ has universal cover $S^{2n}$; since $\pi_1(\RP^{2n}) = \ZZ/2$ and $g_*$ maps $\ZZ/2$ into itself, the lift exists (the induced map on $\pi_1$ is either identity or zero, both compatible with the covering).
:::
<2>2. By <1>1, $\tilde g(x) = x$ or $\tilde g(x) = -x$ for some $x$.
::: {.proof}
apply <1>1 to $\tilde g$.
:::
<2>3. In either case $g([x]) = [x]$.
::: {.proof}
$[x] = [-x]$ in $\RP^{2n}$, and $g([x]) = [\tilde g(x)] = [x]$ or $[-x] = [x]$.
:::

<1>3. Fixed-point-free maps of $\RP^{2n-1}$.
<2>1. A linear map $T: \RR^{2n} \to \RR^{2n}$ without real eigenvectors induces a map $\RP^{2n-1} \to \RP^{2n-1}$.
::: {.proof}
$T$ sends lines to lines (it is linear), and no line is fixed because a fixed line would be an eigenspace, i.e. an eigenvector.
:::
<2>2. Example: $T(x_1, \dots, x_{2n}) = (-x_2, x_1, -x_4, x_3, \dots, -x_{2n}, x_{2n-1})$, a block rotation by $90^\circ$ in each coordinate pair.
::: {.proof}
$T$ has no real eigenvectors (its eigenvalues are $\pm i$), so the induced map on $\RP^{2n-1}$ has no fixed point.
:::

<1>4. Q.E.D.
::: {.proof}
<1>1, <1>2, and <1>3 are the three requested statements.
:::
:::
