---
schema: qual/card@1
id: E-SS5.EX-17
kind: problem
title: Entire interpolation on a discrete sequence
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Weierstrass Products
relations: []
review: draft
---

::: {.exercise}
Given two countably infinite sequences of complex numbers $\{a_k\}_{k=0}^{\infty}$ and $\{b_k\}_{k=0}^{\infty}$ with $\lim_{k\to\infty}\abs{a_k}=\infty$, it is always possible to find an entire function $F$ satisfying $F(a_k)=b_k$ for all $k$.

(a) Given $n$ distinct complex numbers $a_1,\ldots,a_n$ and another $n$ complex numbers $b_1,\ldots,b_n$, construct a polynomial $P$ of degree at most $n-1$ with $P(a_i)=b_i$ for $i=1,\ldots,n$.

(b) Let $\{a_k\}_{k=0}^{\infty}$ be a sequence of distinct complex numbers with $a_0=0$ and $\lim_{k\to\infty}\abs{a_k}=\infty$. Let $E$ be a Weierstrass product associated with $\{a_k\}$. Given complex numbers $\{b_k\}_{k=0}^{\infty}$, show that integers $m_k\geq1$ can be chosen so that
$$
F(z)=\frac{b_0}{E'(z)}\frac{E(z)}{z}
+\sum_{k=1}^{\infty}\frac{b_k}{E'(a_k)}\frac{E(z)}{z-a_k}\left(\frac{z}{a_k}\right)^{m_k}
$$
defines an entire function with $F(a_k)=b_k$ for every $k\geq0$. This is the Pringsheim interpolation formula.
:::

::: {.remark}
The source's opening claim needs the interpolation values to agree whenever two $a_k$ coincide. Its formula in (b) prints $E'(z)$ in the first denominator. This makes that summand meromorphic at zeros of $E'$ and gives $F(0)=b_0$ only after replacing it with $E'(0)$.
:::
