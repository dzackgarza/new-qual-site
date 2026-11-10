---
schema: qual/card@1
id: E-CFH1Q
kind: problem
title: Closed sets satisfy the topology axioms
classification:
  areas:
  - topology
  topics:
  - Closed Sets
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §17 Exercise 1, printed p. 100; the stored
    statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 17.1, printed p. 158.
    The content is his: X minus a union is the intersection of the complements and X minus a
    finite intersection is the finite union of the complements, so the three axioms transfer
    to T from the union and intersection axioms of C. (tmp/sources/munkres-solutions-
    whitman.pdf).
---

::: {.exercise}

Let $\mathcal{C}$ be a collection of subsets of the set $X$.
Suppose that $\varnothing$ and $X$ are in $\mathcal{C}$, and that finite unions and arbitrary intersections of elements of $\mathcal{C}$ are in $\mathcal{C}$.
Show that the collection

$$
\mathcal{T} = \theset{X - C \mid C \in \mathcal{C}}
$$

is a topology on $X$.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 17.1, printed p. 158** (`tmp/sources/munkres-solutions-whitman.pdf`); the argument is his, in the book's notation.

Let $\mathcal{T}=\{X-C\mid C\in\mathcal{C}\}$. Since $\varnothing=X-X$ and $X=X-\varnothing$ with $X,\varnothing\in\mathcal{C}$, both $\varnothing$ and $X$ lie in $\mathcal{T}$.

Let $\mathcal{A}\subset\mathcal{T}$ be arbitrary. For each $A\in\mathcal{A}$ choose $B_{A}\in\mathcal{C}$ with $A=X-B_{A}$, and put $\mathcal{B}=\{B_{A}\mid A\in\mathcal{A}\}\subset\mathcal{C}$. Then by De Morgan's law
$$
\bigcup_{A\in\mathcal{A}}A=\bigcup_{B\in\mathcal{B}}(X-B)=X-\bigcap_{B\in\mathcal{B}}B,
$$
and $\bigcap_{B\in\mathcal{B}}B\in\mathcal{C}$ because $\mathcal{C}$ is closed under arbitrary intersections; so the union lies in $\mathcal{T}$.

Let $A_{1},\dots,A_{n}\in\mathcal{T}$, say $A_{k}=X-B_{k}$ with $B_{k}\in\mathcal{C}$. Then
$$
\bigcap_{k=1}^{n}A_{k}=\bigcap_{k=1}^{n}(X-B_{k})=X-\bigcup_{k=1}^{n}B_{k},
$$
and $\bigcup_{k=1}^{n}B_{k}\in\mathcal{C}$ because $\mathcal{C}$ is closed under finite unions; so the finite intersection lies in $\mathcal{T}$.

Hence $\mathcal{T}$ satisfies the three defining properties of a topology on $X$.
:::
