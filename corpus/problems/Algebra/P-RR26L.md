---
schema: qual/card@1
id: P-RR26L
kind: problem
title: Self-adjoint operators have real eigenvalues and are unitarily diagonalizable,
  and Schur's theorem
classification:
  areas:
  - algebra
  topics:
  - Eigenvalues and Eigenvectors
  - Diagonalization
  - Inner Product Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The problem block held a worked argument (real eigenvalues, Schur triangularization, an induction proof of Schur) instead of a statement; it is replaced by the statement that argument answers, and the argument is merged into the structured solution.'
---

::: {.problem}
Let $V$ be a finite-dimensional complex inner product space and let $A\colon V\to V$ be a linear operator with $A^*=A$.

(a) Show that every eigenvalue of $A$ is real.

(b) Prove Schur's theorem: every linear operator on $V$ has an upper-triangular matrix with respect to some orthonormal basis of $V$.

(c) Show that $A$ is unitarily diagonalizable: $V$ has an orthonormal basis of eigenvectors of $A$.
:::

::: {.solution}

::: pf

::: pf-step

(a) Every eigenvalue of $A$ is real.

::: pf-proof

Let $A\vector v=\lambda\vector v$ with $\vector v\neq 0$. Then
$$
\lambda\norm{\vector v}^2=\inner{A\vector v}{\vector v}=\inner{\vector v}{A^*\vector v}=\inner{\vector v}{A\vector v}=\overline\lambda\norm{\vector v}^2 .
$$
Since $\norm{\vector v}\neq 0$, $\lambda=\overline\lambda$, so $\lambda\in\RR$.

:::

:::

::: {.pf-step #schur}

(b) Every linear operator $B$ on $V$ has an upper-triangular matrix in some orthonormal basis of $V$.

::: pf-proof

We argue by induction on $n=\dim_\CC V$; the case $n\le 1$ is trivial.

::: pf-step

$B^*$ has an eigenvector $\vector v_1$ with $\norm{\vector v_1}=1$.

::: pf-proof

The characteristic polynomial of $B^*$ has a root $\mu\in\CC$ by the fundamental theorem of algebra, and an eigenvector for $\mu$ can be normalized.

:::

:::

::: {.pf-step #invariant}

The subspace $W\coloneqq\vector v_1^{\perp}$ satisfies $B(W)\subseteq W$ and $\dim W=n-1$.

::: pf-proof

Let $B^*\vector v_1=\mu\vector v_1$ and $\vector w\in W$. Then
$$
\inner{\vector v_1}{B\vector w}=\inner{B^*\vector v_1}{\vector w}=\inner{\mu\vector v_1}{\vector w}=\overline\mu\inner{\vector v_1}{\vector w}=0 ,
$$
so $B\vector w\in W$. Since $V=\CC\vector v_1\oplus W$, $\dim W=n-1$.

:::

:::

::: pf-qed

By the inductive hypothesis applied to $B\restrict_W$, there is an orthonormal basis $\mathcal B$ of $W$ in which $B\restrict_W$ has an upper-triangular matrix $\mathbf A'$. Let $\mathcal C$ be $\mathcal B$ followed by $\vector v_1$; it is an orthonormal basis of $V$. By step [](#invariant){.pf-ref}, the first $n-1$ columns of $[B]_{\mathcal C}$ have no $\vector v_1$-component, so
$$
[B]_{\mathcal C}=\begin{pmatrix}\mathbf A' & \vector u\\ 0 & c\end{pmatrix}
$$
for a column $\vector u$ and a scalar $c$ that record $B\vector v_1$. This matrix is upper triangular because $\mathbf A'$ is. Placing $\vector v_1$ first instead would give a lower-triangular matrix.

:::

:::

:::

::: pf-qed

(c) By step [](#schur){.pf-ref}, there is a unitary $U$ such that $T\coloneqq U^*AU$ is upper triangular. Then
$$
T^*=U^*A^*U=U^*AU=T .
$$
Upper triangularity gives $T_{ij}=0$ for $i>j$, and then $T_{ij}=\overline{T_{ji}}=0$ for $i<j$. Thus $T$ is diagonal, $A=UTU^*$, and the columns of $U$ form an orthonormal basis of eigenvectors of $A$.

:::

:::

:::
