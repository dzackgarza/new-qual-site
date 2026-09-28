---
schema: qual/card@1
id: P-IPPQ6
kind: problem
title: Consider a nonconstant function between two compact Riemann Surfaces.
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Geometry
relations: []
review: draft
---

::: {.problem}
Consider a nonconstant function between two compact Riemann Surfaces.
How is it related to Galois theory?
:::


::: {.solution}
Let
\[
f:X\longrightarrow Y
\]
be a nonconstant holomorphic map of compact Riemann surfaces. Pullback of meromorphic functions gives an injective field homomorphism
\[
f^*:\CC(Y)\hookrightarrow\CC(X),
\qquad h\longmapsto h\circ f.
\]
Thus geometry reverses arrows: a map of compact Riemann surfaces determines an extension of their meromorphic function fields.

Because $f$ is nonconstant and $X,Y$ are compact, $f$ is a finite branched covering. Correspondingly,
\[
\CC(X)/f^*\CC(Y)
\]
is a finite extension, and its field degree equals the degree of the map:
\[
[\CC(X):f^*\CC(Y)]=\deg(f).
\]
This is the one-dimensional complex-analytic instance of the anti-equivalence between compact Riemann surfaces and transcendence-degree-one function fields over $\CC$.

The Galois-theoretic symmetry is also geometric. A deck transformation $\gamma:X\to X$ satisfying
\[
f\circ\gamma=f
\]
acts on meromorphic functions by pullback and fixes $f^*\CC(Y)$. Hence
\[
\operatorname{Deck}(f)
\cong
\Aut_{\CC(Y)}\bigl(\CC(X)\bigr).
\]
If the finite function-field extension is Galois, then the corresponding branched covering is a Galois (regular) covering in this sense, and its deck-transformation group is the field-theoretic Galois group.

Thus finite extensions of function fields of compact Riemann surfaces, their intermediate fields, and their automorphism groups are the algebraic counterparts of finite holomorphic maps, their factorizations through intermediate surfaces, and their deck symmetries.
:::
