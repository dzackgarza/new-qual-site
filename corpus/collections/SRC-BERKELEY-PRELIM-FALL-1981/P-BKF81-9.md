---
schema: qual/card@1
id: P-BKF81-9
kind: problem
title: Trace and determinant of $X\mapsto AXB$
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Computed the trace from diagonal coefficients of X↦AXB and factored the determinant through left and right multiplication on the two columns and rows."
---

::: problem
Let $M_{2\times2}(\mathbb R)$ be the space of real $2\times2$ matrices and
\[
A=\begin{pmatrix}1&2\\-1&3\end{pmatrix},\qquad
B=\begin{pmatrix}2&1\\0&4\end{pmatrix}.
\]
Define $L(X)=AXB$. Compute the trace and determinant of $L$.
:::

::: solution
Write
$$
L=L_A\circ R_B,
$$
where
$$
L_A(X)=AX,
\qquad
R_B(X)=XB.
$$

<1>1. Compute the trace of $L$.
::: proof
Let $E_{ij}$ be the standard basis of $M_{2\times2}(\mathbb R)$. For a
general matrix $X=(x_{ij})$,
$$
(AXB)_{ij}=\sum_{k,\ell}a_{ik}x_{k\ell}b_{\ell j}.
$$
The coefficient of $x_{ij}$ in the same $(i,j)$ output coordinate is
$$
a_{ii}b_{jj}.
$$
Therefore the trace of the linear transformation is
$$
\operatorname{tr}L
=\sum_{i,j}a_{ii}b_{jj}
=(\operatorname{tr}A)(\operatorname{tr}B).
$$
Here
$$
\operatorname{tr}A=1+3=4,
\qquad
\operatorname{tr}B=2+4=6,
$$
so
$$
\boxed{\operatorname{tr}L=24.}
$$
:::

<1>2. Compute the determinant of left multiplication by $A$.
::: proof
Left multiplication acts independently on the two columns of $X$, applying
$A$ to each column. Hence, in a basis grouped by columns, the matrix of
$L_A$ is block diagonal with two copies of $A$. Thus
$$
\det L_A=(\det A)^2.
$$
Since
$$
\det A=1\cdot3-2(-1)=5,
$$
we get
$$
\det L_A=25.
$$
:::

<1>3. Compute the determinant of right multiplication by $B$ and conclude.
::: proof
Right multiplication acts independently on the two rows of $X$. On each row
it has determinant $\det B$, so
$$
\det R_B=(\det B)^2.
$$
Here
$$
\det B=2\cdot4=8,
$$
and therefore
$$
\det R_B=64.
$$

Since $L=L_A\circ R_B$,
$$
\det L
=(\det L_A)(\det R_B)
=25\cdot64
=1600.
$$
Hence
$$
\boxed{\det L=1600.}
$$
:::
:::
