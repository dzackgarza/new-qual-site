---
schema: qual/card@1
id: P-HBWYH
kind: problem
title: $F(\alpha)=F(\alpha^2)$ when $\alpha$ has odd degree over $F$, and $\alpha^{2020}$
  has odd degree
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Let $E$ be an extension field of $F$ and $\alpha\in E$ be algebraic of odd degree over $F$.

a. Show that $F(\alpha) = F(\alpha^2)$.

b. Prove that $\alpha^{2020}$ is algebraic of odd degree over $F$.
:::

::: solution
Because $\alpha$ satisfies
\[
x^2-\alpha^2\in F(\alpha^2)[x],
\]
we have
\[
[F(\alpha):F(\alpha^2)]\le2.
\]
By the tower law,
\[
[F(\alpha):F]=[F(\alpha):F(\alpha^2)]\,[F(\alpha^2):F].
\]
The left side is odd, so the first factor cannot be $2$. Hence it equals $1$, and therefore
\[
F(\alpha)=F(\alpha^2).
\]

Now put $\beta=\alpha^{2020}$. Since $\beta\in F(\alpha)$, it is algebraic over $F$, and again the tower law gives
\[
[F(\alpha):F]=[F(\alpha):F(\beta)]\,[F(\beta):F].
\]
The left side is odd, so every positive divisor of it is odd. In particular $[F(\beta):F]$ is odd. Thus $\alpha^{2020}$ is algebraic of odd degree over $F$.
:::
