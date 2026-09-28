---
schema: qual/card@1
id: D-DEFFLAT
kind: definition
title: Flat modules
classification:
  areas:
  - algebraic-geometry
  topics:
  - Commutative Algebra
  - Flatness
  - Modules
relations:
- kind: uses
  target: D-DEFEXACT
review: draft
prompts:
- What is a flat module?
- Give a module that is torsion-free but not flat.
- How do free, projective, and flat compare?
---

::: {.definition title="flat"}
An $A$-module $N$ is \dfn{flat} if the functor $\wait \tensor_A N$ is exact.
A priori this functor is right exact, so the content of the definition is left exactness: for every injection $M' \injects M$, the induced map $M' \tensor_A N \to M \tensor_A N$ is again injective.
An $A$-algebra $B$ is flat if it is flat as an $A$-module.
:::

::: {.remark}
Free $\implies$ projective $\implies$ flat, and none of the implications reverses in general.
$\QQ$ is a flat $\ZZ$-module that is not projective; over a Noetherian local ring the three notions agree for finitely generated modules.

Over a domain, flat implies torsion-free, and the converse fails: $k[x,y]$-modules give the standard counterexample, with the ideal $(x,y)$ torsion-free but not flat.
Over a PID, though, flat and torsion-free do coincide.
Localisation $A \to S\inv A$ is always flat, which is the algebraic reason restriction to an open subscheme is exact.
:::
