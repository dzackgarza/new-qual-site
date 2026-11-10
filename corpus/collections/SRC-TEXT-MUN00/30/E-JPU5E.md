---
schema: qual/card@1
id: E-JPU5E
kind: problem
title: Lindelofness and separability pass to continuous images
classification:
  areas:
  - topology
  topics:
  - Countability
  - Continuous Functions
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Ana Emilia de Orellana, "Solutions -
    Topology Munkres", Section 30 Exercise 11, printed p. 31
    (tmp/sources/munkres-solutions-anadeore.pdf), checked against Munkres, Topology (2000),
    Section 30 Exercise 11, printed p. 194, and Theorem 18.1 for the preimage form of continuity.
    Doug's World, "Munkres - Topology - Chapter 4 Solutions", Problem 30.11, printed p. 3, proves
    the same two implications. Corrections: Orellana closes the separable half with the garbled
    display "f(D) = f(D) == f(X)", which asserts the conclusion rather than deriving it; the card
    derives it from an arbitrary nonempty open W of f(X), whose preimage is nonempty open in X and
    therefore meets D. Her Lindelof half also passes through a cover of f(X) by sets "open in X";
    the card uses a cover of f(X) by sets open in f(X) and their preimages under f, which are open
    in X, and then uses surjectivity of f onto f(X).
---

::: {.exercise}

Let $f: X \to Y$ be continuous.
Show that if $X$ is Lindelöf, or if $X$ has a countable dense subset, then $f(X)$ satisfies the same condition.
:::

::: {.solution}
Write $Z=f(X)$ with the subspace topology.

If $X$ is Lindelöf and $\{U_i\}_{i\in I}$ is an open cover of $Z$, then $\{f^{-1}(U_i)\}_{i\in I}$ is an open cover of $X$. Choose a countable subcover $f^{-1}(U_{i_1}),f^{-1}(U_{i_2}),\dots$. Surjectivity of $f:X\to Z$ implies $U_{i_1},U_{i_2},\dots$ cover $Z$. Hence $Z$ is Lindelöf.

If $D\subset X$ is countable and dense, then $f(D)$ is countable. It is dense in $Z$: if $W\subset Z$ is nonempty open, then $f^{-1}(W)$ is nonempty open in $X$, so it meets $D$; hence $W$ meets $f(D)$. Thus $Z$ is separable.
:::
