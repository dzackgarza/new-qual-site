---
schema: qual/card@1
id: P-BKS16-7A
kind: problem
title: Rationality of eigenvalues of rational symmetric matrices
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the transpose superscript in UDU^T and the hyphenated word orthogonal against Sp16_Exam.pdf page 8 problem 7A.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked symmetry and rationality of the counterexample, its characteristic polynomial, and the identification of the diagonal entries in an orthogonal diagonalization with its eigenvalues.
---

::: {.problem}
Suppose $A$ is a symmetric matrix with rational entries and $A = U D U^T$, where $U$ is orthogonal. Must $D$ have rational entries? Prove or find a counterexample.
:::

::: {.solution}
No.

::: pf

::: {.pf-step #s1}

Consider
$$
A
=
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}.
$$
Then $A$ is symmetric and has rational entries.

::: pf-proof

The displayed matrix equals its transpose, and all four entries lie in $\QQ$.

:::

:::

::: {.pf-step #s2}

The characteristic polynomial of $A$ is
$$
\chi_A(t)=t^2-2.
$$
Hence the eigenvalues of $A$ are
$$
\sqrt2
\qquad\text{and}\qquad
-\sqrt2.
$$

::: pf-proof

One computes
$$
\begin{aligned}
\det(tI-A)
&=
\det
\begin{pmatrix}
t-1&-1\\
-1&t+1
\end{pmatrix}\\
&=
(t-1)(t+1)-1\\
&=
t^2-2.
\end{aligned}
$$
Its two roots are $\pm\sqrt2$.

:::

:::

::: {.pf-step #s3}

If
$$
A=UDU^T
$$
with $U$ orthogonal and $D$ diagonal, then the diagonal entries of $D$ are precisely the eigenvalues of $A$, in some order.

::: pf-proof

Since $U^{-1}=U^T$,
$$
D=U^TAU.
$$
Thus $D$ is similar to $A$, so it has the same eigenvalues. The eigenvalues of a diagonal matrix are its diagonal entries.

:::

:::

::: {.pf-step #s4}

Therefore, for the matrix in step [](#s1){.pf-ref}, every orthogonal diagonalization has
$$
D
=
\begin{pmatrix}
\sqrt2&0\\
0&-\sqrt2
\end{pmatrix}
$$
up to permutation of the diagonal entries, and $D$ does not have rational entries.

::: pf-proof

By the real spectral theorem, the symmetric matrix $A$ has an orthogonal diagonalization. Combine steps [](#s2){.pf-ref} and [](#s3){.pf-ref} to identify its diagonal entries. Since $\sqrt2\notin\QQ$, neither possible ordering gives a rational diagonal matrix. Thus this particular orthogonal factorization $A=UDU^T$ already disproves the assertion that $D$ must have rational entries.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} gives the required counterexample.

:::

:::

:::
