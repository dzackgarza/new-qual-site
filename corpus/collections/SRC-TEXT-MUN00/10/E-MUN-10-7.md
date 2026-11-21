---
schema: qual/card@1
id: E-MUN-10-7
kind: problem
title: Principle of transfinite induction
classification:
  areas:
  - topology
  topics:
  - Well-Ordered Sets
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §10 Exercise 7, printed pp. 67-68; the stored
    statement is the printed definition of inductive and the printed theorem.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 10.7, printed p. 112.
    The proof is his: the least element of J - J_0 has all its predecessors in J_0, so
    inductivity puts it in J_0, a contradiction.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's prose into numbered steps; the proof is Whitman's (Exercise 10.7,
    printed p. 112), as the card cites. Checked: the least-element step, the containment of the
    section, the inductive step and the contradiction. Not checked: the cited page, because
    tmp/sources holds no copy of the Whitman manual and the Munkres text is not retained in this
    VM.
---

::: {.exercise}

Let $J$ be a well-ordered set.
A subset $J_0$ of $J$ is said to be inductive if for every $\alpha \in J$,

$$
(S_\alpha \subset J_0) \Longrightarrow \alpha \in J_0.
$$

Prove the following theorem (the principle of transfinite induction).
If $J$ is a well-ordered set and $J_0$ is an inductive subset of $J$, then $J_0 = J$.
:::

::: {.solution}

The argument is that of the retained published solution: Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 10.7, printed p 112, which the card cites; it is restructured into numbered steps below. Here $J$ is well ordered, $S_\alpha=\set{y\in J\mid y<\alpha}$ is the section of elements below $\alpha$, and $J_0\subset J$ is inductive: $S_\alpha\subset J_0$ implies $\alpha\in J_0$, for every $\alpha\in J$.

::: pf

::: {.pf-step #min}

If $J_0\neq J$ then $J-J_0$ has a smallest element $\alpha$.

::: pf-proof

$J-J_0$ is a nonempty subset of the well-ordered set $J$, so it has a least element.

:::

:::

::: {.pf-step #section}

$S_\alpha\subset J_0$.

::: pf-proof

Let $y\in S_\alpha$. Then $y<\alpha$, so $y$ is not in $J-J_0$, since $\alpha$ is the least element of that set and $y<\alpha$; as $y\in J$, $y\in J_0$.

:::

:::

::: {.pf-step #alpha}

$\alpha\in J_0$.

::: pf-proof

Step [](#section){.pf-ref} gives $S_\alpha\subset J_0$, and $J_0$ is inductive.

:::

:::

::: {.pf-step #done}

$J_0=J$.

::: pf-proof

Step [](#alpha){.pf-ref} contradicts $\alpha\in J-J_0$; so the supposition $J_0\neq J$ is false.

:::

:::

:::

:::
