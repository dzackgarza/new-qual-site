---
schema: qual/card@1
id: P-ALGS06A
kind: problem
title: "Left and right eigenvectors of a matrix for distinct eigenvalues"
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
(a) Consider $\lambda_i, \lambda_j \in \operatorname{eig}(A)$ such that $\lambda_i \neq \lambda_j$.
Let $(x_i, y_i)$ and $(x_j, y_j)$ denote the right and left eigenvectors of $A$ associated with $\lambda_i$ and $\lambda_j$.
Show that $y_i^* x_j = 0$.

(b) Let $x$ denote an eigenvector of $A$ associated with an eigenvalue $\lambda$.
Prove that if $\lambda$ has a left-eigenvector $y$ such that $y^* x = 0$, then $\operatorname{am}(\lambda) > 1$.
:::

::: {.solution}
<1>1. If $\lambda_i\ne\lambda_j$, then $y_i^*x_j=0$.
::: {.proof}
Because $x_j$ is a right eigenvector and $y_i$ is a left eigenvector,
\[
Ax_j=\lambda_jx_j,
\qquad
y_i^*A=\lambda_i y_i^*.
\]
Hence
\[
\lambda_i y_i^*x_j
=y_i^*Ax_j
=\lambda_j y_i^*x_j.
\]
Since $\lambda_i\ne\lambda_j$, it follows that $y_i^*x_j=0$.
:::

<1>2. For part (b), suppose toward a contradiction that $\operatorname{am}(\lambda)=1$.
::: {.proof}
We will show that the assumed orthogonality $y^*x=0$ then forces a generalized eigenvector of rank $2$, contradicting algebraic multiplicity $1$.
:::

<1>3. Under the assumption $\operatorname{am}(\lambda)=1$, both the right and left eigenspaces for $\lambda$ are one-dimensional.
::: {.proof}
The geometric multiplicity is at least $1$ and at most the algebraic multiplicity, so
\[
\dim\ker(A-\lambda I)=1.
\]
Also
\[
\operatorname{rank}(A-\lambda I)
=\operatorname{rank}(A^*-\overline\lambda I),
\]
so the two kernels have the same dimension. Thus
\[
\dim\ker(A^*-\overline\lambda I)=1.
\]
This latter kernel is the left eigenspace, so the given nonzero left eigenvector $y$ spans it.
:::

<1>4. The condition $y^*x=0$ implies
\[
x\in\operatorname{im}(A-\lambda I).
\]
::: {.proof}
For every linear map $B$ on a finite-dimensional inner-product space,
\[
\operatorname{im}B=(\ker B^*)^\perp.
\]
Take $B=A-\lambda I$. By <1>3,
\[
\ker B^*=\operatorname{span}\{y\}.
\]
The hypothesis $y^*x=0$ says exactly that $x\perp\ker B^*$, hence $x\in\operatorname{im}B$.
:::

<1>5. There exists $z$ such that
\[
(A-\lambda I)z=x\ne0,
\qquad
(A-\lambda I)x=0.
\]
::: {.proof}
The first equality follows from <1>4, and the second from the fact that $x$ is a right eigenvector for $\lambda$.
:::

<1>6. The relations in <1>5 imply that the algebraic multiplicity of $\lambda$ is at least $2$.
::: {.proof}
The vectors $x$ and $z$ are linearly independent: if $z=cx$, then $(A-\lambda I)z=0$, contradicting $(A-\lambda I)z=x\ne0$. Their span is invariant under $A$, and in the ordered basis $(x,z)$ the restriction of $A$ has matrix
\[
\begin{pmatrix}
\lambda&1\\
0&\lambda
\end{pmatrix}.
\]
Hence $(t-\lambda)^2$ divides the characteristic polynomial of $A$, so $\operatorname{am}(\lambda)\ge2$.
:::

<1>7. Therefore $\operatorname{am}(\lambda)>1$.
::: {.proof}
This contradicts the assumption in <1>2 that $\operatorname{am}(\lambda)=1$.
:::
:::
