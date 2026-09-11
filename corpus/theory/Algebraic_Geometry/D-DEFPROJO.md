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
An object $P$ in an abelian category is **projective** if the functor $\Hom(P, \wait)$ is exact.
Equivalently, every map $P \to B$ lifts along any epimorphism $A \surjects B$.
In $\mods{A}$ these are the **projective modules**, and free modules are projective.
:::

::: {.remark}
A module is projective iff it is a direct summand of a free module, so over a local ring or a PID projective and free coincide, while over $\ZZ/6$ the summand $\ZZ/2$ is projective and not free.
$\mods{A}$ always has enough projectives, since every module is a quotient of a free one; this is why $\Tor$ and left derived functors are available for modules.

The asymmetry worth remembering: $\mods{\OO_X}$ generally does **not** have enough projectives, which is precisely why sheaf cohomology is built from injectives rather than from the more computable projective side.
:::
