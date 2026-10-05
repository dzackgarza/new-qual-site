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

<1>1. The hypothesis
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

::: {.proof}
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

<1>2. For a complex matrix in Jordan normal form, the exponent of
\[
(t-\lambda)
\]
in the minimal polynomial equals the size of the largest Jordan block with eigenvalue $\lambda$.

::: {.proof}
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

<1>3. For each eigenvalue $\lambda_i$, the largest Jordan block of either $A$ or $B$ has size
\[
a_i-1.
\]

::: {.proof}
By step <1>1, the exponent of
\[
(t-\lambda_i)
\]
in the common minimal polynomial is
\[
a_i-1.
\]
Apply step <1>2 to $A$ and to $B$.
:::

<1>4. For each $i$, one necessarily has
\[
a_i\ge2.
\]

::: {.proof}
Because $\lambda_i$ is an eigenvalue, the minimal polynomial must be divisible by
\[
t-\lambda_i.
\]
Hence
\[
m_i\ge1.
\]
By step <1>1,
\[
a_i-1\ge1,
\]
so
\[
a_i\ge2.
\]
:::

<1>5. For each eigenvalue $\lambda_i$, the Jordan block sizes are uniquely determined:
\[
\boxed{
(a_i-1,\ 1).
}
\]

::: {.proof}
The algebraic multiplicity of $\lambda_i$ is $a_i$, so the sizes of all Jordan blocks carrying eigenvalue $\lambda_i$ sum to $a_i$.

By step <1>3, one of those blocks has size
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

<1>6. The Jordan normal forms of $A$ and $B$ have exactly the same blocks, up to permutation.

::: {.proof}
The characteristic polynomial determines the distinct eigenvalues
\[
\lambda_1,\ldots,\lambda_k
\]
and their algebraic multiplicities
\[
a_1,\ldots,a_k.
\]
For each $\lambda_i$, step <1>5 uniquely determines the Jordan blocks:
\[
J_{a_i-1}(\lambda_i)
\qquad\text{and}\qquad
J_1(\lambda_i).
\]
Therefore both $A$ and $B$ have the same multiset of Jordan blocks.
Only the order of the blocks may differ.
:::

<1>7. Therefore
\[
\boxed{A\text{ and }B\text{ are similar}.}
\]

::: {.proof}
Over $\mathbb C$, two matrices are similar if and only if their Jordan normal forms agree up to permutation of Jordan blocks.
Step <1>6 gives exactly this agreement.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required conclusion.
:::
:::
