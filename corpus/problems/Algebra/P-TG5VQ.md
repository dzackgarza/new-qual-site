---
schema: qual/card@1
id: P-TG5VQ
kind: problem
title: Solving linear ODEs with constant coefficients using linear algebra
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Eigenvalues and Eigenvectors
  - Linear Algebra
relations: []
review: draft
---

::: problem
How can a linear ordinary differential equation with constant coefficients be solved using linear algebra?
:::

::: solution
Consider first a scalar equation of order $n$,
\[
y^{(n)}+a_{n-1}y^{(n-1)}+\cdots+a_1y'+a_0y=0.
\]
Introduce the state vector
\[
Y=\begin{pmatrix}y\\y'\\\vdots\\y^{(n-1)}\end{pmatrix}.
\]
Then the equation is equivalent to the first-order system
\[
Y'=AY,
\]
where $A$ is the companion matrix
\[
A=
\begin{pmatrix}
0&1&0&\cdots&0\\
0&0&1&\cdots&0\\
\vdots&&&\ddots&\vdots\\
0&0&0&\cdots&1\\
-a_0&-a_1&-a_2&\cdots&-a_{n-1}
\end{pmatrix}.
\]

The solution with initial condition $Y(0)=Y_0$ is
\[
Y(t)=e^{tA}Y_0.
\]
Thus the problem reduces to computing the matrix exponential.

If $A$ is diagonalizable, say
\[
A=PDP^{-1},
\]
then
\[
e^{tA}=Pe^{tD}P^{-1},
\]
and the diagonal entries of $e^{tD}$ are $e^{\lambda_i t}$.

More generally, put $A$ in Jordan form. For a Jordan block
\[
J=\lambda I+N,
\qquad N^r=0,
\]
one has
\[
e^{tJ}=e^{\lambda t}e^{tN}
=e^{\lambda t}\sum_{k=0}^{r-1}\frac{t^kN^k}{k!}.
\]
This recovers the usual solutions $t^ke^{\lambda t}$ attached to repeated roots of the characteristic polynomial.
:::
