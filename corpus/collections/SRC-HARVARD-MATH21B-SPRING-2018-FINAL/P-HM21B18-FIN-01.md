---
schema: qual/card@1
id: P-HM21B18-FIN-01
kind: problem
title: True-or-false statements on matrices, linear operators, and Fourier series
classification: {areas: [applied-algebra], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: >-
    Nineteen of the twenty true-or-false statements are recoverable from the
    retained solution packet. The twentieth statement is missing from the
    extraction; only its solution text survives, so it is not reconstructed.
---

::: {.problem}
Mark each statement true or false. No justifications are required.

1. If $A$ and $B$ are orthogonal matrices, then $A+B$ is orthogonal.
2. Every real $2\times2$ matrix has a real eigenvalue.
3. If $\{v_1,v_2\}$ is a basis of $\RR^2$ and $A$ is invertible, then $\{Av_1,Av_2\}$ is also a basis.
4. A basis for $\ker(D-1)^2$ on $C^\infty$ is $\{e^t,te^t\}$.
5. Every symmetric matrix with positive entries has only positive real eigenvalues.
6. Every reflection matrix is invertible.
7. If $A$ is symmetric and $A^6=I$, then $A=I$.
8. The operator $T=D^2+1$ defines a linear map $C^\infty\to C^\infty$.
9. If $A$ and $B$ are symmetric, then $A^2-B^2$ is symmetric.
10. In the Fourier series of $x^5$ on $[-\pi,\pi]$, every cosine coefficient $a_n$ is zero.
11. If $A$ and $B$ are diagonalizable over $\RR$, then $A+B$ is diagonalizable over $\RR$.
12. Every $5\times4$ matrix has a nonzero vector in its kernel.
13. If $A$ is square and $\ker A\subseteq\operatorname{im}A$, then $A^2=0$.
14. The $a_0$ Fourier coefficient of $e^{-x^2}$ is zero.
15. If an invertible square matrix has two QR decompositions $A=Q_1R_1=Q_2R_2$, then $R_1=R_2$.
16. The eigenvalue $1$ of reflection in a line in $\RR^2$ cannot have geometric multiplicity $2$.
17. If $x'=Ax$ is asymptotically stable, then every eigenvalue $\lambda$ of $A$ satisfies $|\lambda|<1$.
18. Solutions of $u_t=u_{xx}$ with initial condition $u(x,0)=\sin(14x)$ converge to $0$ as $t\to\infty$.
19. If $Av=5v$ and $Au=-u$, then $A(3v+2u)=15v-2u$.
:::

For statement 15, use the course convention that a QR decomposition has
$Q$ orthogonal and $R$ upper triangular with positive diagonal entries.

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Statement 1 is false.


::: pf-proof

Take $A=I$ and $B=-I$. Both are orthogonal, but $A+B=0$ is not orthogonal,
since $0^T0=0\neq I$.

:::

:::

::: pf-step

Statement 2 is false.


::: pf-proof

The real matrix
\[
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}
\]
has characteristic polynomial $\lambda^2+1$, so it has no real
eigenvalue.

:::

:::

::: pf-step

Statement 3 is true.


::: pf-proof

Suppose
$c_1Av_1+c_2Av_2=0$. Since $A$ is invertible,
\[
A(c_1v_1+c_2v_2)=0
\]
implies $c_1v_1+c_2v_2=0$, and because $\{v_1,v_2\}$ is a basis,
$c_1=c_2=0$. Thus $Av_1,Av_2$ are linearly independent. Two linearly
independent vectors in $\RR^2$ form a basis.

:::

:::

::: pf-step

Statement 4 is true.


::: pf-proof

If $(D-1)^2f=0$, set $g=(D-1)f$. Then $(D-1)g=0$, so
$g=ce^t$ for some constant $c$. Hence
\[
f'-f=ce^t.
\]
Multiplying by $e^{-t}$ gives
\[
(e^{-t}f)'=c,
\]
so $f=(ct+d)e^t$. Therefore
\[
\ker(D-1)^2=\operatorname{span}\{e^t,te^t\},
\]
and the two displayed functions are linearly independent.

:::

:::

::: pf-step

Statement 5 is false.


::: pf-proof

The matrix
\[
\begin{pmatrix}
1&2\\
2&1
\end{pmatrix}
\]
is symmetric and every entry is positive, but its eigenvalues are $3$ and
$-1$.

:::

:::

::: pf-step

Statement 6 is true.


::: pf-proof

A reflection $R$ satisfies $R^2=I$. Hence $R^{-1}=R$, so $R$ is
invertible.

:::

:::

::: pf-step

Statement 7 is false.


::: pf-proof

Take $A=-I$. Then $A$ is symmetric and
$A^6=(-I)^6=I$, but $A\neq I$.

:::

:::

::: pf-step

Statement 8 is true.


::: pf-proof

