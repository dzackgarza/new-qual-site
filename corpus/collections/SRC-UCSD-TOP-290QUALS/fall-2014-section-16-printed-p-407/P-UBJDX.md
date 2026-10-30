---
schema: qual/card@1
id: P-UBJDX
kind: problem
title: $\pi_2$ of a torus with a disc attached along a meridian
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Covering Spaces
  - Cell Complexes
relations: []
review: draft
---

::: {.problem}
Let $X$ be the space obtained by gluing the boundary of a disc to the curve in the torus shown in the source figure (a meridian circle, bounding a disc in the solid torus).
Compute the second homotopy group $\pi_2(X)$.
:::

::: {.solution}

::: pf

::: {.pf-step #homotopy-type}

$X \simeq S^2\vee S^1$.

::: pf-proof

The meridian $m$ bounds the attached disc $D$, so $T^2\cup D$ is a solid torus's boundary with one meridian disc added. Cutting $T^2$ along $m$ gives an annulus whose two boundary circles are both glued to $\partial D$; collapsing the contractible disc $D$ to a point therefore gives a homotopy equivalence $X\simeq X/D$, and $X/D$ is a sphere (the annulus with each boundary circle collapsed) with its two poles identified.
A sphere with two points identified is homotopy equivalent to $S^2\vee S^1$: attach an arc in $S^2$ joining the two points, which is contractible in $S^2$, and collapse it.

:::

:::

::: {.pf-step #cover}

The universal cover of $S^2\vee S^1$ is homotopy equivalent to $\bigvee_{n\in\ZZ}S^2$.

::: pf-proof

The universal cover is the real line $\RR$ with one copy of $S^2$ wedged on at each integer, because $\pi_1(S^2\vee S^1)\cong\ZZ$ by van Kampen and $S^2$ is simply connected. Collapsing the contractible line $\RR$ is a homotopy equivalence.

:::

:::

::: pf-qed

A covering map induces isomorphisms on $\pi_n$ for $n\ge2$, and $\bigvee_{\ZZ}S^2$ is simply connected, so by Hurewicz and Steps [](#homotopy-type){.pf-ref} and [](#cover){.pf-ref}
$$
\pi_2(X)\cong H_2\Bigl(\bigvee_{n\in\ZZ}S^2\Bigr)\cong\bigoplus_{n\in\ZZ}\ZZ,
$$
a free abelian group of countably infinite rank (a direct sum, not a product). As a module over $\ZZ[\pi_1X]=\ZZ[t,t^{-1}]$ it is free of rank one.

:::

:::

:::
