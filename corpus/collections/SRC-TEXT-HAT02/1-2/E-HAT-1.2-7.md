---
schema: qual/card@1
id: E-HAT-1.2-7
kind: exercise
title: Fundamental group of $S^2$ with north and south poles identified
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Van Kampen
  - CW Complexes
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

Let $X$ be the quotient space of $S^2$ obtained by identifying the north and south poles to a single point.
Put a cell complex structure on $X$ and use this to compute $\pi_1(X)$.

::: {.solution}
**Goal.** Compute $\pi_1(X)$ for $X = S^2$ with north and south poles identified.

<1>1. $X$ is homeomorphic to $S^1 \vee S^2$.
<2>1. Identifying the two poles of $S^2$ gives a space with a single "pinch" point.
Proof: the quotient collapses the two poles to one point.
<2>2. This space is $S^1 \vee S^2$ (a circle wedged with a sphere).
Proof: the arc from north to south pole becomes a circle (the two poles identified), and the rest of $S^2$ becomes a sphere attached at the pinch point; the result is $S^1 \vee S^2$.

<1>2. Cell structure of $S^1 \vee S^2$.
<2>1. $S^1$ has one $0$-cell and one $1$-cell; $S^2$ has one $0$-cell and one $2$-cell.
Proof: standard cell structures.
<2>2. $S^1 \vee S^2$ has one $0$-cell (the wedge point), one $1$-cell, and one $2$-cell.
Proof: the two $0$-cells are identified at the wedge point.

<1>3. Compute $\pi_1(X)$.
<2>1. $\pi_1(S^1 \vee S^2) = \pi_1(S^1) * \pi_1(S^2) = \ZZ * 0 = \ZZ$.
Proof: van Kampen (or the fact that $\pi_1$ of a wedge is the free product of the $\pi_1$'s), and $\pi_1(S^2) = 0$.
<2>2. Hence $\pi_1(X) = \ZZ$.
Proof: <1>1.2 and <1>3.1.

<1>4. Q.E.D.
Proof: $\pi_1(X) = \ZZ$.
:::
