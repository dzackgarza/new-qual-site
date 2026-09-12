---
schema: qual/card@1
id: E-HAT-1.2-4
kind: problem
title: Fundamental group of complement of $n$ lines through origin in $\mathbb{R}^3$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - van Kampen
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.2, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Radially retracted the complement to a sphere punctured at the 2n antipodal line-directions and identified its fundamental group as free of rank 2n-1.
---

Let $X \subset \mathbb{R}^3$ be the union of $n$ lines through the origin.
Compute $\pi_1(\mathbb{R}^3 - X)$.

::: {.solution}
Assume the $n$ lines are distinct.
Let
\[
L_1,\dots,L_n
\]
be these lines and set
\[
Y=\mathbb R^3\setminus X.
\]

<1>1. Radial projection gives a deformation retraction
\[
Y\simeq S^2\setminus\bigl(X\cap S^2\bigr).
\]
::: {.proof}
Since every line $L_i$ passes through the origin, membership in $X$ is invariant under multiplication by a positive scalar.
For $y\in Y$, define
\[
H(y,t)=\left((1-t)+\frac{t}{\|y\|}\right)y.
\]
The scalar factor is positive for all $t\in I$, so $H(y,t)$ lies on the same ray as $y$ and therefore never enters $X$.
At $t=0$ one has $H(y,0)=y$, and at $t=1$ one has
\[
H(y,1)=\frac{y}{\|y\|}\in S^2.
\]
Points already on $S^2$ are fixed.
Thus $H$ is a deformation retraction onto
\[
S^2\setminus(X\cap S^2).
\]
:::

<1>2. The set $X\cap S^2$ consists of exactly $2n$ points.
::: {.proof}
Each line through the origin meets $S^2$ in a pair of antipodal points.
Distinct lines give disjoint antipodal pairs.
Hence
\[
X\cap S^2=\{p_1,-p_1,\dots,p_n,-p_n\}
\]
has cardinality $2n$.
:::

<1>3. A sphere with $k\ge1$ punctures has fundamental group free of rank $k-1$.
::: {.proof}
Choose one puncture $q$.
Stereographic projection from $q$ gives a homeomorphism
\[
S^2\setminus\{q\}\cong\mathbb R^2.
\]
Removing the remaining $k-1$ punctures therefore gives
\[
S^2\setminus\{q,q_2,\dots,q_k\}
\cong
\mathbb R^2\setminus\{a_2,\dots,a_k\}.
\]

Choose pairwise disjoint small closed disks around the points $a_2,\dots,a_k$ and join their boundary circles to a common basepoint by pairwise disjoint arcs arranged as a tree.
The complement deformation retracts onto the union of these $k-1$ circles and the joining tree.
Collapsing the tree gives a wedge of $k-1$ circles.
Hence
\[
\pi_1\bigl(S^2\setminus\{q_1,\dots,q_k\}\bigr)
\cong
F_{k-1},
\]
the free group on $k-1$ generators.
:::

<1>4. Therefore
\[
\pi_1(\mathbb R^3\setminus X)\cong F_{2n-1}.
\]
::: {.proof}
By <1>1--<1>2,
\[
Y\simeq S^2\setminus\{2n\text{ points}\}.
\]
Apply <1>3 with $k=2n$.
Thus
\[
\boxed{\pi_1(\mathbb R^3\setminus X)\cong F_{2n-1}}.
\]
:::
:::
