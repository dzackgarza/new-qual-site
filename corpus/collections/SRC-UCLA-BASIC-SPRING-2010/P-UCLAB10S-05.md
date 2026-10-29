---
schema: qual/card@1
id: P-UCLAB10S-05
kind: problem
title: Similarity from characteristic and minimal polynomials
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 5 of the retained UCLA Basic Examination, Spring 2010.
---

::: {.problem}
Problem 5. Let $A,B$ be $n\times n$ complex matrices with the same minimal polynomial $M(t)$ and the same characteristic polynomial
\[
P(t)=\prod_{i=1}^k(t-\lambda_i)^{a_i},
\qquad \lambda_i\ne\lambda_j\ (i\ne j).
\]
Prove that if
\[
\frac{P(t)}{M(t)}=(t-\lambda_1)\cdots(t-\lambda_k),
\]
then $A$ and $B$ are similar.
:::

::: {.solution}

For each eigenvalue $\lambda_i$, let
\[
m_i
\]
denote the exponent of
\[
(t-\lambda_i)
\]
in the common minimal polynomial $M(t)$.

::: pf

::: {.pf-step #s1-1}

The hypothesis
\[
\frac{P(t)}{M(t)}
=
\prod_{i=1}^k(t-\lambda_i)
\]
implies
\[
\boxed{m_i=a_i-1}
\]
for every $i$.


::: pf-proof

The exponent of
\[
(t-\lambda_i)
\]
in the characteristic polynomial $P$ is $a_i$.
The quotient $P/M$ contains this factor with exponent exactly $1$.
Therefore
\[
a_i-m_i=1,
\]
so
\[
m_i=a_i-1.
\]

:::

:::

::: {.pf-step #s1-2}

For a complex matrix in Jordan normal form, the exponent of
\[
(t-\lambda)
\]
in the minimal polynomial equals the size of the largest Jordan block with eigenvalue $\lambda$.


::: pf-proof

For a single Jordan block
\[
J_r(\lambda)
=
\lambda I+N,
\]
the nilpotent part satisfies
\[
N^r=0
\qquad\text{and}\qquad
N^{r-1}\ne0.
\]
Hence the least power of
\[
J_r(\lambda)-\lambda I
\]
that vanishes is $r$.

For a direct sum of Jordan blocks with eigenvalue $\lambda$, a polynomial power
\[
(t-\lambda)^m
\]
annihilates all such blocks exactly when $m$ is at least the largest block size.
Thus the exponent occurring in the minimal polynomial is precisely that largest size.

:::

:::

::: {.pf-step #s1-3}

For each eigenvalue $\lambda_i$, the largest Jordan block of either $A$ or $B$ has size
\[
a_i-1.
\]


::: pf-proof

By step [](#s1-1){.pf-ref}, the exponent of
\[
(t-\lambda_i)
\]
in the common minimal polynomial is
\[
a_i-1.
\]
Apply step [](#s1-2){.pf-ref} to $A$ and to $B$.

:::

:::

::: pf-step

For each $i$, one necessarily has
\[
a_i\ge2.
\]


::: pf-proof

Because $\lambda_i$ is an eigenvalue, the minimal polynomial must be divisible by
\[
t-\lambda_i.
\]
Hence
\[
m_i\ge1.
\]
By step [](#s1-1){.pf-ref},
\[
a_i-1\ge1,
\]
so
\[
a_i\ge2.
\]

:::

:::

::: {.pf-step #s1-5}

For each eigenvalue $\lambda_i$, the Jordan block sizes are uniquely determined:
\[
\boxed{
(a_i-1,\ 1).
}
\]


::: pf-proof

The algebraic multiplicity of $\lambda_i$ is $a_i$, so the sizes of all Jordan blocks carrying eigenvalue $\lambda_i$ sum to $a_i$.

By step [](#s1-3){.pf-ref}, one of those blocks has size
\[
a_i-1.
\]
The sum of the sizes of all remaining blocks is therefore
\[
a_i-(a_i-1)=1.
\]
Since every Jordan block has positive integer size, there is exactly one remaining block, and it has size $1$.
Thus the complete block-size multiset is
\[
\{a_i-1,1\}.
\]
When
\[
a_i=2,
\]
this means two $1\times1$ blocks.

:::

:::

::: {.pf-step #s1-6}

The Jordan normal forms of $A$ and $B$ have exactly the same blocks, up to permutation.


::: pf-proof

The characteristic polynomial determines the distinct eigenvalues
\[
\lambda_1,\ldots,\lambda_k
\]
and their algebraic multiplicities
\[
a_1,\ldots,a_k.
\]
For each $\lambda_i$, step [](#s1-5){.pf-ref} uniquely determines the Jordan blocks:
\[
J_{a_i-1}(\lambda_i)
\qquad\text{and}\qquad
J_1(\lambda_i).
\]
Therefore both $A$ and $B$ have the same multiset of Jordan blocks.
Only the order of the blocks may differ.

:::

:::

::: {.pf-step #s1-7}

Therefore
\[
\boxed{A\text{ and }B\text{ are similar}.}
\]


::: pf-proof

Over $\CC$, two matrices are similar if and only if their Jordan normal forms agree up to permutation of Jordan blocks.
Step [](#s1-6){.pf-ref} gives exactly this agreement.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required conclusion.

:::

:::

:::
