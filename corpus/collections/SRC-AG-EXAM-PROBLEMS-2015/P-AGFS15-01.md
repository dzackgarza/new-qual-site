---
schema: qual/card@1
id: P-AGFS15-01
kind: problem
title: Rank-one 2-by-3 matrices as an affine variety
classification:
  areas: [algebraic-geometry]
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
Let $X$ be the set of all $2\times3$ matrices over an algebraically closed field $k$ having rank at most one, viewed as a subset of $\operatorname{Mat}_{2,3}(k)=\AA^6$.
Show that $X$ is an affine variety.
Is it irreducible?
What is its dimension?

You may use the Segre embedding.
:::

::: {.solution}
Write a matrix in coordinates as
$$
M=\begin{pmatrix}
x_1&x_2&x_3\\
y_1&y_2&y_3
\end{pmatrix}.
$$
Then

::: pf

::: {.pf-step #s1}

The matrices of rank at most one form the affine variety
$$
\boxed{X=V(x_1y_2-x_2y_1,\ x_1y_3-x_3y_1,\ x_2y_3-x_3y_2)}.
$$

::: pf-proof

A $2\times3$ matrix has rank at most one if and only if every $2\times2$ minor vanishes. The three $2\times2$ minors of $M$ are precisely
$$
x_1y_2-x_2y_1,
\qquad
x_1y_3-x_3y_1,
\qquad
x_2y_3-x_3y_2.
$$
Thus the displayed zero set is exactly $X$, so $X\subseteq\AA^6$ is Zariski closed.

:::

:::

::: {.pf-step #s2}

$X$ is irreducible.

::: pf-proof

Consider
$$
\phi:\AA^2\times\AA^3\longrightarrow\AA^6,
\qquad
(u,v)\longmapsto uv^T.
$$
Every matrix $uv^T$ has rank at most one, so $\operatorname{im}\phi\subseteq X$.
Conversely, every nonzero matrix of rank one can be written as $uv^T$: choose any nonzero column $u$; every other column is a scalar multiple of $u$, and the three scalars form $v$. The zero matrix is $\phi(0,v)$. Hence $\phi$ is surjective onto $X$.

The variety $\AA^2\times\AA^3\cong\AA^5$ is irreducible, and the image of an irreducible topological space under a continuous map is irreducible. Since polynomial maps are Zariski continuous, $X=\phi(\AA^5)$ is irreducible.

Equivalently, $X$ is the affine cone over the Segre embedding
$$
\mathbf P^1\times\mathbf P^2\hookrightarrow\mathbf P^5.
$$

:::

:::

::: {.pf-step #s3}

$\dim X=\boxed{4}$.

::: pf-proof

Use the affine chart
$$
U=X\cap D(x_1).
$$
On $U$, the first two minor equations give
$$
y_2=\frac{x_2y_1}{x_1},
\qquad
y_3=\frac{x_3y_1}{x_1},
$$
and then the third minor vanishes automatically. Therefore
$$
U\cong \operatorname{Spec}k[x_1^{\pm1},x_2,x_3,y_1]
\cong\Gm\times\AA^3,
$$
so $\dim U=4$.

The set $U$ is nonempty and open in the irreducible variety $X$, hence it is dense and has the same dimension as $X$. Thus
$$
\dim X=4.
$$
This also agrees with the cone description: the Segre variety $\mathbf P^1\times\mathbf P^2$ has dimension $1+2=3$, and its affine cone has dimension $3+1=4$.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves that $X$ is an affine variety, step [](#s2){.pf-ref} proves that it is irreducible, and step [](#s3){.pf-ref} computes its dimension.

:::

:::

:::
