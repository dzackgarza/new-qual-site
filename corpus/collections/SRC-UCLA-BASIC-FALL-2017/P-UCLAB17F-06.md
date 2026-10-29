---
schema: qual/card@1
id: P-UCLAB17F-06
kind: problem
title: Diagonalizability of symmetric two-by-two matrices over three fields
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
  note: Checked against the vendored UCLA Basic Examination, Fall 2017, `assets/attachments/basic-17F.pdf`.
---

::: {.problem}
For each field $F=\RR$, $\CC$, and $\FF_3$, determine whether every symmetric matrix in $M_2(F)$ is diagonalizable. Give proofs or counterexamples.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Over
\[
F=\RR,
\]
every symmetric $2\times2$ matrix is diagonalizable.


::: pf-proof

The real spectral theorem states that every real symmetric matrix is orthogonally diagonalizable.
Hence every symmetric matrix in
\[
M_2(\RR)
\]
is diagonalizable over $\RR$.

:::

:::

::: {.pf-step #s1-2}

Over
\[
F=\CC,
\]
the assertion is false.


::: pf-proof

Consider
\[
A=
\begin{pmatrix}
i&1\\
1&-i
\end{pmatrix}.
\]
This matrix is symmetric:
\[
A^T=A.
\]
Direct multiplication gives
\[
A^2
=
\begin{pmatrix}
i^2+1&i-i\\
i-i&1+(-i)^2
\end{pmatrix}
=
\begin{pmatrix}
0&0\\
0&0
\end{pmatrix}.
\]
Thus $A$ is nilpotent and nonzero.

If $A$ were diagonalizable, it would be similar to a diagonal matrix whose diagonal entries are its eigenvalues.
Since $A^2=0$, every eigenvalue satisfies
\[
\lambda^2=0,
\]
so every eigenvalue is $0$.
The only diagonal matrix with both diagonal entries zero is the zero matrix.
Thus a diagonalizable nilpotent matrix must be zero, contradicting
\[
A\ne0.
\]
Hence $A$ is not diagonalizable.

:::

:::

::: {.pf-step #s1-3}

Over
\[
F=\FF_3,
\]
the assertion is also false.


::: pf-proof

Consider
\[
A=
\begin{pmatrix}
0&1\\
1&1
\end{pmatrix}
\in M_2(\FF_3).
\]
It is symmetric.
Its characteristic polynomial is
\[
\begin{aligned}
\chi_A(\lambda)
&=
\det
\begin{pmatrix}
\lambda&-1\\
-1&\lambda-1
\end{pmatrix}\\
&=
\lambda(\lambda-1)-1\\
&=
\lambda^2-\lambda-1.
\end{aligned}
\]
In $\FF_3$, this polynomial takes the values
\[
\chi_A(0)=-1=2,
\]
\[
\chi_A(1)=1-1-1=-1=2,
\]
\[
\chi_A(2)=4-2-1=1.
\]
Thus it has no root in $\FF_3$.
Therefore $A$ has no eigenvalue in $\FF_3$, so it cannot be diagonalizable over $\FF_3$.

:::

:::

::: {.pf-step #s1-4}

Therefore the complete answer is
\[
\boxed{
\begin{array}{c|c}
F&\text{every symmetric }2\times2\text{ matrix diagonalizable?}\\
\hline
\RR&\text{yes}\\
\CC&\text{no}\\
\FF_3&\text{no}
\end{array}
}
\]


::: pf-proof

Step [](#s1-1){.pf-ref} proves the positive real case.
Step [](#s1-2){.pf-ref} gives a complex counterexample.
Step [](#s1-3){.pf-ref} gives a counterexample over $\FF_3$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} records the required classification.

:::

:::

:::
