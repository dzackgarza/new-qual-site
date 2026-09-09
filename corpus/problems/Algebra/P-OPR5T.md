---
schema: qual/card@1
id: P-OPR5T
kind: problem
title: Given a skew-symmetric/skew-Hermitian matrix S, show that
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Inner Product Spaces
  - Matrices
relations: []
review: draft
---

::: problem
Let $S$ be a real skew-symmetric matrix or a complex skew-Hermitian matrix. Define the Cayley transform
\[
U=(S+I)(S-I)^{-1}.
\]
Show that $U$ is respectively orthogonal or unitary, and solve for $S$ in terms of $U$.
:::

::: {.solution}
It suffices to treat the skew-Hermitian case; the real skew-symmetric case is identical with transpose in place of conjugate transpose.

<1>1. The matrix $S-I$ is invertible.
::: {.proof}
If $(S-I)v=0$, then $Sv=v$. But every eigenvalue of a skew-Hermitian matrix is purely imaginary, while $1$ is real and nonzero. Hence $v=0$.
:::

<1>2. The Cayley transform is unitary.
::: {.proof}
Because $S^*=-S$,
\[
U^*=\bigl((S-I)^{-1}\bigr)^*(S+I)^*
=(-S-I)^{-1}(-S+I).
\]
Thus
\[
U^*=(S+I)^{-1}(S-I).
\]
All factors are rational functions of $S$, hence commute. Therefore
\[
U^*U
=(S+I)^{-1}(S-I)(S+I)(S-I)^{-1}=I.
\]
So $U$ is unitary. In the real case the same computation gives $U^TU=I$.
:::

<1>3. Recover $S$ from $U$.
::: {.proof}
From
\[
U(S-I)=S+I
\]
we obtain
\[
(U-I)S=U+I.
\]
Moreover
\[
U-I=2(S-I)^{-1},
\]
so $U-I$ is invertible over $\RR$ or $\CC$. Hence
\[
S=(U-I)^{-1}(U+I).
\]
Since $U$ commutes with polynomials in $U$, this may equivalently be written $(U+I)(U-I)^{-1}$.
:::
:::
