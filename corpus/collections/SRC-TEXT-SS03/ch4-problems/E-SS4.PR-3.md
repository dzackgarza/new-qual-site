---
schema: qual/card@1
id: E-SS4.PR-3
kind: problem
title: Three-lines lemma for bounded holomorphic functions
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
relations: []
review: draft
---

::: {.exercise}
In this problem, we investigate the behavior of certain bounded holomorphic functions in an infinite strip. The particular result described here is sometimes called the three-lines lemma.

(a) Suppose $F(z)$ is holomorphic and bounded in the strip $0<\Im z<1$ and continuous on its closure. If $\abs{F(z)}\leq 1$ on the boundary lines, then prove that $\abs{F(z)}\leq 1$ throughout the strip.

(b) For the more general $F$, let $M_0=\sup_{x\in\RR}\abs{F(x)}$ and $M_1=\sup_{x\in\RR}\abs{F(x+i)}$. Prove that
$$
\sup_{x\in\RR}\abs{F(x+iy)}\leq M_0^{1-y}M_1^y,\qquad 0\leq y\leq 1.
$$

(c) As a consequence, prove that $\log\sup_{x\in\RR}\abs{F(x+iy)}$ is a convex function of $y$ for $0\leq y\leq 1$.
:::

::: {.hint}
For (a), apply the maximum modulus principle to $F_\varepsilon(z)=F(z)e^{-\varepsilon z^2}$. For (b), consider $M_0^{z-1}M_1^{-z}F(z)$.
:::
