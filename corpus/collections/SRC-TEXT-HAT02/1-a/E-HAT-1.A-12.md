---
schema: qual/card@1
id: E-HAT-1.A-12
kind: problem
title: Separating an element from a subgroup by a finite index overgroup in a free group
classification:
  areas:
  - topology
  topics:
  - Free Groups
  - Covering Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.A, Exercise 12; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used the finite core of the H-cover together with Exercise 10 so the H-loops remain closed while the chosen x-loop remains open.
---

Let $F$ be a finitely generated free group, $H \subset F$ a finitely generated subgroup, and $x \in F - H$.
Show there is a subgroup $K$ of finite index in $F$ such that $K \supset H$ and $x \notin K$.
[Apply Exercise 10.]


::: {.solution}
Realize
\[
F=\pi_1(R,r_0)
\]
where $R$ is a finite rose, and let
\[
p:\widetilde R_H\to R
\]
be the connected covering corresponding to $H$.
Choose a base vertex $\tilde r_0$ above $r_0$.

<1>1. Since $H$ is finitely generated, there is a finite connected subgraph
\[
Y_0\subseteq\widetilde R_H
\]
containing $\tilde r_0$ and closed lifts of loops representing a finite generating set of $H$.
::: {.proof}
Choose generators
\[
h_1,\dots,h_k
\]
of $H$ and reduced edge loops in $R$ representing them.
Their lifts beginning at $\tilde r_0$ are closed because each $h_i\in H$.
The union of these finitely many finite lifted edge loops is a finite connected subgraph $Y_0$.
:::

<1>2. Let $\gamma_x$ be a reduced loop in $R$ representing $x$ and let $\widetilde\gamma_x$ be its lift beginning at $\tilde r_0$.
Its endpoint $\tilde r_1$ is distinct from $\tilde r_0$.
::: {.proof}
A based loop in $R$ lifts closed at $\tilde r_0$ exactly when its class lies in the subgroup corresponding to the pointed cover, namely $H$.
Since $x\notin H$, the lift of $\gamma_x$ is not closed.
:::

<1>3. Let
\[
Y=Y_0\cup\operatorname{im}(\widetilde\gamma_x).
\]
Then $Y$ is a finite connected subgraph containing both distinct vertices $\tilde r_0,\tilde r_1$.
::: {.proof}
Both pieces are finite and contain $\tilde r_0$, so their union is finite and connected.
The endpoint $\tilde r_1$ belongs to the lifted path and is distinct from $\tilde r_0$ by <1>2.
:::

<1>4. By Exercise 10, $Y$ is contained in a finite covering graph
\[
q:Z\to R
\]
with exactly the same vertex set as $Y$.
Let
\[
K=q_*\pi_1(Z,\tilde r_0)\le F.
\]
Then $K$ has finite index in $F$.
::: {.proof}
Exercise 10 completes the finite labeled subgraph $Y$ to a finite-sheeted covering without adding vertices.
Since $Y$ is connected and already contains every vertex of $Z$, the graph $Z$ itself is connected.
Hence the subgroup corresponding to the pointed cover $Z\to R$ has index equal to the finite cardinality of the fiber, so $[F:K]<\infty$.
:::

<1>5. One has
\[
H\subseteq K.
\]
::: {.proof}
Each chosen generator loop $h_i$ has a closed lift in $Y_0\subseteq Y\subseteq Z$ based at $\tilde r_0$.
Hence $h_i\in K$ for every $i$, so the subgroup they generate, namely $H$, is contained in $K$.
:::

<1>6. One has
\[
x\notin K.
\]
::: {.proof}
The lift of $\gamma_x$ in $Z$ beginning at $\tilde r_0$ is forced by uniqueness of path lifting to be the same path $\widetilde\gamma_x$ already contained in $Y$.
Its endpoint is $\tilde r_1\ne\tilde r_0$.
Since Exercise 10 added no vertices and did not change existing edges, this lift remains nonclosed.
Therefore $x\notin q_*\pi_1(Z,\tilde r_0)=K$.
:::

<1>7. Thus
\[
\boxed{H\subseteq K\le F,\qquad [F:K]<\infty,\qquad x\notin K.}
\]
::: {.proof}
Combine <1>4--<1>6.
:::
:::