For $f,g\in C^\infty$ and scalars $a,b$,
\[
T(af+bg)
=(af+bg)''+(af+bg)
=a(f''+f)+b(g''+g)
=aTf+bTg.
\]
Also $f''+f$ is smooth whenever $f$ is smooth. Thus
$T\colon C^\infty\to C^\infty$ is linear.

:::

:::

::: pf-step

Statement 9 is true.


::: pf-proof

Since $A^T=A$ and $B^T=B$,
\[
(A^2-B^2)^T
=(A^T)^2-(B^T)^2
=A^2-B^2.
\]
Therefore $A^2-B^2$ is symmetric.

:::

:::

::: pf-step

Statement 10 is true.


::: pf-proof

For every $n\geq0$, the function $\cos(nx)$ is even, whereas $x^5$ is
odd. Hence $x^5\cos(nx)$ is odd, and therefore
\[
\int_{-\pi}^{\pi}x^5\cos(nx)\,dx=0.
\]
Thus every cosine coefficient is zero.

:::

:::

::: pf-step

Statement 11 is false.


::: pf-proof

Let
\[
A=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
0&1\\
0&2
\end{pmatrix}.
\]
The matrix $A$ is diagonal. The matrix $B$ has the distinct real
eigenvalues $0$ and $2$, so it is diagonalizable over $\RR$.
However,
\[
A+B=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}
\]
has only the eigenvalue $1$ and a one-dimensional eigenspace, so it is
not diagonalizable.

:::

:::

::: pf-step

Statement 12 is false.


::: pf-proof

The $5\times4$ matrix
\[
\begin{pmatrix}
1&0&0&0\\
0&1&0&0\\
0&0&1&0\\
0&0&0&1\\
0&0&0&0
\end{pmatrix}
\]
has rank $4$, so by rank-nullity its kernel has dimension $0$. Hence its
kernel contains no nonzero vector.

:::

:::

::: pf-step

Statement 13 is false.


::: pf-proof

Take $A=I$. Then
$\ker A=\{0\}\subseteq\operatorname{im}A$, but $A^2=I\neq0$.

:::

:::

::: pf-step

Statement 14 is false.


::: pf-proof

The zeroth cosine coefficient is a positive constant multiple of
\[
\int_{-\pi}^{\pi}e^{-x^2}\,dx.
\]
The integrand is strictly positive, so this integral, and therefore
$a_0$, is strictly positive rather than zero.

:::

:::

::: pf-step

Statement 15 is true.


::: pf-proof

From
$Q_1R_1=Q_2R_2$ one obtains
\[
U:=Q_2^TQ_1=R_2R_1^{-1}.
\]
The left-hand expression shows that $U$ is orthogonal, while the
right-hand expression shows that $U$ is upper triangular. An upper
triangular orthogonal matrix is diagonal with diagonal entries in
$\{\pm1\}$. Since the diagonal entries of both $R_1$ and $R_2$ are
positive, every diagonal entry of $R_2R_1^{-1}$ is positive. Hence
$U=I$, and therefore $R_1=R_2$.

:::

:::

::: pf-step

Statement 16 is true.


::: pf-proof

For reflection in a line $L\subset\RR^2$, every vector has a
unique decomposition $v=v_L+v_\perp$ with $v_L\in L$ and
$v_\perp\in L^\perp$, and reflection sends
$v_L+v_\perp$ to $v_L-v_\perp$. Thus a vector is fixed exactly when
$v_\perp=0$, so the eigenspace for eigenvalue $1$ is precisely the
one-dimensional line $L$. Its geometric multiplicity is therefore $1$,
not $2$.

:::

:::

::: pf-step

Statement 17 is false.


::: pf-proof

Take $A=-2I_2$. Then every solution of $x'=Ax$ is
\[
x(t)=e^{-2t}x(0),
\]
so the origin is asymptotically stable. But every eigenvalue of $A$ is
$-2$, whose absolute value is $2>1$.

:::

:::

::: pf-step

Statement 18 is true.


::: pf-proof

The initial datum $\sin(14x)$ is a Laplacian eigenfunction:
\[
\frac{d^2}{dx^2}\sin(14x)=-196\sin(14x).
\]
Hence its heat evolution is
\[
u(x,t)=e^{-196t}\sin(14x).
\]
This satisfies $u_t=u_{xx}$ and $u(x,0)=\sin(14x)$, and
$|u(x,t)|\leq e^{-196t}\to0$. Thus the solution converges uniformly to
$0$ as $t\to\infty$.

:::

:::

::: {.pf-step #s1-19}

Statement 19 is true.


::: pf-proof

By linearity of $A$,
\[
A(3v+2u)=3Av+2Au=3(5v)+2(-u)=15v-2u.
\]

:::

:::

::: {.pf-step #s1-20}

The recovered truth values, in order, are
\[
\boxed{\mathrm{F,F,T,T,F,T,F,T,T,T,F,F,F,F,T,T,F,T,T}}.
\]


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-19){.pf-ref} establish the corresponding truth values.

:::

:::

::: pf-qed

Step [](#s1-20){.pf-ref} records the required answers to all recovered statements.

:::

:::

:::
