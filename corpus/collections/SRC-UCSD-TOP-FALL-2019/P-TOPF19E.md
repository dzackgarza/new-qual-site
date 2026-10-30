---
schema: qual/card@1
id: P-TOPF19E
kind: problem
title: '$H_{n-1}$ of a closed $n$-manifold is torsion-free if and only if the manifold is orientable'
classification:
  areas:
  - topology
  topics:
  - Homology
  - Orientation
  - Manifolds
relations: []
review: draft
---

::: {.problem}
Let $M$ be a connected, closed $n$-dimensional manifold.
Show that $H_{n-1}(M; \ZZ)$ is torsion-free if and only if $M$ is orientable.
:::

::: {.solution}

::: pf

::: {.pf-step #top}

$H_n(M;\ZZ)\cong\ZZ$ if $M$ is orientable and $H_n(M;\ZZ)=0$ if not, while $H_n(M;\ZZ/2)\cong\ZZ/2$ in both cases.

::: pf-proof

This is the standard computation of the top homology of a closed connected $n$-manifold (Hatcher, Theorem 3.26).

:::

:::

::: {.pf-step #s1}

If $M$ is orientable, then $H_{n-1}(M;\ZZ)$ is torsion-free.

::: pf-proof

Poincaré duality gives $H_{n-1}(M;\ZZ)\cong H^1(M;\ZZ)$. The universal coefficient theorem gives $H^1(M;\ZZ)\cong\operatorname{Hom}(H_1(M),\ZZ)$, because $\operatorname{Ext}(H_0(M),\ZZ)=\operatorname{Ext}(\ZZ,\ZZ)=0$, and a group of homomorphisms into $\ZZ$ is torsion-free.

:::

:::

::: {.pf-step #s2}

If $M$ is nonorientable, then $H_{n-1}(M;\ZZ)$ has an element of order $2$.

::: pf-proof

The universal coefficient theorem for homology gives
$$
H_n(M;\ZZ/2)\cong \bigl(H_n(M;\ZZ)\otimes\ZZ/2\bigr)\oplus\operatorname{Tor}(H_{n-1}(M;\ZZ),\ZZ/2).
$$
By Step [](#top){.pf-ref} the left side is $\ZZ/2$ and $H_n(M;\ZZ)=0$, so $\operatorname{Tor}(H_{n-1}(M;\ZZ),\ZZ/2)\cong\ZZ/2$. This group is the $2$-torsion subgroup $\{x : 2x=0\}$ of $H_{n-1}(M;\ZZ)$, so it has an element of order $2$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} give both directions.

:::

:::

:::
