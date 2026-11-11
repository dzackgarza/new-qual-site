---
schema: qual/card@1
id: E-4RF8O
kind: problem
title: Finite fixed-point-free actions are properly discontinuous
classification:
  areas:
  - topology
  topics:
  - Covering Transformations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 81 Exercise 4, printed p. 493. A finite fixed-point-free action of a Hausdorff space is properly discontinuous, by separating each point from its finitely many images. Checked against the definition of properly discontinuous, printed p. 488. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Step-by-step check against the printed pages, and the repair. Corrected: the definition of a properly discontinuous action is on printed p. 490, not p. 488 as the previous note said. Corrected: the old solution was not a Lamport proof at all -- its steps carried indented prose labelled "Proof:" instead of pf-proof blocks, the last top-level step had no proof, and a literal "Q.E.D." was typed into the text, which the filter writes itself. The proof is now a proper pf block: one step separating the point from each of its finitely many images, one step taking the finite intersection, and the conclusion as the final step. Every step cites Munkres by number and page: the definition of a proper discontinuity (printed p. 490), the Hausdorff condition (printed p. 98), the closedness of the topology under finite intersections (printed p. 76), and the continuity of each element of $G$, which is a homeomorphism (printed p. 105). What the certificate does not cover: nothing in the exercise needs X to be path connected, and the proof does not use it.
---

::: {.exercise}

Let $G$ be a group of homeomorphisms of $X$.
The action of $G$ on $X$ is said to be fixed-point free if no element of $G$ other than the identity $e$ has a fixed point.
Show that if $X$ is Hausdorff, and if $G$ is a finite group of homeomorphisms of $X$ whose action is fixed-point free, then the action of $G$ is properly discontinuous.

:::

::: {.solution}

The action of $G$ on $X$ is properly discontinuous if for each $x \in X$ there is a neighbourhood $U$ of $x$ with $g(U) \cap U = \varnothing$ for every $g \ne e$ (printed p. 490).

::: pf

::: {.pf-step #single}

For each $g \in G$ with $g \neq e$ there is an open neighbourhood $U_g$ of $x$ with $g(U_g) \cap U_g = \varnothing$.

::: pf-proof

::: {.pf-step}

$g(x) \neq x$.

::: {.pf-proof}

The action is fixed-point free, so no element of $G$ other than $e$ has a fixed point; a fixed point of $g$ is a point $y$ with $g(y) = y$.

:::

:::

::: {.pf-step}

There are disjoint open sets $V_g$ and $W_g$ with $x \in V_g$ and $g(x) \in W_g$.

::: {.pf-proof}

$X$ is Hausdorff, that is, distinct points have disjoint open neighbourhoods (Definition, printed p. 98), and $g(x) \ne x$.

:::

:::

::: {.pf-step}

$U_g = V_g \cap g^{-1}(W_g)$ is an open neighbourhood of $x$, and $g(U_g) \cap U_g = \varnothing$.

::: {.pf-proof}

$g$ is a homeomorphism, hence continuous, so $g^{-1}(W_g)$ is open; it contains $x$ because $g(x) \in W_g$. An intersection of two open sets is open (Definition of a topology, printed p. 76), so $U_g$ is an open neighbourhood of $x$. For $y \in U_g$ one has $y \in V_g$ and $g(y) \in W_g$, so $g(y) \notin V_g$, and since $U_g \subseteq V_g$, also $g(y) \notin U_g$; hence $g(U_g) \cap U_g = \varnothing$.

:::

:::

:::

:::

::: {.pf-step}

$g(U) \cap U = \varnothing$ for every $g \ne e$, where $U$ is the intersection of the sets $U_g$ over the finitely many $g \ne e$.

::: {.pf-proof}

Write $G \setminus \{e\} = \{g_1, \dots, g_n\}$; this is a finite set because $G$ is finite. Let
$$
U = \bigcap_{i=1}^n U_{g_i}.
$$
A finite intersection of open sets is open (printed p. 76) and it contains $x$, so $U$ is a neighbourhood of $x$. For each $g_k \ne e$ one has $U \subseteq U_{g_k}$, hence
$$
g_k(U) \cap U \subseteq g_k(U_{g_k}) \cap U_{g_k} = \varnothing
$$
by step [](#single){.pf-ref}.

:::

:::

::: {.pf-step}

The action of $G$ on $X$ is properly discontinuous.

::: {.pf-proof}

For each $x \in X$ the neighbourhood $U$ just constructed satisfies $g(U) \cap U = \varnothing$ for every $g \neq e$, which is the definition of a properly discontinuous action (printed p. 490).

:::

:::

:::

:::
