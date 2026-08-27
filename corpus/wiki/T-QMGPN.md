---
schema: qual/card@1
id: T-QMGPN
kind: theorem
title: Implicit Function Theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Calculus
relations: []
review: draft
---

::: {.theorem}
Suppose $f\in C^1(\RR^{m+n}, \RR^n)$, written $f(x,y)$ with $x\in\RR^m$ and $y\in\RR^n$, that $f(a, b) = 0$, and that the partial derivative in the second block, $\partial f/\partial y\, (a,b)$, is an invertible $n\times n$ matrix.
Then there exists a neighborhood $U\subseteq \RR^m$ containing $a$ and a unique $g\in C^1(U, \RR^n)$ such that $g(a) = b$ and $f(x, g(x)) = 0$ for all $x\in U$.
:::

::: {.slogan}
A relation is locally the graph of a function wherever the block of the derivative belonging to the solved-for variables is nonsingular.
:::

::: {.concept}
See Munkres, *Analysis on Manifolds*, §9, Theorem 9.2, p. 71. The full derivative $D_f(a,b): \RR^{m+n}\to\RR^n$ is never invertible unless $m=0$; the hypothesis is on the $n\times n$ block belonging to the variables being solved for.
:::
