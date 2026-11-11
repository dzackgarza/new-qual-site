---
schema: qual/card@1
id: E-5WDER
kind: problem
title: Simple closed curves on the torus may or may not separate
classification:
  areas:
  - topology
  topics:
  - Jordan Curve Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Munkres §61 Exercise 1, printed p. 380. No complete published solution located; the searches are listed in
    the COMPLAINTS.md entry for §61--§73 of SRC-TEXT-MUN00. The earlier solution had its steps half inside the
    LaTeX ("Example of a non-separating simple closed curve: *Proof:*" as a step heading, with two pf-proof
    bodies empty) and is replaced. Checked line by line against Theorem 61.3 (printed p. 379), whose statement
    is for S^2 and so is not applied here, and against Theorem 17.2 and Theorem 18.1 (open maps, printed
    pp. 94, 104) for the two homeomorphisms used: S^1 - y_0 is homeomorphic to an open interval, and
    T^2 - C is the product of S^1 with that interval.
---

::: {.exercise}

Give examples to show that a simple closed curve in the torus may or may not separate the torus.
:::

::: {.solution}

Write $T^2=S^1\times S^1$; a subset of $T^2$ separates $T^2$ when its complement is not connected.

::: pf

::: pf-step

The circle $C_1=S^1\times\theset{y_0}$ does not separate $T^2$.

::: pf-proof

$C_1$ is the image of the imbedding $\theta\mapsto(\theta,y_0)$ of $S^1$, so it is a simple closed curve. Its complement is $S^1\times(S^1-\theset{y_0})$: a point of $T^2$ is off $C_1$ exactly when its second coordinate differs from $y_0$. The space $S^1-\theset{y_0}$ is homeomorphic to the open interval $(0,1)$, so

$$
T^2-C_1\cong S^1\times(0,1),
$$

which is path connected. Hence the complement is connected and $C_1$ does not separate.

:::

:::

::: pf-step

A small circle $C_2$ on $T^2$ bounding a disk separates $T^2$.

::: pf-proof

Let $U\subseteq T^2$ be an open set homeomorphic to $\RR^2$ (for instance the image of a small coordinate chart), and let $D\subseteq U$ be a closed disk of radius $r$ with centre in $U$; let $C_2=\operatorname{Bd}D$, the image of a round circle under the homeomorphism $U\cong\RR^2$, hence a simple closed curve. Then

$$
T^2-C_2=\operatorname{Int}D\ \cup\ (T^2-D),
$$

because $T^2$ is the disjoint union of $\operatorname{Int}D$, $C_2$ and $T^2-D$. Both sets are nonempty ($\operatorname{Int}D$ contains the centre; $T^2-D$ contains a point of $T^2$ outside the compact set $D$) and both are open in $T^2-C_2$, which is therefore disconnected.

:::

:::

::: pf-qed

$C_1$ is a non-separating and $C_2$ a separating simple closed curve on $T^2$.

:::

:::
:::
