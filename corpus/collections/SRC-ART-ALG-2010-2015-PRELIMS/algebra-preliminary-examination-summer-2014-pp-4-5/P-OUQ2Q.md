---
schema: qual/card@1
id: P-OUQ2Q
kind: problem
title: $\mathbb{Q}[x]$-modules from order-$6$ matrices in $M_4(\mathbb{Q})$, and groups
  of order $24$
classification:
  areas:
  - prelim
  topics:
  - Rational Canonical Form
  - Modules
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Suppose $A \in M_4(\mathbb{Q})$ is a 4-by-4 matrix of multiplicative order 6. We use $A$ to give $\mathbb{Q}^4$ the structure of a $\mathbb{Q}[x]$-module in the usual way, by setting $x \cdot v = Av$ for $v \in \mathbb{Q}^4$.

a. What are all of the isomorphism classes of $\mathbb{Q}[x]$-modules that can arise this way?

b. For each of your answers above, write down the rational canonical form of the corresponding matrix $A$.

c. What are all the of the abelian groups of size 24 (up to isomorphism)?
:::

::: {.solution}
<1>1. Constraints on minimal and characteristic polynomials of $A$:
<2>1. The condition $A^6 = I$ implies that the minimal polynomial $m_A(x)$ divides $x^6 - 1 \in \mathbb{Q}[x]$.
The factorization of $x^6 - 1$ into irreducible polynomials over $\mathbb{Q}$ is:
\[
x^6 - 1 = (x - 1)(x + 1)(x^2 + x + 1)(x^2 - x + 1) = \Phi_1(x) \Phi_2(x) \Phi_3(x) \Phi_6(x).
\]
Because $x^6 - 1$ is square-free, $m_A(x)$ is square-free.
The multiplicative order of $A$ is $6$ if and only if the least common multiple of the orders of the roots of $m_A(x)$ is $6$.
This requires that either $\Phi_6(x) = x^2 - x + 1 \mid m_A(x)$, or both $\Phi_2(x) = x + 1$ and $\Phi_3(x) = x^2 + x + 1$ divide $m_A(x)$.

<1>2. Parts (a) and (b): Isomorphism classes and Rational Canonical Forms:
<2>1. The invariant factors $d_1(x) \mid \cdots \mid d_k(x)$ of the $\mathbb{Q}[x]$-module $\mathbb{Q}^4$ are monic polynomials with $\sum \deg(d_i) = 4$ and $d_k(x) = m_A(x)$.
The companion matrix of a monic polynomial $p(x) = x^n + c_{n-1}x^{n-1} + \dots + c_0$ is denoted $C(p)$.

<2>2. **Class 1:** Invariant factors $d_1(x) = x^2 - x + 1$, $d_2(x) = x^2 - x + 1$.
- Module: $\mathbb{Q}[x]/\langle x^2 - x + 1 \rangle \oplus \mathbb{Q}[x]/\langle x^2 - x + 1 \rangle$.
- RCF: $\begin{pmatrix} 0 & -1 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 0 & 0 & 0 & -1 \\ 0 & 0 & 1 & 1 \end{pmatrix}$.

<2>3. **Class 2:** Invariant factors $d_1(x) = x - 1$, $d_2(x) = (x - 1)(x^2 - x + 1) = x^3 - 2x^2 + 2x - 1$.
- Module: $\mathbb{Q}[x]/\langle x - 1 \rangle \oplus \mathbb{Q}[x]/\langle x^3 - 2x^2 + 2x - 1 \rangle$.
- RCF: $\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 1 & 0 & -2 \\ 0 & 0 & 1 & 2 \end{pmatrix}$.

<2>4. **Class 3:** Invariant factors $d_1(x) = x + 1$, $d_2(x) = (x + 1)(x^2 - x + 1) = x^3 + 1$.
- Module: $\mathbb{Q}[x]/\langle x + 1 \rangle \oplus \mathbb{Q}[x]/\langle x^3 + 1 \rangle$.
- RCF: $\begin{pmatrix} -1 & 0 & 0 & 0 \\ 0 & 0 & 0 & -1 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{pmatrix}$.

<2>5. **Class 4:** Single invariant factor $d_1(x) = (x^2 - 1)(x^2 - x + 1) = x^4 - x^3 + x - 1$.
- Module: $\mathbb{Q}[x]/\langle x^4 - x^3 + x - 1 \rangle$.
- RCF: $\begin{pmatrix} 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & -1 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 1 \end{pmatrix}$.

<2>6. **Class 5:** Single invariant factor $d_1(x) = (x + 1)(x^3 - 1) = x^4 + x^3 - x - 1$.
- Module: $\mathbb{Q}[x]/\langle x^4 + x^3 - x - 1 \rangle$.
- RCF: $\begin{pmatrix} 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & -1 \end{pmatrix}$.

<2>7. **Class 6:** Single invariant factor $d_1(x) = (x^2 + x + 1)(x^2 - x + 1) = x^4 + x^2 + 1$.
- Module: $\mathbb{Q}[x]/\langle x^4 + x^2 + 1 \rangle$.
- RCF: $\begin{pmatrix} 0 & 0 & 0 & -1 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & -1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$.

<1>3. Part (c): Classification of abelian groups of order 24:
<2>1. Since $24 = 2^3 \cdot 3$, by the Fundamental Theorem of Finite Abelian Groups, any abelian group of order 24 is the direct product of its Sylow 2-subgroup and Sylow 3-subgroup:
\[
G \cong P_2 \times P_3.
\]
<2>2. The Sylow 3-subgroup has order 3, so $P_3 \cong \mathbb{Z}/3\mathbb{Z}$.
The Sylow 2-subgroup has order $2^3 = 8$, corresponding to the partitions of 3:
- Partition $3$: $P_2 \cong \mathbb{Z}/8\mathbb{Z}$,
- Partition $2 + 1$: $P_2 \cong \mathbb{Z}/4\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$,
- Partition $1 + 1 + 1$: $P_2 \cong \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$.
<2>3. Combining with $P_3 \cong \mathbb{Z}/3\mathbb{Z}$ gives exactly three non-isomorphic abelian groups of order 24:
1. $\mathbb{Z}/8\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z} \cong \mathbb{Z}/24\mathbb{Z}$,
2. $\mathbb{Z}/4\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/3\mathbb{Z} \cong \mathbb{Z}/12\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$,
3. $(\mathbb{Z}/2\mathbb{Z})^3 \times \mathbb{Z}/3\mathbb{Z} \cong \mathbb{Z}/6\mathbb{Z} \times (\mathbb{Z}/2\mathbb{Z})^2$.

<1>4. Conclusion:
There are 6 isomorphism classes of $\mathbb{Q}[x]$-modules with their corresponding RCF matrices, and 3 abelian groups of size 24. Q.E.D.
:::
