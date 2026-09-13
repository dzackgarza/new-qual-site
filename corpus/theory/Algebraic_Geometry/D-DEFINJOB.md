---
schema: qual/card@1
id: D-DEFINJOB
kind: definition
title: Injective objects, injective resolutions, and enough injectives
classification:
  areas:
  - algebraic-geometry
  topics:
  - Homological Algebra
  - Injective Objects
  - Resolutions
relations:
- kind: uses
  target: D-DEFABCAT
- kind: uses
  target: D-DEFEXACT
review: draft
prompts:
- What is an injective object, and what is an injective resolution?
- When does a category have enough injectives, and why is that the standing hypothesis for derived functors?
- Do sheaves of $\OO_X$-modules have enough injectives?
---

::: {.definition title="injective object"}
An object $I$ of an abelian category $\mca$ is **injective** if $\Hom(\wait, I)$ is an exact contravariant functor from $\mca$ to abelian groups.

An **injective resolution** of $A$ is a complex $I^\bullet$ of injective objects with a map $A \to I^0$ such that
\[
0 \to A \to I^0 \to I^1 \to \cdots
\]
is exact.

If every object of $\mca$ is isomorphic to a subobject of an injective object, then $\mca$ **has enough injectives**.
:::

::: {.remark}
Concretely, injectivity is an extension property: any map $A \to I$ extends along any monomorphism $A \injects B$.
Over $\ZZ$ the injective objects are the divisible groups, so $\QQ$ and $\QQ/\ZZ$ are injective and no nonzero finitely generated abelian group is.

Enough injectives is what makes right derived functors exist.
$\mods{A}$ has enough injectives for every ring $A$, and so does $\mods{\OO_X}$ on any ringed space --- this last is Hartshorne III.2.2, and it is what licenses defining sheaf cohomology as $R^i\Gamma$.
The injectives it produces are enormous and useless for computation; flasque or otherwise acyclic resolutions are what one actually computes with.
:::
