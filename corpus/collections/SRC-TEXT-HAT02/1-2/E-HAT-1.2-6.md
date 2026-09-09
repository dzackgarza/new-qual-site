---
schema: qual/card@1
id: E-HAT-1.2-6
kind: problem
title: Complement of closed discrete subspace of $\mathbb{R}^n$ simply-connected for $n \geq 3$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - van Kampen
  - Simply Connected
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.2, Exercise 6; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Replaced each puncture by a small boundary sphere, then filled the spheres by n-cells and applied Proposition 1.26(b).
---

Use Proposition 1.26 to show that the complement of a closed discrete subspace of $\mathbb{R}^n$ is simply-connected if $n \geq 3$.

::: {.solution}
Let $D\subset\mathbb R^n$ be closed and discrete, with $n\ge3$, and put
\[
Y=\mathbb R^n\setminus D.
\]

<1>1. Choose pairwise disjoint closed balls
\[
B_d=\overline{B}(d,r_d),\qquad d\in D,
\]
whose family is locally finite.
::: {.proof}
Since $D$ is discrete, for each $d\in D$ there is $\epsilon_d>0$ such that
\[
B(d,\epsilon_d)\cap D=\{d\}.
\]
Choose
\[
0<r_d<\min\{1,\epsilon_d/3\}.
\]
If $d\ne e$, then $\epsilon_d\le\|d-e\|$ and $\epsilon_e\le\|d-e\|$, so
\[
r_d+r_e<\frac23\|d-e\|<\|d-e\|.
\]
Hence the closed balls are pairwise disjoint.
Moreover, if a compact set $K$ meets $B_d$, then $d$ lies in the closed $1$-neighborhood of $K$, which is compact.
A closed discrete subset of Euclidean space meets a compact set in only finitely many points, so only finitely many of the balls meet $K$.
Thus the family is locally finite.
:::

<1>2. The complement $Y$ deformation retracts onto
\[
Z=\mathbb R^n\setminus\bigcup_{d\in D}\operatorname{int}(B_d).
\]
::: {.proof}
Inside each punctured ball $B_d\setminus\{d\}$, radially push every point away from $d$ onto the boundary sphere $\partial B_d$, fixing the boundary.
Outside the interiors of the balls, fix every point.
The balls are pairwise disjoint and locally finite, so these radial homotopies patch to a continuous global deformation retraction
\[
Y\simeq Z.
\]
:::

<1>3. The space $\mathbb R^n$ is obtained from $Z$ by attaching one $n$-cell for each $d\in D$ along the sphere $\partial B_d$.
::: {.proof}
Each omitted open ball is restored by adjoining the closed ball $B_d\cong D^n$ along its boundary
\[
\partial B_d\cong S^{n-1}\subset Z.
\]
Since the balls are disjoint, doing this for all $d\in D$ recovers all of $\mathbb R^n$.
:::

<1>4. The inclusion
\[
Z\hookrightarrow\mathbb R^n
\]
induces an isomorphism on fundamental groups.
::: {.proof}
By <1>3, $\mathbb R^n$ is obtained from $Z$ by attaching cells all of the same dimension $n>2$.
Proposition 1.26(b) says that attaching cells of dimension greater than $2$ does not change the fundamental group.
Hence
\[
\pi_1(Z)\cong\pi_1(\mathbb R^n)=0.
\]
:::

<1>5. Therefore $Y$ is simply connected.
::: {.proof}
By <1>2,
\[
\pi_1(Y)\cong\pi_1(Z)=0.
\]
Also $Y$ is path connected: any two points can be joined by a polygonal path, and since $D$ is discrete one can perturb finitely many segments slightly to avoid the finitely many points of $D$ met by a compact polygonal path.
Thus $Y$ is path connected with trivial fundamental group, hence simply connected.
:::
:::
