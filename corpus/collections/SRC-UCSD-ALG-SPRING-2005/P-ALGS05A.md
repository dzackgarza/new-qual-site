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
T(aX+bY)
=\frac12\bigl(aX+bY-(aX+bY)^T\bigr)
=aT(X)+bT(Y),
\]
because transpose is linear.
:::

<1>2. The null space of \(T\) is the subspace of symmetric matrices.
::: {.proof}
One has
\[
T(X)=0
\iff X-X^T=0
\iff X=X^T.
\]
Thus \(\ker T=\operatorname{Sym}_n(\mathbb R)\).
:::

<1>3. The nullity of \(T\) is \(n(n+1)/2\).
::: {.proof}
A symmetric \(n\times n\) matrix is determined freely by its \(n\) diagonal entries and its \(n(n-1)/2\) entries strictly above the diagonal.
Hence
\[
\dim \ker T=n+\frac{n(n-1)}2=\frac{n(n+1)}2.
\]
:::

<1>4. For the standard matrix units \(E_{ij}\),
\[
T(E_{ii})=0,
\qquad
T(E_{ij})=\frac12(E_{ij}-E_{ji})\quad(i\ne j).
\]
::: {.proof}
Since \(E_{ij}^T=E_{ji}\), this follows directly from the definition of \(T\).
:::

<1>5. With the ordered standard basis
\[
(E_{11},E_{12},E_{13},E_{21},E_{22},E_{23},E_{31},E_{32},E_{33})
\]
of \(M_3(\mathbb R)\), the matrix of \(T\) is
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
The \(j\)-th column is the coordinate vector of the image of the \(j\)-th basis element.
Applying <1>4 to the nine matrix units gives exactly the displayed columns.
:::
:::
