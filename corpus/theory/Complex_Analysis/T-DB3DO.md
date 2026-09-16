---
schema: qual/card@1
id: T-DB3DO
kind: theorem
title: Taylor expansion with holomorphic remainder
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
relations: []
review: draft
---

::: {.theorem}
Let $\Omega\subseteq\CC$ be open, let $z_0\in\Omega$, let $f$ be [[D-V6UQJ|analytic]] on $\Omega$, and let $n\geq1$.
Then there is a function $R_n$ analytic on $\Omega$ such that for all $z\in\Omega$,
$$
f(z)=\sum_{k=0}^{n-1}\frac{f^{(k)}(z_0)}{k!}(z-z_0)^k+R_n(z)(z-z_0)^n.
$$
:::

::: {.proof}
Define $R_n(z)\coloneqq\bigl(f(z)-\sum_{k=0}^{n-1}\frac{f^{(k)}(z_0)}{k!}(z-z_0)^k\bigr)(z-z_0)^{-n}$ for $z\in\Omega\setminus\{z_0\}$.
On a disc about $z_0$ in $\Omega$, $f(z)=\sum_{k\ge0}\frac{f^{(k)}(z_0)}{k!}(z-z_0)^k$, so there $R_n(z)=\sum_{k\ge n}\frac{f^{(k)}(z_0)}{k!}(z-z_0)^{k-n}$ for $z\neq z_0$.
This power series has the same radius of convergence, so setting $R_n(z_0)\coloneqq f^{(n)}(z_0)/n!$ makes $R_n$ analytic at $z_0$; away from $z_0$ it is a quotient of analytic functions with nonvanishing denominator.
:::
