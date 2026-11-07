---
schema: qual/card@1
id: E-HAT-1.2-6
kind: problem
title: Complement of closed discrete subspace of $\RR^n$ simply-connected for $n \geq 3$
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
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Review the local-finiteness estimate for the chosen balls, the radial deformation retraction onto $Z$, and the attachment of $n$-cells with $n\ge3$, which leaves $\pi_1$ unchanged.
---

::: {.problem}
Use Proposition 1.26 to show that the complement of a closed discrete subspace of $\RR^n$ is simply-connected if $n \geq 3$.
:::

::: {.solution}
Let $D\subset\RR^n$ be closed and discrete, with $n\ge3$, and put
$$
Y=\RR^n\setminus D.
$$

::: pf

::: {.pf-step #s1}

Choose pairwise disjoint closed balls
$$
B_d=\overline{B}(d,r_d),\qquad d\in D,
$$
whose family is locally finite.

::: pf-proof

Since $D$ is discrete, for each $d\in D$ there is $\varepsilon_d>0$ such that
$$
B(d,\varepsilon_d)\cap D=\{d\}.
$$
Choose
$$
0<r_d<\min\{1,\varepsilon_d/3\}.
$$
If $d\ne e$, then $\varepsilon_d\le\norm{d-e}$ and $\varepsilon_e\le\norm{d-e}$, so
$$
r_d+r_e<\frac23\norm{d-e}<\norm{d-e}.
$$
Hence the closed balls are pairwise disjoint.
Moreover, if a compact set $K$ meets $B_d$, then $d$ lies in the closed $1$-neighborhood of $K$, which is compact.
A closed discrete subset of Euclidean space meets a compact set in only finitely many points, so only finitely many of the balls meet $K$.
Thus the family is locally finite.

:::

:::

::: {.pf-step #s2}

The complement $Y$ deformation retracts onto
$$
Z=\RR^n\setminus\bigcup_{d\in D}\operatorname{int}(B_d).
$$

::: pf-proof

Inside each punctured ball $B_d\setminus\{d\}$, radially push every point away from $d$ onto the boundary sphere $\partial B_d$, fixing the boundary.
Outside the interiors of the balls, fix every point.
The balls are pairwise disjoint and locally finite, so these radial homotopies patch to a continuous global deformation retraction
$$
Y\simeq Z.
$$

:::

:::

::: {.pf-step #s3}

The space $\RR^n$ is obtained from $Z$ by attaching one $n$-cell for each $d\in D$ along the sphere $\partial B_d$.

::: pf-proof

Each omitted open ball is restored by adjoining the closed ball $B_d\cong D^n$ along its boundary
$$
\partial B_d\cong S^{n-1}\subset Z.
$$
Since the balls are disjoint, doing this for all $d\in D$ recovers all of $\RR^n$.

:::

:::

::: pf-step

The space $Z$ is path connected, and $\RR^n$ carries the topology of the space obtained from $Z$ by attaching the $n$-cells $B_d$ along their boundary spheres $\partial B_d$.

::: pf-proof

Path connectedness: let $x,y\in Z$ and take a polygonal path in $\RR^n$ from $x$ to $y$. Its image is compact, so by the local finiteness proved in step [](#s1){.pf-ref} it meets only finitely many of the balls $B_d$. For each ball whose interior the path enters, it enters and leaves through the sphere $\partial B_d$, and
$$
\partial B_d\subseteq Z,
$$
because the closed balls are pairwise disjoint and lie outside $D$. Since $n-1\ge2$ the sphere $\partial B_d$ is path connected, so the part of the path in $\operatorname{int}(B_d)$ may be replaced by a path in $\partial B_d$ joining the same two points. Only finitely many such replacements are needed, and each replacement stays in $Z$, so $x$ and $y$ are joined in $Z$.

Topology: $Z$ is closed, each $B_d$ is closed, the interiors of the balls are pairwise disjoint, and by step [](#s1){.pf-ref} the family is locally finite. Hence
$$
\{Z\}\cup\{B_d:d\in D\}
$$
is a locally finite closed cover of $\RR^n$, so $\RR^n$ carries the weak topology with respect to it. That is precisely the topology of the space obtained from $Z$ by attaching the $n$-cells $B_d$ along the attaching maps $\partial B_d\to Z$ of the construction on p. 49.

:::

:::

::: pf-step

The inclusion
$$
Z\hookrightarrow\RR^n
$$
induces an isomorphism on fundamental groups.

::: pf-proof

By step [](#s3){.pf-ref} and the preceding step, $\RR^n$ is obtained from the path connected space $Z$ by attaching a collection of $n$-cells with $n>2$. Proposition 1.26(b) (p. 50) applies to the whole collection at once and gives
$$
\pi_1(Z)\cong\pi_1(\RR^n).
$$
The space $\RR^n$ is contractible, so both groups are trivial.

:::

:::

::: pf-step

Therefore $Y$ is simply connected.

::: pf-proof

By step [](#s2){.pf-ref}, $Y$ deformation retracts onto $Z$, so
$$
\pi_1(Y)\cong\pi_1(Z)=0,
$$
and $Y$ is path connected because $Z$ is.
Thus $Y$ is path connected with trivial fundamental group, hence simply connected.

:::

:::

:::

:::
