---
schema: qual/card@1
id: E-M50FF
kind: problem
title: Transitivity of the subspace topology
classification:
  areas:
  - topology
  topics:
  - Subspace Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §16 Exercise 1, printed p. 91, with the
    definition of the subspace topology on printed p. 88; the stored statement is the
    printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 16.1, printed p. 149.
    The content is his: A inherits from Y the sets A cap (Y cap U) and from X the sets A cap
    U, and these agree because A is contained in Y. (tmp/sources/munkres-solutions-
    whitman.pdf).
---

::: {.exercise}

Show that if $Y$ is a subspace of $X$, and $A$ is a subset of $Y$, then the topology $A$ inherits as a subspace of $Y$ is the same as the topology it inherits as a subspace of $X$.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 16.1, printed p. 149** (`tmp/sources/munkres-solutions-whitman.pdf`); the proof is his.

Let $\mathcal{T}$ be the topology of $X$, let $\mathcal{T}_{Y}=\{Y\cap U\mid U\in\mathcal{T}\}$ be the subspace topology of $Y$, and let
$$
\mathcal{T}_{A}=\{A\cap V\mid V\in\mathcal{T}_{Y}\},\qquad \mathcal{T}_{A}'=\{A\cap U\mid U\in\mathcal{T}\}
$$
be the topologies that $A$ inherits from $Y$ and from $X$ respectively. We show $\mathcal{T}_{A}=\mathcal{T}_{A}'$.

If $W\in\mathcal{T}_{A}$ then $W=A\cap V$ with $V=Y\cap U$, $U\in\mathcal{T}$, so
$$
W=A\cap(Y\cap U)=(A\cap Y)\cap U=A\cap U
$$
because $A\subset Y$; hence $W\in\mathcal{T}_{A}'$. Conversely, if $W\in\mathcal{T}_{A}'$ then $W=A\cap U$ with $U\in\mathcal{T}$, and $V=Y\cap U\in\mathcal{T}_{Y}$ satisfies
$$
W=A\cap U=(A\cap Y)\cap U=A\cap(Y\cap U)=A\cap V\in\mathcal{T}_{A}.
$$
So each of the two topologies contains the other, and they are equal.
:::
