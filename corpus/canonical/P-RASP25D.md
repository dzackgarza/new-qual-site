---
schema: qual/card@1
id: P-RASP25D
kind: problem
title: "Closed convex set in L^1 with no best approximation"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
solved: false
---

::: problem
Let $E$ be the Banach space $L^1([0,1])$ and
$$
C := \left\{u \in E : u(x) \geq 0 \text{ a.e. } x \in [0,1],\; \int_0^1 x u(x)\,dx \geq 1\right\}.
$$

Show that

(1) $C$ is nonempty, closed and convex in $E$.

(2) $d(0, C) := \inf\{\|u\| : u \in C\} = 1$.

Hint: try piecewise constant functions.

(3) There is no $u \in C$ such that $\|u\| = d(0, C) = 1$.
:::
