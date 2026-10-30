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
H_7(X, \ZZ) \cong \ZZ, \quad H_6(X, \ZZ) \cong \ZZ, \quad H_5(X, \ZZ) \cong \ZZ/2\ZZ, \quad H_4(X, \ZZ) \cong \ZZ \oplus \ZZ/3\ZZ.
$$
Give all the information you can about the cohomology groups $H^*(X, \ZZ)$.
:::

::: {.solution}

::: pf

::: pf-step
The hypothesis $H_7(X;\ZZ)\cong\ZZ$ implies that $X$ is closed, connected, and orientable, so Poincaré duality gives
$$
H^j(X;\ZZ)\cong H_{7-j}(X;\ZZ).
$$

::: pf-proof
A compact $7$-manifold with nonzero integral top homology has a closed orientable component; rank one top homology together with the manifold hypotheses gives the single connected orientable component relevant here. Cap product with its fundamental class gives integral Poincaré duality.
:::

:::

::: pf-step
Hence immediately
$$
H^0\cong\ZZ,\qquad H^1\cong\ZZ,\qquad H^2\cong\ZZ/2,\qquad H^3\cong\ZZ\oplus\ZZ/3.
$$

::: pf-proof
These are dual respectively to the given groups $H_7,H_6,H_5,H_4$.
:::

:::

::: {.pf-step #uct-forces-h1-h2}
The universal coefficient theorem forces
$$
H_1(X)\cong\ZZ\oplus\ZZ/2,\qquad H_2(X)\cong\ZZ/3.
$$

::: pf-proof
Since $H^1\cong\operatorname{Hom}(H_1,\ZZ)\cong\ZZ$, the free rank of $H_1$ is one. The exact sequence
$$
0\to\operatorname{Ext}(H_1,\ZZ)\to H^2\to\operatorname{Hom}(H_2,\ZZ)\to0
$$
with $H^2=\ZZ/2$ shows $H_2$ has no free part and the torsion subgroup of $H_1$ is $\ZZ/2$. Next,
$$
0\to\operatorname{Ext}(H_2,\ZZ)\to H^3\to\operatorname{Hom}(H_3,\ZZ)\to0
$$
shows $\operatorname{Ext}(H_2,\ZZ)=\ZZ/3$, hence $H_2\cong\ZZ/3$, and that $H_3$ has free rank one.
:::

:::

::: {.pf-step #h3-free-rank}
Write
$$
H_3(X)\cong\ZZ\oplus T
$$
with $T$ finite. The stated data do not determine $T$ further.

::: pf-proof
Finite generation holds for compact manifolds. The calculation in step [](#uct-forces-h1-h2){.pf-ref} fixes only the free rank of $H_3$. The torsion of $H_3$ is paired only with itself, by the torsion linking form $T\times T\to\QQ/\ZZ$, so none of the other given groups constrains it. That form is nonsingular and skew-symmetric in dimension $7$, which forces the odd-order part of $T$ to have the form $A\oplus A$; beyond this the data say nothing about $T$.
:::

:::

::: pf-step
Poincaré duality now gives the remaining cohomology groups:
$$
\boxed{
H^j(X;\ZZ)\cong
\begin{cases}
\ZZ,&j=0,1,7,\\
\ZZ/2,&j=2,\\
\ZZ\oplus\ZZ/3,&j=3,\\
\ZZ\oplus T,&j=4,\\
\ZZ/3,&j=5,\\
\ZZ\oplus\ZZ/2,&j=6,\\
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
