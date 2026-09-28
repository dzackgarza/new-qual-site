---
schema: qual/card@1
id: P-BERK81S-05
kind: problem
title: Determinant of congruence on the skew-symmetric matrices
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Identified the skew-symmetric matrices with the exterior square
    Lambda^2 R^n via u∧v↦uv^T-vu^T. Under this identification
    X↦AXA^T is exactly Lambda^2 A. After complex triangularization of A,
    Lambda^2 A is triangular with diagonal entries lambda_i lambda_j for
    i<j; their product is (prod_i lambda_i)^(n-1)=(det A)^(n-1).
---

::: {.problem}
Let $S$ be the vector space of real $n\times n$ skew-symmetric matrices.
For $A\in GL_n(\mathbb R)$, compute the determinant of the linear map
\[
T_A:S\to S,
\qquad
T_A(X)=AXA^T.
\]
:::

::: {.solution}
Let
$$
V=\RR^n.
$$

<1>1. The map
$$
\Phi:\bigwedge^2V\longrightarrow S
$$
defined on decomposable elements by
$$
\Phi(u\wedge v)
=
uv^T-vu^T
$$
is a linear isomorphism.

::: {.proof}
For the standard basis $e_1,\ldots,e_n$ of $V$,
$$
\Phi(e_i\wedge e_j)
=
E_{ij}-E_{ji}
$$
for $i<j$. The vectors
$$
e_i\wedge e_j,
\qquad
i<j,
$$
form a basis of $\bigwedge^2V$, while the matrices
$$
E_{ij}-E_{ji},
\qquad
i<j,
$$
form a basis of $S$. Thus $\Phi$ sends a basis to a basis.
:::

<1>2. Under the isomorphism $\Phi$, the map $T_A$ corresponds to the
exterior-square operator
$$
\bigwedge^2A:\bigwedge^2V\longrightarrow\bigwedge^2V.
$$

::: {.proof}
For $u,v\in V$,
$$
\begin{aligned}
T_A(\Phi(u\wedge v))
&=
A(uv^T-vu^T)A^T\\
&=
(Au)(Av)^T-(Av)(Au)^T\\
&=
\Phi(Au\wedge Av)\\
&=
\Phi\bigl((\bigwedge^2A)(u\wedge v)\bigr).
\end{aligned}
$$
Since decomposable wedges span $\bigwedge^2V$, the intertwining identity
holds on the whole space.
:::

<1>3. Consequently,
$$
\det T_A
=
\det(\bigwedge^2A).
$$

::: {.proof}
Step <1>2 says that
$$
T_A
=
\Phi\circ(\bigwedge^2A)\circ\Phi^{-1}.
$$
Similar linear transformations have the same determinant.
:::

<1>4. Let
$$
\lambda_1,\ldots,\lambda_n
$$
be the complex eigenvalues of $A$, counted with algebraic multiplicity.
Then
$$
\det(\bigwedge^2A)
=
\prod_{1\leq i<j\leq n}\lambda_i\lambda_j.
$$

::: {.proof}
Complexify the real vector space and the operator. The matrix of the
complexified operator is still $A$, so its determinant is unchanged.

Over $\CC$, choose a basis in which $A$ is upper triangular with diagonal
entries
$$
\lambda_1,\ldots,\lambda_n.
$$
In the induced wedge basis
$$
e_i\wedge e_j,
\qquad
i<j,
$$
the operator $\bigwedge^2A$ is triangular, and its diagonal entry
corresponding to $e_i\wedge e_j$ is
$$
\lambda_i\lambda_j.
$$
The determinant of a triangular matrix is the product of its diagonal
entries, giving the displayed formula.
:::

<1>5. One has
$$
\prod_{1\leq i<j\leq n}\lambda_i\lambda_j
=
\left(
\prod_{i=1}^n\lambda_i
\right)^{n-1}.
$$

::: {.proof}
Fix $i$. The eigenvalue $\lambda_i$ appears once in the factor
$\lambda_i\lambda_j$ for every $j\neq i$, hence exactly $n-1$ times in the
full product. Therefore the total product is
$$
\prod_{i=1}^n\lambda_i^{\,n-1}
=
\left(
\prod_{i=1}^n\lambda_i
\right)^{n-1}.
$$
:::

<1>6. Since
$$
\prod_{i=1}^n\lambda_i=\det A,
$$
the determinant of $T_A$ is
$$
\boxed{
\det T_A=(\det A)^{n-1}.
}
$$

::: {.proof}
Combine steps <1>3--<1>5 and the standard identity that the product of the
eigenvalues of a matrix, counted with algebraic multiplicity, equals its
determinant.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the requested determinant.
:::
:::
