---
schema: qual/card@1
id: P-UGAP11F-02
kind: problem
title: Diagonalize an explicit two-by-two matrix by similarity
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Find an invertible matrix $A$ and a diagonal matrix $B$ such that
$$
\begin{pmatrix}
8&9\\
-6&-7
\end{pmatrix}
=ABA^{-1}.
$$
:::

::: {.solution}

Let
$$
M=
\begin{pmatrix}
8&9\\
-6&-7
\end{pmatrix}.
$$

::: pf

::: pf-step

The characteristic polynomial of $M$ is
$$
\boxed{\chi_M(\lambda)=(\lambda-2)(\lambda+1)}.
$$


::: pf-proof

One computes
$$
\begin{aligned}
\chi_M(\lambda)
&=
\det(\lambda I-M)\\
&=
\det
\begin{pmatrix}
\lambda-8&-9\\
6&\lambda+7
\end{pmatrix}\\
&=
(\lambda-8)(\lambda+7)+54\\
&=
\lambda^2-\lambda-2\\
&=
(\lambda-2)(\lambda+1).
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-2}

An eigenvector for the eigenvalue $2$ is
$$
v_2=
\begin{pmatrix}
-3\\
2
\end{pmatrix},
$$
and an eigenvector for the eigenvalue $-1$ is
$$
v_{-1}=
\begin{pmatrix}
1\\
-1
\end{pmatrix}.
$$


::: pf-proof

For $\lambda=2$,
$$
M-2I
=
\begin{pmatrix}
6&9\\
-6&-9
\end{pmatrix},
$$
and
$$
6(-3)+9(2)=0.
$$
Hence
$$
Mv_2=2v_2.
$$

For $\lambda=-1$,
$$
M+I
=
\begin{pmatrix}
9&9\\
-6&-6
\end{pmatrix},
$$
and
$$
9(1)+9(-1)=0.
$$
Hence
$$
Mv_{-1}=-v_{-1}.
$$

:::

:::

::: {.pf-step #s1-3}

Define
$$
\boxed{
A=
\begin{pmatrix}
-3&1\\
2&-1
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
2&0\\
0&-1
\end{pmatrix}}.
$$
Then $A$ is invertible.


::: pf-proof

The columns of $A$ are the two eigenvectors from step [](#s1-2){.pf-ref}. Moreover,
$$
\det A
=
(-3)(-1)-2
=1\ne0.
$$
Thus $A$ is invertible.

:::

:::

::: {.pf-step #s1-4}

One has
$$
M=ABA^{-1}.
$$


::: pf-proof

Since the columns of $A$ are eigenvectors with eigenvalues given by the diagonal entries of $B$,
$$
MA=AB.
$$
Right-multiplying by $A^{-1}$ gives
$$
M=ABA^{-1}.
$$

:::

:::

::: pf-qed

Steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} provide the requested matrices and verify the similarity relation.

:::

:::

:::
