---
schema: qual/card@1
id: PR-UL3KL
kind: proposition
title: Homology of 3-manifolds
classification:
  areas:
  - topology
  topics:
  - Manifolds
  - Homology
  - Orientation
relations: []
review: draft
---

::: {.proposition}
Let $M^3$ be a **closed connected** 3-manifold and write $H_1(M;\ZZ) = \ZZ^r \oplus F$ with $F$ finite.
Then

- Orientable: $H_* = \qty{ \ZZ,\; \ZZ^r \oplus F,\; \ZZ^r,\; \ZZ }$

- Nonorientable: $H_* = \qty{ \ZZ,\; \ZZ^r \oplus F,\; \ZZ^{r-1} \oplus \ZZ/2,\; 0 }$, and here $r \geq 1$.
:::

::: {.remark}
Hatcher, §3.3, Exercise 24, which is stated for a closed connected 3-manifold and computes $H_2$ from $H_1 = \ZZ^r \oplus F$.

$H_1$ carries torsion in general — the lens space $L(p,1)$ has $H_1 = \ZZ/p$ — so writing it as $\ZZ^r$ was false.
It is $H_2$ that is torsion-free in the orientable case, because Poincaré duality identifies it with $H^1$, and $H^1$ is always torsion-free.
The top group is $\ZZ$ only when $M$ is orientable; a closed connected nonorientable $n$-manifold has $H_n = 0$, by Hatcher Theorem 3.26.
:::
