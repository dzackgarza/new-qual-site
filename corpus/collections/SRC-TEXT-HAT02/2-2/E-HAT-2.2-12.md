---
schema: qual/card@1
id: E-HAT-2.2-12
kind: problem
title: Quotient map $S^1 \times S^1 \to S^2$ inducing isomorphism on $H_2$; all maps $S^2 \to S^1 \times S^1$ nullhomotopic
classification:
  areas:
  - topology
  topics:
  - Homology
  - Degree
  - Covering Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 12; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete proof checked via cellular homology, covering spaces, and degree.
---

::: {.problem}
Show that the quotient map $S^1 \times S^1 \to S^2$ collapsing the subspace $S^1 \lor S^1$ to a point is not nullhomotopic by showing that it induces an isomorphism on $H_2$.
On the other hand, show via covering spaces that any map $S^2 \to S^1 \times S^1$ is nullhomotopic.
:::

::: {.solution}
Let
\[
T^2=S^1\times S^1
\]
with its standard CW structure consisting of one $0$-cell, two $1$-cells, and one $2$-cell. Its $1$-skeleton is $S^1\vee S^1$.

<1>1. Collapsing the $1$-skeleton gives
\[
T^2/(S^1\vee S^1)\cong S^2.
\]
::: {.proof}
The quotient collapses the boundary of the unique $2$-cell to a point, so the quotient of its closed characteristic disk is
\[
D^2/\partial D^2\cong S^2.
\]
:::

<1>2. The quotient map
\[
q:T^2\to S^2
\]
induces an isomorphism on $H_2$.
::: {.proof}
The cellular chain complex of $T^2$ is
\[
0\to\mathbb Z\xrightarrow{0}\mathbb Z^2\xrightarrow{0}\mathbb Z\to0,
\]
so the unique $2$-cell represents a generator of $H_2(T^2)\cong\mathbb Z$. The quotient CW structure on $S^2$ has the same unique $2$-cell and no $1$-cells. The cellular map induced by $q$ is the identity on the top cellular chain group $\mathbb Z$, hence
\[
q_*:H_2(T^2)\xrightarrow{\cong}H_2(S^2).
\]
Therefore $q$ cannot be nullhomotopic.
:::

<1>3. Every map
\[
f:S^2\to T^2
\]
is nullhomotopic.
::: {.proof}
The universal covering map
\[
p:\mathbb R^2\to T^2
\]
has contractible total space. Since $S^2$ is simply connected, the lifting criterion gives a lift
\[
\widetilde f:S^2\to\mathbb R^2
\]
with $p\widetilde f=f$. The lift is nullhomotopic because $\mathbb R^2$ is contractible. Composing such a nullhomotopy with $p$ gives a nullhomotopy of $f$.
:::
:::
