---
schema: qual/card@1
id: P-3ECUR
kind: problem
title: Hungerford 7.4.10
classification:
  areas:
  - algebra
  topics:
  - Rational Canonical Form
  - Jordan Canonical Form
  - Minimal and Characteristic Polynomials
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
<1>1. General theory of Rational and Jordan Canonical Forms:
<2>1. A matrix $A \in M_n(F)$ is determined up to similarity over $F$ by its invariant factors $f_1(x) \mid f_2(x) \mid \dots \mid f_k(x)$ in $F[x]$, where $f_k(x) = q(x)$ is the minimal polynomial and $\sum_{j=1}^k \deg(f_j) = n$.
Proof: structure theorem for finitely generated torsion modules over the PID $F[x]$.
<2>2. The Rational Canonical Form (RCF) is the block diagonal matrix $\bigoplus_{j=1}^k C(f_j)$, where $C(f)$ is the companion matrix of the monic polynomial $f$.
Proof: definition of rational canonical form.
<2>3. Over $\mathbb{C}$, the Jordan Canonical Form (JCF) is the direct sum of Jordan blocks corresponding to the elementary divisors of $A$ (the prime power factors of the invariant factors).
Proof: Jordan decomposition theorem over algebraically closed fields.

<1>2. **Part 1: $n = 6$, $q(x) = (x-2)^2(x+3)$ ($\deg q = 3$).**
<2>1. The monic divisors of $q(x)$ in $\mathbb{Q}[x]$ (and $\mathbb{C}[x]$) are:
\[
1, \; (x-2), \; (x+3), \; (x-2)^2, \; (x-2)(x+3), \; (x-2)^2(x+3).
\]
Proof: unique factorization in $\mathbb{Q}[x]$.
<2>2. The possible sequences of invariant factors $f_1 \mid \dots \mid f_k = q(x)$ summing to degree 6 over $\mathbb{Q}$ and $\mathbb{C}$ are:
1. $((x-2)^2(x+3), (x-2)^2(x+3))$
2. $(x-2, (x-2)^2, (x-2)^2(x+3))$
3. $(x-2, (x-2)(x+3), (x-2)^2(x+3))$
4. $(x+3, (x-2)(x+3), (x-2)^2(x+3))$
5. $(x-2, x-2, x-2, (x-2)^2(x+3))$
6. $(x+3, x+3, x+3, (x-2)^2(x+3))$
Proof: all partitions of degree 3 into degrees of divisors of $q(x)$ satisfying divisibility $f_j \mid f_{j+1}$.
<2>3. Since all roots of $q(x)$ lie in $\mathbb{Q}$, the invariant factors over $\mathbb{C}$ are identical to those over $\mathbb{Q}$, so the RCFs over $\mathbb{C}$ are the same 6 forms.
Proof: invariant factors are invariant under field extensions.
<2>4. The corresponding Jordan Canonical Forms over $\mathbb{C}$ are:
1. $J_2(2) \oplus J_2(2) \oplus J_1(-3) \oplus J_1(-3)$
2. $J_1(2) \oplus J_2(2) \oplus J_2(2) \oplus J_1(-3)$
3. $J_1(2) \oplus J_1(2) \oplus J_2(2) \oplus J_1(-3) \oplus J_1(-3)$
4. $J_1(2) \oplus J_2(2) \oplus J_1(-3) \oplus J_1(-3) \oplus J_1(-3)$
5. $J_1(2) \oplus J_1(2) \oplus J_1(2) \oplus J_2(2) \oplus J_1(-3)$
6. $J_2(2) \oplus J_1(-3) \oplus J_1(-3) \oplus J_1(-3) \oplus J_1(-3)$
Proof: elementary divisors $(x-2)^a$ and $(x+3)^b$ determined from each invariant factor list.

<1>3. **Part 2: $n = 7$, $q(x) = (x^2+1)(x-7)$ ($\deg q = 3$).**
<2>1. In $\mathbb{Q}[x]$, $x^2+1$ is irreducible, so the monic divisors of $q(x)$ are $1, \; x-7, \; x^2+1, \; (x^2+1)(x-7)$.
Proof: $x^2+1$ has no roots in $\mathbb{Q}$.
<2>2. Over $\mathbb{Q}$, divisibility $f_j \mid f_{j+1}$ requires that any invariant factor preceding $x^2+1$ cannot be $x-7$ (since $x-7 \nmid x^2+1$). Thus the sequences of invariant factors over $\mathbb{Q}$ with degree sum 7 are:
1. $(x^2+1, \; x^2+1, \; (x^2+1)(x-7))$
2. $(x-7, \; x-7, \; x-7, \; x-7, \; (x^2+1)(x-7))$
3. $(x-7, \; (x^2+1)(x-7), \; (x^2+1)(x-7))$
Proof: exhaustive search of divisibility chains with degrees summing to 7.
<2>3. Over $\mathbb{C}$, $q(x) = (x-i)(x+i)(x-7)$ is square-free, so every such matrix $A \in M_7(\mathbb{C})$ is diagonalizable.
Proof: minimal polynomial splits into distinct linear factors over $\mathbb{C}$.
<2>4. The Jordan Canonical Form over $\mathbb{C}$ is diagonal:
\[
J = \operatorname{diag}(\underbrace{i, \dots, i}_{m_1}, \; \underbrace{-i, \dots, -i}_{m_2}, \; \underbrace{7, \dots, 7}_{m_3}),
\]
where $m_1, m_2, m_3 \ge 1$ are integers satisfying $m_1 + m_2 + m_3 = 7$.
Proof: each eigenvalue of $q(x)$ must appear at least once, with total algebraic multiplicity $n = 7$.
<2>5. There are $\binom{7-1}{3-1} = \binom{6}{2} = 15$ such Jordan Canonical Forms over $\mathbb{C}$.
Proof: number of compositions of 7 into 3 positive integers.
<2>6. Over $\mathbb{C}$, the invariant factors $f_1 \mid \dots \mid f_k = q(x)$ correspond to these 15 combinations of multiplicities: for $j \le \max(m_1, m_2, m_3)$, the $j$-th invariant factor from the right is the product of $(x-\lambda)$ over all eigenvalues $\lambda \in \{i, -i, 7\}$ having multiplicity $\ge j$.
Proof: construction of invariant factors from elementary divisors.

<1>4. Q.E.D.
Proof: <1>2 and <1>3.
:::
