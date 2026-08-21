---
schema: qual/card@1
id: E-PLJCK
kind: exercise
title: Entire functions with $f(z)/z^{n}\to 0$ at infinity are polynomials of degree
  at most $n-1$
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
solved: true
---

:::{.problem title="?"}
Suppose $f$ is entire and suppose that for some integer $n\geq 1$,
\[
\lim_{z\to \infty} {f(z) \over z^n} = 0
.\]

Prove that $f$ is a polynomial of degree at most $n-1$.

:::

:::{.solution}
Choose $\abs{z}$ large enough so that $\abs{f(z)}/\abs{z}^n < \eps$.
Then write $f(z) = \sum_{k\geq 0} c_k z^k$ and estimate
\[
2\pi \abs{c_k} 
&\leq \oint_{\abs{z} = R} {f(\xi) \over \xi^{k+1}}\dxi \\
&\leq \oint_{\abs{z} = R} {\eps \abs{\xi}^n \over \abs{\xi}^{k+1} } \dxi \\
&= \eps R^{n-(k+1)} \cdot 2\pi R \\
&= \eps C R^{n-k} \\
&\convergesto{\eps \to 0} 0
\]
provided $n-k \leq 0 \iff k\geq n$, since $\eps \to 0$ forces $R\to \infty$.
:::
