---
schema: qual/card@1
id: P-HM21B18-FIN-06
kind: problem
title: Barycentric-refinement eigenvectors and a closed discrete dynamical system
classification: {areas: [applied-algebra], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Let $\vec x=(v,e,f)^T$ record the numbers of vertices, edges, and faces of a polyhedron. Under barycentric refinement suppose
$$
A=\begin{pmatrix}1&1&1\\0&2&6\\0&0&6\end{pmatrix}
$$
acts on $\vec x$.

(a) Verify that
$$
v_1=\begin{pmatrix}1\\0\\0\end{pmatrix},\quad
v_2=\begin{pmatrix}1\\1\\0\end{pmatrix},\quad
v_3=\begin{pmatrix}1\\3\\2\end{pmatrix}
$$
are eigenvectors and find their eigenvalues.

(b) Find a closed form for $\vec x(t+1)=A\vec x(t)$ with initial condition
$$
\vec x(0)=\begin{pmatrix}7\\12\\6\end{pmatrix}.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The vectors $v_1,v_2,v_3$ have eigenvalues $1,2,6$, respectively.


::: pf-proof

Direct multiplication gives
$$
Av_1
=
\begin{pmatrix}1\\0\\0\end{pmatrix}
=v_1,
$$
$$
Av_2
=
\begin{pmatrix}2\\2\\0\end{pmatrix}
=2v_2,
$$
and
$$
Av_3
=
\begin{pmatrix}6\\18\\12\end{pmatrix}
=6v_3.
$$
Thus the corresponding eigenvalues are $1,2,6$.

:::

:::

::: {.pf-step #s1-2}

The initial vector decomposes as
$$
\vec x(0)=v_1+3v_2+3v_3.
$$


::: pf-proof

Indeed,
$$
v_1+3v_2+3v_3
=
\begin{pmatrix}1\\0\\0\end{pmatrix}
+3\begin{pmatrix}1\\1\\0\end{pmatrix}
+3\begin{pmatrix}1\\3\\2\end{pmatrix}
=
\begin{pmatrix}7\\12\\6\end{pmatrix}.
$$

:::

:::

::: {.pf-step #s1-3}

For every integer $t\geq0$,
$$
\vec x(t)=v_1+3\cdot2^t v_2+3\cdot6^t v_3.
$$


::: pf-proof

The recurrence gives $\vec x(t)=A^t\vec x(0)$. Applying $A^t$ to the
decomposition in step [](#s1-2){.pf-ref} and using the eigenvalue equations from
step [](#s1-1){.pf-ref} yields
$$
A^t v_1=1^t v_1,\qquad
A^t v_2=2^t v_2,\qquad
A^t v_3=6^t v_3,
$$
which proves the displayed formula.

:::

:::

::: {.pf-step #s1-4}

Equivalently, the closed form is
$$
\boxed{
\vec x(t)=
\begin{pmatrix}
1+3\cdot2^t+3\cdot6^t\\
3\cdot2^t+9\cdot6^t\\
6\cdot6^t
\end{pmatrix},
\qquad t\geq0.}
$$


::: pf-proof

Expand the expression in step [](#s1-3){.pf-ref} using the coordinates of
$v_1,v_2,v_3$.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} answers part (a), and step [](#s1-4){.pf-ref} answers part (b).

:::

:::

:::
