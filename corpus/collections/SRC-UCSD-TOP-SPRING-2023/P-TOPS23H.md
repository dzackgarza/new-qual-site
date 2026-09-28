---
schema: qual/card@1
id: P-TOPS23H
kind: problem
title: "CP^2 # overline{CP^2} is not homotopy equivalent to S^2 x S^2 via cohomology ring"
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
  - Connected Sum
  - Manifolds
  - Projective Spaces
  - Homotopy Type
relations: []
review: draft
---

::: {.problem}
Let $\mathbb{CP}^2$ be the complex projective plane with its usual orientation, and $\overline{\mathbb{CP}^2}$ be the same manifold with the opposite orientation.
Let $M^4 = \mathbb{CP}^2 \# \overline{\mathbb{CP}^2}$ be the connect-sum of the two manifolds, obtained by removing an open $4$-ball from each one and identifying the resulting $3$-spheres so that the result is oriented.
By working out the cohomology ring $H^*(M; \mathbb{Z})$, show that $M$ is not homotopy-equivalent to $S^2 \times S^2$.
:::

::: {.solution}
<1>1. For
$$M=\mathbb{CP}^2\#\overline{\mathbb{CP}}^{\,2},$$
one has
$$H^0(M;\mathbb Z)\cong H^4(M;\mathbb Z)\cong\mathbb Z,\qquad H^2(M;\mathbb Z)\cong\mathbb Z^2,$$
with all other cohomology zero.
::: {.proof}
Connected sum in dimension $4$ adds the middle homology groups of the summands, while preserving one bottom and one top class.
:::

<1>2. Choose $x,y\in H^2(M;\mathbb Z)$ from the two summands and an orientation class $u\in H^4(M;\mathbb Z)$. Then
$$x^2=u,\qquad y^2=-u,\qquad xy=0.$$
::: {.proof}
The intersection form of $\mathbb{CP}^2$ is $(1)$; reversing orientation changes it to $(-1)$. Classes supported in distinct connected-sum summands have zero intersection.
:::

<1>3. Thus the intersection form of $M$ is the odd form
$$Q_M\cong\begin{pmatrix}1&0\\0&-1\end{pmatrix}.$$
::: {.proof}
The relations in <1>2 are precisely the matrix entries of the cup-product/intersection pairing on $H^2$.
:::

<1>4. For $S^2\times S^2$, with factor classes $a,b\in H^2$, one has
$$a^2=b^2=0,\qquad ab=v,$$
so
$$Q_{S^2\times S^2}\cong\begin{pmatrix}0&1\\1&0\end{pmatrix},$$
which is even.
::: {.proof}
Each factor sphere has zero self-intersection in the product, while the two factor cycles meet transversely once.
:::

<1>5. The two integral cohomology rings are not isomorphic.
::: {.proof}
In $M$ there is a degree-$2$ class $x$ whose square is a generator of $H^4$, an odd multiple of the top class. In $S^2\times S^2$, every class $pa+qb$ has square $2pq\,v$, always an even multiple of the top class. This parity property is preserved by ring isomorphism.
:::

<1>6. Therefore
$$\boxed{\mathbb{CP}^2\#\overline{\mathbb{CP}}^{\,2}\not\simeq S^2\times S^2.}$$
::: {.proof}
A homotopy equivalence induces an isomorphism of integral cohomology rings, contradicting <1>5.
:::
:::
