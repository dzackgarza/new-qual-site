---
schema: qual/card@1
id: P-APASP09C
kind: problem
title: "The Moore–Penrose pseudo-inverse gives the minimum-norm least-squares solution"
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Compared with Problem 3 of the Applied Algebra section of the official UCSD Spring 2009 qualifying-exam PDF.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Used the SVD coordinates to characterize all least-squares solutions and showed the pseudoinverse solution uniquely minimizes the Euclidean norm by setting the nullspace coordinates to zero.
---

::: problem
Let $\tilde{x}$ be a least squares solution to $Ax = b$, where $A$ is $m \times n$ and $m \geq n$.
Let $A^\dagger$ be the pseudo-inverse of $A$.
Use the Singular Value Decomposition to show that $\tilde{x} = A^\dagger b$ is the minimum 2-norm least squares solution to $Ax = b$, i.e.\ show

(a) $\tilde{x}$ is a least squares solution,

(b) if $\hat{x}$ is a least squares solution then $\|\hat{x}\|_2 \geq \|\tilde{x}\|_2$, and

(c) $\tilde{x}$ is unique.
:::

::: {.solution}
Let $r=\operatorname{rank}A$ and choose a singular value decomposition
\[
A=U\Sigma V^H,
\]
where $U\in\mathbb C^{m\times m}$ and $V\in\mathbb C^{n\times n}$ are unitary and
\[
\Sigma=
\begin{pmatrix}
D&0\\0&0
\end{pmatrix},
\qquad
D=\operatorname{diag}(\sigma_1,\ldots,\sigma_r),
\qquad
\sigma_i>0.
\]
Write
\[
c=U^Hb,
\qquad
y=V^Hx.
\]
Because $U$ and $V$ are unitary,
\[
\|Ax-b\|_2=\|\Sigma y-c\|_2
\qquad\text{and}\qquad
\|x\|_2=\|y\|_2.
\]

<1>1. A vector $x$ is a least-squares solution if and only if, in the coordinates $y=V^Hx$,
\[
y_i=\frac{c_i}{\sigma_i}\qquad(1\le i\le r),
\]
while $y_{r+1},\ldots,y_n$ are arbitrary.
::: {.proof}
We have
\[
\|\Sigma y-c\|_2^2
=\sum_{i=1}^r|\sigma_i y_i-c_i|^2
 +\sum_{i=r+1}^m|c_i|^2.
\]
The second sum is independent of $y$.
Each term in the first sum is nonnegative and is uniquely minimized by
\[
y_i=c_i/\sigma_i.
\]
The coordinates $y_i$ for $i>r$ do not occur in the residual and are therefore unrestricted.
:::

<1>2. The vector
\[
\widetilde x=A^\dagger b
\]
is a least-squares solution.
::: {.proof}
For the SVD above,
\[
A^\dagger=V\Sigma^\dagger U^H,
\]
where $\Sigma^\dagger\in\mathbb C^{n\times m}$ has diagonal entries
\[
\sigma_1^{-1},\ldots,\sigma_r^{-1}
\]
in its first $r$ diagonal positions and zeros elsewhere.
Thus for $\widetilde x=A^\dagger b$,
\[
V^H\widetilde x=\Sigma^\dagger c,
\]
whose coordinates are
\[
\widetilde y_i=c_i/\sigma_i\quad(1\le i\le r),
\qquad
\widetilde y_i=0\quad(i>r).
\]
By <1>1 this is a least-squares solution.
:::

<1>3. If $\widehat x$ is any least-squares solution, then
\[
\|\widehat x\|_2\ge\|\widetilde x\|_2.
\]
::: {.proof}
Let
\[
\widehat y=V^H\widehat x.
\]
By <1>1,
\[
\widehat y_i=\widetilde y_i=c_i/\sigma_i
\qquad(1\le i\le r),
\]
while the coordinates $\widehat y_i$ for $i>r$ may be arbitrary.
Hence
\[
\|\widehat x\|_2^2
=\|\widehat y\|_2^2
=\sum_{i=1}^r\left|\frac{c_i}{\sigma_i}\right|^2
 +\sum_{i=r+1}^n|\widehat y_i|^2
\ge
\sum_{i=1}^r\left|\frac{c_i}{\sigma_i}\right|^2
=\|\widetilde x\|_2^2.
\]
:::

<1>4. The minimum-norm least-squares solution is unique.
::: {.proof}
Equality in <1>3 holds if and only if
\[
\widehat y_i=0\qquad(i>r).
\]
But then every coordinate of $\widehat y$ agrees with $\widetilde y$, so
\[
\widehat y=\widetilde y.
\]
Since $V$ is invertible,
\[
\widehat x=V\widehat y=V\widetilde y=\widetilde x.
\]
Thus $A^\dagger b$ is the unique least-squares solution of minimum Euclidean norm.
:::
:::
