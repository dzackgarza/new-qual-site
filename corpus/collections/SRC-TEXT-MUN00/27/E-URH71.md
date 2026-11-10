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
---

::: {.exercise}

Let $X$ be a compact Hausdorff space, let $\theset{A_n}$ be a countable collection of closed sets of $X$.
Show that if each set $A_n$ has empty interior in $X$, then the union $\bigcup A_n$ has empty interior in $X$.
[Hint: Imitate the proof of Theorem 27.7.]

This is a special case of the Baire category theorem, which we shall study in Chapter 8.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 27.5, PDF p. 17** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the nested-open-sets argument follows the hint as they use it.

Let $U$ be a nonempty open subset of the compact Hausdorff space $X$; we find a point of $U$ outside $\bigcup_{n}A_{n}$, where each $A_{n}$ is closed with empty interior.

Since $\operatorname{Int}A_{1}=\varnothing$, $U\not\subset A_{1}$; pick $x\in U-A_{1}$. The set $A_{1}\cup(X-U)$ is closed and does not contain $x$, hence compact (Theorem 26.2) and disjoint from the point $x$; by Lemma 26.4 there are disjoint open sets $V_{1}\ni x$ and $W\supset A_{1}\cup(X-U)$. Then
$$
\overline{V_{1}}\subset X-W\subset U-A_{1}.
$$
Iterating, with $V_{k}$ in place of $U$ and $A_{k+1}$ in place of $A_{1}$, gives nonempty open $V_{1}\supset\overline{V_{2}}\supset V_{2}\supset\cdots$ with $\overline{V_{n}}\subset V_{n-1}-A_{n}$. The sets $\overline{V_{n}}$ are nonempty closed subsets of the compact space $X$ with the finite intersection property, so $\bigcap_{n}\overline{V_{n}}\ne\varnothing$ (Theorem 26.9); a point $x$ of the intersection lies in $V_{0}=U$ and outside every $A_{n}$. So $\bigcup_{n}A_{n}$ has empty interior.
:::
