---
schema: qual/card@1
id: P-UCLAB13F-07
kind: problem
title: Hermite interpolation with prescribed derivatives
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The retained PDF defines z_j and m_j only for 1 <= j <= n but prints N+1=sum_{j=0}^n(1+m_j). This card corrects the forced indexing typo to j=1,...,n.
---

::: {.problem}
Let $z_1,\ldots,z_n$ be distinct complex numbers and let $m_j\ge0$ be integers. Write
$$
N+1=\sum_{j=1}^n(1+m_j).
$$
Prove that, given any $N+1$ complex numbers
$$
c_{j,k},\qquad 1\le j\le n,\quad 0\le k\le m_j,
$$
there is a unique polynomial $P(z)$ of degree at most $N$ such that
$$
P^{(k)}(z_j)=c_{j,k}
$$
for all $j,k$.
:::

::: {.solution}

Let
$$
\mathcal P_N
=
\{P\in\CC[z]:\deg P\le N\}.
$$
Then
$$
\dim_{\CC}\mathcal P_N=N+1.
$$

::: pf

::: pf-step

Define the linear map
$$
\Phi:\mathcal P_N
\longrightarrow
\CC^{N+1}
$$
by
$$
\Phi(P)
=
\bigl(P^{(k)}(z_j)\bigr)_
{\substack{1\le j\le n\\0\le k\le m_j}}.
$$


::: pf-proof

The total number of coordinates is
$$
\sum_{j=1}^n(m_j+1)
=
N+1
$$
by hypothesis.
Each coordinate map
$$
P\mapsto P^{(k)}(z_j)
$$
is linear, so $\Phi$ is linear.

:::

:::

::: {.pf-step #s1-2}

If
$$
P^{(k)}(z_j)=0
$$
for
$$
0\le k\le m_j,
$$
then
$$
(z-z_j)^{m_j+1}
$$
divides $P(z)$.


::: pf-proof

Expand $P$ in powers of $z-z_j$:
$$
P(z)
=
\sum_{\ell=0}^N a_\ell(z-z_j)^\ell.
$$
Then
$$
P^{(k)}(z_j)
=
k!\,a_k.
$$
If all these derivatives vanish for $0\le k\le m_j$, then
$$
a_0=a_1=\cdots=a_{m_j}=0.
$$
Hence every surviving term is divisible by
$$
(z-z_j)^{m_j+1}.
$$

:::

:::

::: {.pf-step #s1-3}

If
$$
\Phi(P)=0,
$$
then
$$
\prod_{j=1}^n
(z-z_j)^{m_j+1}
$$
divides $P(z)$.


::: pf-proof

By step [](#s1-2){.pf-ref}, for each $j$,
$$
(z-z_j)^{m_j+1}
$$
divides $P$.
The numbers $z_1,\ldots,z_n$ are distinct, so the corresponding linear factors are pairwise relatively prime.
Therefore the product of these powers divides $P$.

:::

:::

::: {.pf-step #s1-4}

The polynomial
$$
Q(z)
=
\prod_{j=1}^n
(z-z_j)^{m_j+1}
$$
has degree
$$
N+1.
$$


::: pf-proof

By the definition of $N$,
$$
\deg Q
=
\sum_{j=1}^n(m_j+1)
=
N+1.
$$

:::

:::

::: {.pf-step #s1-5}

The map $\Phi$ is injective.


::: pf-proof

Suppose
$$
\Phi(P)=0.
$$
By step [](#s1-3){.pf-ref}, $Q$ divides $P$, while step [](#s1-4){.pf-ref} gives
$$
\deg Q=N+1.
$$
But
$$
\deg P\le N.
$$
The only polynomial of degree at most $N$ divisible by a nonzero polynomial of degree $N+1$ is the zero polynomial.
Thus
$$
P=0.
$$
Hence $\ker\Phi=\{0\}$.

:::

:::

::: {.pf-step #s1-6}

The map $\Phi$ is bijective.


::: pf-proof

The domain has dimension
$$
\dim\mathcal P_N=N+1.
$$
The codomain $\CC^{N+1}$ also has dimension $N+1$.
By step [](#s1-5){.pf-ref}, $\Phi$ is injective.
A linear map between finite-dimensional vector spaces of equal dimension is injective if and only if it is surjective.
Therefore $\Phi$ is bijective.

:::

:::

::: {.pf-step #s1-7}

For every prescribed array
$$
(c_{j,k}),
$$
there exists a unique polynomial $P$ of degree at most $N$ such that
$$
P^{(k)}(z_j)=c_{j,k}
$$
for all $j,k$.


::: pf-proof

The array $(c_{j,k})$ is an arbitrary element of the codomain of $\Phi$.
Surjectivity from step [](#s1-6){.pf-ref} gives existence of a preimage $P$.
Injectivity gives uniqueness.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is exactly the Hermite interpolation statement required.

:::

:::

:::
