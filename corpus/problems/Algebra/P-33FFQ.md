---
schema: qual/card@1
id: P-33FFQ
kind: problem
title: Jordan form of the $n\times n$ all-ones matrix over $\CC$
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Eigenvalues and Eigenvectors
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Let $n$ be a positive integer and let $B$ denote the $n\times n$ matrix over $\Bbb C$ such that every entry is 1. Find the Jordan normal form of $B$.
:::


::: {.solution}
Let
\[
\mathbf 1=(1,\ldots,1)^t\in\CC^n.
\]

<1>1. The image of $B$ is the line $\CC\mathbf 1$.
::: {.proof}
For $v=(v_1,\ldots,v_n)^t$,
\[
Bv=\left(\sum_{i=1}^n v_i\right)\mathbf 1.
\]
Hence every image vector is a multiple of $\mathbf1$, and $B\mathbf1=n\mathbf1\ne0$, so the image is exactly that line.
:::

<1>2. The eigenvalues are $n$ with multiplicity $1$ and $0$ with multiplicity $n-1$.
::: {.proof}
By <1>1,
\[
B\mathbf1=n\mathbf1,
\]
so $n$ is an eigenvalue. Also
\[
\ker B=\left\{v:\sum_i v_i=0\right\}
\]
has dimension $n-1$, so $0$ is an eigenvalue with geometric multiplicity $n-1$.
:::

<1>3. The matrix $B$ is diagonalizable.
::: {.proof}
A direct multiplication gives
\[
B^2=nB.
\]
Thus the minimal polynomial divides
\[
x(x-n).
\]
Since $n\ne0$ in $\CC$, these two roots are distinct. Therefore the minimal polynomial is squarefree, so $B$ is diagonalizable.
:::

<1>4. Its Jordan normal form is
\[
J=\operatorname{diag}(n,0,\ldots,0).
\]
::: {.proof}
By <1>2 the eigenvalue multiplicities are $1$ and $n-1$, and by <1>3 every Jordan block has size $1$. Hence the displayed diagonal matrix is the Jordan form.
:::
:::
