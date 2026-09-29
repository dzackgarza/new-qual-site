---
schema: qual/card@1
id: P-ETEJW
kind: problem
title: Rational and Jordan forms with given minimal polynomials over $\mathbb{Q}$
  and $\mathbb{C}$
classification:
  areas:
  - algebra
  topics:
  - Rational Canonical Form
  - Jordan Canonical Form
  - Structure Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Find all possible rational canonical forms for a matrix $A\in M_n(\Bbb Q)$ such that

1. $A$ is $6\times 6$ with minimal polynomial $q(x) = (x-2)^2(x+3)$.

2. $A$ is $7\times 7$ with $q(x) = (x^2+1)(x-7)$.

Also find all such forms when $A \in M_n(\Bbb C)$ instead, and find all possible Jordan Canonical Forms over $\Bbb C$.
:::

::: {.solution}
The rational canonical form of $A$ is determined by its invariant factors $a_1\mid a_2\mid\cdots\mid a_k$, which are monic, satisfy $a_k=q$, and have $\sum_i\deg a_i=n$.

::: pf

::: pf-step

For $n=6$ and $q=(x-2)^2(x+3)$, the invariant-factor lists, over $\QQ$ and over $\CC$ alike, are
$$\begin{aligned}
&q,\ q; &&(x-2),\ (x-2)^2,\ q; &&(x-2),\ (x-2)(x+3),\ q;\\
&(x+3),\ (x-2)(x+3),\ q; &&(x-2),\ (x-2),\ (x-2),\ q; &&(x+3),\ (x+3),\ (x+3),\ q.
\end{aligned}$$

::: pf-proof

The factors $a_1,\dots,a_{k-1}$ divide $q$ and have degrees summing to $3$.
The proper monic divisors of $q$ are $x-2$, $x+3$, $(x-2)^2$ and $(x-2)(x+3)$.
A chain of two factors has degrees $1,2$, giving $(x-2)\mid(x-2)^2$, $(x-2)\mid(x-2)(x+3)$ or $(x+3)\mid(x-2)(x+3)$; a chain of three factors of degree $1$ is constant, giving $(x-2)^3$ or $(x+3)^3$; a single factor of degree $3$ is $q$.
Since $q$ splits over $\QQ$, the lists over $\CC$ are the same.

:::

:::

::: pf-step

The corresponding Jordan forms over $\CC$ are, in the same order,
$$\begin{aligned}
&J_2(2)^{\oplus2}\oplus J_1(-3)^{\oplus2}, &&J_2(2)^{\oplus2}\oplus J_1(2)\oplus J_1(-3), &&J_2(2)\oplus J_1(2)^{\oplus2}\oplus J_1(-3)^{\oplus2},\\
&J_2(2)\oplus J_1(2)\oplus J_1(-3)^{\oplus3}, &&J_2(2)\oplus J_1(2)^{\oplus3}\oplus J_1(-3), &&J_2(2)\oplus J_1(-3)^{\oplus4}.
\end{aligned}$$

::: pf-proof

Each invariant factor $\prod_\lambda(x-\lambda)^{e_\lambda}$ contributes the Jordan blocks $J_{e_\lambda}(\lambda)$ with $e_\lambda>0$.

:::

:::

::: pf-step

For $n=7$ and $q=(x^2+1)(x-7)$, the invariant-factor lists over $\QQ$ are
$$(x^2+1),\ (x^2+1),\ q;\qquad (x-7),\ (x-7),\ (x-7),\ (x-7),\ q;\qquad (x-7),\ q,\ q.$$

::: pf-proof

The monic divisors of $q$ in $\QQ[x]$ are $1$, $x-7$, $x^2+1$ and $q$.
The factors before $q$ form a divisibility chain with degrees summing to $4$: four copies of $x-7$, two copies of $x^2+1$, or $x-7$ followed by $q$.

:::

:::

::: pf-step

Over $\CC$, every such $A$ is diagonalizable with Jordan form $\operatorname{diag}(i^{(m_1)},(-i)^{(m_2)},7^{(m_3)})$, where $m_1,m_2,m_3\ge1$ and $m_1+m_2+m_3=7$; there are $\binom62=15$ of them.

::: pf-proof

Over $\CC$, $q=(x-i)(x+i)(x-7)$ has distinct roots, so every Jordan block has size $1$, and each root of $q$ is an eigenvalue.
The multiplicities form a composition of $7$ into three positive parts.

:::

:::

::: pf-step

Over $\CC$, the rational canonical forms for $n=7$ correspond to the same $15$ triples: with $k=\max(m_1,m_2,m_3)$, the invariant factors are
$$a_j=(x-i)^{[j>k-m_1]}(x+i)^{[j>k-m_2]}(x-7)^{[j>k-m_3]},\qquad 1\le j\le k,$$
where $[P]$ is $1$ if $P$ holds and $0$ otherwise.

::: pf-proof

The elementary divisors are $m_1$ copies of $x-i$, $m_2$ of $x+i$ and $m_3$ of $x-7$; the $j$th invariant factor is the product over the eigenvalues whose number of copies is at least $k-j+1$.

:::

:::

:::

:::
