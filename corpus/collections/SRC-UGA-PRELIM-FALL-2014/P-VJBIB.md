---
schema: qual/card@1
id: P-VJBIB
kind: problem
title: Spectral theorem diagonalization with eigenvalues $6$ and $1$, and the minimum
  of $\langle Ax,x\rangle$ on the unit circle
classification:
  areas:
  - prelim
  topics:
  - Diagonalization
  - Eigenvalues and Eigenvectors
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against the examination retained at assets/attachments/grad_prelim_Fall14.pdf, problem 6:
    "Take A := [[2,-2],[-2,5]]. Find an orthogonal matrix P for which P^{-1} A P is diagonal. Then
    find the minimum value of the dot products A x . x as x ranges through the unit vectors in R^2."
    The card's statement is that problem verbatim.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Two defects repaired and the proof restructured. First, the card offered P = [[1,2],[-2,1]] as
    an orthogonal matrix; its columns are the eigenvectors but have length sqrt 5, so it is not
    orthogonal, and the card now carries the normalized P = 5^{-1/2} times it, with the failure of
    the unnormalized matrix stated. Second, the minimization: from 12 y_1 = 2 lambda y_1 and
    2 y_2 = 2 lambda y_2 the card concluded "y_2 in {0,1}", which does not follow, and then took the
    minimum on that basis; the step is replaced by the direct inequality 6 y_1^2 + y_2^2 >= y_1^2 +
    y_2^2 with equality exactly when y_1 = 0, and the attaining vectors are exhibited. Checked the
    characteristic polynomial, both eigenspaces, and the Rayleigh quotient reduction through
    A = P D P^T with y = P^T x a unit vector. No retained published solution covers this problem.
---

::: {.problem}
Take
$$
A := \begin{pmatrix} 2 & -2 \\ -2 & 5 \end{pmatrix}.
$$
Find an orthogonal matrix $P$ for which $P^{-1}AP$ is diagonal.
Then find the minimum value of the dot products $Ax \cdot x$ as $x$ ranges through the unit vectors in $\RR^2$.
:::

::: {.solution}
This is Problem 6 of the University of Georgia graduate preliminary examination of Fall 2014 (`assets/attachments/grad_prelim_Fall14.pdf`). No published solution set is transcribed: the argument is the card's own.

What was repaired: the card's matrix $P=\begin{pmatrix}1&2\\-2&1\end{pmatrix}$ is not orthogonal, its columns having length $\sqrt5$ rather than $1$; the orthogonal matrix is $\frac{1}{\sqrt5}$ times it. And the minimisation was argued from a misreading of the Lagrange equations — "$y_{2}\in\theset{0,1}$" does not follow from $y_{2}=\lambda y_{2}$ — so the last step below replaces it by the direct comparison $6y_{1}^{2}+y_{2}^{2}\geq y_{1}^{2}+y_{2}^{2}$.

::: pf

::: {.pf-step #spectrum}
The characteristic polynomial of $A=\begin{pmatrix}2&-2\\-2&5\end{pmatrix}$ is $x^{2}-7x+6=(x-6)(x-1)$, so the eigenvalues are $6$ and $1$.

::: pf-proof
For a $2\times2$ matrix, $\chi_{A}(x)=x^{2}-(\Tr A)x+\det A$; here $\Tr A=2+5=7$ and $\det A=2\cdot5-(-2)(-2)=10-4=6$, so $\chi_{A}(x)=x^{2}-7x+6=(x-6)(x-1)$.
:::
:::

::: {.pf-step #eigenvectors}
$\begin{pmatrix}1\\-2\end{pmatrix}$ spans the eigenspace for $6$ and $\begin{pmatrix}2\\1\end{pmatrix}$ the eigenspace for $1$; both are nonzero and mutually orthogonal.

::: pf-proof
$A-6I=\begin{pmatrix}-4&-2\\-2&-1\end{pmatrix}$ has kernel spanned by $\begin{pmatrix}1\\-2\end{pmatrix}$, and $A-I=\begin{pmatrix}1&-2\\-2&4\end{pmatrix}$ has kernel spanned by $\begin{pmatrix}2\\1\end{pmatrix}$. The two are orthogonal since $A$ is symmetric and the eigenvalues are distinct, and directly: $1\cdot2+(-2)\cdot1=0$.
:::
:::

::: {.pf-step #orthogonal}
$P=\frac{1}{\sqrt5}\begin{pmatrix}1&2\\-2&1\end{pmatrix}$ is orthogonal and $P^{-1}AP=\begin{pmatrix}6&0\\0&1\end{pmatrix}$.

::: pf-proof
The columns of $P$ are the eigenvectors $v_{1}=\begin{pmatrix}1\\-2\end{pmatrix}$ and $v_{2}=\begin{pmatrix}2\\1\end{pmatrix}$, each of length $\sqrt5$, scaled to unit length; two orthonormal columns make $P$ orthogonal, that is $P^{T}=P^{-1}$. For that $P$ one has $AP=PD$ with $D=\operatorname{diag}(6,1)$, because the columns of $AP$ are $Av_{j}=\lambda_{j}v_{j}$ scaled, so $P^{-1}AP=D$. Note the scaling: the matrix $\begin{pmatrix}1&2\\-2&1\end{pmatrix}$ written without the factor $\frac{1}{\sqrt5}$ is not orthogonal, its columns having length $\sqrt5$.
:::
:::

::: {.pf-step #rayleigh}
For every unit vector $x$, $Ax\cdot x=6y_{1}^{2}+y_{2}^{2}$ where $y=P^{T}x$, and $y$ ranges over the unit vectors.

::: pf-proof
Since $A=PDP^{T}$ with $P$ orthogonal, $Ax\cdot x=x^{T}PDP^{T}x=y^{T}Dy$ with $y=P^{T}x$, and $y$ is a unit vector because $P^{T}$ preserves norms, the map $x\mapsto P^{T}x$ being a bijection of the unit circle onto itself. Expanding, $y^{T}Dy=6y_{1}^{2}+y_{2}^{2}$.
:::
:::

::: {.pf-step #minimum}
The minimum of $Ax\cdot x$ over unit vectors $x$ is $1$, attained at $x=P\begin{pmatrix}0\\1\end{pmatrix}=\frac{1}{\sqrt5}\begin{pmatrix}2\\1\end{pmatrix}$.

::: pf-proof
For a unit $y$, $6y_{1}^{2}+y_{2}^{2}\geq y_{1}^{2}+y_{2}^{2}=1$, with equality exactly when $y_{1}=0$. So the minimum is $1$, attained when $y_{1}=0$ and $y_{2}=\pm1$, that is at $x=\pm\frac{1}{\sqrt5}\begin{pmatrix}2\\1\end{pmatrix}$, which is the unit eigenvector for the eigenvalue $1$. Equivalently, the maximum $6$ is attained at the unit eigenvector for $6$, so the dot product ranges over the closed interval $[1,6]$.
:::
:::
:::

:::
