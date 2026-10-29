---
schema: qual/card@1
id: P-YSL2C
kind: problem
title: Conjugacy classes in $\SL_2(\RR)$
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
Let $A\in\SL_2(\RR)$ with $t=\tr A$, so its characteristic polynomial is $x^2-tx+1$.
Write $R_\theta=\begin{pmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{pmatrix}$, $J=R_{\pi/2}$, $U_\pm=\begin{pmatrix}1&\pm1\\0&1\end{pmatrix}$ and $D=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$.
If $A$ is conjugate to $B$ by some $P\in\GL_2(\RR)$, then it is conjugate to $B$ in $\SL_2(\RR)$ exactly when some such $P$ has $\det P>0$, because scaling $P$ by a positive real does not change the conjugation.

::: pf

::: pf-step
(Hyperbolic, $\abs{t}>2$) There is exactly one class for each such $t$, represented by $\diag(\lambda,\lambda^{-1})$ with $\lambda+\lambda^{-1}=t$.

::: pf-proof
The eigenvalues $\lambda\ne\lambda^{-1}$ are real, so $A$ is diagonalized by a matrix of eigenvectors; negating one column makes its determinant positive.
The swap of $\lambda$ and $\lambda^{-1}$ is conjugation by $J\in\SL_2(\RR)$.
:::

:::

::: pf-step
(Elliptic, $\abs{t}<2$) Write $t=2\cos\theta$ with $0<\theta<\pi$. There are exactly two classes with trace $t$, represented by $R_\theta$ and $R_{-\theta}$.

::: pf-proof
The eigenvalues $e^{\pm i\theta}$ are non-real, so $A$ is $\GL_2(\RR)$-conjugate to $R_\theta$; since $DR_\theta D^{-1}=R_{-\theta}$ and $\det D<0$, $A$ is $\SL_2(\RR)$-conjugate to $R_\theta$ or to $R_{-\theta}$.
If $PR_\theta P^{-1}=R_{-\theta}$, then, as $R_{\pm\theta}=\cos\theta\,I\pm\sin\theta\,J$ and $\sin\theta\ne0$, we get $PJ=-JP$.
Writing $P=\begin{pmatrix}a&b\\c&d\end{pmatrix}$, this forces $c=b$ and $d=-a$, so $\det P=-(a^2+b^2)<0$.
:::

:::

::: {.pf-step #parabolic}
(Parabolic, $t=2$) There are exactly three classes: $\{I\}$, the class of $U_+$, and the class of $U_-$.

::: pf-proof
If $A\ne I$, then $A$ has the single eigenvalue $1$ and is not diagonalizable, so it is $\GL_2(\RR)$-conjugate to $U_+$; since $DU_+D^{-1}=U_-$, it is $\SL_2(\RR)$-conjugate to $U_+$ or to $U_-$.
Every $P$ with $PU_+P^{-1}=U_-$ is $D$ times an element of the centralizer of $U_+$, which consists of the matrices $\begin{pmatrix}a&b\\0&a\end{pmatrix}$ with $a\ne0$, so $\det P=-a^2<0$.
:::

:::

::: pf-step
(Parabolic, $t=-2$) There are exactly three classes: $\{-I\}$, the class of $-U_+$, and the class of $-U_-$.

::: pf-proof
Multiplication by $-I$ is a bijection of $\SL_2(\RR)$ that commutes with conjugation and changes the trace from $2$ to $-2$; apply step [](#parabolic){.pf-ref}.
:::

:::

:::

:::
