---
schema: qual/card@1
id: E-HAT-2.2-4
kind: problem
title: Surjective map $S^n \to S^n$ of degree zero
classification:
  areas:
  - topology
  topics:
  - Degree
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 4; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete proof reviewed using degree theory and orthogonal-group homotopies.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the construction: $g$ carries the first wedge summand identically onto $S^n$, so
    $g\circ p$ is onto, and the pinch map sends $[S^n]$ to the sum of the two summand classes, so
    $\deg f=1+(-1)=0$.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Transcribed DeMason's construction on pp.64-65: an out-and-back loop on S^1 is surjective with
    winding number 0, and suspension preserves both surjectivity and degree by Proposition 2.33, so
    every S^n admits the required map. The order in which suspension is iterated is also stated in
    the proof; it does not alter the answer.
---

::: {.problem}
Construct a surjective map $S^n \to S^n$ of degree zero, for each $n \geq 1$.
:::

::: {.solution}
First define $f_0:S^1\to S^1$ by
$$
f_0(t)=
\begin{cases}
(\cos2t,\sin2t),&0\le t\le\pi,\\
(\cos2t,-\sin2t),&\pi\le t\le2\pi.
\end{cases}
$$
The first piece wraps once around the circle counterclockwise and the second returns clockwise. Both wrap once onto the circle and they have the same value $(-1,0)$ at $t=\pi$, so $f_0$ is continuous, surjective, and has winding number $0$, hence degree $0$.

::: pf

::: pf-step

For each $n\ge1$, there is a surjective degree-zero map $S^n\to S^n$.

::: pf-proof

For $n=1$, use $f_0$ itself. Suppose $f:X\to Y$ is surjective and $Sf:SX\to SY$ denotes its suspension. Given $[y,t]\in SY$, choose $x\in X$ with $f(x)=y$; then $[f(x),t]=[y,t]$, so $Sf$ is surjective (DeMason p. 64). Its degree is the same as that of $f$ by Proposition 2.33. Repeatedly suspending therefore preserves both surjectivity and zero degree: for $n\ge2$, the $(n-1)$-fold suspension of $f_0$ supplies the map. This is exactly DeMason's construction for Hatcher 2.2.4 on printed p. 64, with the out-and-back loop above.
:::

:::

:::

The source is **Kenneth DeMason, *M382C Full Credit HW Problems* (2021)**, Hatcher 2.2.4, printed pp. 64--65, held at `tmp/sources/demason-m382c-hatcher-20210404.pdf`.
:::
