---
schema: qual/card@1
id: P-UCLAB03F-10
kind: problem
title: Two real matrices that cannot be diagonalized over the reals
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 10 of the official UCLA Basic Exam Fall 2003 PDF.
---

::: {.problem}
(a) Let $t\in\mathbb R$ be not an integer multiple of $\pi$.
For
\[
A=
\begin{pmatrix}
\cos t&\sin t\\
-\sin t&\cos t
\end{pmatrix},
\]
prove that there is no real matrix $B$ for which $BAB^{-1}$ is diagonal.

(b) Prove the same assertion for
\[
A=
\begin{pmatrix}
1&\lambda\\
0&1
\end{pmatrix},
\qquad
\lambda\in\mathbb R\setminus\{0\}.
\]
:::

::: {.solution}
<1>1. In part (a), the characteristic polynomial of
\[
A=
\begin{pmatrix}
\cos t&\sin t\\
-\sin t&\cos t
\end{pmatrix}
\]
is
\[
p_A(\mu)=\mu^2-2(\cos t)\mu+1.
\]

::: {.proof}
One computes
\[
\begin{aligned}
\det(\mu I-A)
&=
\det
\begin{pmatrix}
\mu-\cos t&-\sin t\\
\sin t&\mu-\cos t
\end{pmatrix}\\
&=
(\mu-\cos t)^2+\sin^2 t\\
&=
\mu^2-2(\cos t)\mu+\cos^2t+\sin^2t\\
&=
\mu^2-2(\cos t)\mu+1.
\end{aligned}
\]
:::

<1>2. If $t$ is not an integer multiple of $\pi$, then the matrix in part (a) has no real eigenvalues.

::: {.proof}
The discriminant of the polynomial in step <1>1 is
\[
4\cos^2t-4
=
-4\sin^2t.
\]
Since $t\notin\pi\mathbb Z$, one has $\sin t\ne0$, so the discriminant is strictly negative. Hence $p_A$ has no real roots.
:::

<1>3. There is no real invertible matrix $B$ for which $BAB^{-1}$ is diagonal in part (a).

::: {.proof}
Suppose such a real matrix $B$ existed and set
\[
D=BAB^{-1}.
\]
Then $D$ would be a real diagonal matrix similar to $A$. Similar matrices have the same characteristic polynomial, so every diagonal entry of $D$ would be a real eigenvalue of $A$. This contradicts step <1>2.
:::

<1>4. In part (b), the only eigenvalue of
\[
A=
\begin{pmatrix}
1&\lambda\\
0&1
\end{pmatrix},
\qquad \lambda\ne0,
\]
is $1$, and its eigenspace is
\[
E_1=\operatorname{span}\{(1,0)\}.
\]

::: {.proof}
The characteristic polynomial is
\[
\det(\mu I-A)
=
(\mu-1)^2,
\]
so the only eigenvalue is $1$. Moreover,
\[
A-I
=
\begin{pmatrix}
0&\lambda\\
0&0
\end{pmatrix}.
\]
Since $\lambda\ne0$,
\[
\ker(A-I)
=
\{(x,0):x\in\mathbb R\}
=
\operatorname{span}\{(1,0)\}.
\]
:::

<1>5. The matrix in part (b) is not diagonalizable over $\mathbb R$.

::: {.proof}
If a real $2\times2$ matrix is diagonalizable over $\mathbb R$, then $\mathbb R^2$ has a basis consisting of two real eigenvectors. By step <1>4, every eigenvector of this matrix lies in the one-dimensional space $E_1$. Hence there cannot be two linearly independent eigenvectors, so the matrix is not diagonalizable.
:::

<1>6. Therefore there is no real invertible matrix $B$ for which $BAB^{-1}$ is diagonal in part (b).

::: {.proof}
Such a matrix $B$ would make $A$ similar over $\mathbb R$ to a diagonal matrix, which is precisely real diagonalizability. Step <1>5 rules this out.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>3 proves part (a), and step <1>6 proves part (b).
:::
:::
