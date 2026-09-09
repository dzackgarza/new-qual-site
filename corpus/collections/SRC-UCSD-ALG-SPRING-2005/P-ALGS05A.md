---
schema: qual/card@1
id: P-ALGS05A
kind: problem
title: "Properties of the symmetrization map T(X) = (X - X^T)/2 on M_3"
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Let $T: M_n(\mathbb{R}) \to M_n(\mathbb{R})$ be the transformation such that $T(X) = \frac{1}{2}(X - X^T)$.

(a) Prove that $T$ is a linear transformation.

(b) Determine the null space of $T$ and find its dimension.

(c) Derive the matrix representation of $T$ in terms of the standard basis for $M_3$.
:::

::: {.solution}
<1>1. The map \(T\) is linear.
::: {.proof}
For \(X,Y\in M_n(\mathbb R)\) and \(a,b\in\mathbb R\),
\[
\begin{aligned}
T(aX+bY)
&=\frac12\bigl(aX+bY-(aX+bY)^T\bigr)\\
&=\frac12\bigl(a(X-X^T)+b(Y-Y^T)\bigr)\\
&=aT(X)+bT(Y).
\end{aligned}
\]
:::

<1>2. The null space of \(T\) is the space of symmetric matrices,
\[
\ker T=\{X\in M_n(\mathbb R):X=X^T\},
\]
and therefore
\[
\dim\ker T=\frac{n(n+1)}2.
\]
::: {.proof}
One has \(T(X)=0\) iff \(X-X^T=0\), i.e. iff \(X\) is symmetric.
A symmetric \(n\times n\) matrix is determined freely by its \(n\) diagonal entries and its \(n(n-1)/2\) entries above the diagonal, giving dimension \(n+n(n-1)/2=n(n+1)/2\).
:::

<1>3. For \(M_3(\mathbb R)\), order the standard basis as
\[
(E_{11},E_{12},E_{13},E_{21},E_{22},E_{23},E_{31},E_{32},E_{33}).
\]
Then
\[
T(E_{ii})=0,
\qquad
T(E_{ij})=\frac12(E_{ij}-E_{ji})\quad(i\ne j).
\]
::: {.proof}
Since \(E_{ij}^T=E_{ji}\), this is immediate from the definition of \(T\).
:::

<1>4. Relative to that ordered basis, the matrix of \(T\) is
\[
[T]=\frac12
\begin{pmatrix}
0&0&0&0&0&0&0&0&0\\
0&1&0&-1&0&0&0&0&0\\
0&0&1&0&0&0&-1&0&0\\
0&-1&0&1&0&0&0&0&0\\
0&0&0&0&0&0&0&0&0\\
0&0&0&0&0&1&0&-1&0\\
0&0&-1&0&0&0&1&0&0\\
0&0&0&0&0&-1&0&1&0\\
0&0&0&0&0&0&0&0&0
\end{pmatrix}.
\]
::: {.proof}
The \(j\)-th column is the coordinate vector of \(T\) applied to the \(j\)-th basis matrix.
Using <1>3 gives exactly the displayed columns.
:::
:::
