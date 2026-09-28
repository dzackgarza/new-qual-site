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
Let $A \in M_{m,n}(\mathbb{C}) = \mathbb{C}^{m \times n}$.
Prove
\[
\|A\|_1 = \max_{1 \leq j \leq n} \sum_{i=1}^{m} |a_{ij}|
\]
from the definition of the induced matrix $1$-norm in terms of vector $1$-norms:
\[
\|A\|_1 = \max_{\substack{x \in \mathbb{C}^n \\ \|x\|_1 = 1}} \|A x\|_1.
\]
:::

::: {.solution}
Let
\[
M:=\max_{1\le j\le n}\sum_{i=1}^m|a_{ij}|.
\]

<1>1. For every $x\in\mathbb C^n$,
\[
\|Ax\|_1\le M\|x\|_1.
\]
::: {.proof}
Write $x=(x_1,\ldots,x_n)^T$. Then
\[
(Ax)_i=\sum_{j=1}^n a_{ij}x_j,
\]
so by the triangle inequality,
\[
\begin{aligned}
\|Ax\|_1
&=\sum_{i=1}^m\left|\sum_{j=1}^n a_{ij}x_j\right|\\
&\le\sum_{i=1}^m\sum_{j=1}^n|a_{ij}|\,|x_j|\\
&=\sum_{j=1}^n\left(\sum_{i=1}^m|a_{ij}|\right)|x_j|\\
&\le M\sum_{j=1}^n|x_j|=M\|x\|_1.
\end{aligned}
\]
:::

<1>2. Hence
\[
\|A\|_1\le M.
\]
::: {.proof}
If $\|x\|_1=1$, then <1>1 gives
\[
\|Ax\|_1\le M.
\]
Taking the maximum over all such $x$ gives the inequality.
:::

<1>3. There is a unit vector in the vector $1$-norm for which equality holds.
::: {.proof}
Choose $j_0$ with
\[
\sum_{i=1}^m|a_{ij_0}|=M
\]
and let $e_{j_0}$ be the corresponding standard basis vector. Then
\[
\|e_{j_0}\|_1=1
\]
and
\[
\|Ae_{j_0}\|_1
=\sum_{i=1}^m|a_{ij_0}|
=M.
\]
Therefore $\|A\|_1\ge M$.
:::

<1>4. Consequently
\[
\boxed{\|A\|_1=\max_{1\le j\le n}\sum_{i=1}^m|a_{ij}|.}
\]
::: {.proof}
Combine <1>2 and <1>3.
:::
:::
