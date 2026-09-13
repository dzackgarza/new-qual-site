---
schema: qual/card@1
id: T-COHBC
kind: theorem
title: Semicontinuity, constancy of $\chi$, and cohomology and base change
classification:
  areas:
  - algebraic-geometry
  topics:
  - Base Change
  - Semicontinuity
  - Flat Families
relations:
- kind: uses
  target: T-COHFF
- kind: uses
  target: D-COHEULER
review: draft
prompts:
- State the semicontinuity theorem.
- When does cohomology commute with base change?
- What is Grauert's theorem?
---

::: {.theorem title="Semicontinuity"}
Let $f: X \to T$ be projective with $T$ Noetherian and $\mcf$ coherent on $X$, flat over $T$.
Then $t \mapsto h^i(X_t, \mcf_t)$ is upper semicontinuous on $T$, and $t \mapsto \chi(\mcf_t)$ is locally constant.
:::

::: {.theorem title="Grauert and base change"}
If $T$ is reduced and $t \mapsto h^i(X_t,\mcf_t)$ is constant, then $R^i f_* \mcf$ is locally free and
\[
R^i f_* \mcf \tensor k(t) \iso H^i(X_t, \mcf_t)
\]
for all $t$.
Without reducedness there is still Grothendieck's criterion: if the base change map in degree $i$ is surjective at $t$, it is an isomorphism near $t$, and $R^i f_* \mcf$ is locally free at $t$ exactly when the map in degree $i-1$ is surjective as well.
:::

::: {.remark}
The shape to hold: individual $h^i$ can only *jump up* on closed subsets, the alternating sum cannot jump at all, and cohomology commutes with restriction to a fibre exactly when nothing jumps.

Flatness is the load-bearing hypothesis throughout, and dropping it destroys even the constancy of $\chi$.
Reducedness of the base is what Grauert needs, and it is where non-reduced bases genuinely fail.

The standard specimen is a family of line bundles of degree $0$ on a curve: $h^0$ is $0$ at a general point and $1$ at the trivial bundle, a jump on a closed subset, while $\chi = 1 - g$ throughout.
That single example answers "give an example where cohomology does not commute with base change".
:::
