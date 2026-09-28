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
An $A$-algebra $B$ is flat if it is flat as an $A$-module.
:::

::: {.remark}
Since $\wait \tensor_A N$ is right exact, $N$ is flat if and only if for every injection $M' \injects M$, the induced map $M' \tensor_A N \to M \tensor_A N$ is injective.

Free $\implies$ projective $\implies$ flat, and neither implication reverses in general.
Over $A=\ZZ/6$, the module $\ZZ/2$ is projective, being a direct summand of $A\cong\ZZ/2\times\ZZ/3$, and not free.
$\QQ$ is a flat $\ZZ$-module that is not projective; over a Noetherian local ring the three notions agree for finitely generated modules.

Over a domain, flat implies torsion-free.
The ideal $(x,y)$ of $k[x,y]$ is torsion-free but not flat: its localization at $(x,y)$ is finitely generated over a Noetherian local ring and not free, since it has rank $1$ and needs two generators.
Over a PID, flat and torsion-free coincide.
Localisation $A \to \inverseof{S} A$ is flat; so on $\Spec A$, the functor $M\mapsto M_f=\Gamma(D(f),\widetilde M)$ is exact.
:::
