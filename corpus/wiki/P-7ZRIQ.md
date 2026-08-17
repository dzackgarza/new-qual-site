---
schema: qual/card@1
id: P-7ZRIQ
kind: problem
title: Rouché's theorem and $\max_{|z|=1}|P(z)|\ge 1$ for a monic polynomial $P$
classification:
  areas:
  - complex-analysis
  topics:
  - rouche
  - maximum-modulus-principle
  - polynomials
relations: []
review: draft
solved: true
---
:::{.problem}
Prove that
\[
\max_{\abs z = 1} \abs{a_0 + a_1 z + \cdots + a_{n-1}z^{n-1} + z^n} \geq 1
.\]

> Hint: the first part of the problem asks for a statement of Rouche's theorem.

:::

:::{.solution}
Write $p(z) \da a_0 + \cdots + z^n$.
Toward a contradiction, suppose not so that $\abs{p(z)} < 1$ on $\abs{z} = 1$.
Then
\[
\abs{f(z)} < 1 = \abs{z}^n \qquad \text{ on } \abs{z} = 1
.\]
Taking $m(z) \da f(z)$ and $M(z) \da -z^n$, we have 
\[
n = \size Z_M = \size Z_{M+m} = \size Z_{f(z) - z^n} \leq n-1
,\]
since $f(z) - z^n$ is degree at most $n-1$, a contradiction.

:::

