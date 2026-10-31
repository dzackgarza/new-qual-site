---
schema: qual/card@1
id: P-TRIV-LA08
kind: problem
title: Determinant of a $2\times 2$ block matrix
classification:
  areas: [prelim]
  topics:
  - Determinants
  - Block Matrices
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 8, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Let $A$, $B$, $C$, $D$ be non-degenerate matrices of the same dimension. Show that
$$
\det \begin{bmatrix} A & B \\ C & D \end{bmatrix} = \det\left( AD - BD^{-1}CD \right). \tag{1}
$$
:::

::: {.solution}

Let
$$
M=
\begin{pmatrix}
A&B\\
C&D
\end{pmatrix}.
$$

::: pf

::: {.pf-step #s1-1}

Since $D$ is nondegenerate, the block matrix
$$
L=
\begin{pmatrix}
I&-BD^{-1}\\
0&I
\end{pmatrix}
$$
is invertible and satisfies
$$
\det L=1.
$$


::: pf-proof

The matrix $L$ is block upper triangular with identity blocks on its diagonal.
Hence
$$
\det L
=
(\det I)(\det I)
=1.
$$

:::

:::

::: {.pf-step #s1-2}

Multiplying $M$ on the left by $L$ gives
$$
LM
=
\begin{pmatrix}
A-BD^{-1}C&0\\
C&D
\end{pmatrix}.
$$


::: pf-proof

Block multiplication gives
$$
\begin{aligned}
LM
&=
\begin{pmatrix}
I&-BD^{-1}\\
0&I
\end{pmatrix}
\begin{pmatrix}
A&B\\
C&D
\end{pmatrix}\\
&=
\begin{pmatrix}
A-BD^{-1}C&B-BD^{-1}D\\
C&D
\end{pmatrix}\\
&=
\begin{pmatrix}
A-BD^{-1}C&0\\
C&D
\end{pmatrix}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

One has
$$
\det M
=
\det(A-BD^{-1}C)\det D.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\det(LM)
=
(\det L)(\det M)
=
\det M.
$$
By step [](#s1-2){.pf-ref}, $LM$ is block lower triangular, so
$$
\det(LM)
=
\det(A-BD^{-1}C)\det D.
$$

:::

:::

::: {.pf-step #s1-4}

The right-hand side in step [](#s1-3){.pf-ref} equals
$$
\det\left(AD-BD^{-1}CD\right).
$$


::: pf-proof

By multiplicativity of the determinant,
$$
\det(A-BD^{-1}C)\det D
=
\det\left((A-BD^{-1}C)D\right).
$$
Distributing the right multiplication by $D$ gives
$$
(A-BD^{-1}C)D
=
AD-BD^{-1}CD.
$$

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
\det
\begin{pmatrix}
A&B\\
C&D
\end{pmatrix}
=
\det\left(AD-BD^{-1}CD\right).
}
$$


::: pf-proof

Combine steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required identity.

:::

:::

:::
