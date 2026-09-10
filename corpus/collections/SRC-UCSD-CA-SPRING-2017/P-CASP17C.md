---
schema: qual/card@1
id: P-CASP17C
kind: problem
title: "Entire function bounded by 1 + (log(1+|z|))^n is constant"
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Liouville's Theorem
  - Growth Estimates
relations: []
review: draft
---

::: problem
Let $n \geq 0$ be an integer.
Assume $f : \mathbb{C} \to \mathbb{C}$ is an entire function such that
$$
|f(z)| \leq 1 + (\log(1 + |z|))^n.
$$
Prove that $f$ is constant.
:::

::: solution
For every $R>0$, Cauchy's estimate at $0$ gives, for $k\ge1$,
\[
|f^{(k)}(0)|
\le \frac{k!}{R^k}\max_{|z|=R}|f(z)|
\le \frac{k!}{R^k}\Bigl(1+\log(1+R)^n\Bigr).
\]
The right-hand side tends to $0$ as $R\to\infty$. Hence
$f^{(k)}(0)=0$ for every $k\ge1$, so the Taylor series of $f$ is constant.
Thus $f$ is constant on $\mathbb C$.
:::
