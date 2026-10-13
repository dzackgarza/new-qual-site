---
schema: qual/card@1
id: T-COHBC
kind: theorem
title: Semicontinuity, constancy of $\chi$, and cohomology and base change
slogan: 'In a flat projective family, $h^i$ only jumps up, $\chi$ does not jump, and constant fibre cohomology gives base change and local freeness.'
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
In the setup above, if $T$ is reduced and $t \mapsto h^i(X_t,\mcf_t)$ is locally constant, then $R^i f_* \mcf$ is locally free and
$$
(R^i f_* \mcf)\tensor_{\OO_T} \kappa(t) \xrightarrow{\sim} H^i(X_t, \mcf_t)
$$
for every $t\in T$.
Without reducedness there is still Grothendieck's criterion: if the base change map in degree $i$ is surjective at $t$, it is an isomorphism near $t$, and $R^i f_* \mcf$ is locally free at $t$ exactly when the map in degree $i-1$ is surjective as well.
:::

::: {.remark}
Upper semicontinuity means that the loci
$$
\theset{t\in T\st h^i(X_t,\mcf_t)\geq r}
$$
are closed. Flatness makes the Euler characteristic locally constant, while constancy of a fixed $h^i$ on a reduced base is sufficient for local freeness and fibrewise base change in that degree. At a single point, the precise criterion is the surjectivity statement in the theorem above; constancy of all fibre dimensions is not necessary for an individual base-change map to be an isomorphism.

The standard specimen is a family of line bundles of degree $0$ on a curve: $h^0$ is $0$ at a general point and $1$ at the trivial bundle, a jump on a closed subset, while $\chi = 1 - g$ throughout.
At the trivial bundle this jump is the standard source of failure of the naive fibrewise base-change isomorphism.
:::
