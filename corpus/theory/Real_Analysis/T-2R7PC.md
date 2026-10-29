---
schema: qual/card@1
id: T-2R7PC
kind: theorem
title: Taylor remainders in Lagrange, Cauchy, and integral form
slogan: 'The Taylor remainder $R_n(x)$ equals an $n$th-derivative term at an intermediate point in Lagrange and Cauchy form, and an integral of $f^{(n)}$ when $f^{(n)}$ is continuous.'
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

::: {.remark title="Variations"}
The Lagrange form holds on a closed interval with the expansion point allowed at an endpoint.
Let $a<b$, $n\geq1$ and $c\in[a,b]$, and let $f\colon[a,b]\to\RR$ have $f^{(n-1)}$ continuous on $[a,b]$ and $f^{(n)}$ defined on $(a,b)$.
Then for every $x\in[a,b]$ with $x\neq c$ there exists $\xi$ strictly between $c$ and $x$ with
$$
f(x)=\sum_{k=0}^{n-1}\frac{f^{(k)}(c)}{k!}(x-c)^k+\frac{f^{(n)}(\xi)}{n!}(x-c)^{n}.
$$
In particular, if $\abs{f^{(n)}(t)}\leq M$ for all $t\in(a,b)$, then the remainder satisfies $\abs{R_n(x)}\leq M\abs{x-c}^{n}/n!$ for all $x\in[a,b]$.
:::
