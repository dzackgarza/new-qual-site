---
schema: qual/card@1
id: D-PTIW0
kind: definition
title: Čech cohomology, and when it is the right cohomology
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Cech Cohomology
relations:
- kind: uses
  target: PR-C9ZEK
review: draft
prompts:
- Define Čech cohomology.
- When does Čech cohomology agree with derived functor cohomology?
- What is the Leray map, and for which covers is it an isomorphism?
- How does Čech cohomology of a Noetherian separated scheme compare with derived functor cohomology, and with singular cohomology?
---

::: {.definition title="Čech complex"}
For a cover $\mcu = \ts{U_i}$ of $X$ and a sheaf $\mcf$, put
\[
C^p(\mcu, \mcf) = \prod_{i_0 < \cdots < i_p} \mcf(U_{i_0} \intersect \cdots \intersect U_{i_p}) ,
\]
with the alternating-sum differential.
$\check{H}^p(\mcu,\mcf)$ is its cohomology.
:::

::: {.definition title="Leray map"}
For any open cover $\mcu$ of $X$ and sheaf of abelian groups $\mcf$ there is a natural map
\[
\check{H}^p(\mcu, \mcf) \to H^p(X, \mcf),
\]
the \dfn{Leray map}, induced by comparing the Čech resolution of $\mcf$ by the sheaves $\prod j_* \mcf|_{U_{i_0 \cdots i_p}}$ with an injective resolution.
It is always an isomorphism in degree $0$ and injective in degree $1$, and it is an isomorphism in all degrees when $H^q(U_{i_0} \cap \cdots \cap U_{i_p}, \mcf) = 0$ for all $q > 0$ and all finite intersections.
:::

::: {.theorem title="Leray"}
If $X$ is Noetherian and separated, $\mcu$ is a finite affine open cover, and $\mcf$ is quasicoherent, then
\[
\check{H}^p(\mcu,\mcf) \cong H^p(X,\mcf)
\]
for all $p$.
:::

::: {.remark}
Derived functor cohomology is what the theory is defined by and Čech cohomology is what one computes with, so the agreement theorem is the bridge every computation crosses.
Its hypotheses are the ones that make the cover good enough: affines have no higher cohomology for quasicoherent sheaves, and separatedness makes the intersections affine too.

The practical consequence is a bound that is often the fastest route to a vanishing statement: a scheme covered by $n+1$ affines has $H^p = 0$ for $p > n$ and all quasicoherent $\mcf$.
On $\PP^n$ with the standard $n+1$ charts this gives vanishing above degree $n$ before any computation is done.
:::

::: {.remark}
The affine hypothesis on the cover cannot be dropped, even for a Noetherian separated scheme and a quasicoherent sheaf.
For the cover $\mcu = \{\PP^1\}$ of $\PP^1$ by itself, $\check{H}^1(\mcu, \OO(-2)) = 0$ because the Čech complex has a single term, while $H^1(\PP^1, \OO(-2)) \cong k$.
:::

::: {.remark}
For a Noetherian separated scheme the comparison is between Čech cohomology of an affine cover and derived-functor cohomology of a quasicoherent sheaf, both in the Zariski topology; singular cohomology does not enter.
Singular cohomology appears only for a variety $X$ over $\CC$ with its analytic topology: $H^i_{\mathrm{sing}}(X(\CC), \ZZ) \cong H^i(X^{an}, \ul{\ZZ})$.
In the Zariski topology the constant sheaf on an irreducible space is flasque, so $H^i(X, \ul{\ZZ}) = 0$ for $i > 0$, and Zariski cohomology of constant sheaves carries no topological information.
:::
