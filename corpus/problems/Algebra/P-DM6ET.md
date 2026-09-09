---
schema: qual/card@1
id: P-DM6ET
kind: problem
title: A diagonalizable matrix has a cyclic vector if and only if its eigenvalues
  are distinct
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Eigenvalues and Eigenvectors
  - Minimal and Characteristic Polynomials
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
Let $A$ be an $n\times n$ matrix over a field $F$ such that $A$ is diagonalizable.
Prove that the following are equivalent:

1. There is a vector $v\in F^n$ such that $v, Av, \cdots A^{n-1}v$ is a basis for $F^n$.

2. The eigenvalues of $A$ are distinct.
:::


::: {.solution}
<1>1. Suppose first that $A$ has $n$ distinct eigenvalues $\lambda_1,\dots,\lambda_n$ with eigenbasis $e_1,\dots,e_n$. Set
\[
v=e_1+\cdots+e_n.
\]
Then $v,Av,\dots,A^{n-1}v$ is a basis.
::: {.proof}
Relative to the eigenbasis, the columns of
\[
[v\ Av\ \cdots\ A^{n-1}v]
\]
form the Vandermonde matrix
\[
\begin{pmatrix}
1&\lambda_1&\cdots&\lambda_1^{n-1}\\
\vdots&\vdots&&\vdots\\
1&\lambda_n&\cdots&\lambda_n^{n-1}
\end{pmatrix}.
\]
Its determinant is
\[
\prod_{i<j}(\lambda_j-\lambda_i),
\]
which is nonzero because the eigenvalues are distinct. Hence the displayed vectors are linearly independent and therefore form a basis.
:::

<1>2. Conversely, suppose there is $v$ such that
\[
v,Av,\dots,A^{n-1}v
\]
is a basis. Then the minimal polynomial of $A$ has degree $n$.
::: {.proof}
If a nonzero polynomial
\[
p(t)=c_0+c_1t+\cdots+c_dt^d
\]
of degree $d<n$ satisfied $p(A)=0$, then
\[
c_0v+c_1Av+\cdots+c_dA^dv=0,
\]
contradicting linear independence of the basis vectors. Thus no annihilating polynomial of degree less than $n$ exists. Since the characteristic polynomial has degree $n$ and annihilates $A$, the minimal polynomial has degree exactly $n$.
:::

<1>3. Since $A$ is diagonalizable, its minimal polynomial is a product of distinct linear factors, one for each distinct eigenvalue.
::: {.proof}
For a diagonalizable operator, the minimal polynomial is
\[
\prod_{\lambda\in\operatorname{Spec}(A)}(t-\lambda).
\]
Therefore its degree equals the number of distinct eigenvalues. By <1>2 this degree is $n$, so $A$ has $n$ distinct eigenvalues.
:::

Thus the two conditions are equivalent.
:::
