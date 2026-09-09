---
schema: qual/card@1
id: P-9RRSR
kind: problem
title: $\CP^2\#\CP^2$ and $S^2\times S^2$ are not homotopy-equivalent
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Manifolds
  - Cohomology
relations: []
review: draft
---

Prove that $\CP^2\#\CP^2$ and $S^2\times S^2$ are not homotopy-equivalent.
(Recall that the connect-sum ($\#$) of two closed oriented connected $n$-manifolds is defined by removing an open $n$-ball from each and gluing the resulting manifolds using a homeomorphism between their boundary $(n-1)$-spheres, in such a way that the orientations match to make a new closed oriented connected $n$-manifold.)

::: {.solution}
<1>1. Both manifolds have $H^2(-;\mathbb Z)\cong\mathbb Z^2$, but their integral intersection forms are different.
::: {.proof}
For a closed oriented $4$-manifold, the cup product followed by evaluation on the fundamental class defines a unimodular bilinear form on $H^2$ modulo torsion.
:::

<1>2. For $\mathbb{CP}^2\#\mathbb{CP}^2$, the intersection form is
$$
\begin{pmatrix}1&0\\0&1\end{pmatrix}.
$$
::: {.proof}
The two summands contribute their standard generators in degree two; classes supported in different connect-sum summands have zero intersection, and each $\mathbb{CP}^2$ generator has square $+1$ with the chosen orientation.
:::

<1>3. For $S^2\times S^2$, with generators
$$
a=[S^2\times\{*\}]^*,\qquad b=[\{*\}\times S^2]^*,
$$
the intersection form is
$$
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$
::: {.proof}
Each factor class has square zero, while the two factor surfaces meet transversely in one point, so $a\smile b$ evaluates to $1$ on the fundamental class.
:::

<1>4. The first form is odd, whereas the second is even.
::: {.proof}
In the first form the vector $(1,0)$ has self-intersection $1$. In the hyperbolic form, a vector $(m,n)$ has self-intersection $2mn$, always even. Thus no integral change of basis, even after multiplying the whole form by $-1$, can identify them.
:::

<1>5. Hence $\mathbb{CP}^2\#\mathbb{CP}^2$ and $S^2\times S^2$ are not homotopy-equivalent.
::: {.proof}
A homotopy equivalence induces an isomorphism of integral cohomology rings and takes the top class to its positive or negative generator, so it preserves the intersection form up to overall sign. This contradicts <1>4.
:::
:::
