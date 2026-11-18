---
schema: qual/card@1
id: E-URH71
kind: problem
title: Countable unions of nowhere dense closed sets in compact Hausdorff spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §27 Exercise 5, printed p. 178, with Theorem
    26.2, Lemma 26.4 and Theorem 26.9; the stored statement and the hint are printed there.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 27.5, PDF p. 17. A nested sequence of open sets,
    each closed piece avoiding the next closed set with empty interior, has nonempty
    intersection in the compact space, and a point of it lies outside the union.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps from the retained positron0802 solution (Chapter 3,
    Exercise 27.5, PDF p. 17). Pages verified: the exercise on printed p. 178; Theorem 26.2
    on printed p. 165; Lemma 26.4 on printed p. 166, the separation of a compact set from a
    point that the construction uses; Theorem 26.9 on printed p. 169, the finite intersection
    property; and Theorem 27.7 on printed p. 176, which is what the printed hint points at
    and whose proof carries the same nested-open-sets device. Two things made explicit that
    the prose left to the reader: that a set with empty interior meets no nonempty open set,
    which is what produces the point x in U - A_n, and that the complement of the open set W
    is closed, which is what makes closure(V) lie in U - A_n. The index bookkeeping is now a
    stated induction with V_0 = U, where the earlier prose wrote "iterating" and then
    referred to V_0 without defining it. No repair to the statement.
---

::: {.exercise}

Let $X$ be a compact Hausdorff space, let $\theset{A_n}$ be a countable collection of closed sets of $X$.
Show that if each set $A_n$ has empty interior in $X$, then the union $\bigcup A_n$ has empty interior in $X$.
[Hint: Imitate the proof of Theorem 27.7.]

This is a special case of the Baire category theorem, which we shall study in Chapter 8.
:::

::: {.solution}
The argument is the retained published solution, **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 27.5, PDF p. 17** (`tmp/sources/munkres-solutions-positron-ch3.pdf`), restructured into steps and following the printed hint, which points at the nested-open-sets construction in the proof of Theorem 27.7 (printed p. 176).

Throughout, $X$ is a compact Hausdorff space and $\{A_n\}_{n\ge1}$ is a countable family of closed subsets of $X$, each with empty interior; the exercise is §27 Exercise 5 (printed p. 178). The tools are Theorem 26.2 (a closed subspace of a compact space is compact, printed p. 165), Lemma 26.4 (a compact subspace and a point outside it are separated by disjoint open sets, printed p. 166) and Theorem 26.9 (in a compact space a family of closed sets with the finite intersection property has nonempty intersection, printed p. 169).

::: pf

::: {.pf-step #step}
For every nonempty open $U\subset X$ and every $n$ there is a nonempty open $V$ with $\closure{V}\subset U-A_n$.

::: pf-proof
Since $A_n$ has empty interior, $U\not\subset A_n$, so there is $x\in U-A_n$. The set $A_n\cup(X-U)$ is closed, being the union of the closed set $A_n$ and the complement of the open set $U$, and it does not contain $x$; being a closed subset of the compact space $X$, it is compact (Theorem 26.2, printed p. 165). Lemma 26.4 (printed p. 166) then gives disjoint open sets $V\ni x$ and $W\supset A_n\cup(X-U)$, and
$$
\closure{V}\subset X-W\subset X-\big(A_n\cup(X-U)\big)=U-A_n,
$$
because the complement of the open set $W$ is closed and contains $V$. Finally $V$ is nonempty since $x\in V$.
:::

:::

::: {.pf-step #sequence}
There are nonempty open sets $V_0=U,V_1,V_2,\ldots$ with $\closure{V_n}\subset V_{n-1}-A_n$ for every $n\ge1$.

::: pf-proof
Induct on $n$: given the nonempty open $V_{n-1}$, step [](#step){.pf-ref} with $U=V_{n-1}$ produces a nonempty open $V_n$ with $\closure{V_n}\subset V_{n-1}-A_n$.
:::

:::

::: {.pf-step #point}
For every nonempty open $U\subset X$ there is a point of $U$ lying outside $\bigcup_nA_n$.

::: pf-proof
The sets $\closure{V_n}$ are nonempty and closed, and $\closure{V_{n+1}}\subset V_n\subset\closure{V_n}$, so they are nested and the family has the finite intersection property; by Theorem 26.9 (printed p. 169) the intersection $\bigcap_n\closure{V_n}$ is nonempty. Let $x$ lie in it. Since $\closure{V_1}\subset V_0-A_1=U-A_1$, we have $x\in U$. And for each $n\ge1$, $x\in\closure{V_n}\subset V_{n-1}-A_n$, so $x\notin A_n$. Hence $x\in U-\bigcup_nA_n$.
:::

:::

::: {.pf-step}
$\bigcup_nA_n$ has empty interior in $X$.

::: pf-proof
A set has empty interior exactly when every nonempty open set meets its complement; by step [](#point){.pf-ref} every nonempty open $U$ contains a point outside $\bigcup_nA_n$. So $\bigcup_nA_n$ contains no nonempty open set.
:::

:::

:::
:::
