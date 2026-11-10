---
schema: qual/card@1
id: E-QR3SP
kind: problem
title: The countable complement topology and an infinite complement collection
classification:
  areas:
  - topology
  topics:
  - Topological Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §13 Exercise 3, printed p. 83, with T_c as
    defined in Example 4, printed p. 77; the stored statement is the printed question.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 13.3, printed p. 142.
    From him: T_c is a topology, checked on the three axioms, and T_inf fails for X = Z_+
    with the family of singletons {2}, {3}, ... whose union misses only 1. He writes T_alpha
    for T_c; the card keeps the book's notation, and adds the empty-union case in the union
    axiom, which his sentence leaves implicit. (tmp/sources/munkres-solutions-whitman.pdf).
---

::: {.exercise}

Show that the collection $\mathcal{T}_c$ given in Example 4 of §12 is a topology on the set $X$.
Is the collection

$$
\mathcal{T}_\infty = \theset{U \mid X - U \text{ is infinite or empty or all of } X}
$$

a topology on $X$?
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 13.3, printed p. 142** (`tmp/sources/munkres-solutions-whitman.pdf`); both halves are his. He writes $\mathcal{T}_{\alpha}$ for the collection the book calls $\mathcal{T}_{c}$; the notation of the book is kept below.

Recall from Example 4 of §12 that
$$
\mathcal{T}_{c}=\{U\subset X\mid X-U \text{ is countable or is all of } X\}.
$$

*$\mathcal{T}_{c}$ is a topology.* First, $X-\varnothing=X$ is all of $X$, so $\varnothing\in\mathcal{T}_{c}$, and $X-X=\varnothing$ is countable (finite), so $X\in\mathcal{T}_{c}$.

Let $\mathcal{A}\subset\mathcal{T}_{c}$ and let $U=\bigcup\mathcal{A}$. If $\mathcal{A}$ contains a nonempty member $A_{0}$, then $X-A_{0}$ is countable and
$$
X-U=X-\bigcup_{A\in\mathcal{A}}A=\bigcap_{A\in\mathcal{A}}(X-A)\subset X-A_{0},
$$
so $X-U$ is countable and $U\in\mathcal{T}_{c}$. If every $A\in\mathcal{A}$ is empty then $U=\varnothing\in\mathcal{T}_{c}$. So $\mathcal{T}_{c}$ is closed under arbitrary unions.

Let $U_{1},\dots,U_{n}\in\mathcal{T}_{c}$. Then
$$
X-\bigcap_{i=1}^{n}U_{i}=\bigcup_{i=1}^{n}(X-U_{i}).
$$
If some $X-U_{i}$ is all of $X$ then this union is $X$ and the intersection is empty, which lies in $\mathcal{T}_{c}$; otherwise each $X-U_{i}$ is countable and their finite union is countable, so the intersection lies in $\mathcal{T}_{c}$. Hence $\mathcal{T}_{c}$ is closed under finite intersections and is a topology on $X$.

*$\mathcal{T}_{\infty}$ is not in general a topology.* Take $X=\ZZ_{+}$ and consider
$$
\mathcal{T}_{\infty}=\{U\mid X-U \text{ is infinite or empty or all of } X\}.
$$
Every finite subset $U$ of $X$ has infinite complement, so every finite set is in $\mathcal{T}_{\infty}$; in particular $\{i\}\in\mathcal{T}_{\infty}$ for each $i\ge2$. But
$$
\bigcup_{i\ge2}\{i\}=\{2,3,4,\dots\}=X-\{1\},
$$
whose complement is $\{1\}$, which is neither infinite, nor empty, nor all of $X$; so the union does not belong to $\mathcal{T}_{\infty}$. The collection $\mathcal{T}_{\infty}$ therefore fails axiom (2) of a topology and is not a topology on $X$.
:::
