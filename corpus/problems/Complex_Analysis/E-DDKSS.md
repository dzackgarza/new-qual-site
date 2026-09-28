---
schema: qual/card@1
id: E-DDKSS
kind: problem
title: An entire function with $\abs{f(z)}\le M\abs z^n$ for large $\abs z$ is a polynomial
  of degree at most $n$
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Cauchy Estimates
  - Polynomials
  - Liouville's Theorem
relations: []
review: draft
---

::: {.exercise}
Suppose that $f$ is entire and has polynomial growth in the following sense:
\[
\abs{f(z)\over z^n} \leq M \text{ for }\abs{z} \geq R
,\]
for some constants $k$ and $R$.
Show that $f$ is a polynomial of degree at most $n$.

:::

::: {.solution}
Since $f$ is entire, it equals its Taylor expansion about $z_0 = 0$, so for every $\rho>0$
\[
f(z) = \sum_{k\geq 0} c_k z^k, && c_k = {f^{(k)}(0)\over k! } = {1\over 2\pi i}\int_{\abs{\xi} = \rho} {f(\xi) \over \xi^{k+1}}\dxi
.\]
For $\rho\geq R$, a direct estimate yields
\[
\abs{c_k} 
&\leq {1\over 2\pi} \int_{\abs{\xi} = \rho} {\abs{f(\xi)} \over \abs{\xi}^{k+1} }\abs{\dxi}\\
&\leq {1\over 2\pi} \int_{\abs{\xi} = \rho} {M \abs{\xi}^n \over \abs{\xi}^{k+1} }\abs{\dxi} \\
&= {M\over 2\pi} \rho^{n-k-1} \cdot 2\pi \rho \\
&= M\rho^{n-k}
,\]
which converges to $0$ as $\rho\to \infty$ provided $k>n$.
So $c_k=0$ for $k>n$, and $f$ is a polynomial of degree at most $n$.
:::

