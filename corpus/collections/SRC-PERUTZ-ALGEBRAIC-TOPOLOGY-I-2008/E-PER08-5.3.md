---
schema: qual/card@1
id: E-PER08-5.3
kind: problem
title: $T^2$ minus four points double covers $S^2$ minus four points
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Completed from the retained Perutz Algebraic Topology I source and checked against the stated hypotheses.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retyped the mathematics against Exercise 5.3 of the Perutz 2008 notes.
---

::: {.problem}
Show that $T^2\setminus\{4\text{ points}\}$ is a $2$-sheeted covering of $S^2\setminus\{4\text{ points}\}$.
Some possible approaches are (a) a direct topological argument; (b) the Weierstrass $\wp$-function from complex analysis; (c) a pencil of divisors of degree $2$ on an elliptic curve.
:::

::: {.solution}
Use the involution $\iota:T^2\to T^2$, $\iota([z])=[-z]$ on a complex torus $T^2=\mathbb C/\Lambda$.

<1>1. The quotient $T^2/\langle\iota\rangle$ is a sphere and the quotient map has four branch points.
::: {.proof}
The fixed points of $\iota$ are exactly the four $2$-torsion points
\[
T^2[2]=\tfrac12\Lambda/\Lambda.
\]
The quotient is a compact connected orientable surface.
Away from the fixed points the quotient is a genuine two-sheeted covering.
The Riemann--Hurwitz formula for the degree-$2$ quotient gives
\[
\chi(T^2)=2\chi(T^2/\iota)-4,
\]
so $0=2\chi(T^2/\iota)-4$ and therefore $\chi(T^2/\iota)=2$.
Hence the quotient surface is $S^2$.
:::

<1>2. Removing the ramification points gives the claimed covering.
::: {.proof}
Let $F=T^2[2]$ and let $B$ be its four images in $S^2=T^2/\iota$.
The involution acts freely on $T^2\setminus F$, so the quotient map restricts to
\[
T^2\setminus F\longrightarrow S^2\setminus B.
\]
A free action of the finite group $\mathbb Z/2$ is a covering action; every fibre has two points.
Thus this restriction is a two-sheeted covering.
:::
:::
