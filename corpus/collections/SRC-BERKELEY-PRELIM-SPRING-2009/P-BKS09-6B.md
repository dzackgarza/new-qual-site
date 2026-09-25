---
schema: qual/card@1
id: P-BKS09-6B
kind: problem
title: Courant--Fischer min-max characterization of eigenvalues
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with the Spring 2009 solution-packet extraction and independently reviewed its eigenbasis/intersection argument.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the dimension-intersection bound and the extremizing span of the first k eigenvectors.
---

::: {.problem}
Let $\lambda _ { 1 } \geq \cdots \geq \lambda _ { n }$ be eigenvalues of a symmetric real $n \times n$ -matrix A. Prove that

$$
\lambda _ { k } = \operatorname* { m a x } _ { V ^ { k } } \operatorname* { m i n } _ { x \in \left( V ^ { k } - 0 \right) } \frac { \left( A x , x \right) } { \left( x , x \right) } ,
$$

where the maximum is taken over all k-dimensional linear subspaces $V ^ { k }$ , the minimum over all non-zero vectors in the subspace, and $( x , y )$ denotes the Euclidean dot-product.
(Hint: any k-dimensional subspace intersects the space spanned by the eigenvectors of the $n + 1 - k$ smallest eigenvalues in a space of dimension at least 1.)
:::

::: {.solution}
For $x\neq0$, write
$$
R_A(x)\coloneqq
\frac{\inner{Ax}{x}}{\inner{x}{x}}
$$
for the Rayleigh quotient of $A$.

<1>1. There is an orthonormal basis $e_1,\ldots,e_n$ of $\RR^n$ such that
$$
Ae_i=\lambda_i e_i
$$
for every $i$, and for
$$
x=\sum_{i=1}^n x_i e_i
$$
one has
$$
R_A(x)
=
\frac{\sum_{i=1}^n\lambda_i x_i^2}
{\sum_{i=1}^n x_i^2}.
$$

::: {.proof}
Because $A$ is real symmetric, the spectral theorem gives an orthonormal
eigenbasis with the eigenvalues ordered as in the statement. Then
$$
Ax=\sum_{i=1}^n\lambda_i x_i e_i,
$$
so orthonormality gives
$$
\inner{Ax}{x}
=
\sum_{i=1}^n\lambda_i x_i^2,
\qquad
\inner{x}{x}
=
\sum_{i=1}^n x_i^2.
$$
:::

<1>2. For every $k$-dimensional subspace $V\subseteq\RR^n$, the minimum
of $R_A$ on $V\setminus\{0\}$ is attained.

::: {.proof}
The Rayleigh quotient is homogeneous of degree $0$, so its values on
$V\setminus\{0\}$ are the same as its values on the unit sphere
$$
S(V)\coloneqq\{x\in V:\norm{x}=1\}.
$$
The set $S(V)$ is compact and $R_A$ is continuous there. Hence $R_A$
attains a minimum on $S(V)$.
:::

<1>3. Let
$$
W\coloneqq\operatorname{span}\{e_k,e_{k+1},\ldots,e_n\}.
$$
Then every nonzero $x\in W$ satisfies
$$
R_A(x)\leq\lambda_k.
$$

::: {.proof}
If
$$
x=\sum_{i=k}^n x_i e_i\neq0,
$$
then step <1>1 and the inequalities
$$
\lambda_i\leq\lambda_k
\qquad
(i\geq k)
$$
give
$$
R_A(x)
=
\frac{\sum_{i=k}^n\lambda_i x_i^2}
{\sum_{i=k}^n x_i^2}
\leq
\lambda_k.
$$
:::

<1>4. For every $k$-dimensional subspace $V\subseteq\RR^n$,
$$
\min_{x\in V\setminus\{0\}}R_A(x)
\leq
\lambda_k.
$$

::: {.proof}
The subspace $W$ in step <1>3 has dimension
$$
\dim W=n-k+1.
$$
Therefore
$$
\dim V+\dim W
=
k+(n-k+1)
=
n+1,
$$
so
$$
\dim(V\cap W)
\geq
\dim V+\dim W-n
\geq
1.
$$
Choose $0\neq x\in V\cap W$. By step <1>3,
$$
R_A(x)\leq\lambda_k.
$$
The minimum on $V\setminus\{0\}$ is at most this value.
:::

<1>5. For
$$
V_0\coloneqq\operatorname{span}\{e_1,\ldots,e_k\},
$$
one has
$$
\min_{x\in V_0\setminus\{0\}}R_A(x)
=
\lambda_k.
$$

::: {.proof}
If
$$
x=\sum_{i=1}^k x_i e_i\neq0,
$$
then step <1>1 and
$$
\lambda_i\geq\lambda_k
\qquad
(i\leq k)
$$
give
$$
R_A(x)
=
\frac{\sum_{i=1}^k\lambda_i x_i^2}
{\sum_{i=1}^k x_i^2}
\geq
\lambda_k.
$$
Equality is attained at $x=e_k$, since
$$
R_A(e_k)=\lambda_k.
$$
Hence the minimum is exactly $\lambda_k$.
:::

<1>6. Therefore
$$
\boxed{
\lambda_k
=
\max_{\dim V=k}
\min_{x\in V\setminus\{0\}}
\frac{\inner{Ax}{x}}{\inner{x}{x}}
}.
$$

::: {.proof}
Step <1>4 shows that every $k$-dimensional subspace contributes a minimum
at most $\lambda_k$, so the displayed maximum is at most $\lambda_k$.
Step <1>5 exhibits the $k$-dimensional subspace $V_0$ whose minimum equals
$\lambda_k$, so the maximum is at least $\lambda_k$.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required min-max identity.
:::
:::
