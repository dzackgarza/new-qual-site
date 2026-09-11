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
---

::: {.definition title="Čech complex"}
For a cover $\mcu = \ts{U_i}$ of $X$ and a sheaf $\mcf$, put
\[
C^p(\mcu, \mcf) = \prod_{i_0 < \cdots < i_p} \mcf(U_{i_0} \intersect \cdots \intersect U_{i_p}) ,
\]
with the alternating-sum differential.
$\check{H}^p(\mcu,\mcf)$ is its cohomology.
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
