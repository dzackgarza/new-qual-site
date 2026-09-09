---
schema: qual/card@1
id: E-HAT-1.2-11
kind: problem
title: Fundamental group of mapping torus of map on wedge of circles
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Mapping Torus
  - van Kampen
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.2, Exercise 11; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Derived the HNN-type presentation by adjoining the mapping-torus circle and imposing one conjugacy relation for each free generator.
---

The mapping torus $T_f$ of a map $f: X \to X$ is the quotient of $X \times I$ obtained by identifying each point $(x, 0)$ with $(f(x), 1)$.
In the case $X = S^1 \lor S^1$ with $f$ basepoint-preserving, compute a presentation for $\pi_1(T_f)$ in terms of the induced map $f_*: \pi_1(X) \to \pi_1(X)$.
Do the same when $X = S^1 \lor S^1 \lor S^1$.
[One way to do this is to regard $T_f$ as built from $X \lor S^1$ by attaching cells.]

::: {.solution}
Let $x_0$ be the wedge point of $X$ and assume $f(x_0)=x_0$.
Let $t$ denote the loop in the mapping torus traced by the basepoint as the $I$-coordinate runs once around the quotient.

<1>1. If $X=S^1\vee S^1$ with free generators $a,b$ of
\[
\pi_1(X,x_0)\cong F(a,b),
\]
then $T_f$ is obtained from
\[
X\vee S^1
\]
by attaching two $2$-cells.
::: {.proof}
Give each circle of $X$ one $0$-cell and one $1$-cell.
The product of each $1$-cell with $I$ descends in the mapping torus to a $2$-cell.
The $1$-skeleton of the mapping torus consists of the two original loops $a,b$ together with the loop $t$ coming from $x_0\times I$.
Thus its $1$-skeleton is $X\vee S^1$.
:::

<1>2. The two attaching maps impose
\[
t a t^{-1}=f_*(a),
\qquad
t b t^{-1}=f_*(b).
\]
::: {.proof}
Use the copy $X\times\{1\}$ to name the generators $a$ and $b$, and orient $t$ from level $0$ to level $1$ along the basepoint.
Consider the square obtained from the cylinder over the $a$-edge.
Its oriented boundary traverses the bottom edge, the right vertical edge, the top edge backwards, and the left vertical edge backwards.
Because the quotient identifies $(x,0)$ with $(f(x),1)$, the bottom edge represents $f_*(a)$ in the chosen top copy, while the reversed top edge represents $a^{-1}$.
Hence the boundary word is
\[
f_*(a)\,t\,a^{-1}\,t^{-1},
\]
so its relation is equivalent to
\[
t a t^{-1} f_*(a)^{-1}=1.
\]
The same argument for the $b$-edge gives the second relation.
:::

<1>3. Therefore
\[
\boxed{
\pi_1(T_f)
\cong
\left\langle a,b,t\ \middle|\ t a t^{-1}=f_*(a),\ t b t^{-1}=f_*(b)\right\rangle .
}
\]
::: {.proof}
The $1$-skeleton contributes the free group on $a,b,t$, and <1>2 gives exactly the attaching relations of the two $2$-cells.
Van Kampen for CW complexes yields the displayed presentation.
:::

<1>4. More generally, if
\[
X=S^1\vee S^1\vee S^1
\]
with free generators $a,b,c$, then
\[
\boxed{
\pi_1(T_f)
\cong
\left\langle a,b,c,t\ \middle|\
t a t^{-1}=f_*(a),\
t b t^{-1}=f_*(b),\
t c t^{-1}=f_*(c)
\right\rangle .
}
\]
::: {.proof}
The same CW decomposition now has four $1$-cells, namely $a,b,c,t$, and one $2$-cell for the cylinder over each of the three circle edges.
Each cylinder supplies the corresponding conjugacy relation exactly as in <1>2.
:::

<1>5. In fact, for a wedge of $r$ circles with free basis $x_1,\dots,x_r$,
\[
\pi_1(T_f)
\cong
\left\langle x_1,\dots,x_r,t\ \middle|\
t x_i t^{-1}=f_*(x_i),\ 1\le i\le r
\right\rangle .
\]
::: {.proof}
This is the same construction with one cylinder $2$-cell for each circle of the wedge.
:::
:::
