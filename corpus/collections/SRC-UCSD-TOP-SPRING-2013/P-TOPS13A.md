---
schema: qual/card@1
id: P-TOPS13A
kind: problem
title: "Cohomology groups of a compact 7-manifold from partial homology data"
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Poincaré Duality
  - Universal Coefficient Theorem
  - Manifolds
relations: []
review: draft
---

::: {.problem}
Let $X$ be a compact $7$-dimensional manifold with
$$
H_7(X, \mathbb{Z}) \cong \mathbb{Z}, \quad H_6(X, \mathbb{Z}) \cong \mathbb{Z}, \quad H_5(X, \mathbb{Z}) \cong \mathbb{Z}/2\mathbb{Z}, \quad H_4(X, \mathbb{Z}) \cong \mathbb{Z} \oplus \mathbb{Z}/3\mathbb{Z}.
$$
Give all the information you can about the cohomology groups $H^*(X, \mathbb{Z})$.
:::

::: {.solution}

::: pf

::: pf-step
The hypothesis $H_7(X;\mathbb Z)\cong\mathbb Z$ implies that $X$ is closed, connected, and orientable, so Poincaré duality gives
$$
H^j(X;\mathbb Z)\cong H_{7-j}(X;\mathbb Z).
$$

::: pf-proof
A compact $7$-manifold with nonzero integral top homology has a closed orientable component; rank one top homology together with the manifold hypotheses gives the single connected orientable component relevant here. Cap product with its fundamental class gives integral Poincaré duality.
:::

:::

::: pf-step
Hence immediately
$$
H^0\cong\mathbb Z,\qquad H^1\cong\mathbb Z,\qquad H^2\cong\mathbb Z/2,\qquad H^3\cong\mathbb Z\oplus\mathbb Z/3.
$$

::: pf-proof
These are dual respectively to the given groups $H_7,H_6,H_5,H_4$.
:::

:::

::: {.pf-step #uct-forces-h1-h2}
The universal coefficient theorem forces
$$
H_1(X)\cong\mathbb Z\oplus\mathbb Z/2,\qquad H_2(X)\cong\mathbb Z/3.
$$

::: pf-proof
Since $H^1\cong\operatorname{Hom}(H_1,\mathbb Z)\cong\mathbb Z$, the free rank of $H_1$ is one. The exact sequence
$$
0\to\operatorname{Ext}(H_1,\mathbb Z)\to H^2\to\operatorname{Hom}(H_2,\mathbb Z)\to0
$$
with $H^2=\mathbb Z/2$ shows $H_2$ has no free part and the torsion subgroup of $H_1$ is $\mathbb Z/2$. Next,
$$
0\to\operatorname{Ext}(H_2,\mathbb Z)\to H^3\to\operatorname{Hom}(H_3,\mathbb Z)\to0
$$
shows $\operatorname{Ext}(H_2,\mathbb Z)=\mathbb Z/3$, hence $H_2\cong\mathbb Z/3$, and that $H_3$ has free rank one.
:::

:::

::: {.pf-step #h3-free-rank}
Write
$$
H_3(X)\cong\mathbb Z\oplus T
$$
with $T$ finite. The stated data do not determine $T$ further.

::: pf-proof
Finite generation holds for compact manifolds. The calculation in step [](#uct-forces-h1-h2){.pf-ref} fixes only the free rank of $H_3$. Middle-dimensional torsion is self-paired by the torsion linking form in dimension seven, so the already stated homology groups impose no additional isomorphism type on $T$.
:::

:::

::: pf-step
Poincaré duality now gives the remaining cohomology groups:
$$
\boxed{
H^j(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&j=0,1,7,\\
\mathbb Z/2,&j=2,\\
\mathbb Z\oplus\mathbb Z/3,&j=3,\\
\mathbb Z\oplus T,&j=4,\\
\mathbb Z/3,&j=5,\\
\mathbb Z\oplus\mathbb Z/2,&j=6,\\
0,&\text{otherwise},
\end{cases}}
$$
where $T$ is an undetermined finite abelian group.

::: pf-proof
Use $H^j\cong H_{7-j}$ together with steps [](#uct-forces-h1-h2){.pf-ref}--[](#h3-free-rank){.pf-ref} and the given high-degree homology groups.
:::

:::

:::
:::
