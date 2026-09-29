---
schema: qual/card@1
id: P-TOPF02J
kind: problem
title: "No smooth retraction of the ball onto its boundary (Brouwer fixed point theorem)"
classification:
  areas:
  - topology
  topics:
  - Transversality
  - Fixed Point Theory
relations: []
review: draft
---

::: {.problem}
Use transversality to prove that there is no smooth retraction $r : B^n \to S^{n-1}$, and consequently (the Brouwer fixed point theorem) that any smooth automorphism of $B^n$ has a fixed point.
:::

::: {.solution}

::: pf

::: {.pf-step #suppose-retraction-exists}
Suppose, for contradiction, that there is a smooth retraction
$$
r:B^n\to S^{n-1}.
$$

::: pf-proof
Thus $r|_{S^{n-1}}=\operatorname{id}_{S^{n-1}}$.
:::

:::

::: pf-step
Choose a regular value $y\in S^{n-1}$ for $r$.

::: pf-proof
By Sard's theorem, regular values are dense. Along the boundary, $r$ is the identity, so $r|_{\partial B^n}$ is transverse to every point; after choosing a regular value of the interior map as well, $r$ is transverse to $\{y\}$ as a map of a manifold with boundary.
:::

:::

::: {.pf-step #m-compact-1manifold}
The inverse image
$$
M=r^{-1}(y)
$$
is a compact $1$-dimensional manifold with boundary
$$
\partial M=M\cap\partial B^n=\{y\}.
$$

::: pf-proof
Transversality to a point of the $(n-1)$-manifold $S^{n-1}$ gives a submanifold of dimension $n-(n-1)=1$. Compactness follows because $M$ is closed in the compact ball. The boundary transversality theorem gives $\partial M=M\cap\partial B^n$. Since the boundary restriction is the identity, its inverse image of $y$ consists of exactly the single point $y$.
:::

:::

::: {.pf-step #contradiction-parity}
This is impossible.

::: pf-proof
Every compact $1$-manifold is a finite disjoint union of circles and closed intervals. Its boundary therefore has an even number of points, whereas step [](#m-compact-1manifold){.pf-ref} gives exactly one boundary point.
:::

:::

::: {.pf-step #no-retraction-exists}
Hence no smooth retraction $B^n\to S^{n-1}$ exists.

::: pf-proof
The assumption in step [](#suppose-retraction-exists){.pf-ref} leads to the contradiction in step [](#contradiction-parity){.pf-ref}.
:::

:::

::: {.pf-step #fixed-point-free-gives-retraction}
Let $f:B^n\to B^n$ be a smooth self-map with no fixed point. Then one obtains a smooth retraction $r_f:B^n\to S^{n-1}$.

::: pf-proof
For each $x\in B^n$, the vector $x-f(x)$ is nonzero. Starting at $f(x)$ and following the ray through $x$, there is a unique first point where the ray meets $S^{n-1}$; define this point to be $r_f(x)$. Solving the quadratic equation
$$
\bigl|f(x)+t(x-f(x))\bigr|^2=1
$$
for the positive root $t\ge1$ shows that $t$ depends smoothly on $x$ because $x-f(x)\ne0$. If $x\in S^{n-1}$, the first boundary point on this ray is $x$ itself, so $r_f(x)=x$. Thus $r_f$ is a smooth retraction.
:::

:::

::: pf-step
Therefore every smooth self-map of $B^n$ has a fixed point; in particular every smooth automorphism does.

::: pf-proof
A fixed-point-free smooth self-map would produce the forbidden retraction from step [](#fixed-point-free-gives-retraction){.pf-ref}, contradicting step [](#no-retraction-exists){.pf-ref}.
:::

:::

:::

:::

