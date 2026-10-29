---
schema: qual/card@1
id: P-UCLAB15S-12
kind: problem
title: Matrix exponential and existence of a real logarithm
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UCLA Basic Examination, Spring 2015, `assets/attachments/basic-15S.pdf`.
---

::: {.problem}
Let
\[
M=\begin{pmatrix}3&5\\1&-1\end{pmatrix}.
\]

1. Compute $\exp(M)$.

2. Does there exist a real $2\times2$ matrix $A$ such that $M=\exp(A)$?
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The characteristic polynomial of $M$ is
\[
\chi_M(\lambda)
=
\lambda^2-2\lambda-8
=
(\lambda-4)(\lambda+2).
\]


::: pf-proof

\[
\begin{aligned}
\det(\lambda I-M)
&=
\det
\begin{pmatrix}
\lambda-3&-5\\
-1&\lambda+1
\end{pmatrix}\\
&=
(\lambda-3)(\lambda+1)-5\\
&=
\lambda^2-2\lambda-8.
\end{aligned}
\]

:::

:::

::: pf-step

The matrix $M$ is diagonalizable over $\RR$.


::: pf-proof

Step [](#s1-1){.pf-ref} gives two distinct real eigenvalues, $4$ and $-2$.
Therefore $M$ has a basis of eigenvectors.

:::

:::

::: pf-step

The corresponding spectral projections are
\[
P_4=\frac{M+2I}{6},
\qquad
P_{-2}=\frac{4I-M}{6}.
\]


::: pf-proof

The polynomial
\[
\frac{t+2}{6}
\]
equals $1$ at $t=4$ and $0$ at $t=-2$, while
\[
\frac{4-t}{6}
\]
equals $0$ at $t=4$ and $1$ at $t=-2$.
Applying these polynomials to $M$ gives the two eigenspace projections.

:::

:::

::: {.pf-step #s1-4}

Therefore
\[
\boxed{
\exp(M)
=
e^4P_4+e^{-2}P_{-2}.
}
\]


::: pf-proof

On the eigenspace for eigenvalue $4$, the exponential acts by multiplication by $e^4$; on the eigenspace for eigenvalue $-2$, it acts by multiplication by $e^{-2}$.

:::

:::

::: {.pf-step #s1-5}

Explicitly,
\[
M+2I
=
\begin{pmatrix}
5&5\\
1&1
\end{pmatrix},
\qquad
4I-M
=
\begin{pmatrix}
1&-5\\
-1&5
\end{pmatrix}.
\]


::: pf-proof

These follow by direct matrix addition and subtraction.

:::

:::

::: {.pf-step #s1-6}

Hence
\[
\boxed{
\exp(M)
=
\frac16
\begin{pmatrix}
5e^4+e^{-2}
&
5e^4-5e^{-2}\\
e^4-e^{-2}
&
e^4+5e^{-2}
\end{pmatrix}.
}
\]


::: pf-proof

Substitute the matrices from step [](#s1-5){.pf-ref} into the formula of step [](#s1-4){.pf-ref}.
This answers part 1.

:::

:::

::: {.pf-step #s1-7}

If a real matrix $A$ satisfied
\[
\exp(A)=M,
\]
then
\[
\det M>0.
\]


::: pf-proof

For every real square matrix $A$,
\[
\det(\exp A)
=
\exp(\operatorname{tr}A).
\]
The right-hand side is strictly positive.

:::

:::

::: {.pf-step #s1-8}

But
\[
\det M
=
-8
<
0.
\]


::: pf-proof

Direct computation gives
\[
\det M
=
3(-1)-5(1)
=
-8.
\]

:::

:::

::: {.pf-step #s1-9}

Therefore no real $2\times2$ matrix $A$ satisfies
\[
\exp(A)=M.
\]


::: pf-proof

Steps [](#s1-7){.pf-ref} through [](#s1-8){.pf-ref} give a contradiction to the existence of such an $A$.
Thus the answer to part 2 is
\[
\boxed{\text{No}.}
\]

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} computes $\exp(M)$, and step [](#s1-9){.pf-ref} answers the second question.

:::

:::

:::
