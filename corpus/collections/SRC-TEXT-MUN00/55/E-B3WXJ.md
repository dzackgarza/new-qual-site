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
---

::: {.exercise}

Show that if $A$ is a retract of $B^2$, then every continuous map $f: A \to A$ has a fixed point.
:::

::: {.solution}
<1>1. Retraction and map extension:
<2>1. Since $A$ is a retract of $B^2$, there exists a continuous map $r: B^2 \to A$ such that:
\[
r(a) = a \quad \text{for all } a \in A.
\]
Let $i: A \hookrightarrow B^2$ denote the inclusion map.
<2>2. Let $f: A \to A$ be an arbitrary continuous map.
Define the map $g: B^2 \to B^2$ by composition:
\[
g = i \circ f \circ r : B^2 \to B^2.
\]
Because $r, f$, and $i$ are continuous, $g$ is a continuous map from the closed unit disk $B^2$ to itself.

<1>2. Existence of a fixed point via Brouwer’s Fixed Point Theorem:
<2>1. By the Brouwer Fixed Point Theorem in dimension 2, every continuous map from $B^2$ to $B^2$ has at least one fixed point.
Thus there exists a point $x_0 \in B^2$ such that:
\[
g(x_0) = x_0.
\]

<1>3. Proof that $x_0 \in A$ and $f(x_0) = x_0$:
<2>1. By definition of $g$, the image of $g$ is contained in $A$:
\[
x_0 = g(x_0) = f(r(x_0)) \in A.
\]
Thus the fixed point $x_0$ necessarily belongs to the subspace $A$.
<2>2. Since $x_0 \in A$ and $r$ is the identity on $A$, we have $r(x_0) = x_0$.
<2>3. Substituting $r(x_0) = x_0$ into the equation $x_0 = f(r(x_0))$ gives:
\[
f(x_0) = x_0.
\]
Thus $x_0 \in A$ is a fixed point of $f$.

<1>4. Conclusion:
Every continuous map $f: A \to A$ has a fixed point. Q.E.D.
:::
