---
schema: qual/card@1
id: P-AMD-5A2VNO4E
kind: problem
title: Letters of the alphabet up to homeomorphism and homotopy
classification:
  areas:
  - topology
  topics:
  - Homeomorphisms
  - Homotopy
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Classify the capital letters of the alphabet up to homeomorphism, and up to homotopy.

Regard each letter as a finite graph in the plane, drawn in a standard sans-serif font: the leg of R is a segment that leaves the bowl at a point other than where the bowl meets the stem, the two arms of K meet each other at a point off the stem, the tail of Q is a segment attached to the circle at one point, and J has no top bar.
:::

::: {.hint}
Invariants that separate letters: the number of connected components after removing one or two points, and the presence of a nontrivial loop.
:::

::: {.solution}
Take the capital letters in a sans-serif font, drawn as finite graphs in the plane, with the following conventions: the leg of R leaves the bowl at a point other than where the bowl meets the stem, the two arms of K meet each other at a point off the stem, the tail of Q is attached to the circle at one point, and J has no top bar.
For a point $x$ of such a graph, the number of components of $U \setminus \{x\}$, for $U$ a small connected neighbourhood of $x$, is the degree of $x$; a homeomorphism preserves the degree of each point, and endpoints have degree $1$.

::: pf

::: {.pf-step #homotopy}
Up to homotopy there are three classes: $\{A, D, O, P, Q, R\} \simeq S^1$, $\{B\} \simeq S^1 \vee S^1$, and the remaining $19$ letters, which are contractible.

::: pf-proof
A connected finite graph is homotopy equivalent to a wedge of $r$ circles, where $r$ is the number of independent loops, and wedges of different numbers of circles have non-isomorphic $H_1 \cong \ZZ^r$.
The letters A, D, O, P, Q, and R contain exactly one loop, B contains two, and every other letter is a tree, hence contractible.
:::

:::

::: pf-step
Up to homeomorphism there are eight classes:

(i) $\{C, G, I, J, L, M, N, S, U, V, W, Z\}$, an arc;

(ii) $\{D, O\}$, a circle;

(iii) $\{P, Q\}$, a circle with one arc attached at one point;

(iv) $\{A, R\}$, a circle with two arcs attached at two distinct points;

(v) $\{B\}$, a wedge of two circles;

(vi) $\{E, F, T, Y\}$, three arcs joined at one point;

(vii) $\{X\}$, four arcs joined at one point;

(viii) $\{H, K\}$, two points of degree $3$ joined by an arc, each carrying two further arcs.

::: pf-proof
Each letter is homeomorphic to the model named in its class, because corners of the drawn letter are points of degree $2$ and can be straightened.
The models are pairwise non-homeomorphic: the number of loops is a homotopy invariant by step [](#homotopy){.pf-ref}, so, the classes split as $\{$(ii), (iii), (iv)$\}$, $\{$(v)$\}$, and the trees $\{$(i), (vi), (vii), (viii)$\}$.
Among the circles with arcs, (ii) has no point of degree $3$, (iii) has one, and (iv) has two.
Among the trees, (i) has no point of degree at least $3$, (vi) has one point of degree $3$, (vii) has one point of degree $4$, and (viii) has two points of degree $3$.
:::

:::

:::

:::
