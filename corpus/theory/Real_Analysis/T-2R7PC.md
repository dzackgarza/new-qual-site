---
schema: qual/card@1
id: T-2R7PC
kind: theorem
title: Taylor remainders in Lagrange, Cauchy, and integral form
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Series of Functions
relations: []
review: draft
---

::: {.theorem}
Let $n\geq1$, $p\in\RR$, $\delta>0$, and let $f\colon(p-\delta,p+\delta)\to\RR$ be $n$ times differentiable.
For $x\in(p-\delta,p+\delta)$ put
$$
R_n(x)\coloneqq f(x)-\sum_{k=0}^{n-1} \frac{f^{(k)}(p)}{k!}(x-p)^k .
$$
Let $x\in(p-\delta,p+\delta)$ with $x\neq p$.

1. (Lagrange form) There exists $\xi$ strictly between $p$ and $x$ such that
$$
R_n(x)=\frac{f^{(n)}(\xi)}{n!}(x-p)^n .
$$

2. (Cauchy form) There exists $\eta$ strictly between $p$ and $x$ such that
$$
R_n(x)=\frac{f^{(n)}(\eta)}{(n-1)!}(x-\eta)^{n-1}(x-p) .
$$

3. (Integral form) If moreover $f^{(n)}$ is continuous on $(p-\delta,p+\delta)$, then
$$
R_n(x)=\int_p^x \frac{f^{(n)}(t)}{(n-1)!}(x-t)^{n-1}\,dt .
$$

Part 1 is in [@Rud76].
:::
