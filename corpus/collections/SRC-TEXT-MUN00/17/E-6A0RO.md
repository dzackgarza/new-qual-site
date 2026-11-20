---
schema: qual/card@1
id: E-6A0RO
kind: problem
title: Hausdorff spaces and the closed diagonal
classification:
  areas:
  - topology
  topics:
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §17 Exercise 13, printed p. 101; the stored
    statement is the printed equivalence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 17.13, PDF p. 8. The complement of the diagonal is
    covered by the products of disjoint neighbourhoods, and a basis element inside that
    complement has disjoint factors. (tmp/sources/munkres-solutions-positron-ch2.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into STYLE-08 as the two directions of the equivalence, with the openness of $X\times X-\Delta$ and of its complement as the working content. Both were re-checked against the basis of $X\times X$ (printed p. 86). No statement change.
---

::: {.exercise}

Show that $X$ is Hausdorff if and only if the diagonal $\Delta = \theset{x \times x \mid x \in X}$ is closed in $X \times X$.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 17.13** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); both directions are theirs. Whitman, proves the same two directions with Theorem 17.5 and Corollary 17.7 in place of the direct openness arguments.

Let $\Delta=\theset{x\times x\mid x\in X}\subset X\times X$. A basis element of $X\times X$ is a product $U\times V$ of open subsets of $X$ (printed p. 86).

::: pf

::: {.pf-step #hausdorff-to-closed}

If $X$ is Hausdorff then $\Delta$ is closed.

::: pf-proof

It suffices to show that $X\times X-\Delta$ is open. Let $(x,y)\in X\times X-\Delta$, so that $x\ne y$. Choose disjoint open sets $U\ni x$ and $V\ni y$. For $(u,v)\in U\times V$ we have $u\in U$ and $v\in V$ with $U\cap V=\varnothing$, so $u\ne v$; hence $(x,y)\in U\times V\subset X\times X-\Delta$. So each point of $X\times X-\Delta$ lies in a basis element contained in that set, which is therefore open, and $\Delta$ is closed.

:::

:::

::: {.pf-step #closed-to-hausdorff}

If $\Delta$ is closed then $X$ is Hausdorff.

::: pf-proof

Let $x\ne y$ in $X$. Then $(x,y)\in X\times X-\Delta$, which is open, so there is a basis element $U\times V$ of $X\times X$ with
$$
(x,y)\in U\times V\subset X\times X-\Delta .
$$
Here $U$ and $V$ are open in $X$ and $U\cap V=\varnothing$: a point $z\in U\cap V$ would give $(z,z)\in U\times V\subset X\times X-\Delta$ while $(z,z)\in\Delta$. So $U$ and $V$ are disjoint neighbourhoods of $x$ and $y$.

:::

:::

::: pf-step

$X$ is Hausdorff if and only if $\Delta$ is closed in $X\times X$.

::: pf-proof

The two implications are steps [](#hausdorff-to-closed){.pf-ref} and [](#closed-to-hausdorff){.pf-ref}.

:::

:::

:::
:::
