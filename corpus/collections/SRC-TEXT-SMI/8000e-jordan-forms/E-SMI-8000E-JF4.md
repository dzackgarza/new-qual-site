---
schema: qual/card@1
id: E-SMI-8000E-JF4
kind: problem
title: Change-of-basis matrices into Jordan form
classification:
  areas:
  - algebra
  topics:
  - Modules over PIDs
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared all five matrices with the PDF text layer and local 8000e extraction, Jordan forms exercise 4."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Constructed explicit eigenvector and generalized-eigenvector bases for all five matrices and checked each Q is invertible and satisfies Q^{-1}AQ equal to the stated upper Jordan form."
---

::: {.exercise}
Find matrices $Q$ which put each of the following matrices in upper (or lower) Jordan form over $\CC$:

$$
\text{(i)} \quad A = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}
$$

$$
\text{(ii)} \quad B = \begin{bmatrix} 3 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 1 & 2 \end{bmatrix}
$$

$$
\text{(iii)} \quad C = \begin{bmatrix} 1 & -1 & 4 \\ 3 & 2 & -1 \\ 2 & 1 & -1 \end{bmatrix}
$$

$$
\text{(iv)} \quad D = \begin{bmatrix} 1 & -2 & -1 & 0 \\ 1 & 0 & -3 & 0 \\ -1 & -2 & 1 & 0 \\ 1 & 2 & 1 & 2 \end{bmatrix}
$$

$$
\text{(v)} \quad E = \begin{bmatrix} 5 & -1 & -3 & 2 & -5 \\ 0 & 2 & 0 & 0 & 0 \\ 1 & 0 & 1 & 1 & -2 \\ 0 & -1 & 0 & 3 & 1 \\ 1 & -1 & -1 & 1 & 1 \end{bmatrix}
$$
:::


::: solution
In each part, the columns of $Q$ are chosen as Jordan chains. We verify the
chain equations, which are equivalent to
$$
AQ=QJ
$$
and hence to $Q^{-1}AQ=J$ once $Q$ is invertible.

<1>1. Matrix $A$.
::: proof
Let $i^2=-1$ and take
$$
Q_A=
\begin{pmatrix}
1&1\\
-i&i
\end{pmatrix}.
$$
Its columns
$$
v_i=(1,-i)^t,
\qquad
v_{-i}=(1,i)^t
$$
satisfy
$$
Av_i=i v_i,
\qquad
Av_{-i}=-i v_{-i}.
$$
Also
$$
\det Q_A=2i\ne0.
$$
Therefore
$$
\boxed{
Q_A^{-1}AQ_A=
\begin{pmatrix}i&0\\0&-i\end{pmatrix}.}
$$
:::

<1>2. Matrix $B$.
::: proof
Set
$$
v_3=(1,0,0)^t,
\qquad
w_3=(0,1,1)^t,
\qquad
v_1=(1,-2,2)^t.
$$
A direct multiplication gives
$$
Bv_3=3v_3,
\qquad
Bw_3=3w_3+v_3,
\qquad
Bv_1=v_1.
$$
Thus with
$$
Q_B=
\begin{pmatrix}
1&0&1\\
0&1&-2\\
0&1&2
\end{pmatrix}
$$
one has $\det Q_B=4$, and
$$
\boxed{
Q_B^{-1}BQ_B=
\begin{pmatrix}
3&1&0\\
0&3&0\\
0&0&1
\end{pmatrix}.}
$$
:::

<1>3. Matrix $C$.
::: proof
Choose eigenvectors
$$
v_{-2}=(1,-1,-1)^t,
\qquad
v_1=(1,-4,-1)^t,
\qquad
v_3=(1,2,1)^t.
$$
They satisfy
$$
Cv_{-2}=-2v_{-2},
\qquad
Cv_1=v_1,
\qquad
Cv_3=3v_3.
$$
Hence, with
$$
Q_C=
\begin{pmatrix}
1&1&1\\
-1&-4&2\\
-1&-1&1
\end{pmatrix},
$$
we have
$$
\det Q_C=-6\ne0
$$
and
$$
\boxed{
Q_C^{-1}CQ_C=
\begin{pmatrix}
-2&0&0\\
0&1&0\\
0&0&3
\end{pmatrix}.}
$$
:::

<1>4. Matrix $D$.
::: proof
Let
$$
v=(-1,1,-1,1)^t,
\qquad
w=(1,0,0,0)^t,
$$
$$
u=(0,0,0,1)^t,
\qquad
z=(1,1,1,-1)^t.
$$
Then
$$
Dv=2v,
\qquad
Dw=2w+v,
$$
$$
Du=2u,
\qquad
Dz=-2z.
$$
Thus $(v,w)$ is a length-$2$ Jordan chain at eigenvalue $2$, while $u$ and
$z$ are eigenvectors. Put
$$
Q_D=
\begin{pmatrix}
-1&1&0&1\\
1&0&0&1\\
-1&0&0&1\\
1&0&1&-1
\end{pmatrix}.
$$
Since
$$
\det Q_D=2\ne0,
$$
we obtain
$$
\boxed{
Q_D^{-1}DQ_D=
\begin{pmatrix}
2&1&0&0\\
0&2&0&0\\
0&0&2&0\\
0&0&0&-2
\end{pmatrix}.}
$$
:::

<1>5. Matrix $E$.
::: proof
At eigenvalue $3$, take
$$
v_3=(1,0,0,-1,0)^t,
\qquad
w_3=(-2,0,0,0,-1)^t.
$$
At eigenvalue $2$, take
$$
v_2=(1,0,1,0,0)^t,
\qquad
w_2=(0,1,0,1,0)^t,
$$
and
$$
u_2=(0,1,-2,0,1)^t.
$$
Direct multiplication gives
$$
Ev_3=3v_3,
\qquad
Ew_3=3w_3+v_3,
$$
$$
Ev_2=2v_2,
\qquad
Ew_2=2w_2+v_2,
\qquad
Eu_2=2u_2.
$$
Therefore set
$$
Q_E=
\begin{pmatrix}
1&-2&1&0&0\\
0&0&0&1&1\\
0&0&1&0&-2\\
-1&0&0&1&0\\
0&-1&0&0&1
\end{pmatrix}.
$$
Its determinant is
$$
\det Q_E=1,
$$
so it is invertible, and
$$
\boxed{
Q_E^{-1}EQ_E=
\begin{pmatrix}
3&1&0&0&0\\
0&3&0&0&0\\
0&0&2&1&0\\
0&0&0&2&0\\
0&0&0&0&2
\end{pmatrix}.}
$$
:::
:::
