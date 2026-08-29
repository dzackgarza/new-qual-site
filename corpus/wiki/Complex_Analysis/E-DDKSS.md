---
schema: qual/card@1
id: E-DDKSS
kind: exercise
title: Polynomial growth
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

:::{.exercise}
Suppose that $f$ is entire and has polynomial growth in the following sense:
\[
\abs{f(z)\over z^n} \leq M \text{ for }\abs{z} \geq R
,\]
for some constants $k$ and $R$.
Show that $f$ is a polynomial of degree at most $n$.

:::

:::{.solution}
Since $f$ is entire, it equals its Laurent expansion about $z_0 = 0$, so
\[
f(z) = \sum_{k\geq 0} c_k z^k, && c_k = {f^{(k)}(0)\over k! } = {1\over 2\pi i}\int_{\abs{\xi} = R} {f(\xi) \over \xi^{k+1}}\dxi
.\]
A direct estimate yields
\[
\abs{c_k} 
&\leq {1\over 2\pi} \int_{\abs{\xi} = R} {\abs{f(\xi)} \over \abs{\xi}^{k+1} }\dxi\\
&\leq {1\over 2\pi} \int_{\abs{\xi} = R} {M \abs{\xi}^n \over \abs{\xi}^{k+1} }\dxi \\
&\leq {M\over 2\pi} \int_{\abs{\xi} = R} \abs{\xi}^{n-(k+1)} \dxi \\
&\leq {M\over 2\pi} \int_{\abs{\xi} = R} R^{n-(k+1)} \dxi \\
&= {M\over 2\pi} R^{n-k-1} \cdot 2\pi R \\
&= MR^{n-k}
,\]
which converges to $0$ as $R\to \infty$ provided $n-k<0$, i.e. $k>n$.
:::

