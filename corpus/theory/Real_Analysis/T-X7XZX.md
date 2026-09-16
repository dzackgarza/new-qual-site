---
schema: qual/card@1
id: T-X7XZX
kind: theorem
title: Fubini--Tonelli theorem
classification:
  areas:
  - real-analysis
  topics:
  - Fubini-Tonelli
  - Integrals
relations: []
review: draft
---

::: {.theorem}
Let $(X,\mcm,\mu)$ and $(Y,\mcn,\nu)$ be $\sigma$-finite [[D-QYLPH|measure]] spaces, and let $f\colon X\times Y\to\CC$ be $\mcm\otimes\mcn$-[[D-DHFN4|measurable]].
Suppose that one of the iterated integrals of $\abs{f}$ is finite:
$$
\int_X\qty{\int_Y\abs{f(x,y)}\,d\nu(y)}d\mu(x)<\infty\quad\text{or}\quad\int_Y\qty{\int_X\abs{f(x,y)}\,d\mu(x)}d\nu(y)<\infty.
$$
Then $f\in L^1(X\times Y,\mu\times\nu)$, and
$$
\int_{X\times Y}f\,d(\mu\times\nu)=\int_X\qty{\int_Y f(x,y)\,d\nu(y)}d\mu(x)=\int_Y\qty{\int_X f(x,y)\,d\mu(x)}d\nu(y),
$$
where the inner integrals exist for almost every value of the outer variable.
:::
