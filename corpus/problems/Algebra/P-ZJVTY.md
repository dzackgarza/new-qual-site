---
schema: qual/card@1
id: P-ZJVTY
kind: problem
title: $R^n/\im A$ is torsion iff $\operatorname{rank} A=n$ iff the Smith form of
  $A$ has $n$ nonzero invariant factors
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Smith Normal Form
  - Torsion
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $R$ be a Principal Ideal Domain (PID) and let $A \in M_n(R)$ be an $n \times n$ matrix representing an $R$-module homomorphism $A: R^n \to R^n$.
Let $M = R^n / \operatorname{im}(A)$ be the cokernel module.
Prove that the following three conditions are equivalent:
(1) $M = R^n / \operatorname{im}(A)$ is a **torsion module** (every element of $M$ is annihilated by some non-zero $r \in R$).
(2) The matrix rank of $A$ is $\operatorname{rank}_R(A) = n$ (equivalently, $\det(A) \ne 0$).
(3) The Smith Normal Form of $A$ has exactly $n$ non-zero invariant factors $d_1, d_2, \dots, d_n \ne 0$.
:::

::: solution
**Goal:** Prove the equivalence of torsion cokernel, full matrix rank, and non-vanishing invariant factors over a PID using the Smith Normal Form and the Structure Theorem for finitely generated modules.

<1>1. Smith Normal Form and Decomposition of $M$:
    *Proof:*
    <2>1. Since $R$ is a PID, every matrix $A \in M_n(R)$ can be diagonalized via invertible elementary row and column operations (matrices $P, Q \in \operatorname{GL}_n(R)$):
        $$P A Q = D = \operatorname{diag}(d_1, d_2, \dots, d_n)$$
        where $d_1 \mid d_2 \mid \cdots \mid d_n \in R$ are the **invariant factors** of $A$.
    <2>2. The invertible changes of basis $P, Q$ induce an isomorphism of $R$-modules on the cokernel:
        $$M = R^n / \operatorname{im}(A) \cong R^n / \operatorname{im}(D) \cong \bigoplus_{i=1}^n R / (d_i).$$

<1>2. Equivalence of (1) and (3) ($M$ is Torsion $\iff$ All $d_i \ne 0$):
    *Proof:*
    <2>1. A direct sum of modules $\bigoplus_{i=1}^n R/(d_i)$ is torsion if and only if each component $R/(d_i)$ is a torsion $R$-module.
    <2>2. For any $d \in R$:
        - If $d \ne 0$: for any $x + (d) \in R/(d)$, we have $d \cdot (x + (d)) = 0 + (d)$, so every element is annihilated by the non-zero element $d \in R \setminus \{0\}$. Thus $R/(d)$ is torsion.
        - If $d = 0$: $R/(0) \cong R$. Since $R$ is an integral domain, $R$ is a free $R$-module of rank 1, which contains non-zero non-torsion elements (e.g. $1 \in R$ has $\operatorname{Ann}(1) = (0)$).
    <2>3. Therefore, $M \cong \bigoplus_{i=1}^n R/(d_i)$ is a torsion module if and only if $d_i \ne 0$ for all $i = 1, \dots, n$.
    <2>4. Since the divisibility chain is $d_1 \mid d_2 \mid \cdots \mid d_n$, all $d_i \ne 0 \iff d_1 \ne 0 \iff$ all $n$ invariant factors are non-zero.

<1>3. Equivalence of (2) and (3) (Full Rank $\iff$ All $d_i \ne 0$):
    *Proof:*
    <2>1. Let $K = \operatorname{Frac}(R)$ be the field of fractions of the PID $R$.
    <2>2. The rank of $A$ over $R$ is the dimension of the column space of $A$ over $K$: $\operatorname{rank}_R(A) = \operatorname{rank}_K(A)$.
    <2>3. Since $P, Q \in \operatorname{GL}_n(R) \subset \operatorname{GL}_n(K)$ are invertible over $K$:
        $$\operatorname{rank}_R(A) = \operatorname{rank}_K(D) = \operatorname{rank}_K(\operatorname{diag}(d_1, \dots, d_n)).$$
    <2>4. The rank of a diagonal matrix over a field is the number of its non-zero diagonal entries.
    <2>5. Thus $\operatorname{rank}_R(A) = n \iff d_i \ne 0$ for all $i = 1, \dots, n$.
    <2>6. Equivalently, $\det(A) = \det(P^{-1}) \left(\prod_{i=1}^n d_i\right) \det(Q^{-1}) \ne 0 \iff \prod_{i=1}^n d_i \ne 0 \iff d_i \ne 0$ for all $i$.

<1>4. Conclusion:
    $M = R^n / \operatorname{im}(A)$ is torsion $\iff \operatorname{rank}_R(A) = n \iff d_1, \dots, d_n \ne 0$ in the Smith Normal Form. Q.E.D.
:::
