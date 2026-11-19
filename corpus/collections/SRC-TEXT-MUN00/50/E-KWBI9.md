---
schema: qual/card@1
id: E-KWBI9
kind: problem
title: Connected $T_1$ spaces have positive dimension
classification:
  areas:
  - topology
  topics:
  - Dimension
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution was located; the sets searched are listed in the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00.
    Checked against Munkres, Topology (2000), §50 Exercise 2, printed p. 315, with the definition of dimension by
    order of refinements and the $T_1$ axiom. The argument: for distinct a, b the two open sets X - {a} and
    X - {b} cover X; a refinement of order 1 has pairwise disjoint members, none of them all of X, so splitting
    it at one member separates X, contradicting connectedness. Nothing needed correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). Nothing located proves Munkres §50 Exercise 2 (printed p. 315),
    and the card's own argument stands: the two-set cover by the complements of two distinct points refines to
    a cover of order at most 1 only if that cover separates the space. Murayama's selection has no Chapter 8,
    dbFin has no chapter-8 page, the ten GitHub repositories of Munkres solutions listed in COMPLAINTS.md stop
    before §36, and the AoPS post *Topology by Munkres Chapter 8 | Day 18*
    (https://artofproblemsolving.com/community/c3401823h3647630) answers §50 with its formulas lost. The
    Stack Exchange queries of this pass are in the COMPLAINTS.md entry for §43--§50; none of them returned this
    exercise. Nothing needed correction.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2. One substantive repair: the earlier text said the
    refinement has "order at most $1$", which is the wrong bound — order at most $0$ is what makes
    the members pairwise disjoint, and that is what the argument uses; the card now states the
    definition of $\dim X\le0$ and derives pairwise disjointness from it. Re-checked: $U=X-\{a\}$
    and $V=X-\{b\}$ are open in a $T_1$ space and cover $X$ because $a\ne b$; no member of a
    refinement equals $X$ since each lies in the proper set $U$ or $V$; and one member together
    with the union of the rest separates $X$. Added: the openness of the union of the remaining
    members and the nonemptiness of each piece. The statement is §50 Exercise 2 on printed p. 315; the
    earlier events record that no retained set covers it, and the argument is the card's own.
---

::: {.exercise}

Show that any connected $T_1$ space having more than one point has dimension at least 1.
:::

::: {.solution}
No retained solution set covers this exercise, so the argument is the card's own. Recall that $\dim X\le0$ when every open cover of $X$ has an open refinement of order at most $0$, that is, one whose members are pairwise disjoint; a space has dimension at least $1$ when it does not have dimension $0$.

::: pf

::: {.pf-step #cover}
For distinct points $a,b$ of a $T_1$ space $X$, the sets $U=X-\{a\}$ and $V=X-\{b\}$ are open and cover $X$.

::: pf-proof
In a $T_1$ space the one-point sets are closed, so their complements $U$ and $V$ are open. Their union is $X$: a point of $X$ is $a$ or is not, and if it is $a$ then $a\ne b$ puts it in $V$, while if it is not $a$ it lies in $U$.
:::

:::

::: {.pf-step #refinement}
If $\dim X=0$, then the cover $\{U,V\}$ has an open refinement $\mathcal{W}$ whose members are pairwise disjoint.

::: pf-proof
Dimension $0$ means that every open cover has an open refinement of order at most $0$, and a family has order at most $0$ exactly when no point lies in two of its members, that is, when its members are pairwise disjoint. The family $\{U,V\}$ is an open cover by step [](#cover){.pf-ref}, so it has such a refinement $\mathcal{W}$, which also covers $X$.
:::

:::

::: {.pf-step #two-members}
No member of $\mathcal{W}$ equals $X$, so $\mathcal{W}$ has at least two nonempty members.

::: pf-proof
A refinement of $\{U,V\}$ assigns to each $W\in\mathcal{W}$ some member of $\{U,V\}$ containing it, so $W\subseteq U$ or $W\subseteq V$; both $U$ and $V$ are proper, since $a\notin U$ and $b\notin V$, hence $W\ne X$. As $\mathcal{W}$ covers the nonempty space $X$ and no member is $X$, the union of its members is $X$ without any single member being all of it, so there are at least two nonempty members.
:::

:::

::: {.pf-step}
$\boxed{\dim X\ge1}$.

::: pf-proof
Let $W_0\in\mathcal{W}$ be nonempty and let $Z=\bigcup(\mathcal{W}-\{W_0\})$, which is a union of open sets and hence open, and nonempty by step [](#two-members){.pf-ref}. Since the members of $\mathcal{W}$ are pairwise disjoint, $W_0\cap Z=\varnothing$; since $\mathcal{W}$ covers $X$, $W_0\cup Z=X$. So $W_0$ and $Z$ are disjoint nonempty open sets covering $X$, a separation of $X$, contradicting the connectedness of $X$. Hence $\dim X\ne0$, and since dimension is a non-negative integer or $\infty$ for a space with a base of open sets, $\dim X\ge1$.
:::

:::

:::
:::
