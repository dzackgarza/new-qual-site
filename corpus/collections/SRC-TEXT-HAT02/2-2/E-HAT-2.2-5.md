---
schema: qual/card@1
id: E-HAT-2.2-5
kind: problem
title: Any two reflections of $S^n$ are homotopic through reflections
classification:
  areas:
  - topology
  topics:
  - Degree
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 5; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete proof reviewed using degree theory and orthogonal-group homotopies.
---

Show that any two reflections of $S^n$ across different $n$ dimensional hyperplanes are homotopic, in fact homotopic through reflections.
[The linear algebra formula for a reflection in terms of inner products may be helpful.]

::: {.solution}
A reflection of $S^n\subset\mathbb R^{n+1}$ across the hyperplane perpendicular to a unit vector $u$ is
\[
R_u(x)=x-2\langle x,u\rangle u.
\]
Note that $R_u=R_{-u}$.

<1>1. Given two reflections $R_u$ and $R_v$, choose a continuous path of unit vectors
\[
u_t\in S^n,
\qquad u_0=u,\quad u_1=v,
\]
when $n\ge1$.
::: {.proof}
The sphere $S^n$ is path connected for $n\ge1$. If necessary one may replace $v$ by $-v$, which defines the same reflection.
:::

<1>2. The formula
\[
H_t(x)=R_{u_t}(x)=x-2\langle x,u_t\rangle u_t
\]
defines a homotopy through reflections from $R_u$ to $R_v$.
::: {.proof}
The displayed expression depends continuously on $(x,t)$. For each fixed $t$, it is exactly reflection across the hyperplane $u_t^\perp$, hence restricts to a self-map of $S^n$. At $t=0$ and $t=1$ it equals the two prescribed reflections.
:::

For $n=0$ there is only one hyperplane in $\mathbb R$, so the assertion is trivial. Hence any two reflections of $S^n$ are homotopic, indeed homotopic through reflections.
:::
