---
schema: qual/card@1
id: PR-CRVGRP
kind: proposition
title: The group law on an elliptic curve, and multiplication by $n$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Group Schemes
  - Torsion
relations:
- kind: uses
  target: T-U5QSY
- kind: uses
  target: T-MWDVL
review: draft
prompts:
- Why is an elliptic curve a group?
- Is an elliptic curve a group scheme?
- What is the kernel of multiplication by $n$?
---

::: {.proposition}
Let $E$ be a curve of genus $1$ with a chosen point $p_0$.
Then $p \mapsto \OO_E(p - p_0)$ is a bijection $E \to \Pic^0(E)$, and the group structure it pulls back makes $E$ a group variety: inversion and addition are morphisms, so $E$ is a group scheme over $k$ with identity $p_0$.
Under the embedding by $\abs{3p_0}$ as a plane cubic, three points sum to zero exactly when they are collinear.
:::

::: {.proposition title="Multiplication by $n$"}
$[n] \colon E \to E$ is a finite morphism of degree $n^2$.
If $n$ is prime to $\operatorname{char} k$ then $E[n] \cong (\ZZ/n)^2$.
If $n = p = \operatorname{char} k$ then $E[p]$ is $\ZZ/p$ or trivial, according to the Hasse invariant; the trivial case is called supersingular.
:::

::: {.remark}
The bijection is the whole proof and is pure Riemann--Roch: given $D$ of degree zero, $D + p_0$ has degree $1 > 2g-2 = 0$, so $\ell(D+p_0) = 1$ and there is a unique effective divisor $x$ with $x \sim D + p_0$, that is $D \sim x - p_0$.
Surjectivity and injectivity both fall out of this uniqueness.

The chord-and-tangent construction is then a translation of the same statement: $p + q + r \sim 3p_0$ exactly when $p, q, r$ are cut out by a line, since $\abs{3p_0}$ is the hyperplane system.
So the geometric group law is not an extra structure, it is the linear equivalence written in coordinates.

Two facts worth having: a morphism of elliptic curves carrying base point to base point is automatically a group homomorphism, and $\operatorname{End}(E, p_0)$ is a ring containing $\ZZ$. When it is strictly larger, $E$ has complex multiplication, which over $\CC$ means $\tau$ generates an imaginary quadratic field.
:::
