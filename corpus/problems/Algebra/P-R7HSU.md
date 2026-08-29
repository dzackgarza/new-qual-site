---
schema: qual/card@1
id: P-R7HSU
kind: problem
title: The cokernel of $A\in M_n(\mathbb{Z})$ is finite iff $\det A\neq 0$, with order
  $|\det A|$
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Determinants
  - Modules
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $A \in M_n(\mathbb{Z})$ be an $n \times n$ matrix with integer entries, viewed as a $\mathbb{Z}$-module homomorphism $A: \mathbb{Z}^n \to \mathbb{Z}^n$.
(1) Prove that the cokernel $\operatorname{coker}(A) = \mathbb{Z}^n / \operatorname{im}(A)$ is **finite** if and only if $\det(A) \ne 0$.
(2) Prove that when $\det(A) \ne 0$, the order of the cokernel is given by:
$$|\operatorname{coker}(A)| = |\det(A)|.$$
:::

::: solution
**Goal:** Prove finiteness and compute the cardinality of the cokernel of an integer matrix using the Smith Normal Form over the PID $\mathbb{Z}$.

<1>1. Smith Normal Form Decomposition:
    *Proof:*
    <2>1. Since $\mathbb{Z}$ is a Principal Ideal Domain, for any $A \in M_n(\mathbb{Z})$ there exist unimodular (invertible) integer matrices $P, Q \in \operatorname{GL}_n(\mathbb{Z})$ such that:
        $$P A Q = D = \operatorname{diag}(d_1, d_2, \dots, d_n)$$
        where $d_i \in \mathbb{Z}_{\ge 0}$ and $d_1 \mid d_2 \mid \cdots \mid d_n$ are the invariant factors of $A$.
    <2>2. Since $P, Q \in \operatorname{GL}_n(\mathbb{Z})$, their determinants are units in $\mathbb{Z}$:
        $$\det(P) = \pm 1, \qquad \det(Q) = \pm 1.$$
    <2>3. Taking determinants of $P A Q = D$:
        $$\det(D) = \det(P) \det(A) \det(Q) = \pm \det(A) \implies |\det(A)| = |\det(D)| = \prod_{i=1}^n d_i.$$

<1>2. Isomorphism on the Cokernel:
    *Proof:*
    <2>1. The matrix $P: \mathbb{Z}^n \to \mathbb{Z}^n$ is an automorphism of $\mathbb{Z}^n$ that maps $\operatorname{im}(A) = A(\mathbb{Z}^n)$ onto $\operatorname{im}(A Q) = P A Q(\mathbb{Z}^n) = D(\mathbb{Z}^n) = \operatorname{im}(D)$.
    <2>2. Thus $P$ induces an isomorphism of quotient abelian groups ($\mathbb{Z}$-modules):
        $$\operatorname{coker}(A) = \mathbb{Z}^n / \operatorname{im}(A) \cong \mathbb{Z}^n / \operatorname{im}(D) = \mathbb{Z}^n / D(\mathbb{Z}^n).$$
    <2>3. Since $D = \operatorname{diag}(d_1, \dots, d_n)$, the image $D(\mathbb{Z}^n) = d_1 \mathbb{Z} \oplus d_2 \mathbb{Z} \oplus \cdots \oplus d_n \mathbb{Z}$.
    <2>4. Therefore:
        $$\operatorname{coker}(A) \cong \bigoplus_{i=1}^n \mathbb{Z} / d_i \mathbb{Z} = (\mathbb{Z} / d_1 \mathbb{Z}) \times (\mathbb{Z} / d_2 \mathbb{Z}) \times \cdots \times (\mathbb{Z} / d_n \mathbb{Z}).$$

<1>3. Characterization of Finiteness:
    *Proof:*
    <2>1. A direct product of cyclic groups $\bigoplus_{i=1}^n \mathbb{Z}/d_i\mathbb{Z}$ is **finite** if and only if each factor $\mathbb{Z}/d_i\mathbb{Z}$ is finite.
    <2>2. The cyclic group $\mathbb{Z}/d_i\mathbb{Z}$ is finite if and only if $d_i \ge 1$ (i.e. $d_i \ne 0$).
    <2>3. All $d_i \ne 0 \iff \prod_{i=1}^n d_i \ne 0 \iff |\det(D)| \ne 0 \iff \det(A) \ne 0$.
    <2>4. Thus $\operatorname{coker}(A)$ is finite if and only if $\det(A) \ne 0$.

<1>4. Computation of Order $|\operatorname{coker}(A)|$:
    *Proof:*
    <2>1. When $\det(A) \ne 0$, all $d_i > 0$.
    <2>2. The order of each cyclic group $|\mathbb{Z}/d_i\mathbb{Z}| = d_i$.
    <2>3. By the product rule for direct products:
        $$|\operatorname{coker}(A)| = \prod_{i=1}^n |\mathbb{Z}/d_i\mathbb{Z}| = \prod_{i=1}^n d_i = |\det(D)| = |\det(A)|.$$

<1>5. Conclusion:
    $\operatorname{coker}(A) \cong \bigoplus \mathbb{Z}/d_i\mathbb{Z}$ is finite $\iff \det(A) \ne 0$, in which case $|\operatorname{coker}(A)| = \prod d_i = |\det(A)|$. Q.E.D.
:::
