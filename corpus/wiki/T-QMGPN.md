---
schema: qual/card@1
id: T-QMGPN
kind: theorem
title: "Implicit Function Theorem"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---

::: {.theorem title="Implicit Function Theorem"}
Suppose $f\in C^1(\RR^{n+m}, \RR^n)$, that $f(a, b) = 0$, and the derivative $D_f(a, b)$ at $(a, b)$ is an invertible linear map.
Then there exists a neighborhood $U\subseteq \RR^n$ containing $a$ and a unique $g\in C^1(U, \RR^m)$ such that $g(a) = b$ and $f(a, g(a)) = 0$ for all $x\in U$.
:::
