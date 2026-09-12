---
schema: qual/card@1
id: P-52WSU
kind: problem
title: Toeplitz operator
classification:
  areas:
  - algebra
  topics:
  - Functional Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
What is a Toeplitz operator? Define the Hardy space $H^2(\mathbb{T})$, the Toeplitz operator $T_\varphi$ associated with a symbol $\varphi \in L^\infty(\mathbb{T})$, and describe its matrix representation.
:::

::: solution
Let $\mathbb T=\{z\in\mathbb C:|z|=1\}$ with normalized Lebesgue measure. The Hardy space is
\[
H^2(\mathbb T)
=
\left\{f\in L^2(\mathbb T):\widehat f(n)=0\text{ for }n<0\right\}
=
\overline{\operatorname{span}}\{1,z,z^2,\ldots\}.
\]
Let
\[
P_+:L^2(\mathbb T)\to H^2(\mathbb T)
\]
be the orthogonal (Szegő) projection.

For $\varphi\in L^\infty(\mathbb T)$, multiplication by $\varphi$ is bounded on $L^2$, and the Toeplitz operator with symbol $\varphi$ is
\[
T_\varphi=P_+M_\varphi|_{H^2},
\qquad
T_\varphi f=P_+(\varphi f).
\]
In particular,
\[
\|T_\varphi\|\le \|\varphi\|_\infty.
\]

Write the Fourier coefficients of $\varphi$ as
\[
a_k=\widehat\varphi(k).
\]
For the orthonormal basis $e_j(z)=z^j$, $j\ge0$,
\[
\langle T_\varphi e_j,e_i\rangle
=
\langle \varphi z^j,z^i\rangle
=a_{i-j}.
\]
Thus the matrix is the semi-infinite Toeplitz matrix
\[
[T_\varphi]=(a_{i-j})_{i,j\ge0}
=
\begin{pmatrix}
a_0&a_{-1}&a_{-2}&\cdots\\
a_1&a_0&a_{-1}&\cdots\\
a_2&a_1&a_0&\cdots\\
\vdots&\vdots&\vdots&\ddots
\end{pmatrix},
\]
so its entries are constant along diagonals.

Also $T_\varphi^*=T_{\overline\varphi}$, and for $\varphi(z)=z$, $T_z$ is the unilateral shift. The Brown--Halmos characterization says that a bounded operator $T$ on $H^2$ is Toeplitz exactly when
\[
S^*TS=T,
\]
where $S=T_z$.
:::
