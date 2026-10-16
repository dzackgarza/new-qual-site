---
schema: qual/card@1
id: P-XTPAP
kind: problem
title: Homotopy and homeomorphism types of the letters of the alphabet
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Homeomorphism
relations: []
review: draft
---

::: {.problem}
Classify the letters of the alphabet up to homeomorphism, and up to homotopy.
:::

::: {.hint}
Invariants that separate letters: the number of connected components after removing one or two points, and the presence of a nontrivial loop.
:::

::: {.solution}
Up to homotopy (ignoring font-dependent ligatures), each capital letter deformation-retracts onto one of: a point, $S^1$, $S^1\vee S^1$, or a two-point space.

- $\{A, D, O, P, Q, R\}$ and the lowercase letters $\{a, b, d, e, g, o, p, q\}$ are homotopy equivalent to $S^1$: each carries exactly one loop.
- $\{B\}$ is homotopy equivalent to $S^1\vee S^1$: two loops joined at a junction.
- The letters $\{i, j\}$, drawn with detached dots, are homotopy equivalent to a two-point discrete space $\{*_1, *_2\}$.
- Every remaining letter — $\{C, E, F, G, H, I, J, K, L, M, N, S, T, U, V, W, X, Y, Z\}$ and the dotless lowercase forms — is contractible.

Up to homeomorphism, more invariants survive, since homotopy equivalence collapses the wire graphs:

1. $\{A, R\}$: removing the junction point yields two components homeomorphic to $I$ and $F$ respectively.
2. $\{D, O\}$: no single point removal disconnects the space; each is homeomorphic to $S^1$.
3. $\{B\}$: removing the junction point of $S^1\vee S^1$ yields two arcs.
4. $\{C, G, I, J, L, M, N, S, U, V, W, Z\}$: each has a point whose removal yields exactly two components and none yielding three — each is a straight wire up to twisting, homeomorphic to $[0,1]$.
5. $\{E, F, T, Y\}$: each has a point (the pasting point of the vee) whose removal yields three components homeomorphic to $I$; these are homeomorphic to $\bigvee_{i=1}^3[0,1]$.
6. $\{H, K\}$: removing two points disconnects into five components; homeomorphic to $\bigvee_{i=1}^5[0,1]$.
7. $\{P, Q\}$: each contains a nontrivial loop with an attached arc; homeomorphic to $S^1\vee[0,1]$.
8. $\{X\}$: removing one point yields four components; homeomorphic to $\bigvee_{i=1}^4[0,1]$.

The classifications depend on the chosen font: a lowercase letter may have one or two components depending on whether its dot is detached.
:::