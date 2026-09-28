---
schema: qual/card@1
id: P-RGCVM
kind: problem
title: Characteristic and minimal polynomials classify similarity of $3\times 3$ matrices
  over $\CC$, but not $4\times 4$
classification:
  areas:
  - algebra
  topics:
  - Canonical Forms
  - Minimal and Characteristic Polynomials
  - Jordan Canonical Form
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-11
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-11
---

::: {.problem}
a. Show that two $3\times 3$ matrices over $\CC$ are similar $\iff$ their characteristic polynomials are equal and their minimal polynomials are equal.

b. Does the conclusion in (a) hold for $4\times 4$ matrices?
Justify your answer with a proof or counterexample.
:::

::: {.solution}
<1>1. Over $\mathbb C$, two matrices are similar if and only if they have the same Jordan canonical form.
::: {.proof}
Every complex matrix is similar to a Jordan matrix, and the multiset of Jordan blocks is uniquely determined up to reordering. Thus it suffices to determine the Jordan block sizes from the characteristic and minimal polynomials.
:::

<1>2. Let $A\in M_3(\mathbb C)$. For each eigenvalue $\lambda$, write
\[
\chi_A(t)=\prod_\lambda (t-\lambda)^{m_\lambda}
\]
and
\[
\mu_A(t)=\prod_\lambda (t-\lambda)^{e_\lambda}.
\]
Then $m_\lambda$ is the total size of the Jordan blocks for $\lambda$, while $e_\lambda$ is the size of the largest Jordan block for $\lambda$.
::: {.proof}
The algebraic multiplicity $m_\lambda$ is the dimension of the generalized $\lambda$-eigenspace, hence the sum of the sizes of all Jordan blocks for $\lambda$. For a Jordan block $J_r(\lambda)$, the minimal polynomial is $(t-\lambda)^r$; taking the least common multiple over all blocks shows that the exponent of $(t-\lambda)$ in $\mu_A$ is the largest such block size.
:::

<1>3. If $m_\lambda\le3$, then the pair $(m_\lambda,e_\lambda)$ uniquely determines the partition of $m_\lambda$ given by the Jordan block sizes.
::: {.proof}
The possible partitions are
\[
1=(1),
\]
\[
2=(2)\quad\text{or}\quad(1,1),
\]
and
\[
3=(3),\quad(2,1),\quad(1,1,1).
\]
For $m=1$ there is only one partition. For $m=2$, the largest part is respectively $2$ or $1$. For $m=3$, the largest part is respectively $3$, $2$, or $1$. Hence the largest block size determines the entire partition whenever $m\le3$.
:::

<1>4. Therefore two $3\times3$ complex matrices are similar if and only if they have the same characteristic polynomial and the same minimal polynomial.
::: {.proof}
If two matrices are similar, their characteristic and minimal polynomials are invariant under similarity, so the forward implication is immediate.

Conversely, suppose $A,B\in M_3(\mathbb C)$ have the same characteristic and minimal polynomials. Then for every eigenvalue $\lambda$, they have the same numbers $m_\lambda$ and $e_\lambda$. Since $m_\lambda\le3$, <1>3 shows that the Jordan block sizes for $\lambda$ are identical for $A$ and $B$. This holds for every eigenvalue, so $A$ and $B$ have the same Jordan form and are similar.
:::

<1>5. The corresponding statement is false for $4\times4$ matrices.
::: {.proof}
Take
\[
A=J_2(0)\oplus J_2(0)
\]
and
\[
B=J_2(0)\oplus J_1(0)\oplus J_1(0).
\]
Both are $4\times4$ nilpotent matrices. Their characteristic polynomials are both
\[
\chi_A(t)=\chi_B(t)=t^4,
\]
and because the largest Jordan block in each case has size $2$, their minimal polynomials are both
\[
\mu_A(t)=\mu_B(t)=t^2.
\]
However, their Jordan block multisets are different: $A$ has type $(2,2)$ while $B$ has type $(2,1,1)$. Hence they are not similar.

Thus the conclusion of part (a) fails in dimension $4$.
:::
:::
