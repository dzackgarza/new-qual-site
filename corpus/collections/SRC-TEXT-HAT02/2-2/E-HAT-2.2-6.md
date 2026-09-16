---
schema: qual/card@1
id: E-HAT-2.2-6
kind: problem
title: Every map $S^n \to S^n$ can be homotoped to have a fixed point
classification:
  areas:
  - topology
  topics:
  - Degree
  - Fixed Point Theorems
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 6; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete proof reviewed using degree theory and orthogonal-group homotopies.
---

::: {.problem}
Show that every map $S^n \to S^n$ can be homotoped to have a fixed point if $n > 0$.
:::

::: {.solution}
Let
\[
f:S^n\to S^n,
\qquad n>0.
\]
Choose a point $x_0\in S^n$.

<1>1. There exists a rotation $R\in SO(n+1)$ such that
\[
R(f(x_0))=x_0.
\]
::: {.proof}
The group $SO(n+1)$ acts transitively on $S^n$ for $n>0$, so some orientation-preserving orthogonal transformation carries $f(x_0)$ to $x_0$.
:::

<1>2. The rotation $R$ is joined to the identity by a path in $SO(n+1)$.
::: {.proof}
The group $SO(m)$ is path connected for every $m\ge2$. Here $m=n+1\ge2$, so there is a continuous path
\[
R_t\in SO(n+1),
\qquad R_0=I,\quad R_1=R.
\]
:::

<1>3. The maps
\[
f_t=R_t\circ f
\]
form a homotopy from $f$ to a map having a fixed point.
::: {.proof}
Clearly $f_0=f$. At the other endpoint,
\[
f_1(x_0)=R(f(x_0))=x_0,
\]
so $x_0$ is a fixed point of $f_1$.
:::

Therefore every map $S^n\to S^n$ with $n>0$ is homotopic to a map with a fixed point.
:::
