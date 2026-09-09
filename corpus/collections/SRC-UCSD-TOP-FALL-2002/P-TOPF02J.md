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

::: problem
Use transversality to prove that there is no smooth retraction $r : B^n \to S^{n-1}$, and consequently (the Brouwer fixed point theorem) that any smooth automorphism of $B^n$ has a fixed point.
:::

::: {.solution}
<1>1. Suppose, for contradiction, that there is a smooth retraction
$$
r:B^n\to S^{n-1}.
$$
::: {.proof}
Thus $r|_{S^{n-1}}=\operatorname{id}_{S^{n-1}}$.
:::

<1>2. Choose a regular value $y\in S^{n-1}$ for $r$.
::: {.proof}
By Sard's theorem, regular values are dense. Along the boundary, $r$ is the identity, so $r|_{\partial B^n}$ is transverse to every point; after choosing a regular value of the interior map as well, $r$ is transverse to $\{y\}$ as a map of a manifold with boundary.
:::

<1>3. The inverse image
$$
M=r^{-1}(y)
$$
is a compact $1$-dimensional manifold with boundary
$$
\partial M=M\cap\partial B^n=\{y\}.
$$
::: {.proof}
Transversality to a point of the $(n-1)$-manifold $S^{n-1}$ gives a submanifold of dimension $n-(n-1)=1$. Compactness follows because $M$ is closed in the compact ball. The boundary transversality theorem gives $\partial M=M\cap\partial B^n$. Since the boundary restriction is the identity, its inverse image of $y$ consists of exactly the single point $y$.
:::

<1>4. This is impossible.
::: {.proof}
Every compact $1$-manifold is a finite disjoint union of circles and closed intervals. Its boundary therefore has an even number of points, whereas <1>3 gives exactly one boundary point.
:::

<1>5. Hence no smooth retraction $B^n\to S^{n-1}$ exists.
::: {.proof}
The assumption in <1>1 leads to the contradiction in <1>4.
:::

<1>6. Let $f:B^n\to B^n$ be a smooth self-map with no fixed point. Then one obtains a smooth retraction $r_f:B^n\to S^{n-1}$.
::: {.proof}
For each $x\in B^n$, the vector $x-f(x)$ is nonzero. Starting at $f(x)$ and following the ray through $x$, there is a unique first point where the ray meets $S^{n-1}$; define this point to be $r_f(x)$. Solving the quadratic equation
$$
\bigl|f(x)+t(x-f(x))\bigr|^2=1
$$
for the positive root $t\ge1$ shows that $t$ depends smoothly on $x$ because $x-f(x)\ne0$. If $x\in S^{n-1}$, the first boundary point on this ray is $x$ itself, so $r_f(x)=x$. Thus $r_f$ is a smooth retraction.
:::

<1>7. Therefore every smooth self-map of $B^n$ has a fixed point; in particular every smooth automorphism does.
::: {.proof}
A fixed-point-free smooth self-map would produce the forbidden retraction from <1>6, contradicting <1>5.
:::
:::

