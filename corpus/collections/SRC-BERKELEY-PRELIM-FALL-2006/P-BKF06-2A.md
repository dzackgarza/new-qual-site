---
schema: qual/card@1
id: P-BKF06-2A
kind: problem
title: Exponential of a $2\times2$ integer matrix with eigenvalues $1$ and $2$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 2A of the retained Berkeley Fall 2006 preliminary-exam solution packet f06solution.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained diagonalization. The eigenvectors
    (2,1) and (1,1), the change-of-basis inverse, and the final matrix product
    all reproduce the source value.
---

::: {.problem}
Let
\[
A=\begin{pmatrix}3&-2\\1&0\end{pmatrix}.
\]
Compute
\[
e^A:=\sum_{n=0}^{\infty}\frac{A^n}{n!}.
\]
:::

::: {.solution}
<1>1. The vectors
$$
v_2=
\begin{pmatrix}
2\\
1
\end{pmatrix},
\qquad
v_1=
\begin{pmatrix}
1\\
1
\end{pmatrix}
$$
are eigenvectors of $A$ with eigenvalues $2$ and $1$, respectively.

::: {.proof}
Direct multiplication gives
$$
A v_2
=
\begin{pmatrix}
3&-2\\
1&0
\end{pmatrix}
\begin{pmatrix}
2\\
1
\end{pmatrix}
=
\begin{pmatrix}
4\\
2
\end{pmatrix}
=
2v_2,
$$
and
$$
A v_1
=
\begin{pmatrix}
3&-2\\
1&0
\end{pmatrix}
\begin{pmatrix}
1\\
1
\end{pmatrix}
=
\begin{pmatrix}
1\\
1
\end{pmatrix}
=
v_1.
$$
:::

<1>2. With
$$
C=
\begin{pmatrix}
2&1\\
1&1
\end{pmatrix},
\qquad
D=
\begin{pmatrix}
2&0\\
0&1
\end{pmatrix},
$$
one has
$$
A=CDC^{-1},
\qquad
C^{-1}
=
\begin{pmatrix}
1&-1\\
-1&2
\end{pmatrix}.
$$

::: {.proof}
The columns of $C$ are the eigenvectors from step <1>1, so
$$
AC=CD.
$$
Also
$$
\det C=2\cdot1-1\cdot1=1,
$$
which gives the displayed inverse. Multiplying $AC=CD$ on the right
by $C^{-1}$ yields $A=CDC^{-1}$.
:::

<1>3. The matrix exponential satisfies
$$
e^A=Ce^D C^{-1}.
$$

::: {.proof}
From step <1>2,
$$
A^n=CD^nC^{-1}
$$
for every $n\ge0$. Therefore the absolutely convergent matrix power
series gives
$$
\begin{aligned}
e^A
&=
\sum_{n=0}^\infty\frac{A^n}{n!}
\\
&=
C\left(\sum_{n=0}^\infty\frac{D^n}{n!}\right)C^{-1}
\\
&=
Ce^D C^{-1}.
\end{aligned}
$$
:::

<1>4. Hence
$$
\boxed{
e^A=
\begin{pmatrix}
2e^2-e&-2e^2+2e\\
e^2-e&-e^2+2e
\end{pmatrix}
}.
$$

::: {.proof}
Since $D$ is diagonal,
$$
e^D=
\begin{pmatrix}
e^2&0\\
0&e
\end{pmatrix}.
$$
Using steps <1>2 and <1>3,
$$
\begin{aligned}
e^A
&=
\begin{pmatrix}
2&1\\
1&1
\end{pmatrix}
\begin{pmatrix}
e^2&0\\
0&e
\end{pmatrix}
\begin{pmatrix}
1&-1\\
-1&2
\end{pmatrix}
\\
&=
\begin{pmatrix}
2e^2&e\\
e^2&e
\end{pmatrix}
\begin{pmatrix}
1&-1\\
-1&2
\end{pmatrix}
\\
&=
\begin{pmatrix}
2e^2-e&-2e^2+2e\\
e^2-e&-e^2+2e
\end{pmatrix}.
\end{aligned}
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the required matrix exponential.
:::
:::
