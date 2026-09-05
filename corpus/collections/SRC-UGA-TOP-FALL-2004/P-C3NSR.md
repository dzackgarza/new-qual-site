---
schema: qual/card@1
id: P-C3NSR
kind: problem
title: Every self-map of $S^{2n}$ has a fixed point or an antipodal point
classification:
  areas:
  - topology
  topics:
  - Degree
  - Fixed Points
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 9 of the official UGA Spring 2021 topology exam.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Checked the core statement against problem 8 of the official UGA Fall 2004
    topology exam; that appearance omits the optional degree hint present in
    Spring 2021.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Verified the two normalized straight-line homotopies: no fixed points
    forces degree -1, while no antipodal points forces degree 1.
---

::: {.problem}
Prove that for every continuous map $f: S^{2n} \to S^{2n}$ there is a point $x\in S^{2n}$ such that either $f(x) = x$ or $f(x) = -x$.

> You may use standard facts about degrees of maps of spheres, including that the antipodal map on $S^{2n}$ has degree $d=-1$.
:::

::: {.solution}
<1>1. The conclusion is immediate when $n=0$.
::: {.proof}
The sphere $S^0$ consists of two antipodal points.
For either $x\in S^0$, the value $f(x)$ is necessarily one of those two points, hence
\[
f(x)=x
\qquad\text{or}\qquad
f(x)=-x.
\]
Thus assume from now on that $n\ge1$.
:::

<1>2. Suppose, for contradiction, that $f$ has neither a fixed point nor an antipodal point.
::: {.proof}
Assume that for every $x\in S^{2n}$,
\[
f(x)\ne x
\qquad\text{and}\qquad
f(x)\ne -x.
\]
We will derive two incompatible values for $\deg f$.
:::

<1>3. Since $f$ has no fixed point, it is homotopic to the antipodal map
\[
A(x)=-x.
\]
::: {.proof}
Define
\[
H:S^{2n}\times[0,1]\longrightarrow S^{2n}
\]
by
\[
H(x,t)
=
\frac{(1-t)f(x)-tx}
{\|(1-t)f(x)-tx\|}.
\]
We must check that the denominator never vanishes.
If
\[
(1-t)f(x)-tx=0,
\]
then for $0<t<1$,
\[
(1-t)f(x)=tx.
\]
Taking norms and using $\|f(x)\|=\|x\|=1$ gives
\[
1-t=t,
\]
so $t=\tfrac12$, and then $f(x)=x$, contrary to <1>2. At $t=0$ and $t=1$ the numerator is respectively $f(x)$ and $-x$, both nonzero.
Thus $H$ is well defined and continuous, with
\[
H(x,0)=f(x),
\qquad
H(x,1)=-x=A(x).
\]
Hence $f\simeq A$.
:::

<1>4. Therefore
\[
\deg f=-1.
\]
::: {.proof}
Degree is invariant under homotopy.
By <1>3,
\[
\deg f=\deg A.
\]
The problem allows the standard fact that the antipodal map on the even-dimensional sphere $S^{2n}$ has degree $-1$.
Thus
\[
\deg f=-1.
\]
:::

<1>5. Since $f$ has no antipodal point, it is homotopic to the identity map.
::: {.proof}
Define
\[
K:S^{2n}\times[0,1]\longrightarrow S^{2n}
\]
by
\[
K(x,t)
=
\frac{(1-t)f(x)+tx}
{\|(1-t)f(x)+tx\|}.
\]
If the numerator vanished for some $0<t<1$, then
\[
(1-t)f(x)=-tx.
\]
Taking norms again forces $t=\tfrac12$, and then
\[
f(x)=-x,
\]
contrary to <1>2. The endpoint numerators are nonzero as well.
Hence $K$ is a well-defined homotopy satisfying
\[
K(x,0)=f(x),
\qquad
K(x,1)=x.
\]
Thus $f\simeq\operatorname{id}_{S^{2n}}$.
:::

<1>6. Therefore
\[
\deg f=1.
\]
::: {.proof}
By <1>5 and homotopy invariance of degree,
\[
\deg f
=\deg\operatorname{id}_{S^{2n}}
=1.
\]
:::

<1>7. The assumption in <1>2 is impossible.
::: {.proof}
Steps <1>4 and <1>6 give simultaneously
\[
\deg f=-1
\qquad\text{and}\qquad
\deg f=1,
\]
a contradiction.
Therefore there is some $x\in S^{2n}$ such that
\[
\boxed{f(x)=x\quad\text{or}\quad f(x)=-x}.
\]
:::
:::
