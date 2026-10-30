---
schema: qual/card@1
id: P-APA24D
kind: problem
title: Induced matrix $1$-norm equals the maximum absolute column sum
classification:
  areas:
  - applied-algebra
  topics:
  - Norms
  - Linear Algebra
relations: []
review: draft
---

::: {.problem}
Let $A \in M_{m,n}(\CC) = \CC^{m \times n}$.
Prove
$$
\norm{A}_1 = \max_{1 \leq j \leq n} \sum_{i=1}^{m} \abs{a_{ij}}
$$
from the definition of the induced matrix $1$-norm in terms of vector $1$-norms:
$$
\norm{A}_1 = \max_{\substack{x \in \CC^n \\ \norm{x}_1 = 1}} \norm{A x}_1.
$$
:::

::: {.solution}

Let
$$
M:=\max_{1\le j\le n}\sum_{i=1}^m\abs{a_{ij}}.
$$

::: pf

::: {.pf-step #ax-bound-by-m}
For every $x\in\CC^n$,
$$
\norm{Ax}_1\le M\norm{x}_1.
$$

::: pf-proof
Write $x=(x_1,\ldots,x_n)^T$. Then
$$
(Ax)_i=\sum_{j=1}^n a_{ij}x_j,
$$
so by the triangle inequality,
$$
\begin{aligned}
\norm{Ax}_1
&=\sum_{i=1}^m\abs{\sum_{j=1}^n a_{ij}x_j}\\
&\le\sum_{i=1}^m\sum_{j=1}^n\abs{a_{ij}}\,\abs{x_j}\\
&=\sum_{j=1}^n\left(\sum_{i=1}^m\abs{a_{ij}}\right)\abs{x_j}\\
&\le M\sum_{j=1}^n\abs{x_j}=M\norm{x}_1.
\end{aligned}
$$
:::

:::

::: {.pf-step #norm-upper-bound}
Hence
$$
\norm{A}_1\le M.
$$

::: pf-proof
If $\norm{x}_1=1$, then step [](#ax-bound-by-m){.pf-ref} gives
$$
\norm{Ax}_1\le M.
$$
Taking the maximum over all such $x$ gives the inequality.
:::

:::

::: {.pf-step #equality-achieved}
There is a unit vector in the vector $1$-norm for which equality holds.

::: pf-proof
Choose $j_0$ with
$$
\sum_{i=1}^m\abs{a_{ij_0}}=M
$$
and let $e_{j_0}$ be the corresponding standard basis vector. Then
$$
\norm{e_{j_0}}_1=1
$$
and
$$
\norm{Ae_{j_0}}_1
=\sum_{i=1}^m\abs{a_{ij_0}}
=M.
$$
Therefore $\norm{A}_1\ge M$.
:::

:::

::: pf-step
Consequently
$$
\boxed{\norm{A}_1=\max_{1\le j\le n}\sum_{i=1}^m\abs{a_{ij}}.}
$$

::: pf-proof
Combine steps [](#norm-upper-bound){.pf-ref} and [](#equality-achieved){.pf-ref}.
:::

:::

:::

:::
