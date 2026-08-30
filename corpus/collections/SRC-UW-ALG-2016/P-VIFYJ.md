---
schema: qual/card@1
id: P-VIFYJ
kind: problem
title: $\CC[x,y]/(y^2-(x-1)^3-(x-1)^2)$ is a domain, its real points, and its integral
  closure
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $A = \CC[x,y]/(y^2-(x-1)^3 - (x-1)^2)$.

- Show that $A$ is an integral domain and sketch the $\RR$-points of $\text{Spec} A$.

- Find the integral closure of $A$.
  Recall that for an integral domain $A$ with fraction field $K$, the integral closure of $A$ in $K$ is the set of all elements of $K$ integral over $A$.
:::

::: {.solution}
<1>1. $y^2-(x-1)^2x$ is irreducible in $\C[x,y]$ (Eisenstein at $(x-1)$).
Proof: as polynomial in $y$, $y^2 - (x-1)^2x$.

<1>2. Hence $A$ is domain.
Proof: <1>1.

<1>3. Real points: $y=\pm(x-1)\sqrt{x}$ for $x\ge0$, node at $(1,0)$.
Proof: solve.

<1>4. Let $t=y/(x-1)$, then $t^2=x$, so $A\subset\C[t]$ and $\C[t]$ is integral over $A$ (since $t$ satisfies $t^2-x=0$).
Proof: <1>3.

<1>5. $\C[t]$ is integrally closed, so integral closure is $\C[t]$.
Proof: PID.

<1>6. Q.E.D.
Proof: <1>2 and <1>5.
:::
