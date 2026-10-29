---
schema: qual/card@1
id: E-ZQGR5
kind: problem
title: Radius of convergence
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Convergence Tests
relations: []
review: draft
---

::: {.exercise}
Find the radius of convergence of the following series, where $a$ is a constant.

(a) $\sum a^k z^k$.

(b) $\sum a^{k^2}z^k$.
:::

::: {.solution}

By the Cauchy--Hadamard formula, the radius of convergence $R$ of $\sum c_kz^k$ satisfies $1/R=\limsup_{k\to\infty}\abs{c_k}^{1/k}$, with the conventions $1/0=\infty$ and $1/\infty=0$.

::: pf

::: pf-step
(a) $R = \boxed{\infty}$ if $a=0$ and $R=\boxed{\abs{a}^{-1}}$ if $a\neq 0$.

::: pf-proof
For $c_k=a^k$, $\abs{c_k}^{1/k}=\abs{a}$ for every $k$, so $1/R=\abs{a}$.
:::

:::

::: pf-step
(b) $R=\boxed{\infty}$ if $\abs{a}<1$, $R=\boxed{1}$ if $\abs{a}=1$, and $R=\boxed{0}$ if $\abs{a}>1$.

::: pf-proof
For $c_k=a^{k^2}$, $\abs{c_k}^{1/k}=\abs{a}^k$, whose limit is $0$, $1$ or $\infty$ according as $\abs{a}<1$, $\abs{a}=1$ or $\abs{a}>1$.
:::

:::

:::

:::
