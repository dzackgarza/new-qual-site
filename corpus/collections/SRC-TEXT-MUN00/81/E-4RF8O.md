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
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Munkres §81 Exercise 4, printed p. 493. Searched outside the checkout for issue #146; the record is
    tmp/sources/mse-searches-146.md and the saved sources are tmp/sources/mse-412317-E-4RF8O.md,
    tmp/sources/mse-3172278-E-4RF8O.md and tmp/sources/gh-dyang5-MATH104-Topology-E-4RF8O.md, all read
    whole. Three published proofs of the exercise were located, all of them the finite-intersection
    separation argument: martini's answer 412360 (2013-06-05) to question 412317, answer 3534338 by Kuldeep
    Guha Mazumder (2020-02-04) to question 3172278, and David Yang's MATH104 Fall 2023 Homework 11
    HW/hw11.tex lines 127-153. The card now names martini's answer as the argument its steps write out, and
    records a typo in it: line 25 of the saved file reads "there are open neighbourhoods U_g of x, V_g of
    g-bar x such that U_g cap V_g neq empty", where Hausdorffness gives "= empty"; the intersection and the
    computation that follow in the same answer use the equality, so the inequality is a slip and the argument
    is sound. The other two proofs are recorded beside it. The card's own proof is unchanged.
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

The separation argument below is that of martini's accepted answer 412360 (https://math.stackexchange.com/a/412360), posted 2013-06-05 to Math Stack Exchange question 412317, "Finite group acting freely on Hausdorff space" (https://math.stackexchange.com/questions/412317, asked by alans on the same day), which states the exercise as its three parts (a), (b), (c): for each $g\ne e$ choose disjoint open sets $U_g\ni x$ and $V_g\ni g(x)$, replace $U_g$ by $U_g\cap g^{-1}(V_g)$, and intersect over the finitely many $g\ne e$ at once. The answer prints "such that $U_g\cap V_g\ne\emptyset$" where the Hausdorff choice gives "$=\emptyset$"; the intersection $\bigcap_{h\ne e}(U_h\cap\bar h^{-1}V_h)$ that it then forms and the computation $gU\cap U\subseteq \bar g\bar g^{-1}V_g\cap U_g=\emptyset$ use the equality, so the printed inequality is a slip in the answer and not a step of the argument. The steps below are that argument written out with the book's citations. Two other threads prove the same statement: answer 3534338 by Kuldeep Guha Mazumder (2020-02-04) to question 3172278, which separates the finitely many points of an orbit by induction and takes the intersection $E=\bigcap_i g_i^{-1}E_i$; and answer 3172451 by Adam Bartoš in the same thread, which is a single sentence of hint.

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
