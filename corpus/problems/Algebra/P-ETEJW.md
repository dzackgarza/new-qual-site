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

::: problem
Find all possible rational canonical forms for a matrix $A\in M_n(\Bbb Q)$ such that

1. $A$ is $6\times 6$ with minimal polynomial $q(x) = (x-2)^2(x+3)$.

2. $A$ is $7\times 7$ with $q(x) = (x^2+1)(x-7)$.

Also find all such forms when $A \in M_n(\Bbb C)$ instead, and find all possible Jordan Canonical Forms over $\Bbb C$.
:::

::: {.solution}
<1>1. Part 1: $n = 6$ with $q(x) = (x-2)^2(x+3)$:
<2>1. The invariant factors $a_1(x) \mid \dots \mid a_k(x) = q(x)$ must satisfy $\sum_{i=1}^k \deg(a_i) = 6$.
The divisors of $q(x)$ are:
- Degree 1: $(x-2), (x+3)$,
- Degree 2: $(x-2)^2, (x-2)(x+3)$,
- Degree 3: $(x-2)^2(x+3) = q(x)$.
Proof: factorization over $\mathbb{Q}$ and $\mathbb{C}$.
<2>2. The possible chains of invariant factors $a_1 \mid \dots \mid a_k$ summing to degree 6 are:
1. $q(x), q(x)$
2. $(x-2), (x-2)^2, q(x)$
3. $(x-2), (x-2)(x+3), q(x)$
4. $(x+3), (x-2)(x+3), q(x)$
5. $(x-2), (x-2), (x-2), q(x)$
6. $(x+3), (x+3), (x+3), q(x)$
Since all roots lie in $\mathbb{Q}$, these 6 lists are the possible invariant factors (and determine the Rational Canonical Form) over both $\mathbb{Q}$ and $\mathbb{C}$.
Proof: classification of divisibility chains of degrees summing to 6.
<2>3. **Jordan Canonical Forms over $\mathbb{C}$:**
The elementary divisors for the eigenvalues $\lambda = 2$ and $\lambda = -3$ correspond to Jordan blocks (where the largest block for $\lambda = 2$ is $J_2(2)$ and for $\lambda = -3$ is $J_1(-3)$):
1. $J_2(2) \oplus J_2(2) \oplus J_1(-3) \oplus J_1(-3)$
2. $J_2(2) \oplus J_2(2) \oplus J_1(2) \oplus J_1(-3)$
3. $J_2(2) \oplus J_1(2) \oplus J_1(2) \oplus J_1(-3) \oplus J_1(-3)$
4. $J_2(2) \oplus J_1(2) \oplus J_1(-3) \oplus J_1(-3) \oplus J_1(-3)$
5. $J_2(2) \oplus J_1(2) \oplus J_1(2) \oplus J_1(2) \oplus J_1(-3)$
6. $J_2(2) \oplus J_1(-3) \oplus J_1(-3) \oplus J_1(-3) \oplus J_1(-3)$
Proof: elementary divisor decomposition.

<1>2. Part 2: $n = 7$ with $q(x) = (x^2+1)(x-7)$:
<2>1. **Rational Canonical Forms over $\mathbb{Q}$:**
The irreducible factors of $q(x)$ over $\mathbb{Q}$ are $(x^2+1)$ (degree 2) and $(x-7)$ (degree 1).
The possible invariant factor chains $a_1 \mid \dots \mid a_k = q(x)$ in $\mathbb{Q}[x]$ summing to degree 7 are:
1. $(x^2+1), (x^2+1), (x^2+1)(x-7)$
2. $(x-7), (x-7), (x-7), (x-7), (x^2+1)(x-7)$
3. $(x-7), (x^2+1)(x-7), (x^2+1)(x-7)$
Proof: partitions of remaining degree 4 by degrees of rational divisors of $q(x)$.
<2>2. **Jordan Canonical Forms over $\mathbb{C}$:**
Over $\mathbb{C}$, $q(x) = (x - i)(x + i)(x - 7)$ has square-free distinct linear factors.
Thus all matrices with minimal polynomial $q(x)$ are **diagonalizable**, so every Jordan block has size 1.
The eigenvalues are $i, -i, 7$, with multiplicities $m_1, m_2, m_3 \ge 1$ such that:
\[
m_1 + m_2 + m_3 = 7.
\]
There are $\binom{7-1}{3-1} = \binom{6}{2} = 15$ such integer triples $(m_1, m_2, m_3)$, each giving a distinct JCF:
\[
J = \operatorname{diag}(\underbrace{i, \dots, i}_{m_1}, \underbrace{-i, \dots, -i}_{m_2}, \underbrace{7, \dots, 7}_{m_3}).
\]
Proof: number of compositions of 7 into 3 positive parts.
<2>3. **Rational Canonical Forms over $\mathbb{C}$:**
Each of the 15 combinations of multiplicities above yields a unique list of invariant factors in $\mathbb{C}[x]$:
For multiplicities $m_1, m_2, m_3 \ge 1$, let $k = \max(m_1, m_2, m_3)$. The $j$-th invariant factor ($1 \le j \le k$) is:
\[
a_j(x) = (x-i)^{\mathbf{1}_{k - m_1 < j}} (x+i)^{\mathbf{1}_{k - m_2 < j}} (x-7)^{\mathbf{1}_{k - m_3 < j}}.
\]
Proof: invariant factors from elementary divisors over $\mathbb{C}$.

<1>3. Conclusion:
The RCFs and JCFs are completely determined by the invariant factor and elementary divisor classifications above. Q.E.D.
Proof: <1>1 and <1>2.
:::
