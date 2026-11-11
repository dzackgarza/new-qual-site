---
schema: qual/card@1
id: E-9LY2B
kind: problem
title: Infinite wedges of circles are not first countable
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Countability
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-corrected
  by: claude
  date: 2026-11-11
  note: >-
    Munkres §71 Exercise 4, printed p. 438. A published solution is Takumi Murayama, Selected Solutions to
    Munkres's Topology, 2nd Ed. (MAT365, Princeton, Fall 2012), §71 (printed there as Exercise 71.4), and it is
    defective: it replaces a countable base at p by one it assumes strictly nested, which a countable base
    need not admit, and its closing comparison "U_i cap S_j is contained in V cap S_j = U_j, contradicting
    U_i > U_j" produces no point of U_i outside V. What is correct in it is kept: V is built by choosing one
    point on each circle, and V is open by the coherence definition (printed p. 435). The card's proof
    replaces the nesting step by the diagonal choice of the points, which needs no nesting. Checked against the
    definition of coherent topology (printed p. 435) and the definition of the infinitely generated wedge
    (printed p. 435).
---

::: {.exercise}

Show that if $X$ is an infinite wedge of circles, then $X$ does not satisfy the first countability axiom.
:::

::: {.solution}

Write $X = \bigvee_{\alpha \in J} S_\alpha$ with $J$ infinite and $p$ the common point; here $X$ is the union of the circles $S_\alpha$ with the topology coherent with them (printed p. 435).

::: pf

::: pf-step

A set $U\subseteq X$ containing $p$ is open in $X$ if and only if $U\cap S_\alpha$ is open in $S_\alpha$ for every $\alpha$.

::: pf-proof

That is the coherence definition of the wedge of circles (printed p. 435), in its open-set form.

:::

:::

::: pf-step

$p$ has no countable neighbourhood basis.

::: pf-proof

Suppose $\theset{U_n}_{n\ge1}$ were a countable basis of neighbourhoods of $p$, each open in $X$. Choose distinct indices $\alpha_n$ for $n\ge1$, possible since $J$ is infinite. Since $U_n\cap S_{\alpha_n}$ is an open neighbourhood of $p$ in the circle $S_{\alpha_n}$, which has no isolated points, pick $x_n\in (U_n\cap S_{\alpha_n})\setminus\theset{p}$. Define

$$
V\cap S_\alpha=\begin{cases}S_\alpha\setminus\theset{x_n},&\alpha=\alpha_n\ \text{for some }n,\\ S_\alpha,&\text{otherwise.}\end{cases}
$$

Each $V\cap S_\alpha$ is open in $S_\alpha$ and contains $p$ (as $x_n\neq p$), so $V$ is an open neighbourhood of $p$ by step 1. But $x_k\in U_k$ and $x_k\notin V$, so no $U_k$ is contained in $V$; hence $\theset{U_n}$ is not a basis at $p$.

:::

:::

::: pf-qed

$X$ is not first countable at $p$.

:::

:::
:::
