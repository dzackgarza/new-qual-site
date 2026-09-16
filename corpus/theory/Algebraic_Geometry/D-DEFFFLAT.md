---
schema: qual/card@1
id: D-DEFFFLAT
kind: definition
title: Faithfully flat modules, and descent of exactness
classification:
  areas:
  - algebraic-geometry
  topics:
  - Commutative Algebra
  - Flatness
relations:
- kind: uses
  target: D-DEFFLAT
review: draft
prompts:
- What is a faithfully flat module, and how does it differ from a flat one?
- Give a flat module that is not faithfully flat.
---

::: {.definition title="faithfully flat"}
An $A$-module $N$ is \dfn{faithfully flat} if for every complex of $A$-modules
\[
M' \to M \to M''
\]
the complex is exact **if and only if**
\[
M' \tensor_A N \to M \tensor_A N \to M'' \tensor_A N
\]
is exact.
Flatness gives only one direction of this equivalence.
An $A$-algebra $B$ is faithfully flat if it is so as an $A$-module.
:::

::: {.remark}
Equivalently, $N$ is flat and $M \tensor_A N = 0$ forces $M = 0$; for an algebra $A \to B$ this is flatness plus surjectivity of $\Spec B \to \Spec A$.

$\QQ$ is flat over $\ZZ$ but not faithfully flat, since it kills every torsion module --- localisation is the standard source of flat-but-not-faithfully-flat maps, because it discards the primes it inverts.
The reason to care is descent: over a faithfully flat extension, exactness, and with more work many other properties, may be checked after base change and then pulled back down.
:::
