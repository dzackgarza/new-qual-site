---
schema: qual/card@1
id: P-UGAP08F-04
kind: problem
title: Diagonalization and nineteenth power of a $3\times 3$ matrix with eigenvalues $-1,0,1$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: "The retained markdown extraction does not preserve the displayed matrix A reliably: it declares a three-column array but emits four entry fields per row, with blank fields. Repository history contains the same damaged extraction and no independent statement of the matrix, so the missing entries are not guessed."
---

::: {.problem}
Let
$$
A=\begin{pmatrix}
-1&0&0\\
-2&3&-2\\
-2&3&-2
\end{pmatrix}.
$$

Prove that $A$ is diagonalizable and use this fact to compute
$$
A^{19}.
$$
:::

::: {.solution}

::: pf

::: pf-step

One has
$$
\det(A-\lambda I)=-(\lambda+1)\lambda(\lambda-1),
$$
so the eigenvalues are $-1,0,1$.


::: pf-proof

Because the first row of $A-\lambda I$ is $(-1-\lambda,0,0)$,
$$
\begin{aligned}
\det(A-\lambda I)
&=(-1-\lambda)
\det\begin{pmatrix}3-\lambda&-2\\3&-2-\lambda\end{pmatrix}\\
&=(-1-\lambda)\bigl((3-\lambda)(-2-\lambda)+6\bigr)\\
&=(-1-\lambda)\lambda(\lambda-1).
\end{aligned}
$$
Thus the roots are $-1,0,1$.

:::

:::

::: {.pf-step #s1-2}

Corresponding eigenvectors are
$$
v_{-1}=\begin{pmatrix}1\\1\\1\end{pmatrix},
\qquad
v_0=\begin{pmatrix}0\\2\\3\end{pmatrix},
\qquad
v_1=\begin{pmatrix}0\\1\\1\end{pmatrix}.
$$


::: pf-proof

Direct multiplication gives
$$
Av_{-1}=-v_{-1},
\qquad
Av_0=0,
\qquad
Av_1=v_1.
$$

:::

:::

::: {.pf-step #s1-3}

The matrix $A$ is diagonalizable. In fact, with
$$
P=\begin{pmatrix}
1&0&0\\
1&2&1\\
1&3&1
\end{pmatrix},
\qquad
D=\begin{pmatrix}
-1&0&0\\
0&0&0\\
0&0&1
\end{pmatrix},
$$
one has
$$
A=PDP^{-1}.
$$


::: pf-proof

The columns of $P$ are the eigenvectors from step [](#s1-2){.pf-ref}. Moreover,
$$
\det P=2-3=-1\ne0,
$$
so they form a basis of $\RR^3$. Therefore $P^{-1}AP=D$, equivalently $A=PDP^{-1}$.

:::

:::

::: {.pf-step #s1-4}

One has
$$
\boxed{
A^{19}=A=
\begin{pmatrix}
-1&0&0\\
-2&3&-2\\
-2&3&-2
\end{pmatrix}.
}
$$


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
A^{19}=PD^{19}P^{-1}.
$$
Since the diagonal entries of $D$ are $-1,0,1$ and $19$ is odd,
$$
D^{19}=D.
$$
Hence
$$
A^{19}=PDP^{-1}=A.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves diagonalizability, and step [](#s1-4){.pf-ref} computes $A^{19}$.

:::

:::

:::
