---
schema: qual/card@1
id: P-BKS03-9A
kind: problem
title: The ring $\ZZ+3i\ZZ$ is not a UFD
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Let
\[
R=\{a+3bi:a,b\in\mathbb Z\}.
\]
Prove that $R$ is a subring of $\mathbb C$, an integral domain, and not a unique factorization domain.
:::

::: {.solution}
It's routine to verify that $R$ is an additive subgroup and is closed under multiplication.
Since $\CC$ is a field, any subring is an integral domain.
Consider two factorizations of the integer $10$ in $R$, namely $10=2\cdot5$ and $10=(1+3i)(1-3i)$. The norm $\abs{z}^2=a^2+9b^2$ of any $z\in R$ is an integer, and if $\abs{z}^2<9$ then $b=0$, so $z$ is a real integer.
This implies in particular that $2$ has no nontrivial factorization in $R$. If $R$ were a UFD, then $2$ would divide $1+3i$ or $1-3i$. But that can't be, since $(1\pm3i)/2$ are not in $R$.
:::
