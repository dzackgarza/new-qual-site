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
(a) Let $t\in\RR$ be not an integer multiple of $\pi$.
For
$$
A=
\begin{pmatrix}
\cos t&\sin t\\
-\sin t&\cos t
\end{pmatrix},
$$
prove that there is no real matrix $B$ for which $BAB^{-1}$ is diagonal.

(b) Prove the same assertion for
$$
A=
\begin{pmatrix}
1&\lambda\\
0&1
\end{pmatrix},
\qquad
\lambda\in\RR\setminus\{0\}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

In part (a), the characteristic polynomial of
$$
A=
\begin{pmatrix}
\cos t&\sin t\\
-\sin t&\cos t
\end{pmatrix}
$$
is
$$
p_A(\mu)=\mu^2-2(\cos t)\mu+1.
$$


::: pf-proof

One computes
$$
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
$$

:::

:::

::: {.pf-step #s1-2}

If $t$ is not an integer multiple of $\pi$, then the matrix in part (a) has no real eigenvalues.


::: pf-proof

The discriminant of the polynomial in step [](#s1-1){.pf-ref} is
$$
4\cos^2t-4
=
-4\sin^2t.
$$
Since $t\notin\pi\ZZ$, one has $\sin t\ne0$, so the discriminant is strictly negative. Hence $p_A$ has no real roots.

:::

:::

::: {.pf-step #s1-3}

There is no real invertible matrix $B$ for which $BAB^{-1}$ is diagonal in part (a).


::: pf-proof

Suppose such a real matrix $B$ existed and set
$$
D=BAB^{-1}.
$$
Then $D$ would be a real diagonal matrix similar to $A$. Similar matrices have the same characteristic polynomial, so every diagonal entry of $D$ would be a real eigenvalue of $A$. This contradicts step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

In part (b), the only eigenvalue of
$$
A=
\begin{pmatrix}
1&\lambda\\
0&1
\end{pmatrix},
\qquad \lambda\ne0,
$$
is $1$, and its eigenspace is
$$
E_1=\operatorname{span}\{(1,0)\}.
$$


::: pf-proof

The characteristic polynomial is
$$
\det(\mu I-A)
=
(\mu-1)^2,
$$
so the only eigenvalue is $1$. Moreover,
$$
A-I
=
\begin{pmatrix}
0&\lambda\\
0&0
\end{pmatrix}.
$$
Since $\lambda\ne0$,
$$
\ker(A-I)
=
\{(x,0):x\in\RR\}
=
\operatorname{span}\{(1,0)\}.
$$

:::

:::

::: {.pf-step #s1-5}

The matrix in part (b) is not diagonalizable over $\RR$.


::: pf-proof

If a real $2\times2$ matrix is diagonalizable over $\RR$, then $\RR^2$ has a basis consisting of two real eigenvectors. By step [](#s1-4){.pf-ref}, every eigenvector of this matrix lies in the one-dimensional space $E_1$. Hence there cannot be two linearly independent eigenvectors, so the matrix is not diagonalizable.

:::

:::

::: {.pf-step #s1-6}

Therefore there is no real invertible matrix $B$ for which $BAB^{-1}$ is diagonal in part (b).


::: pf-proof

Such a matrix $B$ would make $A$ similar over $\RR$ to a diagonal matrix, which is precisely real diagonalizability. Step [](#s1-5){.pf-ref} rules this out.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves part (a), and step [](#s1-6){.pf-ref} proves part (b).

:::

:::

:::
