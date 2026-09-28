---
schema: qual/card@1
id: P-PRELIM82S-07
kind: problem
title: Determinant of $X\mapsto(AX+XA)/2$ on $M_3(\mathbb R)$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The extraction garbles the matrix-space size as B-by-B, but the source displays A as 3-by-3 and AX+XA therefore forces V=M_3(R).
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    The standard matrix units E_ij are eigenvectors for T, with eigenvalue
    (lambda_i+lambda_j)/2 when A=diag(lambda_1,lambda_2,lambda_3).
    For lambda=(1,2,1), the nine eigenvalues are four copies of 1,
    four copies of 3/2, and one copy of 2, whose product is 81/8.
---

::: {.problem}
Let $V=M_3(\mathbb R)$ and let
\[
A=\begin{pmatrix}
1&0&0\\
0&2&0\\
0&0&1
\end{pmatrix}.
\]
Define the linear transformation $T:V\to V$ by
\[
T(X)=\frac12(AX+XA).
\]
Compute $\det T$.
:::

::: {.solution}
Let $E_{ij}$ denote the standard matrix unit with a $1$ in position
$(i,j)$ and zeros elsewhere, and write
$$
A=\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3)
$$
with
$$
(\lambda_1,\lambda_2,\lambda_3)=(1,2,1).
$$

<1>1. For every $1\leq i,j\leq3$,
$$
T(E_{ij})
=
\frac{\lambda_i+\lambda_j}{2}E_{ij}.
$$

::: {.proof}
Left multiplication by the diagonal matrix $A$ scales the $i$th row of
$E_{ij}$ by $\lambda_i$, so
$$
AE_{ij}=\lambda_iE_{ij}.
$$
Right multiplication by $A$ scales the $j$th column by $\lambda_j$, so
$$
E_{ij}A=\lambda_jE_{ij}.
$$
Therefore
$$
T(E_{ij})
=
\frac12(AE_{ij}+E_{ij}A)
=
\frac{\lambda_i+\lambda_j}{2}E_{ij}.
$$
:::

<1>2. Relative to the basis
$$
\{E_{ij}:1\leq i,j\leq3\},
$$
the eigenvalues of $T$ are
$$
1,\frac32,1,
\frac32,2,\frac32,
1,\frac32,1.
$$

::: {.proof}
Step <1>1 shows that every basis vector $E_{ij}$ is an eigenvector with
eigenvalue
$$
\frac{\lambda_i+\lambda_j}{2}.
$$
Substituting
$$
(\lambda_1,\lambda_2,\lambda_3)=(1,2,1)
$$
for the nine ordered pairs $(i,j)$ gives the displayed list.
:::

<1>3. The determinant is
$$
\boxed{\det T=\frac{81}{8}}.
$$

::: {.proof}
Since the matrix of $T$ in the basis of step <1>2 is diagonal,
its determinant is the product of its nine diagonal entries. Hence
$$
\begin{aligned}
\det T
&=
1^4
\left(\frac32\right)^4
2\\
&=
\frac{81}{8}.
\end{aligned}
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested determinant.
:::
:::
