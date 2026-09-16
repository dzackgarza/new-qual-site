---
schema: qual/card@1
id: T-RA-WORKSHOP-D5-4-3
kind: theorem
title: Taylor's theorem with Lagrange remainder
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
relations: []
review: draft
---

::: {.theorem}
Let $a<b$, $n\geq0$, and $c\in[a,b]$.
Suppose $f\colon[a,b]\to\RR$ is $n$ times continuously differentiable on $[a,b]$ and $f^{(n+1)}$ exists on $(a,b)$.
Let
$$
P_n(x)\coloneqq\sum_{k=0}^{n}\frac{f^{(k)}(c)}{k!}(x-c)^k
=f(c)+f'(c)(x-c)+\cdots+\frac{f^{(n)}(c)}{n!}(x-c)^n .
$$
Then for every $x\in[a,b]$ with $x\neq c$ there exists $\xi$ strictly between $c$ and $x$ such that
$$
f(x)=P_n(x)+\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-c)^{n+1}.
$$
In particular, if $M\geq0$ and $\abs{f^{(n+1)}(t)}\leq M$ for all $t\in(a,b)$, then
$$
\abs{f(x)-P_n(x)}\leq\frac{M\abs{x-c}^{n+1}}{(n+1)!}\quad\text{for all } x\in[a,b].
$$
[@Rud76].
:::
