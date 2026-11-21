---
schema: qual/card@1
id: E-MUN-6-7
kind: problem
title: Finiteness of function sets between finite sets
classification:
  areas:
  - topology
  topics:
  - Finite Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 6, Exercise 7; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §6 Exercise 7, printed p. 44; the stored
    statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 6.7,
    printed pp. 79-80 (tmp/sources/munkres-solutions-whitman.pdf). His bijection
    B^A -> B^n is g -> g o f^{-1} for a fixed bijection f : A -> {1,...,n}, which is the
    card's n-tuple correspondence; he treats the case A empty separately, as the card
    does. No defect found.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's prose into numbered steps; the bijection and the empty-set cases are
    Whitman's (Exercise 6.7, printed pp. 79-80), as the card cites. Checked: the bijection and its
    inverse, the finiteness of a finite product, and the two degenerate cases. Not checked: the
    cited pages, because tmp/sources holds no copy of the Whitman manual and the Munkres text is
    not retained in this VM.
---

::: {.exercise}

If $A$ and $B$ are finite, show that the set of all functions $f: A \to B$ is finite.
:::

::: {.solution}

The argument is that of the retained published solution: Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 6.7, printed ps 79-80, which the card cites; it is restructured into numbered steps below. His bijection $B^{A}\to B^{n}$, $g\mapsto g\circ f^{-1}$, is the $n$-tuple correspondence below, and he separates the case $A=\varnothing$ as the card does.

::: pf

::: {.pf-step #bij}

Choose a bijection $\sigma:\set{1,\dots,n}\to A$.

::: pf-proof

$\cardinality{A}=n$ means exactly that such a bijection exists.

:::

:::

::: {.pf-step #tuple}

$g\mapsto(g(\sigma(1)),\dots,g(\sigma(n)))$ is a bijection $B^{A}\to B^{n}$.

::: pf-proof

The recipe assigns to each function the $n$-tuple of its values on the enumeration of $A$. Two functions with the same tuple agree at every $\sigma(i)$ and hence, since $\sigma$ is surjective, at every point of $A$; and every $n$-tuple $(b_1,\dots,b_n)$ arises, from the function $g(\sigma(i))\coloneqq b_i$.

:::

:::

::: {.pf-step #finite}

$B^{n}$ is finite.

::: pf-proof

A finite product of finite sets is finite, by induction on $n$ from the case of two: $B\times B$ has $m^{2}$ elements, and $B^{n+1}=B^{n}\times B$.

:::

:::

::: {.pf-step #done}

The set $B^{A}$ of all functions $A\to B$ is finite.

::: pf-proof

It is in bijection with the finite set $B^{n}$ by step [](#tuple){.pf-ref}.

:::

:::

::: {.pf-step #empty}

The degenerate cases are finite as well.

::: pf-proof

If $A=\varnothing$ there is exactly one function $A\to B$, the empty function; if $B=\varnothing$ and $A\neq\varnothing$ there is none, since a function must assign a value in $B$. When $n,m>0$ the count is $\cardinality{B^{A}}=m^{n}$.

:::

:::

:::

:::
