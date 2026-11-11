---
schema: qual/card@1
id: E-UMMOE
kind: problem
title: A two-fold covering detecting nonabelian fundamental group
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
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
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 60 Exercise 5, printed p. 375,
    with Lemma 60.5 and the homotopy lifting criterion, Lemma 54.3. The lifts of $f*g$ and $g*f$ from the same point end at distinct vertices of the covering shown in Figure 60.3, so the loops are not path homotopic and the two classes do not commute. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
---

::: {.exercise}

Consider the covering map indicated in Figure 60.3 of the text.
Here, $p$ wraps $A_1$ around $A$ twice and wraps $B_1$ around $B$ twice; $p$ maps $A_0$ and $B_0$ homeomorphically onto $A$ and $B$, respectively.
Use this covering space to show that the fundamental group of the figure eight is not abelian.
:::

::: {.solution}
Let $X=A\vee B$ be the figure eight, based at $x_0$. Let $f$ traverse $A$ once counterclockwise and let $g$ traverse $B$ once counterclockwise.

Use the covering in Figure 60.3 and begin lifts at the central point $e_0$. The lift $\widetilde f$ runs along the half of $A_1$ from $e_0$ to the vertex $e_2$. From $e_2$, the loop $g$ lifts to the loop $B_0$, so the lift of $f*g$ beginning at $e_0$ ends at $e_2$.

Similarly, the lift $\widetilde g$ runs along the half of $B_1$ from $e_0$ to the vertex $e_1$. From $e_1$, the loop $f$ lifts to the loop $A_0$, so the lift of $g*f$ beginning at $e_0$ ends at $e_1$.

The endpoints $e_1$ and $e_2$ are distinct. By the homotopy-lifting criterion, path-homotopic loops based at $x_0$ have lifts beginning at $e_0$ with the same endpoint. Therefore
$$
f*g\not\simeq_p g*f.
$$
Consequently
$$
[f][g]\ne[g][f]
$$
in $\pi_1(X,x_0)$. Hence the fundamental group of the figure eight is not abelian.
:::
