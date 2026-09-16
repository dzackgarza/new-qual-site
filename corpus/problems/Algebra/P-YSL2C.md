---
schema: qual/card@1
id: P-YSL2C
kind: problem
title: Conjugacy classes in $\mathrm{SL}_2(\RR)$
classification:
  areas:
  - algebra
  topics:
  - Conjugacy
  - Matrix Groups
  - Jordan Canonical Form
relations: []
review: draft
---

::: {.problem}
Classify the conjugacy classes in $\SL_2(\RR)$.
:::

::: {.solution}
Let $A\in\SL_2(\RR)$ and set
\[
t=\operatorname{tr}(A).
\]
Its characteristic polynomial is
\[
x^2-tx+1.
\]
The conjugacy classification is determined by the sign of $t^2-4$, with an additional orientation sign in the elliptic and nontrivial parabolic cases.

<1>1. Hyperbolic classes: $|t|>2$.

The eigenvalues are distinct real numbers $\lambda,\lambda^{-1}$. Thus $A$ is $\SL_2(\RR)$-conjugate to
\[
\begin{pmatrix}\lambda&0\\0&\lambda^{-1}\end{pmatrix},
\qquad
\lambda+\lambda^{-1}=t.
\]
Swapping the two eigenvalues is achieved by
\[
\begin{pmatrix}0&-1\\1&0\end{pmatrix}\in\SL_2(\RR),
\]
so there is one conjugacy class for each trace $|t|>2$.

<1>2. Elliptic classes: $|t|<2$.

Write
\[
t=2\cos\theta,
\qquad
0<\theta<\pi.
\]
Then $A$ is conjugate in $\GL_2(\RR)$ to a rotation. In $\SL_2(\RR)$ there are two classes:
\[
R_\theta=
\begin{pmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{pmatrix},
\qquad
R_{-\theta}.
\]
They are not $\SL_2(\RR)$-conjugate. Indeed, if $P R_\theta P^{-1}=R_{-\theta}$, then, after subtracting $\cos\theta I$ and dividing by $\sin\theta$, one gets
\[
PJP^{-1}=-J,
\qquad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
Every real matrix satisfying $PJ=-JP$ has negative determinant unless it is singular, so no such $P$ lies in $\SL_2(\RR)$.

<1>3. Parabolic classes: $t=2$.

Either $A=I$, or $A$ is nontrivial unipotent. Every nontrivial unipotent is $\SL_2(\RR)$-conjugate to exactly one of
\[
U_+=\begin{pmatrix}1&1\\0&1\end{pmatrix},
\qquad
U_-=\begin{pmatrix}1&-1\\0&1\end{pmatrix}.
\]
They are not $\SL_2(\RR)$-conjugate: a $\GL_2(\RR)$-conjugator between them has negative determinant, while the centralizer of $U_+$ consists of matrices
\[
\begin{pmatrix}a&b\\0&a\end{pmatrix}
\]
with determinant $a^2>0$. Hence the sign cannot be changed by a determinant-$1$ conjugator.

<1>4. Parabolic classes: $t=-2$.

Likewise there are exactly three classes:
\[
-I,
\qquad
-U_+,
\qquad
-U_-.
\]

Therefore trace determines the hyperbolic class, while for each elliptic trace there are two classes and for each trace $\pm2$ there are the scalar class and two nontrivial parabolic classes.
:::
