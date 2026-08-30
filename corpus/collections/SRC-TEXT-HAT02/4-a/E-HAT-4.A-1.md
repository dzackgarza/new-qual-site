---
schema: qual/card@1
id: E-HAT-4.A-1
kind: exercise
title: "Homotopies of maps to topological groups are basepoint-preserving"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

Show directly that if $X$ is a topological group with identity element $x_0$, then any two maps $f, g: (Z, z_0) \to (X, x_0)$ which are homotopic are homotopic through basepoint-preserving maps.

::: {.solution}
<1>1. Let $F:Z\times I\to X$ be a homotopy with $F(z_0,t)=\gamma(t)$ a path from $x_0$ to $x_0$.
Proof: given.

<1>2. Define $G(z,t)=F(z,t)\cdot \gamma(t)^{-1}$ (using group multiplication).
Proof: translate by $\gamma(t)^{-1}$.

<1>3. $G(z_0,t)=x_0$ for all $t$, and $G(\cdot,0)=f$, $G(\cdot,1)=g$.
Proof: <1>2 and $\gamma(0)=\gamma(1)=x_0$ up to homotopy; adjust.

<1>4. Hence $f$ and $g$ are homotopic through basepoint-preserving maps.
Proof: <1>3.

<1>5. Q.E.D.
Proof: <1>4.
:::
