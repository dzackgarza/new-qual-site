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
For a cover $\mathcal{U} = \ts{U_i}$ of $X$ and a sheaf $\mathcal{F}$, put
\[
C^p(\mathcal{U}, \mathcal{F}) = \prod_{i_0 < \cdots < i_p} \mathcal{F}(U_{i_0} \intersect \cdots \intersect U_{i_p}) ,
\]
with the alternating-sum differential.
$\check{H}^p(\mathcal{U},\mathcal{F})$ is its cohomology.
:::

::: {.theorem title="Leray"}
If $X$ is Noetherian and separated, $\mathcal{U}$ is a finite affine open cover, and $\mathcal{F}$ is quasicoherent, then
\[
\check{H}^p(\mathcal{U},\mathcal{F}) \cong H^p(X,\mathcal{F})
\]
for all $p$.
:::

::: {.remark}
Derived functor cohomology is what the theory is defined by and Čech cohomology is what one computes with, so the agreement theorem is the bridge every computation crosses.
Its hypotheses are the ones that make the cover good enough: affines have no higher cohomology for quasicoherent sheaves, and separatedness makes the intersections affine too.

The practical consequence is a bound that is often the fastest route to a vanishing statement: a scheme covered by $n+1$ affines has $H^p = 0$ for $p > n$ and all quasicoherent $\mathcal{F}$.
On $\PP^n$ with the standard $n+1$ charts this gives vanishing above degree $n$ before any computation is done.
:::
