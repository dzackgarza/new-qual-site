---
schema: qual/card@1
id: E-SRFW8
kind: problem
title: Subgroups need not be direct summands
classification:
  areas:
  - topology
  topics:
  - Free Abelian Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Munkres §67 Exercise 2, printed p. 411. Proof transcribed from Takumi Murayama, Selected Solutions to
    Munkres's Topology, 2nd Ed. (MAT365, Princeton, Fall 2012), §67 Exercise 2, and checked against dbFin,
    Munkres (2000) Topology with Solutions, §67 Problem 2 (web page, read 2026-11-11), which argues by the
    intersection 2Z cap G2. Murayama's step "G = 2Z + Z/2Z by Corollary 67.3" is written out here as it is
    meant: Corollary 67.3 (printed p. 409) applied with the two summands interchanged gives G/G1 = Z/2Z
    isomorphic to G2. Nothing of his is false; the card only makes his citation explicit.
---

::: {.exercise}

Show that if $G_1$ is a subgroup of $G$, there may be no subgroup $G_2$ of $G$ such that $G = G_1 \oplus G_2$.
[Hint: Set $G = \ZZ$ and $G_1 = 2\ZZ$.]
:::

::: {.solution}

Take $G=\ZZ$ and $G_1=2\ZZ$, as the hint suggests, and suppose that $G_2\le\ZZ$ satisfies $\ZZ=2\ZZ\oplus G_2$.

::: pf

::: pf-step

$G_2$ is isomorphic to $\ZZ/2\ZZ$.

::: pf-proof

A direct sum is symmetric in its two summands, so Corollary 67.3 (printed p. 409), applied to the decomposition $\ZZ=G_2\oplus 2\ZZ$, gives $\ZZ/2\ZZ=\ZZ/G_1\cong G_2$.

:::

:::

::: pf-step

No subgroup of $\ZZ$ is isomorphic to $\ZZ/2\ZZ$.

::: pf-proof

A subgroup of $\ZZ$ is $m\ZZ$ for some $m\ge 0$. If $m=0$ it is trivial; if $m>0$ the map $k\mapsto mk$ is an isomorphism $\ZZ\to m\ZZ$, so $m\ZZ$ is infinite cyclic and has no element of order $2$. Neither is $\ZZ/2\ZZ$.

:::

:::

::: pf-step

The same conclusion by direct computation.

::: pf-proof

With $G_2=m\ZZ$ for some $m$, either $m=0$ and $2\ZZ+G_2=2\ZZ\neq\ZZ$, or $m>0$ and $2m$ is a nonzero element of $2\ZZ\cap m\ZZ$, so the two summands are not independent and the sum is not direct. Either way $2\ZZ$ has no complementary subgroup in $\ZZ$.

:::

:::

::: pf-qed

Steps 1 and 2 contradict each other, so no such $G_2$ exists; step 3 gives the same conclusion element by element.

:::

:::
:::
