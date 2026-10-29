---
schema: qual/card@1
id: T-QMGPN
kind: theorem
title: Implicit function theorem
slogan: 'A relation is locally the graph of a function wherever the derivative block in the solved-for variables is invertible.'
classification:
  areas:
    - complex-analysis
    - real-analysis
  topics:
    - Calculus
relations: []
review: draft
---

::: {.theorem}
Suppose $f\in C^1(\RR^{m+n}, \RR^n)$, written $f(x,y)$ with $x\in\RR^m$ and $y\in\RR^n$, that $f(a, b) = 0$, and that the partial derivative in the second block, $\partial f/\partial y\, (a,b)$, is an invertible $n\times n$ matrix.
Then there exists a connected open neighborhood $U\subseteq \RR^m$ of $a$ and a unique $g\in C^1(U, \RR^n)$ such that $g(a) = b$ and $f(x, g(x)) = 0$ for all $x\in U$ [@Mun91, Section 9, Theorem 9.2].
:::
