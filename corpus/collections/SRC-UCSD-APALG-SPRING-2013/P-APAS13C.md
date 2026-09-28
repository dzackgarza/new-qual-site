---
schema: qual/card@1
id: P-APAS13C
kind: problem
title: Matrix $p$- and Frobenius norms; diagonal $p$-norm; two explicit $\|B\|_2$ computations
classification:
  areas:
  - applied-algebra
  topics:
  - Norms
relations: []
review: draft
---

::: {.problem}
(a) Define the $p$-norm $\|A\|_p$ and Frobenius norm $\|A\|_F$ of a matrix $A\in M_{m,n}$.

(b) Suppose that $D\in M_n$ with $D=\operatorname{diag}(d_1,d_2,\ldots,d_n)$.
Prove that for all $1\le p\le\infty$ the $p$-norm of $D$ is given by $\|D\|_p=\max_{1\le i\le n}|d_i|$.

(c) Given $b\in\mathbb{C}^{n-1}$, find $\|B\|_2$ for the matrices
\[
B=\begin{pmatrix} 0 & b^H \\ b & 0 \end{pmatrix}
\quad\text{and}\quad
B=bb^H.
\]
(Show your work.
Simply writing down the answer will not be sufficient.)
:::

::: {.solution}
For a vector \(x=(x_1,\ldots,x_n)^T\in\mathbb C^n\), write
\[
\|x\|_p=\left(\sum_i |x_i|^p\right)^{1/p}
\quad (1\le p<\infty),
\qquad
\|x\|_\infty=\max_i |x_i|.
\]
The induced matrix \(p\)-norm is
\[
\|A\|_p=\sup_{x\ne0}\frac{\|Ax\|_p}{\|x\|_p}.
\]
The Frobenius norm is
\[
\|A\|_F=\left(\sum_{i,j}|a_{ij}|^2\right)^{1/2}
       =\sqrt{\operatorname{tr}(A^HA)}.
\]

For part (b), let \(D=\operatorname{diag}(d_1,\ldots,d_n)\), and put
\[
M=\max_i |d_i|.
\]
If \(1\le p<\infty\), then for every \(x\),
\[
\|Dx\|_p^p
 =\sum_i |d_i x_i|^p
 \le M^p\sum_i |x_i|^p
 =M^p\|x\|_p^p,
\]
so \(\|D\|_p\le M\). For \(p=\infty\), similarly,
\[
\|Dx\|_\infty=\max_i |d_i x_i|\le M\|x\|_\infty.
\]
If \(j\) is chosen with \(|d_j|=M\), then for the coordinate vector \(e_j\),
\[
\frac{\|De_j\|_p}{\|e_j\|_p}=|d_j|=M
\]
for every \(1\le p\le\infty\). Hence
\[
\boxed{\|D\|_p=\max_i|d_i|}.
\]

For part (c), first let
\[
B=\begin{pmatrix}0&b^H\\ b&0\end{pmatrix}.
\]
This matrix is Hermitian. If \(b=0\), then \(B=0\) and the answer is immediate. Assume \(b\ne0\), and let
\[
u=\frac{b}{\|b\|_2}.
\]
Then
\[
B\binom{1}{u}
 =\binom{b^Hu}{b}
 =\|b\|_2\binom{1}{u},
\]
while
\[
B\binom{1}{-u}
 =-\|b\|_2\binom{1}{-u}.
\]
Every vector \(\binom{0}{v}\) with \(v\perp b\) lies in the kernel of \(B\). Thus the eigenvalues of the Hermitian matrix \(B\) are
\[
\|b\|_2,\ -\|b\|_2,\ 0,\ldots,0.
\]
For a Hermitian matrix, the induced \(2\)-norm is the largest absolute value of an eigenvalue. Therefore
\[
\boxed{\|B\|_2=\|b\|_2}.
\]

Now let \(B=bb^H\). Again \(B\) is Hermitian positive semidefinite. Moreover,
\[
Bb=b(b^Hb)=\|b\|_2^2 b,
\]
and if \(v\perp b\), then \(Bv=b(b^Hv)=0\). Hence the eigenvalues are
\[
\|b\|_2^2,0,\ldots,0,
\]
so
\[
\boxed{\|bb^H\|_2=\|b\|_2^2}.
\]
:::
