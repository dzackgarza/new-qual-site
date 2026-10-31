---
schema: qual/card@1
id: E-SS2.PR-4
kind: problem
title: Converse of Runge's theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Runge
  - Polynomial Approximation
relations: []
review: draft
---

::: {.exercise}
Prove the converse to Runge's theorem: if $K$ is a compact set whose complement is not connected, then there exists a function $f$ holomorphic in a neighborhood of $K$ which cannot be approximated uniformly by polynomials on $K$.

[Hint: Pick a point $z_0$ in a bounded component of $K^c$, and let $f(z) = 1/(z - z_0)$. If $f$ can be approximated uniformly by polynomials on $K$, show that there exists a polynomial $p$ such that $\abs{(z - z_0)p(z) - 1} < 1$ on $K$. Use the maximum modulus principle (Chapter 3) to show that this inequality continues to hold for all $z$ in the component of $K^c$ that contains $z_0$.]
:::
