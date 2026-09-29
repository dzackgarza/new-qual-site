---
schema: qual/card@1
id: P-BKF15-6B
kind: problem
title: Simultaneous diagonalization of circulant matrices
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2015 solution packet: the common
    eigenvectors are the discrete Fourier basis indexed by nth roots of
    unity, and the eigenvalues are the Fourier evaluations of the periodic
    coefficient sequence.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the row-by-row eigenvector calculation, Hermitian
    orthonormality by the geometric-series sum, and independence of the
    eigenbasis from the coefficients c_k.
---

::: {.problem}
Given a positive integer $n$, let $\ldots,c_{-1},c_0,c_1,\ldots$ be a sequence of real numbers with period $n$, that is, $c_{k+n}=c_k$ for all $k\in\mathbb Z$.
Let $C$ be the $n\times n$ matrix defined by $c_{ij}=c_{j-i}$.
Prove that all matrices of this form (for $n$ fixed) have a common Hermitian-orthonormal basis of complex eigenvectors, find these eigenvectors, and the corresponding eigenvalues.
:::

::: {.solution}
For
$$
k=0,1,\ldots,n-1,
$$
put
$$
\zeta_k\coloneqq\exp\left(\frac{2\pi i k}{n}\right)
$$
and
$$
v_k
\coloneqq
\frac1{\sqrt n}
\begin{pmatrix}
1\\
\zeta_k\\
\zeta_k^2\\
\vdots\\
\zeta_k^{n-1}
\end{pmatrix}
\in\CC^n.
$$

::: pf

::: {.pf-step #s1}

For every $k$,
$$
Cv_k
=
\left(
\sum_{m=0}^{n-1}c_m\zeta_k^m
\right)v_k.
$$

::: pf-proof

Number rows and columns by
$$
0,1,\ldots,n-1
$$
instead of $1,\ldots,n$. Then
$$
C_{ij}=c_{j-i},
$$
where the subscript on $c$ is read modulo $n$.

The $j$th coordinate of the unnormalized vector underlying $v_k$ is
$\zeta_k^j$. Hence its $i$th image coordinate is
$$
\sum_{j=0}^{n-1}c_{j-i}\zeta_k^j.
$$
As $j$ runs through the residue classes modulo $n$, so does
$$
m=j-i.
$$
Since $\zeta_k^n=1$,
$$
\begin{aligned}
\sum_{j=0}^{n-1}c_{j-i}\zeta_k^j
&=
\sum_{m=0}^{n-1}c_m\zeta_k^{m+i}\\
&=
\zeta_k^i
\sum_{m=0}^{n-1}c_m\zeta_k^m.
\end{aligned}
$$
Thus the vector is multiplied by the displayed scalar. The
normalizing factor $1/\sqrt n$ does not affect the calculation.

:::

:::

::: {.pf-step #s2}

The corresponding eigenvalue of $C$ on $v_k$ is
$$
\boxed{
\lambda_k(C)
=
\sum_{m=0}^{n-1}c_m
\exp\left(\frac{2\pi i km}{n}\right).
}
$$

::: pf-proof

This is the scalar obtained in step [](#s1){.pf-ref} after substituting the
definition of $\zeta_k$.

:::

:::

::: {.pf-step #s3}

Every vector $v_k$ has Hermitian norm $1$.

::: pf-proof

Since $\abs{\zeta_k}=1$,
$$
\begin{aligned}
\norm{v_k}^2
&=
\frac1n
\sum_{j=0}^{n-1}\abs{\zeta_k^j}^2\\
&=
\frac1n\sum_{j=0}^{n-1}1\\
&=
1.
\end{aligned}
$$

:::

:::

::: {.pf-step #s4}

If $k\ne\ell$, then
$$
\inner{v_k}{v_\ell}=0.
$$

::: pf-proof

Using the standard Hermitian inner product,
$$
\inner{v_k}{v_\ell}
=
\frac1n
\sum_{j=0}^{n-1}
\zeta_k^j\overline{\zeta_\ell^j}
=
\frac1n
\sum_{j=0}^{n-1}
\left(
\zeta_k\overline{\zeta_\ell}
\right)^j.
$$
Because $k\ne\ell$, the number
$$
q\coloneqq\zeta_k\overline{\zeta_\ell}
$$
is a nontrivial $n$th root of unity. Therefore
$$
\sum_{j=0}^{n-1}q^j
=
\frac{1-q^n}{1-q}
=
0.
$$

:::

:::

::: {.pf-step #s5}

The vectors
$$
\boxed{v_0,v_1,\ldots,v_{n-1}}
$$
form a Hermitian-orthonormal basis of $\CC^n$.

::: pf-proof

By steps [](#s3){.pf-ref} and [](#s4){.pf-ref}, the $n$ vectors are orthonormal. Any
orthonormal family is linearly independent, and an independent family
of $n$ vectors in the $n$-dimensional space $\CC^n$ is a basis.

:::

:::

::: {.pf-step #s6}

This basis is a common eigenbasis for every matrix of the form
in the problem.

::: pf-proof

The vectors $v_k$ depend only on $n$, not on the coefficients
$c_0,\ldots,c_{n-1}$. Step [](#s1){.pf-ref} shows that each $v_k$ is an
eigenvector for every such matrix $C$, while step [](#s5){.pf-ref} shows that the
vectors form a Hermitian-orthonormal basis.

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} give the requested common eigenvectors,
their eigenvalues, and their Hermitian-orthonormality.

:::

:::

:::
