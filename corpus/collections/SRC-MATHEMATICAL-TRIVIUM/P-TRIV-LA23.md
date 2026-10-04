---
schema: qual/card@1
id: P-TRIV-LA23
kind: problem
title: Matrices of stretching transformations of $\mathbb{R}^3$ and their eigenvectors
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 23, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider the basis $\vec { e } _ { i } , i = 1 , 2 , 3$ , in the vector space $\mathbb { R } ^ { 3 }$ In this basis, write the matrix of the transformation that

(a) stretches all directions by a factor of λ.

(b) stretches each direction along $\vec { e _ { i } }$ by a factor of $\lambda _ { i } , i = 1 , 2 , 3$

(c) stretches the direction determined by a unit vector \~n with components $n _ { x } , n _ { y } , n _ { z }$ by a factor of λ.

Find the eigenvectors of these transformations.
:::

::: {.solution}
<1>1. If every direction is stretched by the same factor $\lambda$, then the
matrix is
$$
\boxed{S=\lambda I_3}.
$$

::: {.proof}
The transformation sends every vector $v$ to
$$
Sv=\lambda v.
$$
In the basis $e_1,e_2,e_3$, this is represented by the scalar matrix
$\lambda I_3$.
:::

<1>2. For the transformation in part (a), every nonzero vector is an
eigenvector with eigenvalue $\lambda$.

::: {.proof}
By step <1>1,
$$
Sv=\lambda v
$$
for every vector $v$.
:::

<1>3. If the three basis directions are stretched by factors
$$
\lambda_1,\lambda_2,\lambda_3,
$$
then the matrix is
$$
\boxed{
S=
\begin{pmatrix}
\lambda_1&0&0\\
0&\lambda_2&0\\
0&0&\lambda_3
\end{pmatrix}.
}
$$

::: {.proof}
By hypothesis,
$$
Se_i=\lambda_i e_i,
\qquad
i=1,2,3.
$$
The $i$th column of the matrix of $S$ is therefore $\lambda_i e_i$.
:::

<1>4. In part (b), each basis vector $e_i$ is an eigenvector with eigenvalue
$\lambda_i$.

::: {.proof}
This is exactly the relation
$$
Se_i=\lambda_i e_i.
$$
If some of the $\lambda_i$ coincide, the corresponding coordinate subspace is
the full eigenspace for that common eigenvalue.
:::

<1>5. Let
$$
n=
\begin{pmatrix}
n_x\\
n_y\\
n_z
\end{pmatrix},
\qquad
\|n\|=1.
$$
Every vector decomposes as
$$
v=(n\cdot v)n+\bigl(v-(n\cdot v)n\bigr).
$$

::: {.proof}
The first term is the orthogonal projection of $v$ onto the line spanned by
$n$, and the second lies in $n^\perp$.
:::

<1>6. Stretching only the direction $n$ by a factor $\lambda$ while fixing
all perpendicular directions gives
$$
Sv
=
\lambda(n\cdot v)n
+
v-(n\cdot v)n.
$$

::: {.proof}
The component parallel to $n$ is multiplied by $\lambda$ and the component in
$n^\perp$ is unchanged.
:::

<1>7. Therefore the matrix for part (c) is
$$
\boxed{S=I_3+(\lambda-1)nn^T}.
$$

::: {.proof}
Since
$$
nn^Tv=(n\cdot v)n,
$$
step <1>6 becomes
$$
Sv
=
v+(\lambda-1)nn^Tv.
$$
:::

<1>8. Explicitly,
$$
\boxed{
S=
\begin{pmatrix}
1+(\lambda-1)n_x^2&(\lambda-1)n_xn_y&(\lambda-1)n_xn_z\\
(\lambda-1)n_yn_x&1+(\lambda-1)n_y^2&(\lambda-1)n_yn_z\\
(\lambda-1)n_zn_x&(\lambda-1)n_zn_y&1+(\lambda-1)n_z^2
\end{pmatrix}.
}
$$

::: {.proof}
Expand the outer product $nn^T$ in step <1>7.
:::

<1>9. In part (c), $n$ is an eigenvector with eigenvalue $\lambda$.

::: {.proof}
Since $n^Tn=1$,
$$
Sn
=
n+(\lambda-1)n(n^Tn)
=
\lambda n.
$$
:::

<1>10. Every nonzero vector in $n^\perp$ is an eigenvector with eigenvalue
$1$.

::: {.proof}
If $n\cdot v=0$, then
$$
nn^Tv=0.
$$
Hence step <1>7 gives
$$
Sv=v.
$$
:::

<1>11. Q.E.D.

::: {.proof}
Steps <1>1--<1>2 solve part (a), steps <1>3--<1>4 solve part (b), and steps
<1>5--<1>10 solve part (c) and identify all eigendirections.
:::
:::
