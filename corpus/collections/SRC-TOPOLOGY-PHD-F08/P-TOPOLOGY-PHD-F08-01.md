---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F08-01
kind: problem
title: Compact subsets of metric spaces are closed and bounded
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against Part One, question 1 of the Topology Ph.D. Qualifying Exam dated January 17, 2009 in assets/attachments/F08phdtop.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Boundedness follows from the countable cover by balls centered at one point.
    For closedness, separated an exterior point from each compact-set point by
    disjoint metric balls and used a finite subcover to obtain one neighborhood
    of the exterior point disjoint from the compact set.
---

::: {.problem}
Prove that in a metric space a compact subset is closed and bounded.
If you cannot do it for a general metric space do it for $\mathbb R^n$.
:::

::: {.solution}
Let $(X,d)$ be a metric space and let $K\subseteq X$ be compact.

::: pf

::: {.pf-step #k-bounded}
The set $K$ is bounded.

::: pf-proof
If $K=\varnothing$, it is bounded trivially.
Assume $K\ne\varnothing$ and choose $x_0\in X$.
The family
\[
\{B(x_0,n):n\in\mathbb N,\ n\ge1\}
\]
is an open cover of $K$, since every distance $d(x_0,x)$ is a finite real number.
By compactness, finitely many of these balls cover $K$.
If $N$ is the largest radius among that finite collection, then the balls are nested and
\[
K\subseteq B(x_0,N).
\]
Hence $K$ is bounded.
:::

:::

::: {.pf-step #disjoint-nbhds}
Fix $x\in X\setminus K$.
For every $y\in K$, there are disjoint open neighborhoods $U_y$ of $y$ and $V_y$ of $x$.

::: pf-proof
Since $x\ne y$,
\[
r_y=\frac13d(x,y)>0.
\]
Set
\[
U_y=B(y,r_y),
\qquad
V_y=B(x,r_y).
\]
If $z\in U_y\cap V_y$, the triangle inequality would give
\[
d(x,y)
\le d(x,z)+d(z,y)
<2r_y
=\frac23d(x,y),
\]
a contradiction.
Thus
\[
U_y\cap V_y=\varnothing.
\]
:::

:::

::: {.pf-step #neighborhood-disjoint-from-k}
The point $x$ has an open neighborhood disjoint from $K$.

::: pf-proof
The sets
\[
\{U_y:y\in K\}
\]
form an open cover of $K$.
By compactness, choose
\[
y_1,\ldots,y_m\in K
\]
such that
\[
K\subseteq U_{y_1}\cup\cdots\cup U_{y_m}.
\]
Set
\[
V=V_{y_1}\cap\cdots\cap V_{y_m}.
\]
This is an open neighborhood of $x$.

Suppose $z\in V\cap K$.
Since the $U_{y_i}$ cover $K$, some $i$ satisfies
\[
z\in U_{y_i}.
\]
But $z\in V$ implies
\[
z\in V_{y_i},
\]
contradicting step [](#disjoint-nbhds){.pf-ref}. Therefore
\[
V\cap K=\varnothing.
\]
:::

:::

::: {.pf-step #k-closed}
The set $K$ is closed.

::: pf-proof
By step [](#neighborhood-disjoint-from-k){.pf-ref}, every point of
\[
X\setminus K
\]
has an open neighborhood contained in $X\setminus K$.
Hence $X\setminus K$ is open, so $K$ is closed.
:::

:::

::: pf-step
Therefore every compact subset of a metric space is closed and bounded.

::: pf-proof
Boundedness is step [](#k-bounded){.pf-ref} and closedness is step [](#k-closed){.pf-ref}.
:::

:::

:::

:::
