---
schema: qual/card@1
id: P-TOPQ17G
kind: problem
title: "A closed simply-connected 3-manifold is homotopy equivalent to S^3"
classification:
  areas:
  - topology
  topics:
  - Homotopy Type
  - Manifolds
  - Homology
relations: []
review: draft
---

::: problem
Show that a closed, compact, simply-connected $3$-manifold $M^3$ is homotopy-equivalent to $S^3$.
:::

::: {.solution}
<1>1. A closed simply connected $3$-manifold $M$ is orientable and satisfies
$$H_i(M;\mathbb Z)\cong\begin{cases}\mathbb Z,&i=0,3,\\0,&i=1,2.\end{cases}$$
::: {.proof}
Simply connected implies orientable and $H_1(M)=0$. Poincaré duality gives $H_3(M)\cong\mathbb Z$ and $H_2(M)\cong H^1(M)=0$.
:::

<1>2. Choose an embedded oriented $3$-ball $B\subset M$ and collapse $M\setminus\operatorname{int}B$ to a point. The quotient map
$$q:M\to B/\partial B\cong S^3$$
has degree $1$.
::: {.proof}
The relative fundamental class of $(B,\partial B)$ maps to the fundamental class of the quotient sphere, so with compatible orientations $q_*[M]=[S^3]$.
:::

<1>3. The map $q$ induces an isomorphism on every integral homology group.
::: {.proof}
By <1>1, only degrees $0$ and $3$ are nonzero. Connectedness gives the isomorphism in degree $0$, and degree $1$ gives the isomorphism in degree $3$.
:::

<1>4. Since both $M$ and $S^3$ are simply connected CW complexes, a homology isomorphism $q$ is a homotopy equivalence.
::: {.proof}
The homological Whitehead theorem says that a homology equivalence between simply connected CW complexes is a homotopy equivalence.
:::

<1>5. Hence
$$\boxed{M\simeq S^3.}$$
::: {.proof}
This is <1>2--<1>4.
:::
:::
