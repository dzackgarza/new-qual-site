---
schema: qual/card@1
id: P-ALGF24C
kind: problem
title: $p$-elements in $\mathrm{GL}_n(\mathbb{F}_p)$ and conjugacy classes matching $S_n$
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Group Theory
  - Permutations
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-6-astra-pro
  date: 2026-09-07
  note: Compared both parts with Problem 3 on page 4 of the official FA24 algebra exam PDF.
- event: solution-written
  by: gpt-6-astra-pro
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-6-astra-pro
  date: 2026-09-07
  note: Checked both implications of the p-element criterion, Jordan form over the base field, uniqueness from kernel dimensions, and the identity element of order p^0.
---

::: problem
Suppose $p$ is a prime and $n$ is a positive integer.
An element $x \in \mathrm{GL}_n(\mathbb{F}_p)$ is called a $p$-element if its order is a power of $p$.

(a) Prove that $x$ is a $p$-element if and only if $x - 1$ is nilpotent.

(b) Prove that the number of conjugacy classes of $\mathrm{GL}_n(\mathbb{F}_p)$ that consist of $p$-elements is the same as the number of conjugacy classes of the symmetric group $S_n$.
:::

::: {.solution}
Write $I$ for the identity matrix and $N=x-I$.

<1>1. The matrix $x$ has $p$-power order if and only if $N$ is nilpotent.
::: {.proof}
In characteristic $p$, commuting matrices $A,B$ satisfy
\[
(A+B)^{p^r}=A^{p^r}+B^{p^r}\qquad(r\ge0).
\]
For $r=1$ this follows from the binomial theorem and the divisibility of $\binom pj$ by $p$ for $0<j<p$; iteration proves the formula for all $r$.
In particular,
\[
(x-I)^{p^r}=x^{p^r}-I.
\]
If $x$ has order $p^r$, this shows $N^{p^r}=0$.
Conversely, if $N^s=0$, choose $r\ge0$ with $p^r\ge s$.
Then
\[
x^{p^r}=(I+N)^{p^r}=I+N^{p^r}=I,
\]
so the order of $x$ divides $p^r$ and is a power of $p$.
This includes the identity, whose order is $1=p^0$, and proves part (a).
:::

<1>2. The correspondence $N\mapsto I+N$ induces a bijection from similarity classes of nilpotent matrices to conjugacy classes of $p$-elements in $\mathrm{GL}_n(\mathbb{F}_p)$.
::: {.proof}
For nilpotent $N$ with $N^s=0$, the finite sum
\[
I-N+N^2-\cdots+(-1)^{s-1}N^{s-1}
\]
is an inverse of $I+N$.
Thus <1>1 applies and identifies exactly the $p$-elements.
For every invertible matrix $S$,
\[
S(I+N)S^{-1}=I+SNS^{-1}.
\]
Consequently $I+N$ and $I+N'$ are conjugate if and only if $N$ and $N'$ are similar.
:::

<1>3. Similarity classes of nilpotent $n\times n$ matrices over $\mathbb{F}_p$ are indexed by partitions of $n$.
::: {.proof}
The minimal polynomial of a nilpotent matrix is a power of $t$, which splits over $\mathbb{F}_p$.
Its Jordan form therefore exists over $\mathbb{F}_p$, not merely over an extension field, and consists of blocks
\[
J_{\lambda_1}(0),\ldots,J_{\lambda_k}(0),
\qquad \lambda_1\ge\cdots\ge\lambda_k\ge1,
\qquad \sum_i\lambda_i=n.
\]
Conversely, every such partition defines a nilpotent matrix by taking this block diagonal sum.

To see explicitly that distinct partitions cannot become similar over $\mathbb{F}_p$, put $d_j=\dim\ker N^j$, with $d_0=0$.
For these blocks,
\[
d_j=\sum_i\min(j,\lambda_i),\qquad
d_j-d_{j-1}=\#\{i:\lambda_i\ge j\}.
\]
The similarity-invariant numbers $d_j$ recover the number of blocks of each size, hence the partition.
Matrices with the same partition have the same Jordan form and are similar.
:::

<1>4. Conjugacy classes in $S_n$ are also indexed by partitions of $n$, proving part (b).
::: {.proof}
The lengths of the disjoint cycles of a permutation, including its fixed points as cycles of length one, form a partition of $n$.
Conjugation relabels each cycle and preserves these lengths.
Conversely, for two permutations with the same cycle lengths, choose a bijection of their letters that matches cycles of equal length in cyclic order.
This bijection conjugates one permutation to the other.
Every partition occurs by arranging the $n$ letters into disjoint cycles of its prescribed lengths.
Thus <1>2 and <1>3 identify the conjugacy classes of $p$-elements, and the cycle decomposition identifies the conjugacy classes of $S_n$, with the same set of partitions.
:::
:::
