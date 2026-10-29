---
schema: qual/card@1
id: P-HM21B18-FIN-09
kind: problem
title: Determinants from permutation, block, low-rank, and circulant structure
classification: {areas: [applied-algebra], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Compute the determinants of the following matrices, giving computational details.

(a)
$$
A=\begin{pmatrix}
1&0&0&0&0\\
0&0&0&0&1\\
0&0&0&1&0\\
0&0&1&0&0\\
0&1&0&0&0
\end{pmatrix}.
$$

(b)
$$
B=\begin{pmatrix}
0&0&3&1&0\\
0&2&1&0&0\\
0&0&0&4&1\\
0&0&0&0&5\\
1&1&0&0&0
\end{pmatrix}.
$$

(c)
$$
C=\begin{pmatrix}
1&2&3&8&8\\
4&5&0&8&8\\
6&0&0&8&8\\
0&0&0&2&1\\
0&0&0&1&3
\end{pmatrix}.
$$

(d)
$$
D=\begin{pmatrix}
11&2&3&2&1\\
1&12&3&2&1\\
1&2&13&2&1\\
1&2&3&12&1\\
1&2&3&2&11
\end{pmatrix}.
$$

(e) Compute the determinant of
$$
E=2Q+5Q^{-1}+7I
=\begin{pmatrix}
7&2&0&0&5\\
5&7&2&0&0\\
0&5&7&2&0\\
0&0&5&7&2\\
2&0&0&5&7
\end{pmatrix},
$$
and you may leave the answer in terms of eigenvalues of the basic circulant matrix $Q$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

$\det A=1$.


::: pf-proof

The matrix $A$ is the permutation matrix for
$$
(1,2,3,4,5)\longmapsto(1,5,4,3,2).
$$
This permutation is $(2\,5)(3\,4)$, a product of two transpositions.
Therefore its sign, and hence the determinant of its permutation matrix,
is $(-1)^2=1$.

:::

:::

::: pf-step

$\det B=-120$.


::: pf-proof

Expand along the first column. Its only nonzero entry is the $1$ in
position $(5,1)$, whose cofactor sign is $(-1)^{5+1}=1$. Hence
$$
\det B
=
\det
\begin{pmatrix}
0&3&1&0\\
2&1&0&0\\
0&0&4&1\\
0&0&0&5
\end{pmatrix}.
$$
This matrix is block upper triangular, so
$$
\det B
=
\det\begin{pmatrix}0&3\\2&1\end{pmatrix}
\det\begin{pmatrix}4&1\\0&5\end{pmatrix}
=(-6)(20)=-120.
$$

:::

:::

::: pf-step

$\det C=-450$.


::: pf-proof

The matrix $C$ is block upper triangular with diagonal blocks
$$
C_1=
\begin{pmatrix}
1&2&3\\
4&5&0\\
6&0&0
\end{pmatrix},
\qquad
C_2=
\begin{pmatrix}
2&1\\
1&3
\end{pmatrix}.
$$
Thus $\det C=\det C_1\det C_2$. Expanding $\det C_1$ along its third
column gives
$$
\det C_1
=3\det\begin{pmatrix}4&5\\6&0\end{pmatrix}
=3(-30)=-90,
$$
while $\det C_2=6-1=5$. Therefore
$$
\det C=(-90)(5)=-450.
$$

:::

:::

::: pf-step

$\det D=190000$.


::: pf-proof

Let
$$
u=(1,1,1,1,1)^T,
\qquad
v=(1,2,3,2,1)^T.
$$
Then
$$
D=10I+uv^T.
$$
The rank-one matrix $uv^T$ sends $u$ to
$$
uv^Tu=(v^Tu)u=9u,
$$
and it vanishes on the four-dimensional subspace $v^\perp$. Hence its
eigenvalues are $9,0,0,0,0$. Therefore the eigenvalues of $D$ are
$19,10,10,10,10$, and
$$
\det D=19\cdot10^4=190000.
$$

:::

:::

::: {.pf-step #s1-5}

If $\zeta_k=e^{2\pi i k/5}$ for $k=0,\ldots,4$, then
$$
\det E
=\prod_{k=0}^4
\left(7+2\zeta_k+5\zeta_k^{-1}\right)
=6314.
$$


::: pf-proof

The cyclic shift $Q$ has eigenvalues $\zeta_k$, so $Q^{-1}$ has
eigenvalues $\zeta_k^{-1}$. Thus $E=2Q+5Q^{-1}+7I$ has eigenvalues
$$
\mu_k=7+2\zeta_k+5\zeta_k^{-1}.
$$
Therefore $\det E=\prod_k\mu_k$. Since
$$
\mu_k
=\zeta_k^{-1}(2\zeta_k^2+7\zeta_k+5)
=\zeta_k^{-1}(2\zeta_k+5)(\zeta_k+1)
$$
and $\prod_k\zeta_k=1$, it remains to compute the other two products.
From $x^5-1=\prod_k(x-\zeta_k)$,
$$
\prod_{k=0}^4(1+\zeta_k)=2
$$
and
$$
\prod_{k=0}^4(2\zeta_k+5)
=2^5\left(\left(\frac52\right)^5+1\right)
=3157.
$$
Hence
$$
\det E=2\cdot3157=6314.
$$

:::

:::

::: {.pf-step #s1-6}

The five requested determinants are
$$
\boxed{
\det A=1,\qquad
\det B=-120,\qquad
\det C=-450,\qquad
\det D=190000,\qquad
\det E=6314.}
$$


::: pf-proof

These are the results of steps [](#s1-1){.pf-ref} through [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} records all five determinants.

:::

:::

:::
