---
schema: qual/card@1
id: P-3ECUR
kind: problem
title: Rational and Jordan canonical forms with minimal polynomial $(x-2)^2(x+3)$ or $(x^2+1)(x-7)$
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
By the structure theorem for finitely generated torsion modules over the PID $F[x]$, a matrix $A\in M_n(F)$ is determined up to similarity by its invariant factors, monic polynomials $f_1 \mid f_2 \mid \cdots \mid f_k$ of positive degree with $f_k = q$ the minimal polynomial and $\sum_j \deg f_j = n$. The rational canonical form is $\bigoplus_{j=1}^k C(f_j)$, where $C(f)$ is the companion matrix of $f$. Over $\CC$, the Jordan form is the direct sum of the Jordan blocks $J_a(\lambda)$, one for each elementary divisor $(x-\lambda)^a$, and the elementary divisors are the prime-power factors of the invariant factors. We list each rational canonical form by its invariant factors.

::: pf

::: {.pf-step #s1}

(1) Over $\QQ$, the possible invariant factor lists for $n=6$, $q=(x-2)^2(x+3)$ are exactly:

1. $(x-2)^2(x+3),\ (x-2)^2(x+3)$;
2. $x-2,\ (x-2)^2,\ (x-2)^2(x+3)$;
3. $x-2,\ (x-2)(x+3),\ (x-2)^2(x+3)$;
4. $x+3,\ (x-2)(x+3),\ (x-2)^2(x+3)$;
5. $x-2,\ x-2,\ x-2,\ (x-2)^2(x+3)$;
6. $x+3,\ x+3,\ x+3,\ (x-2)^2(x+3)$.

::: pf-proof

The factors $f_1\mid\cdots\mid f_{k-1}$ are monic divisors of $q$ of positive degree with degrees summing to $6-3=3$. The monic divisors of $q$ of positive degree are $x-2$, $x+3$, $(x-2)^2$, $(x-2)(x+3)$, and $q$. A single factor of degree $3$ is $q$, giving list 1. A factor of degree $2$ preceded by one of degree $1$ that divides it gives lists 2, 3, and 4, since $x+3\nmid(x-2)^2$. Three factors of degree $1$ in a divisibility chain are equal, giving lists 5 and 6.

:::

:::

::: pf-step

(1) Over $\CC$, the rational canonical forms are the same six, with Jordan forms respectively
$$\begin{aligned}
&1.\ J_2(2) \oplus J_2(2) \oplus J_1(-3) \oplus J_1(-3),\\
&2.\ J_1(2) \oplus J_2(2) \oplus J_2(2) \oplus J_1(-3),\\
&3.\ J_1(2) \oplus J_1(2) \oplus J_2(2) \oplus J_1(-3) \oplus J_1(-3),\\
&4.\ J_1(2) \oplus J_2(2) \oplus J_1(-3) \oplus J_1(-3) \oplus J_1(-3),\\
&5.\ J_1(2) \oplus J_1(2) \oplus J_1(2) \oplus J_2(2) \oplus J_1(-3),\\
&6.\ J_2(2) \oplus J_1(-3) \oplus J_1(-3) \oplus J_1(-3) \oplus J_1(-3).
\end{aligned}$$

::: pf-proof

The monic divisors of $q$ in $\CC[x]$ are the same as in $\QQ[x]$ because $q$ splits over $\QQ$, so the argument of step [](#s1){.pf-ref} gives the same six lists. Factoring each invariant factor into powers of $x-2$ and $x+3$ gives the displayed Jordan forms.

:::

:::

::: pf-step

(2) Over $\QQ$, the possible invariant factor lists for $n=7$, $q=(x^2+1)(x-7)$ are exactly:

1. $x^2+1,\ x^2+1,\ (x^2+1)(x-7)$;
2. $x-7,\ x-7,\ x-7,\ x-7,\ (x^2+1)(x-7)$;
3. $x-7,\ (x^2+1)(x-7),\ (x^2+1)(x-7)$.

::: pf-proof

Since $x^2+1$ has no rational root, it is irreducible over $\QQ$, and the monic divisors of $q$ of positive degree are $x-7$, $x^2+1$, and $q$. The factors $f_1\mid\cdots\mid f_{k-1}$ have degrees summing to $4$. Because $x-7\nmid x^2+1$, a chain containing $x^2+1$ below $q$ consists of copies of $x^2+1$, giving list 1; a chain containing $q$ below $q$ has one further factor of degree $1$, giving list 3; the remaining chain is four copies of $x-7$, list 2.

:::

:::

::: pf-step

(2) Over $\CC$, the possible Jordan forms are
$$\operatorname{diag}(\underbrace{i, \ldots, i}_{m_1}, \underbrace{-i, \ldots, -i}_{m_2}, \underbrace{7, \ldots, 7}_{m_3})$$
with $m_1, m_2, m_3 \ge 1$ and $m_1 + m_2 + m_3 = 7$; there are $\binom{6}{2} = 15$ of them. For the rational canonical form with multiplicities $m_1,m_2,m_3$, the $j$th invariant factor counted from the last is $\prod_{\lambda\in\{i,-i,7\},\ m_\lambda\ge j}(x-\lambda)$, for $1\le j\le\max(m_1,m_2,m_3)$.

::: pf-proof

Over $\CC$, $q = (x-i)(x+i)(x-7)$ has distinct roots, so $A$ is diagonalizable with eigenvalues among $i,-i,7$, and each root of the minimal polynomial is an eigenvalue. The number of compositions of $7$ into three positive parts is $\binom62=15$. The elementary divisors are $m_\lambda$ copies of $x-\lambda$ for each $\lambda$; the last invariant factor is the product of one copy of each, and removing it and repeating gives the stated formula.

:::

:::

:::

:::
