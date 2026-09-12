---
schema: qual/card@1
id: E-HAT-2.2-7
kind: problem
title: Induced map on local homology of invertible linear transformation is $\pm 1$ according to sign of determinant
classification:
  areas:
  - topology
  topics:
  - Degree
  - Local Homology
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 7; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete degree/cellular proof checked.
---

For an invertible linear transformation $f: \mathbb{R}^n \to \mathbb{R}^n$ show that the induced map on $H_n(\mathbb{R}^n, \mathbb{R}^n - \{0\}) \approx \tilde{H}_{n-1}(\mathbb{R}^n - \{0\}) \approx \mathbb{Z}$ is $\mathbb{1}$ or $-\mathbb{1}$ according to whether the determinant of $f$ is positive or negative.
[Use Gaussian elimination to show that the matrix of $f$ can be joined by a path of invertible matrices to a diagonal matrix with $\pm 1$'s on the diagonal.]

::: {.solution}
Let $f:\mathbb R^n\to\mathbb R^n$ be invertible. The induced automorphism of
\[
H_n(\mathbb R^n,\mathbb R^n-\{0\})\cong\mathbb Z
\]
depends only on the path component of $f$ in $GL_n(\mathbb R)$.

<1>1. If $f_t$ is a path in $GL_n(\mathbb R)$, then all $(f_t)_*$ on local homology are equal.
::: {.proof}
The map
\[
H(x,t)=f_t(x)
\]
is a homotopy of maps of pairs
\[
(\mathbb R^n,\mathbb R^n-\{0\})\to(\mathbb R^n,\mathbb R^n-\{0\}),
\]
since every $f_t$ is invertible and hence takes nonzero vectors to nonzero vectors. Homotopy invariance of relative homology gives equality of the induced maps.
:::

<1>2. Every matrix with positive determinant is path connected in $GL_n(\mathbb R)$ to the identity, while every matrix with negative determinant is path connected to
\[
r=\operatorname{diag}(-1,1,\dots,1).
\]
::: {.proof}
Gaussian elimination through invertible elementary matrices reduces any matrix to a diagonal one without crossing determinant zero. Positive diagonal entries can be deformed to $1$, and negative entries can be paired and deformed through an invertible $2\times2$ block to two positive entries. Thus the positive-determinant component contains $I$ and the negative-determinant component contains $r$. Equivalently, $GL_n(\mathbb R)$ has exactly the two components distinguished by the sign of the determinant.
:::

<1>3. The identity induces $+1$ and the reflection $r$ induces $-1$ on local homology.
::: {.proof}
Under the boundary isomorphism
\[
H_n(\mathbb R^n,\mathbb R^n-\{0\})
\cong
\widetilde H_{n-1}(\mathbb R^n-\{0\})
\cong
\widetilde H_{n-1}(S^{n-1}),
\]
the map induced by $r$ is the usual reflection of $S^{n-1}$. A reflection reverses orientation and therefore has degree $-1$. The identity has degree $+1$.
:::

Combining <1>1--<1>3,
\[
\boxed{
f_*=
\begin{cases}
+1,&\det f>0,\\
-1,&\det f<0.
\end{cases}}
\]
:::
