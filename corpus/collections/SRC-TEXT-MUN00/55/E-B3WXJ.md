---
schema: qual/card@1
id: E-B3WXJ
kind: problem
title: Fixed points for maps of retracts of the disk
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against the located published solution: dbFin, "Section 55: Problem 1 Solution",
    https://dbfin.com/topology/munkres/chapter-9/section-55-retractions-and-fixed-points/problem-1-solution/
    (read 2026-11-11; kept at tmp/sources/dbfin/section-55-retractions-and-fixed-points/problem-1-solution.txt), and against Munkres,
    Topology (2000), Section 55 Exercise 1, printed p. 353. dbFin's is the same composition $i\circ f\circ r$ and Theorem 55.6; the card writes the three steps out. Nothing needed repair.
---

::: {.exercise}

Show that if $A$ is a retract of $B^2$, then every continuous map $f: A \to A$ has a fixed point.
:::

::: {.solution}
::: pf

::: pf-step
Retraction and map extension:

::: pf-proof

::: pf-step
Since $A$ is a retract of $B^2$, there exists a continuous map $r: B^2 \to A$ such that:
$$
r(a) = a \quad \text{for all } a \in A.
$$
Let $i: A \hookrightarrow B^2$ denote the inclusion map.
:::

::: pf-step
Let $f: A \to A$ be an arbitrary continuous map.
Define the map $g: B^2 \to B^2$ by composition:
$$
g = i \circ f \circ r : B^2 \to B^2.
$$
Because $r, f$, and $i$ are continuous, $g$ is a continuous map from the closed unit disk $B^2$ to itself.
:::

:::

:::

::: pf-step
Existence of a fixed point via Brouwer’s Fixed Point Theorem:

::: pf-proof

::: pf-step
By the Brouwer Fixed Point Theorem in dimension 2, every continuous map from $B^2$ to $B^2$ has at least one fixed point.
Thus there exists a point $x_0 \in B^2$ such that:
$$
g(x_0) = x_0.
$$
:::

:::

:::

::: pf-step
Proof that $x_0 \in A$ and $f(x_0) = x_0$:

::: pf-proof

::: pf-step
By definition of $g$, the image of $g$ is contained in $A$:
$$
x_0 = g(x_0) = f(r(x_0)) \in A.
$$
Thus the fixed point $x_0$ necessarily belongs to the subspace $A$.
:::

::: pf-step
Since $x_0 \in A$ and $r$ is the identity on $A$, we have $r(x_0) = x_0$.
:::

::: pf-step
Substituting $r(x_0) = x_0$ into the equation $x_0 = f(r(x_0))$ gives:
$$
f(x_0) = x_0.
$$
Thus $x_0 \in A$ is a fixed point of $f$.
:::

:::

:::

::: pf-step
Conclusion:
Every continuous map $f: A \to A$ has a fixed point.
:::

:::

:::
