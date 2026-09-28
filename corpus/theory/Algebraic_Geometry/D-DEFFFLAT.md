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
$$
M' \to M \to M''
$$
the complex is exact if and only if
$$
M' \tensor_A N \to M \tensor_A N \to M'' \tensor_A N
$$
is exact.
An $A$-algebra $B$ is faithfully flat if it is so as an $A$-module.
:::

::: {.remark}
A flat module satisfies the implication from exactness of the first complex to exactness of the second.
Equivalently, $N$ is faithfully flat if and only if $N$ is flat and $M \tensor_A N = 0$ implies $M = 0$; for an algebra $A \to B$, faithful flatness is equivalent to flatness together with surjectivity of $\Spec B \to \Spec A$.

$\QQ$ is flat over $\ZZ$ but not faithfully flat, since $\ZZ/p\tensor_\ZZ\QQ=0$.
More generally, for a multiplicative subset $S\subseteq A$, $A\to S^{-1}A$ is flat, and it is faithfully flat only if $\Spec S^{-1}A\to\Spec A$ is surjective, which fails when some $s\in S$ lies in a prime ideal of $A$.
If $A\to B$ is faithfully flat, then an $A$-module $M$ is zero, finitely generated, or flat if and only if $M\tensor_AB$ is.
:::
