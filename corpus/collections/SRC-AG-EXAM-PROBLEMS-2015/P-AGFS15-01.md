---
schema: qual/card@1
id: P-AGFS15-01
kind: problem
title: Rank-one 2-by-3 matrices as an affine variety
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained Algebraic Geometry FS 15 exam-guidelines PDF dated August 12, 2015.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the determinantal equations, irreducibility via the Segre cone, and the dimension by an explicit dense affine chart.
---

::: {.problem}
Let $X$ be the set of all $2\times3$ matrices over an algebraically closed field $k$ having rank at most one, viewed as a subset of $\operatorname{Mat}_{2,3}(k)=\mathbb A^6$.
Show that $X$ is an affine variety.
Is it irreducible?
What is its dimension?

You may use the Segre embedding.
:::


::: {.solution}
Write a matrix in coordinates as
\[
M=\begin{pmatrix}
x_1&x_2&x_3\\
y_1&y_2&y_3
\end{pmatrix}.
\]
Then
\[
\boxed{X=V(x_1y_2-x_2y_1,\ x_1y_3-x_3y_1,\ x_2y_3-x_3y_2)}.
\]
In particular, \(X\) is an affine variety. Moreover, \(X\) is irreducible and
\[
\boxed{\dim X=4}.
\]

<1>1. The displayed equations cut out exactly the matrices of rank at most one.
::: {.proof}
A \(2\times3\) matrix has rank at most one if and only if every \(2\times2\) minor vanishes. The three \(2\times2\) minors of \(M\) are precisely
\[
x_1y_2-x_2y_1,
\qquad
x_1y_3-x_3y_1,
\qquad
x_2y_3-x_3y_2.
\]
Thus the displayed zero set is exactly \(X\), so \(X\subseteq\mathbb A^6\) is Zariski closed.
:::

<1>2. \(X\) is irreducible.
::: {.proof}
Consider
\[
\phi:\mathbb A^2\times\mathbb A^3\longrightarrow\mathbb A^6,
\qquad
(u,v)\longmapsto uv^T.
\]
Every matrix \(uv^T\) has rank at most one, so \(\operatorname{im}\phi\subseteq X\).
Conversely, every nonzero matrix of rank one can be written as \(uv^T\): choose any nonzero column \(u\); every other column is a scalar multiple of \(u\), and the three scalars form \(v\). The zero matrix is \(\phi(0,v)\). Hence \(\phi\) is surjective onto \(X\).

The variety \(\mathbb A^2\times\mathbb A^3\cong\mathbb A^5\) is irreducible, and the image of an irreducible topological space under a continuous map is irreducible. Since polynomial maps are Zariski continuous, \(X=\phi(\mathbb A^5)\) is irreducible.

Equivalently, \(X\) is the affine cone over the Segre embedding
\[
\mathbf P^1\times\mathbf P^2\hookrightarrow\mathbf P^5.
\]
:::

<1>3. \(\dim X=4\).
::: {.proof}
Use the affine chart
\[
U=X\cap D(x_1).
\]
On \(U\), the first two minor equations give
\[
y_2=\frac{x_2y_1}{x_1},
\qquad
y_3=\frac{x_3y_1}{x_1},
\]
and then the third minor vanishes automatically. Therefore
\[
U\cong \operatorname{Spec}k[x_1^{\pm1},x_2,x_3,y_1]
\cong\mathbb G_m\times\mathbb A^3,
\]
so \(\dim U=4\).

The set \(U\) is nonempty and open in the irreducible variety \(X\), hence it is dense and has the same dimension as \(X\). Thus
\[
\dim X=4.
\]
This also agrees with the cone description: the Segre variety \(\mathbf P^1\times\mathbf P^2\) has dimension \(1+2=3\), and its affine cone has dimension \(3+1=4\).
:::
:::
