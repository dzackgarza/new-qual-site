---
schema: qual/card@1
id: P-PRACT20-W4-23
kind: problem
title: Real $2\times2$ solutions of $A^{100}=\operatorname{diag}(-1,-\alpha)$
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Matrices
  - Eigenvalues and Eigenvectors
relations: []
review: draft
---

::: {.problem}
Show that there is no $A\in\mathbb R^{2\times2}$ satisfying
\[
A^{100}=\begin{pmatrix}-1&0\\0&-\alpha\end{pmatrix}
\]
when $\alpha>1$.
If $\alpha=1$, find $A\in\mathbb R^{2\times2}$ satisfying the equation.
:::

::: {.solution}
<1>1. If $\alpha>1$, any solution $A$ would have to be diagonal.
::: {.proof}
Set
$$
D=\begin{pmatrix}-1&0\\0&-\alpha\end{pmatrix}.
$$
If $A^{100}=D$, then $A$ commutes with $D$ because every matrix commutes with its powers:
$$
AD=AA^{100}=A^{101}=A^{100}A=DA.
$$
Write
$$
A=\begin{pmatrix}a&b\\c&d\end{pmatrix}.
$$
The equality $AD=DA$ gives
$$
(\alpha-1)b=0,
\qquad
(\alpha-1)c=0.
$$
Since $\alpha>1$, we obtain $b=c=0$. Thus $A$ is diagonal.
:::

<1>2. No real diagonal matrix has the required hundredth power when $\alpha>1$.
::: {.proof}
By step <1>1, write
$$
A=\begin{pmatrix}a&0\\0&d\end{pmatrix}.
$$
Then
$$
A^{100}=\begin{pmatrix}a^{100}&0\\0&d^{100}\end{pmatrix}.
$$
For real $a$ and $d$, both $a^{100}$ and $d^{100}$ are nonnegative, so they cannot equal $-1$ and $-\alpha$. Therefore no such real matrix exists.
:::

<1>3. When $\alpha=1$, rotation through angle $\pi/100$ is a solution.
::: {.proof}
Let
$$
A=
\begin{pmatrix}
\cos(\pi/100)&-\sin(\pi/100)\\
\sin(\pi/100)&\cos(\pi/100)
\end{pmatrix}.
$$
This is the rotation matrix $R_{\pi/100}$. Since rotation matrices satisfy
$$
R_\theta R_\varphi=R_{\theta+\varphi},
$$
we have
$$
A^{100}=R_\pi
=\begin{pmatrix}-1&0\\0&-1\end{pmatrix}.
$$
Thus $A^{100}=\operatorname{diag}(-1,-\alpha)$ when $\alpha=1$.
:::

<1>4. Q.E.D.
::: {.proof}
Steps <1>1--<1>2 prove nonexistence for $\alpha>1$, and step <1>3 gives the requested example for $\alpha=1$.
:::
:::
