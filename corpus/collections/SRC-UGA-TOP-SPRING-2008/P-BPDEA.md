---
schema: qual/card@1
id: P-BPDEA
kind: problem
title: A quotient of a Hausdorff space that is not Hausdorff
classification:
  areas:
  - topology
  topics:
  - Quotient Spaces
  - Hausdorff Spaces
  - Counterexamples
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 3 of the official UGA Spring 2008 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Made the quotient relation x~y iff x-y is rational explicit and proved that
    every nonempty quotient-open set is the whole quotient by density of Q.
    Since R/Q has distinct classes, its indiscrete topology is not Hausdorff.
    Compare Strickland, General Topology, Example 5.63.
---

::: {.problem}
Give an example of a quotient map in which the domain is Hausdorff, but the quotient is not.
:::

::: {.solution}
Define an equivalence relation on $\RR$ by
\[
x\sim y
\quad\Longleftrightarrow\quad
x-y\in\QQ,
\]
and let
\[
q:\RR\longrightarrow\RR/{\sim}
\]
be the quotient map.

<1>1. The domain $\RR$ is Hausdorff.
::: {.proof}
The usual topology on $\RR$ is induced by the metric
\[
d(x,y)=|x-y|,
\]
and every metric space is Hausdorff.
:::

<1>2. Every nonempty open subset of $\RR/{\sim}$ is the whole quotient.
::: {.proof}
Let
\[
V\subseteq\RR/{\sim}
\]
be nonempty and open.
By definition of the quotient topology,
\[
U=q^{-1}(V)
\]
is a nonempty open subset of $\RR$.
Choose $x\in U$ and $\varepsilon>0$ such that
\[
(x-\varepsilon,x+\varepsilon)\subseteq U.
\]

Fix arbitrary $y\in\RR$.
The interval
\[
(x-y-\varepsilon,x-y+\varepsilon)
\]
contains some rational number $r$, since $\QQ$ is dense in $\RR$.
Therefore
\[
y+r\in(x-\varepsilon,x+\varepsilon)\subseteq U.
\]
But
\[
(y+r)-y=r\in\QQ,
\]
so
\[
q(y+r)=q(y).
\]
Since $y+r\in U=q^{-1}(V)$, one has $q(y+r)\in V$, hence $q(y)\in V$.

As $y$ was arbitrary and $q$ is surjective,
\[
V=\RR/{\sim}.
\]
Thus the quotient topology is indiscrete.
:::

<1>3. The quotient $\RR/{\sim}$ has at least two points.
::: {.proof}
The classes of $0$ and $\sqrt2$ are distinct because
\[
\sqrt2-0\notin\QQ.
\]
:::

<1>4. The quotient $\RR/{\sim}$ is not Hausdorff.
::: {.proof}
By <1>2, the only nonempty open subset is the whole space.
By <1>3 there are distinct points in the quotient.
Any neighborhoods of two such points are therefore both the whole quotient and cannot be disjoint.
:::

Hence
\[
\boxed{q:\RR\to\RR/{\sim}}
\]
is a quotient map from a Hausdorff space onto a non-Hausdorff space.
:::
