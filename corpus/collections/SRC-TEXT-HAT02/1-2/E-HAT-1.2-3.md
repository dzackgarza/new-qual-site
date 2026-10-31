---
schema: qual/card@1
id: E-HAT-1.2-3
kind: problem
title: Complement of a finite set of points in $\RR^n$ is simply-connected for $n \geq 3$
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
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Show that the complement of a finite set of points in $\RR^n$ is simply-connected if $n \geq 3$.
:::

::: {.solution}
Let $F\subset\RR^n$ be finite, where $n\ge3$, and put $X=\RR^n\setminus F$.

::: pf

::: pf-step
The space $X$ is path connected.

::: pf-proof
For $x,y\in X$, choose $q\in X$ outside the finitely many lines through $x$ and a point of $F$, and through $y$ and a point of $F$. The polygonal path from $x$ to $q$ to $y$ then avoids $F$.
:::

:::

::: pf-step
Every loop in $X$ is homotopic relative to its basepoint to a polygonal loop in $X$.

::: pf-proof
The complement $X$ is open in $\RR^n$, hence locally star-shaped. Apply the path approximation of [[E-HAT-1.1-4|Exercise 1.1.4]] relative to endpoints.
:::

:::

::: pf-step
Every polygonal loop $\gamma$ in $X$ extends to a map $D^2\to X$.

::: pf-proof
Let $e_1,\ldots,e_m$ be its finitely many straight segments. For each $p\in F$ and each $e_i$, the affine span of $p$ and $e_i$ has dimension at most $2$. Since $n\ge3$, choose $q\in X$ outside the union of these finitely many proper affine subspaces. If a segment joining $q$ to a point of $e_i$ contained $p$, then $q$ would lie in the affine span of $p$ and $e_i$, contrary to the choice of $q$. Thus every triangle with vertex $q$ and base $e_i$ avoids $F$. Coning $\gamma$ to $q$ across these triangles defines the required disk map.
:::

:::

::: pf-step
The space $X$ is simply connected.

::: pf-proof
A loop in $X$ is based-homotopic to a polygonal loop by the second step. The third step extends that loop over a disk, so its based homotopy class is trivial. The first step gives path connectedness.
:::

:::

:::

:::
