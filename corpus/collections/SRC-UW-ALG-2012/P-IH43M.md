---
schema: qual/card@1
id: P-IH43M
kind: problem
title: Values of $b$ for which $X^2=B$ has finitely many, but at least one, real $3\times3$ solutions, $B$ tridiagonal with entries $1,b$
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Matrices
  - Eigenvalues
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement read from the card in `corpus/collections/SRC-UW-ALG-2012`; no correction is claimed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Answer: $0<\abs b\le 1/\sqrt2$. For $b\ne0$ the matrix $B$ is symmetric with the three distinct
    eigenvalues $1\pm\sqrt2b$ and $1$, so any solution commutes with $B$ and is diagonal in its
    eigenbasis with entries squaring to the eigenvalues; real solutions exist exactly when all three
    eigenvalues are non-negative, and then there are $8$ of them for $\abs b<1/\sqrt2$ and $4$ at
    $\abs b=1/\sqrt2$. At $b=0$ one has $B=I$ and there are infinitely many solutions. Nothing is
    left in outline.
---

::: {.problem}
Let $M_3(\RR)$ be the $3\times3$-matrix algebra over the real numbers $\RR$.
For any $b\in\RR$, let $B\in M_3(\RR)$ be the matrix
$$
B=\begin{pmatrix}
1&b&0\\
b&1&b\\
0&b&1
\end{pmatrix}.
$$
Find the set of numbers $b$ so that the matrix equation $X^2=B$ has at least one, and only finitely many, solutions in $M_3(\RR)$.
:::

::: {.solution}

Let $b\in\RR$ and $B=\bigl(\begin{smallmatrix}1&b&0\\ b&1&b\\ 0&b&1\end{smallmatrix}\bigr)$. The answer is
$$
0<\abs b\le\frac1{\sqrt2},
$$
with $8$ solutions when $0<\abs b<1/\sqrt2$ and $4$ solutions when $\abs b=1/\sqrt2$.

::: pf

::: {.pf-step #s1}

$B$ is real symmetric, never has $0$ as an eigenvalue, and its eigenvalues are
$$
1+\sqrt2\,b,\qquad 1,\qquad 1-\sqrt2\,b .
$$
They are distinct if and only if $b\ne0$.

::: pf-proof

$B$ is symmetric, so it is orthogonally diagonalisable with real eigenvalues. It is the tridiagonal Toeplitz matrix with constant diagonal $1$ and off-diagonal $b$, whose eigenvalues for the $n\times n$ case are $1+2b\cos\frac{k\pi}{n+1}$, $k=1,\dots,n$. For $n=3$ this gives $1+2b\cos\frac{\pi}4=1+\sqrt2b$, $1+2b\cos\frac{\pi}2=1$ and $1+2b\cos\frac{3\pi}4=1-\sqrt2b$.

(Directly: expanding $\det(B-\lambda I_3)$ gives $(1-\lambda)\bigl((1-\lambda)^2-2b^2\bigr)$, with roots $1$ and $1\pm\sqrt2b$.)

The three roots coincide pairwise only when $\sqrt2b=0$, i.e. $b=0$; and no root is $0$ unless $b=\pm1/\sqrt2$, where the zero root is simple.

:::

:::

::: {.pf-step #s2}

Every solution $X$ of $X^2=B$ commutes with $B$.

::: pf-proof

$XB=X\,X^2=X^3$ and $BX=X^2\,X=X^3$, so $XB=BX$.

:::

:::

::: {.pf-step #s3}

Suppose $b\ne0$. Then there are as many solutions as there are orthonormal eigenbases-compatible diagonal forms: $X$ is diagonal in an eigenbasis of $B$, and $X^2=B$ has a real solution if and only if every eigenvalue of $B$ is $\ge0$; the number of solutions is then $2^{k}$, where $k$ is the number of positive eigenvalues.

::: pf-proof

Since $b\ne0$ the eigenvalues $\lambda_1,\lambda_2,\lambda_3$ of $B$ are distinct, so each eigenspace is one-dimensional. As $X$ commutes with $B$, it preserves every eigenspace of $B$: if $Bv=\lambda v$ then $B(Xv)=X(Bv)=\lambda(Xv)$, so $Xv$ lies in the same eigenspace, which is the line spanned by $v$. Hence, in an orthonormal eigenbasis $(v_1,v_2,v_3)$ of $B$, the matrix of $X$ is diagonal, $X=\operatorname{diag}(x_1,x_2,x_3)$.

The equation $X^2=B$ then reads $x_i^2=\lambda_i$ for each $i$. Such real $x_i$ exist exactly when every $\lambda_i\ge0$, and then each $x_i$ is determined up to sign, with $x_i=0$ forced when $\lambda_i=0$. So the number of solutions is $2^{k}$, where $k$ is the number of positive eigenvalues.

:::

:::

::: {.pf-step #s4}

$b=0$ gives infinitely many solutions; for $b\ne0$ the hypotheses hold exactly when $0<\abs b\le1/\sqrt2$.

::: pf-proof

If $b=0$ then $B=I_3$, and $X^2=I_3$ is solved by every involutive matrix, for instance by $\operatorname{diag}(1,1,-1)$ and by any orthogonal reflection, of which there are infinitely many; so there is at least one solution and infinitely many.

Let $b\ne0$. By step [](#s1){.pf-ref} the eigenvalues are $1+\sqrt2b$, $1$, $1-\sqrt2b$. All are non-negative exactly when $\sqrt2\abs b\le1$, that is $\abs b\le1/\sqrt2$. Since $b\ne0$ they are distinct, and by step [](#s3){.pf-ref} there are then finitely many solutions: for $0<\abs b<1/\sqrt2$ all three eigenvalues are positive and there are $2^3=8$ solutions; for $\abs b=1/\sqrt2$ one eigenvalue is $0$ and there are $2^2=4$ solutions.

So the set of $b$ for which $X^2=B$ has at least one and only finitely many solutions in $M_3(\RR)$ is exactly $0<\abs b\le1/\sqrt2$.

:::

:::

:::

:::
