---
schema: qual/card@1
id: E-AMD-RRYNGX7L
kind: exercise
title: The cokernel of $A\in M_n(\ZZ)$ is finite of order $|\det A|$ iff $\det A\neq
  0$
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

::: {.exercise}
Prove that the cokernel of an integer matrix $A \in M_n(\mathbb{Z})$ (viewed as a linear map $A: \mathbb{Z}^n \to \mathbb{Z}^n$) is finite if and only if $\det(A) \ne 0$.
Furthermore, show that in this case:
$$|\operatorname{coker}(A)| = |\det(A)|.$$
:::

::: solution
**Goal:** Prove that $\operatorname{coker}(A) = \mathbb{Z}^n / A(\mathbb{Z}^n)$ has order $|\det(A)|$ when $\det(A) \ne 0$, and is infinite otherwise, via Smith Normal Form.

<1>1. Smith Normal Form of Integer Matrices:
    *Proof:*
    <2>1. By the **Smith Normal Form Theorem** over the PID $\mathbb{Z}$, there exist unimodular matrices $P, Q \in \operatorname{GL}_n(\mathbb{Z})$ (so $\det(P) = \pm 1$ and $\det(Q) = \pm 1$) such that:
        $$D = P A Q = \operatorname{diag}(d_1, d_2, \dots, d_r, 0, \dots, 0)$$
        where $d_1 \mid d_2 \mid \cdots \mid d_r$ are positive invariant factors in $\mathbb{Z}_{\ge 1}$, and $r = \operatorname{rank}(A) \le n$.
    <2>2. Since $A = P^{-1} D Q^{-1}$, taking determinants gives:
        $$\det(A) = \det(P^{-1}) \det(D) \det(Q^{-1}) = (\pm 1) \det(D) (\pm 1) = \pm \det(D).$$

<1>2. Isomorphism of Cokernels:
    *Proof:*
    <2>1. The cokernel is the quotient module:
        $$\operatorname{coker}(A) = \mathbb{Z}^n / A(\mathbb{Z}^n) = \mathbb{Z}^n / \operatorname{im}(A).$$
    <2>2. Since $P, Q \in \operatorname{GL}_n(\mathbb{Z})$ are automorphisms of $\mathbb{Z}^n$, change of basis preserves the quotient module structure:
        $$\operatorname{coker}(A) = \mathbb{Z}^n / A(\mathbb{Z}^n) \cong \mathbb{Z}^n / D(\mathbb{Z}^n) = \operatorname{coker}(D).$$
    <2>3. The image of the diagonal map $D$ is:
        $$D(\mathbb{Z}^n) = d_1 \mathbb{Z} \oplus d_2 \mathbb{Z} \oplus \cdots \oplus d_r \mathbb{Z} \oplus 0 \oplus \cdots \oplus 0.$$
    <2>4. Therefore:
        $$\operatorname{coker}(D) \cong (\mathbb{Z}/d_1\mathbb{Z}) \oplus (\mathbb{Z}/d_2\mathbb{Z}) \oplus \cdots \oplus (\mathbb{Z}/d_r\mathbb{Z}) \oplus \mathbb{Z}^{n-r}.$$

<1>3. Case 1: $\det(A) = 0$:
    *Proof:*
    <2>1. If $\det(A) = 0$, then $\det(D) = 0$, so $r = \operatorname{rank}(A) < n$.
    <2>2. Thus $\operatorname{coker}(D)$ contains a free summand $\mathbb{Z}^{n-r}$ with $n - r \ge 1$.
    <2>3. Consequently, $\operatorname{coker}(A)$ is **infinite** ($|\operatorname{coker}(A)| = \infty$).

<1>4. Case 2: $\det(A) \ne 0$:
    *Proof:*
    <2>1. If $\det(A) \ne 0$, then $r = n$, so $D = \operatorname{diag}(d_1, d_2, \dots, d_n)$ has full rank with all $d_i > 0$.
    <2>2. The free summand vanishes ($n - r = 0$), so:
        $$\operatorname{coker}(A) \cong \bigoplus_{i=1}^n (\mathbb{Z}/d_i\mathbb{Z}).$$
    <2>3. This is a finite abelian group of order:
        $$|\operatorname{coker}(A)| = \prod_{i=1}^n d_i.$$
    <2>4. On the other hand, the determinant of $D$ is $\det(D) = \prod_{i=1}^n d_i$.
    <2>5. From Step <1>1, $|\det(A)| = |\det(D)| = \prod_{i=1}^n d_i$.
    <2>6. Therefore:
        $$|\operatorname{coker}(A)| = |\det(A)|.$$

<1>5. Conclusion:
    $\operatorname{coker}(A)$ is finite $\iff \det(A) \ne 0$, and in that case $|\operatorname{coker}(A)| = |\det(A)|$. Q.E.D.
:::
