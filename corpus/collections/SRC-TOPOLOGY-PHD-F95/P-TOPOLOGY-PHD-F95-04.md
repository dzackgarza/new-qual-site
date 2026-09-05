---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F95-04
kind: problem
title: Hausdorffness of the radial quotient of the closed disk
classification:
  areas:
  - topology
  topics:
  - Quotient Spaces
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked the statement against Section I, problem 4 of the 23 September 1995 topology qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Separated the boundary singleton classes from the collapsed interior
    circles and proved that saturated neighborhoods of two distinct boundary
    classes must meet on circles of radius sufficiently close to one.
---

::: {.problem}
Let $D$ be the closed unit disk in the complex plane.
Let $\sim$ be the equivalence relation on $D$ defined by $z_1\sim z_2$ if and only if $z_1=z_2$ or $|z_1|=|z_2|<1$.
Is the quotient topological space Hausdorff?
(Prove your assertion.)
:::

::: {.solution}
Let
\[
q:D\longrightarrow D/{\sim}
\]
be the quotient map.
The quotient is **not Hausdorff**.

<1>1. Distinct points of the boundary circle determine distinct points of the quotient.
::: {.proof}
Choose distinct points
\[
u,v\in S^1=\{z\in\mathbb C:|z|=1\}.
\]
By definition of the relation, two distinct points can be equivalent only when their common modulus is strictly less than $1$.
Since
\[
|u|=|v|=1
\quad\text{and}\quad
u\ne v,
\]
we have $u\not\sim v$.
Thus
\[
q(u)\ne q(v).
\]
:::

<1>2. Every open neighborhood of $q(u)$ has preimage containing an entire circle of some radius arbitrarily close to $1$.
::: {.proof}
Let $O\subseteq D/{\sim}$ be open and suppose $q(u)\in O$.
Then
\[
U=q^{-1}(O)
\]
is an open subset of $D$ containing $u$.
It is also saturated: if $x\in U$ and $x\sim y$, then
\[
q(y)=q(x)\in O,
\]
so $y\in U$.

Consider the radial path
\[
\gamma_u:[0,1]\longrightarrow D,
\qquad
\gamma_u(t)=(1-t)u.
\]
It is continuous and $\gamma_u(0)=u\in U$.
Hence, for some $\varepsilon>0$,
\[
(1-t)u\in U
\qquad(0<t<\varepsilon).
\]
For each such $t$, the radius $1-t$ is strictly less than $1$.
Therefore every point $z\in D$ satisfying
\[
|z|=1-t
\]
is equivalent to $(1-t)u$ and, by saturation, also belongs to $U$.
:::

<1>3. The two quotient points $q(u)$ and $q(v)$ cannot have disjoint open neighborhoods.
::: {.proof}
Suppose, for contradiction, that there are disjoint open sets $O_u,O_v\subseteq D/{\sim}$ such that
\[
q(u)\in O_u,
\qquad
q(v)\in O_v.
\]
Set
\[
U=q^{-1}(O_u),
\qquad
V=q^{-1}(O_v).
\]
Then $U$ and $V$ are disjoint open saturated subsets of $D$, with $u\in U$ and $v\in V$.

By <1>2 applied to $U$, there is $\varepsilon_u>0$ such that
\[
(1-t)u\in U
\qquad(0<t<\varepsilon_u).
\]
The same argument applied to $V$ gives $\varepsilon_v>0$ such that
\[
(1-t)v\in V
\qquad(0<t<\varepsilon_v).
\]
Choose
\[
0<t<\min\{\varepsilon_u,\varepsilon_v,1\}.
\]
Then
\[
|(1-t)u|=|(1-t)v|=1-t<1,
\]
so
\[
(1-t)u\sim(1-t)v.
\]
Since $U$ is saturated and $(1-t)u\in U$, it follows that $(1-t)v\in U$.
But $(1-t)v\in V$ as well.
Thus
\[
U\cap V\ne\varnothing,
\]
contradicting the disjointness of $O_u$ and $O_v$.
:::

<1>4. Therefore $D/{\sim}$ is not Hausdorff.
::: {.proof}
By <1>1, $q(u)$ and $q(v)$ are distinct points of the quotient.
By <1>3, they cannot be separated by disjoint open neighborhoods.
This violates the Hausdorff separation axiom.
Hence
\[
\boxed{D/{\sim}\text{ is not Hausdorff}.}
\]
:::
:::
