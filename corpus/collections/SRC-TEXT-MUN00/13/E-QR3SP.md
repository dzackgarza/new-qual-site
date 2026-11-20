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
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf`
    with seven steps, four for the topology axioms of $\mathcal T_c$ and three for the
    counterexample for $\mathcal T_\infty$, each carrying a `pf-proof`; the two answers and the
    attribution are unchanged. Cited by number only: the definition of $\mathcal T_c$ from
    Example 4 of §12 and the three axioms of a topology. Checked: the empty-union and
    empty-intersection cases, the inclusion
    $X-\bigcup_{A\in\mathcal A}A=\bigcap_{A\in\mathcal A}(X-A)\subseteq X-A_0$, and that
    $X-\{1\}$ satisfies none of the three alternatives defining $\mathcal T_\infty$.
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

::: pf

::: pf-step

$\varnothing\in\mathcal{T}_{c}$ and $X\in\mathcal{T}_{c}$.

::: pf-proof

$X-\varnothing=X$, which is all of $X$; and $X-X=\varnothing$, which is countable, indeed finite.

:::

:::

::: pf-step

$\mathcal{T}_{c}$ is closed under arbitrary unions: if $\mathcal{A}\subset\mathcal{T}_{c}$ and $U=\bigcup\mathcal{A}$, then $U\in\mathcal{T}_{c}$.

::: pf-proof

If $\mathcal A$ has a nonempty member $A_0$, then $X-A_0$ is countable, and $X-U=X-\bigcup_{A\in\mathcal A}A=\bigcap_{A\in\mathcal A}(X-A)\subseteq X-A_0$, so $X-U$ is a subset of a countable set and is countable. If every member of $\mathcal A$ is empty then $U=\varnothing$, which lies in $\mathcal T_c$ by step 1. (The empty subfamily is the case $U=\varnothing$.)

:::

:::

::: pf-step

$\mathcal{T}_{c}$ is closed under finite intersections: if $U_{1},\dots,U_{n}\in\mathcal{T}_{c}$ then $\bigcap_{i=1}^{n}U_{i}\in\mathcal{T}_{c}$.

::: pf-proof

$X-\bigcap_{i=1}^{n}U_{i}=\bigcup_{i=1}^{n}(X-U_{i})$. If some $U_i=\varnothing$ then $X-U_i=X$, the union is $X$ and the intersection is $\varnothing\in\mathcal T_c$; otherwise each $X-U_i$ is countable by membership, and a finite union of countable sets is countable, so the intersection lies in $\mathcal T_c$. The case $n=0$ is the intersection $X\in\mathcal T_c$ by step 1.

:::

:::

::: pf-step

Hence $\mathcal{T}_{c}$ is a topology on $X$.

::: pf-proof

The three axioms are: $X$ and $\varnothing$ belong (step 1), arbitrary unions belong (step 2) and finite intersections belong (step 3).

:::

:::

::: pf-step

For $X=\ZZ_{+}$, every finite subset of $X$ lies in $\mathcal{T}_{\infty}$; in particular $\{i\}\in\mathcal{T}_{\infty}$ for every $i\ge2$.

::: pf-proof

If $U$ is finite then $X-U$ is infinite, since $X=\ZZ_+$ is infinite and removing finitely many elements leaves infinitely many; being infinite, it is one of the alternatives in the definition of $\mathcal T_\infty$.

:::

:::

::: pf-step

But
$$
\bigcup_{i\ge2}\{i\}=\{2,3,4,\dots\}=X-\{1\},
$$
whose complement is $\{1\}$, which is neither infinite, nor empty, nor all of $X$; so this union is not in $\mathcal{T}_{\infty}$.

::: pf-proof

A point of the union is some integer $i\ge2$; every such integer is in $\{2,3,\dots\}=X-\{1\}$, and $1$ is in none of the sets $\{i\}$ with $i\ge2$. Hence the union is $X-\{1\}$, whose complement in $X$ is $\{1\}$. That set is finite and nonempty, and is not $X$ since $X$ is infinite, so none of the three alternatives holds and $X-\{1\}\notin\mathcal T_\infty$.

:::

:::

::: pf-step

The collection $\mathcal{T}_{\infty}$ therefore fails the axiom on unions and is not a topology on $X$.

::: pf-proof

Step 6 exhibits a subfamily of $\mathcal T_\infty$ whose union is not in $\mathcal T_\infty$, which is exactly the failure of the axiom that the union of any collection of members is a member.

:::

:::

:::
:::
