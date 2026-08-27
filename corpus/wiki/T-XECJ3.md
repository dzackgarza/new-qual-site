---
schema: qual/card@1
id: T-XECJ3
kind: theorem
title: Inverse Function Theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Calculus
  - Biholomorphisms
relations: []
review: draft
---

:::{.theorem}
For $f \in C^1(\RR; \RR)$ with $f'(a) \neq 0$, then $f$ is invertible in a neighborhood $U \ni a$, $g\da f\inv \in C^1(U; \RR)$, and at $b\da f(a)$ the derivative of $g$ is given by
\[
g'(b) = {1 \over f'(a)}
.\]
For $F \in C^1(\RR^n, \RR^n)$ with $D_f$ invertible in a neighborhood of $a$, so $\det(J_f)\neq 0$, then setting $b\da F(a)$,
\[
J_{F\inv}(q) = \qty{J_F(p)}\inv
.\]

The version for holomorphic functions: if $f\in \Hol(\CC; \CC)$ with $f'(p)\neq 0$ then there is a neighborhood $V\ni p$ with that $f\in \BiHol(V, f(V))$.
:::
