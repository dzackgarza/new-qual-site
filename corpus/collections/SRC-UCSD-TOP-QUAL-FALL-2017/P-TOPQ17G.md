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

::: {.problem}
Show that a closed, compact, simply-connected $3$-manifold $M^3$ is homotopy-equivalent to $S^3$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

A closed simply connected $3$-manifold $M$ is orientable and satisfies
$$H_i(M;\mathbb Z)\cong\begin{cases}\mathbb Z,&i=0,3,\\0,&i=1,2.\end{cases}$$

::: pf-proof

Simply connected implies orientable and $H_1(M)=0$. Poincaré duality gives $H_3(M)\cong\mathbb Z$ and $H_2(M)\cong H^1(M)=0$.

:::

:::

::: {.pf-step #s2}

Choose an embedded oriented $3$-ball $B\subset M$ and collapse $M\setminus\operatorname{int}B$ to a point. The quotient map
$$q:M\to B/\partial B\cong S^3$$
has degree $1$.

::: pf-proof

The relative fundamental class of $(B,\partial B)$ maps to the fundamental class of the quotient sphere, so with compatible orientations $q_*[M]=[S^3]$.

:::

:::

::: {.pf-step #s3}

The map $q$ induces an isomorphism on every integral homology group.

::: pf-proof

By step [](#s1){.pf-ref}, only degrees $0$ and $3$ are nonzero. Connectedness gives the isomorphism in degree $0$, and degree $1$ gives the isomorphism in degree $3$.

:::

:::

::: {.pf-step #s4}

Since both $M$ and $S^3$ are simply connected CW complexes, a homology isomorphism $q$ is a homotopy equivalence.

::: pf-proof

The homological Whitehead theorem says that a homology equivalence between simply connected CW complexes is a homotopy equivalence.

:::

:::

::: pf-step

Hence
$$\boxed{M\simeq S^3.}$$

::: pf-proof

This is steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

:::

:::
