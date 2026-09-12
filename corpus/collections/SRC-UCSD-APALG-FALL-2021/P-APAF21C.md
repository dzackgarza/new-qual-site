---
schema: qual/card@1
id: P-APAF21C
kind: problem
title: Square root and modulus; singular values; PSD characterization; similarity of $|A|$ and $|A^H|$
classification:
  areas:
  - applied-algebra
  topics:
  - Singular Values
  - Positive Definite Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
  note: Completed the rectangular zero-block similarity statement in part (e).
---

::: problem
(a) Define $A^{1/2}$ for a positive semidefinite matrix $A \in M_n(\mathbb{C})$.
(b) Define $|A|$ for any matrix $A \in M_{m,n}(\mathbb{C})$.
(c) Prove that the eigenvalues of $|A|$ are the singular values of $A$.
(d) Prove that a square matrix $A \in M_n(\mathbb{C})$ is positive semidefinite if and only if $|A| = A$.
(e) Prove that $|A|$ and $|A^H|$ have the same non-zero eigenvalues and are similar up to embedding/direct sum with zero blocks.
:::

::: {.solution}
<1>1. If $A\in M_n(\mathbb C)$ is positive semidefinite, define its positive semidefinite square root by spectral calculus.
::: {.proof}
By the Hermitian spectral theorem,
\[
A=U\operatorname{diag}(\lambda_1,\ldots,\lambda_n)U^H,
\qquad \lambda_i\ge0,
\]
for a unitary $U$. Define
\[
A^{1/2}=U\operatorname{diag}(\sqrt{\lambda_1},\ldots,\sqrt{\lambda_n})U^H.
\]
Then $A^{1/2}$ is positive semidefinite and $(A^{1/2})^2=A$. Uniqueness follows because any positive semidefinite square root is diagonalized in the same eigenspaces and must have eigenvalues $\sqrt{\lambda_i}$.
:::

<1>2. For $A\in M_{m,n}(\mathbb C)$, define
\[
|A|=(A^HA)^{1/2}\in M_n(\mathbb C).
\]
::: {.proof}
The matrix $A^HA$ is Hermitian positive semidefinite because
\[
x^HA^HAx=\|Ax\|^2\ge0.
\]
Hence <1>1 applies.
:::

<1>3. The eigenvalues of $|A|$ are exactly the singular values of $A$, with multiplicity.
::: {.proof}
If the eigenvalues of $A^HA$ are $\mu_1,\ldots,\mu_n\ge0$, then by definition the singular values are $\sqrt{\mu_i}$. Spectral calculus in <1>1 shows that these are precisely the eigenvalues of $(A^HA)^{1/2}=|A|$.
:::

<1>4. For square $A$, one has
\[
A\ge0\iff |A|=A.
\]
::: {.proof}
If $A\ge0$, then $A=A^H$ and $A^HA=A^2$. Since $A$ itself is the positive semidefinite square root of $A^2$, uniqueness gives
\[
|A|=(A^2)^{1/2}=A.
\]
Conversely, $|A|$ is positive semidefinite by definition, so if $A=|A|$, then $A\ge0$.
:::

<1>5. Let $r=\operatorname{rank}A$ and let
\[
A=U\Sigma V^H
\]
be an SVD, with positive singular values $\sigma_1,\ldots,\sigma_r$. Then
\[
|A|=V\operatorname{diag}(\sigma_1,\ldots,\sigma_r,0_{n-r})V^H
\]
and
\[
|A^H|=U\operatorname{diag}(\sigma_1,\ldots,\sigma_r,0_{m-r})U^H.
\]
::: {.proof}
The SVD gives
\[
A^HA=V\Sigma^H\Sigma V^H,
\qquad
AA^H=U\Sigma\Sigma^H U^H.
\]
The matrices $\Sigma^H\Sigma$ and $\Sigma\Sigma^H$ are diagonal, with diagonal entries $\sigma_1^2,\ldots,\sigma_r^2$ followed by the appropriate number of zeros. Taking their positive square roots yields the displayed formulas.
:::

<1>6. Therefore $|A|$ and $|A^H|$ have the same nonzero eigenvalues with the same multiplicities, and they are unitarily similar after adjoining zero blocks to equalize sizes.
::: {.proof}
The formulas in <1>5 show that both nonzero spectra are exactly
\[
\sigma_1,\ldots,\sigma_r.
\]
If $m\ge n$, then
\[
|A^H|\sim_u |A|\oplus 0_{m-n},
\]
because both are unitarily similar to
\[
\operatorname{diag}(\sigma_1,\ldots,\sigma_r,0_{m-r}).
\]
If $n\ge m$, similarly
\[
|A|\sim_u |A^H|\oplus0_{n-m}.
\]
In particular, when $m=n$, the two matrices are unitarily similar without adding any zero block.
:::
:::
