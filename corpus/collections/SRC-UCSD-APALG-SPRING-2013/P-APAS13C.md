---
schema: qual/card@1
id: P-APAS13C
kind: problem
title: Matrix $p$- and Frobenius norms; diagonal $p$-norm; two explicit $\norm{B}_2$ computations
classification:
  areas:
  - applied-algebra
  topics:
  - Norms
relations: []
review: draft
---

::: {.problem}
(a) Define the $p$-norm $\norm{A}_p$ and Frobenius norm $\norm{A}_F$ of a matrix $A\in M_{m,n}$.

(b) Suppose that $D\in M_n$ with $D=\operatorname{diag}(d_1,d_2,\ldots,d_n)$.
Prove that for all $1\le p\le\infty$ the $p$-norm of $D$ is given by $\norm{D}_p=\max_{1\le i\le n}\abs{d_i}$.

(c) Given $b\in\CC^{n-1}$, find $\norm{B}_2$ for the matrices
$$
B=\begin{pmatrix} 0 & b^H \\ b & 0 \end{pmatrix}
\quad\text{and}\quad
B=bb^H.
$$
(Show your work.
Simply writing down the answer will not be sufficient.)
:::

::: {.solution}
For a vector $x=(x_1,\ldots,x_n)^T\in\CC^n$, write
$$
\norm{x}_p=\left(\sum_i \abs{x_i}^p\right)^{1/p}
\quad (1\le p<\infty),
\qquad
\norm{x}_\infty=\max_i \abs{x_i}.
$$
The induced matrix $p$-norm is
$$
\norm{A}_p=\sup_{x\ne0}\frac{\norm{Ax}_p}{\norm{x}_p}.
$$
The Frobenius norm is
$$
\norm{A}_F=\left(\sum_{i,j}\abs{a_{ij}}^2\right)^{1/2}
       =\sqrt{\operatorname{tr}(A^HA)}.
$$

For part (b), let $D=\operatorname{diag}(d_1,\ldots,d_n)$, and put
$$
M=\max_i \abs{d_i}.
$$
If $1\le p<\infty$, then for every $x$,
$$
\norm{Dx}_p^p
 =\sum_i \abs{d_i x_i}^p
 \le M^p\sum_i \abs{x_i}^p
 =M^p\norm{x}_p^p,
$$
so $\norm{D}_p\le M$. For $p=\infty$, similarly,
$$
\norm{Dx}_\infty=\max_i \abs{d_i x_i}\le M\norm{x}_\infty.
$$
If $j$ is chosen with $\abs{d_j}=M$, then for the coordinate vector $e_j$,
$$
\frac{\norm{De_j}_p}{\norm{e_j}_p}=\abs{d_j}=M
$$
for every $1\le p\le\infty$. Hence
$$
\boxed{\norm{D}_p=\max_i\abs{d_i}}.
$$

For part (c), first let
$$
B=\begin{pmatrix}0&b^H\\ b&0\end{pmatrix}.
$$
This matrix is Hermitian. If $b=0$, then $B=0$ and the answer is immediate. Assume $b\ne0$, and let
$$
u=\frac{b}{\norm{b}_2}.
$$
Then
$$
B\binom{1}{u}
 =\binom{b^Hu}{b}
 =\norm{b}_2\binom{1}{u},
$$
while
$$
B\binom{1}{-u}
 =-\norm{b}_2\binom{1}{-u}.
$$
Every vector $\binom{0}{v}$ with $v\perp b$ lies in the kernel of $B$. Thus the eigenvalues of the Hermitian matrix $B$ are
$$
\norm{b}_2,\ -\norm{b}_2,\ 0,\ldots,0.
$$
For a Hermitian matrix, the induced $2$-norm is the largest absolute value of an eigenvalue. Therefore
$$
\boxed{\norm{B}_2=\norm{b}_2}.
$$

Now let $B=bb^H$. Again $B$ is Hermitian positive semidefinite. Moreover,
$$
Bb=b(b^Hb)=\norm{b}_2^2 b,
$$
and if $v\perp b$, then $Bv=b(b^Hv)=0$. Hence the eigenvalues are
$$
\norm{b}_2^2,0,\ldots,0,
$$
so
$$
\boxed{\norm{bb^H}_2=\norm{b}_2^2}.
$$
:::
