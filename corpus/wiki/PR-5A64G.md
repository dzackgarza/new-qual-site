---
schema: qual/card@1
id: PR-5A64G
kind: proposition
title: Zeros and their orders
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros
  - Power Series
  - Holomorphic Functions
relations: []
review: draft
---

:::{.proposition title="Zeros and their orders"}
A **zero** of an analytic function on a domain $\Omega$ is any $z_0$ such that $f(z_0)=0$, with no further conditions.
If $f$ is analytic and not identically zero on $\Omega$ with $f(z_0) = 0$, then there exists a  neighborhood $U\ni z_0$ and function $g$ that is holomorphic and nonvanishing on $U$ such that 
\[
f(z) = (z-z_0)^n g(z)
.\]
We refer to $z_0$ as a **zero of order $n$**.
Equivalently, $f^{(n-1)}(z_0)=0$ but $f^{(n)}(z) \neq 0$, so the Laurent expansion has the form $f(z) = \sum_{k\geq n} c_k (z-z_0)^k$ where $c_n\neq 0$.
:::
