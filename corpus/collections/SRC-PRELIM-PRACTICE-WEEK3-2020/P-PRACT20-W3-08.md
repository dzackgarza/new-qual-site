---
schema: qual/card@1
id: P-PRACT20-W3-08
kind: problem
title: Maclaurin series of $f(x)/(1-x)$
classification:
  areas:
  - prelim
  topics:
  - Power Series
relations: []
review: draft
---

::: {.problem}
Assume that $f(x) = \sum_{n=0}^{\infty} a_{n} x^{n}$ converges on $(-1, 1)$. Find the Maclaurin series for $g(x) = f(x)/(1 - x)$.
:::

::: {.solution}
On $(-1,1)$ the series $\frac{1}{1-x}=\sum_{n\ge0}x^n$ converges absolutely, and so does $\sum a_nx^n$ (a power series converges absolutely inside its interval of convergence). Their Cauchy product therefore converges to the product on $(-1,1)$:

$$
g(x)=\left(\sum_{n=0}^{\infty}a_nx^n\right)\left(\sum_{n=0}^{\infty}x^n\right)=\sum_{n=0}^{\infty}\left(\sum_{k=0}^{n}a_k\right)x^n.
$$

Equivalently, writing $g(x)=\sum b_nx^n$ and comparing coefficients in $f(x)=(1-x)g(x)=b_0+\sum_{n\ge1}(b_n-b_{n-1})x^n$ gives $b_0=a_0$ and $b_n=a_n+b_{n-1}$, so by induction $b_n=a_0+a_1+\cdots+a_n$.

More generally, if two power series converge on an open interval $(-r,r)$, then on that interval their product is given by the Cauchy product formula:

$$
\left(\sum_{n=0}^{\infty}c_nx^n\right)\left(\sum_{n=0}^{\infty}d_nx^n\right)=\sum_{n=0}^{\infty}\left(\sum_{k=0}^{n}c_kd_{n-k}\right)x^n.
$$

This formula, with the binomial formula, proves that $e^{x+y}=e^xe^y$ for $x,y\in\RR$.
:::
