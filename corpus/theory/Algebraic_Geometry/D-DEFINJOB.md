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
An object $I$ of an abelian category $\mca$ is \dfn{injective} if $\Hom(\wait, I)$ is an exact contravariant functor from $\mca$ to abelian groups.

An \dfn{injective resolution} of $A$ is a complex $I^\bullet$ of injective objects with a map $A \to I^0$ such that
$$
0 \to A \to I^0 \to I^1 \to \cdots
$$
is exact.

If every object of $\mca$ is isomorphic to a subobject of an injective object, then $\mca$ \dfn{has enough injectives}.
:::

::: {.remark}
An object $I$ is injective if and only if every map $A \to I$ extends along every monomorphism $A \injects B$.
Over $\ZZ$ the injective objects are the divisible groups, so $\QQ$ and $\QQ/\ZZ$ are injective and no nonzero finitely generated abelian group is.

If $\mca$ has enough injectives, every object has an injective resolution, so the right derived functors $R^iF$ of every left exact additive functor $F$ on $\mca$ are defined.
$\mods{A}$ has enough injectives for every ring $A$, and so does $\mods{\OO_X}$ on any ringed space [@Har10a, Proposition III.2.2]; hence $H^i(X,\wait)=R^i\Gamma(X,\wait)$ is defined on $\mods{\OO_X}$.
Flasque and other acyclic resolutions also compute the derived functors of global sections.
:::
