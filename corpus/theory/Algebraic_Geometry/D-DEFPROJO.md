---
schema: qual/card@1
id: D-DEFPROJO
kind: definition
title: Projective objects and projective modules
classification:
  areas:
  - algebraic-geometry
  topics:
  - Homological Algebra
  - Projective Objects
  - Resolutions
relations:
- kind: uses
  target: D-DEFABCAT
- kind: related-to
  target: D-DEFINJOB
review: draft
prompts:
- What is a projective object in an abelian category?
- Which modules are projective, and how do projectives relate to free modules?
- Does the category of $\OO_X$-modules have enough projectives?
---

::: {.definition title="projective object"}
An object $P$ in an abelian category is \dfn{projective} if the functor $\Hom(P, \wait)$ is exact.
Equivalently, every map $P \to B$ lifts along any epimorphism $A \surjects B$.
In $\mods{A}$ these are the \dfn{projective modules}, and free modules are projective.
:::

::: {.remark}
A module is projective if and only if it is a direct summand of a free module.
Over a local ring or a PID, projective modules are free; over $\ZZ/6$ the summand $\ZZ/2$ is projective and not free.
$\mods{A}$ has enough projectives, since every module is a quotient of a free one; so the left derived functors of every right exact additive functor on $\mods{A}$, such as $\Tor$, are defined.

For $X=\PP^1_k$, neither $\mods{\OO_X}$ nor the category of quasicoherent $\OO_X$-modules has enough projectives [@Har10a, Exercise III.6.2], whereas $\mods{\OO_X}$ has enough injectives on every ringed space [@Har10a, Proposition III.2.2].
:::
