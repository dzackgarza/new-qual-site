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
Under the theorem's hypotheses, the Čech complex computes derived-functor cohomology: affines have no higher cohomology for quasicoherent sheaves, and separatedness makes the intersections affine too.

Consequently, a Noetherian separated scheme covered by $n+1$ affines has $H^p(X,\mcf) = 0$ for $p > n$ and every quasicoherent $\mcf$.
On $\PP^n$ with the standard $n+1$ charts this gives vanishing above degree $n$ before any computation is done.
:::
