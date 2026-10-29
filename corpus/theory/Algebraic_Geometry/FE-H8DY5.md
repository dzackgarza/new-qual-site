---
schema: qual/card@1
id: FE-H8DY5
kind: example
title: The line with doubled origin, and dropping each hypothesis
classification:
  areas:
  - algebraic-geometry
  topics:
  - Separated Morphisms
  - Reduced Schemes
  - Counterexamples
relations:
- kind: uses
  target: PR-QX0VL
review: draft
prompts:
- Give an example of a non-separated morphism.
- Give two morphisms agreeing on a dense open that are not equal.
---

::: {.example title="Not separated"}
Glue two copies of $\AA^1_k$ along $\AA^1 \sm \theset{0}$ by the identity.
The result $X$ has two origins, and $X \to \Spec k$ is not separated: the two inclusions $\AA^1 \to X$ agree on the dense open $\AA^1 \sm \theset{0}$ and differ at $0$, so the agreement locus is not closed.

Here the source $\AA^1$ is reduced, so the conclusion of [[PR-QX0VL]] fails only because $X$ is not separated.
:::

::: {.example title="Separated but not reduced"}
Let
$$
Z
=
\Spec A,
\qquad
A
=
k[t,\varepsilon]/(\varepsilon^2,t\varepsilon),
$$
and let $X=\AA^1_k=\Spec k[x]$.
Define $g,h\colon Z\to X$ by the ring maps
$$
g^\sharp(x)=0,
\qquad
h^\sharp(x)=\varepsilon.
$$
They are distinct because $\varepsilon\neq0$ in $A$.
On the dense open $D(t)\subseteq Z$, however, $t$ is invertible and the relation $t\varepsilon=0$ forces $\varepsilon=0$, so
$$
\restrictionof{g}{D(t)}
=
\restrictionof{h}{D(t)}.
$$
Thus the reducedness hypothesis cannot be removed even when the target is separated and the two morphisms agree on a genuine dense open subscheme.
:::

::: {.remark}
The two examples separate the roles of separatedness and reducedness.
The doubled line is also a standard example of a scheme that is not a classical variety, showing why separatedness is imposed in the scheme-theoretic definition of a variety.
:::
