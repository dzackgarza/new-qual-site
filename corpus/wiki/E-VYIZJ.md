---
schema: qual/card@1
id: E-VYIZJ
kind: exercise
title: 'Fixed points: multiple'
classification:
  areas:
  - complex-analysis
  topics:
  - Fixed Points
  - Schwarz Lemma
  - Blaschke Factors
relations: []
review: draft
---

::: {.exercise}
Show that the only holomorphic map $f:\DD\to \DD$ two distinct fixed points $a\neq b$ is the identity.
:::

::: {.solution}
Note that without loss of generality we can assume $a=0$ so $f(0) = 0$ and $b\neq 0$.
If not, if $a,b\neq 0$ then let $F\da \psi_a \circ f \circ \psi_a$, then $F(0) = 0$ and $F(b') = b'$ for $b\da \psi_a(b)$.

Since $f(0) = 0$, Schwarz applies, so $\abs{f(z)} = \abs{z}$ with equality attained because $\abs{f(b)} = \abs{b}$, and $f(z) = \lambda z$ must be a rotation.
Since $b = f(b) = \lambda b$, we have $\lambda = 1$.
:::
