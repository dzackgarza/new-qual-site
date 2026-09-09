---
schema: qual/card@1
id: P-APAF06A
kind: problem
title: Eigenpair of algebraic and geometric multiplicity one yields a complementary block form
classification:
  areas:
  - applied-algebra
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
Assume that $(\lambda, x)$ is an eigenpair of $A \in M_n$ such that
$am(\lambda) = gm(\lambda) = 1$. Prove that there exists a nonsingular matrix
$(x \quad X)$ with inverse $(y \quad Y)^*$ such that
\[
\begin{pmatrix} y^* \\ Y^* \end{pmatrix} A (x \quad X) = \begin{pmatrix} \lambda & 0 \\ 0 & M \end{pmatrix}.
\]
:::

::: {.solution}
<1>1. Let \(y\neq 0\) be a left eigenvector for \(\lambda\), so
\[
y^*A=\lambda y^*.
\]
Then one may choose \(y\) so that \(y^*x=1\).
::: {.proof}
Since \(\lambda\) has algebraic multiplicity one for \(A\), it also has algebraic
multiplicity one for \(A^*\), so a nonzero left eigenvector \(y\) exists. We claim that
\(y^*x\neq 0\). If \(y^*x=0\), then
\(x\in(\ker(A^*-\overline\lambda I))^\perp=\operatorname{im}(A-\lambda I)\). Thus there
is \(z\) with
\[
(A-\lambda I)z=x\neq 0,
\qquad
(A-\lambda I)x=0.
\]
Hence \(z,x\) form a Jordan chain of length at least two for \(\lambda\), contradicting
\(am(\lambda)=1\). Therefore \(y^*x\neq0\), and rescaling \(y\) gives \(y^*x=1\).
:::

<1>2. The hyperplane \(W:=\ker y^*\) is \(A\)-invariant and is complementary to
\(\operatorname{span}\{x\}\).
::: {.proof}
If \(w\in W\), then
\[
y^*Aw=\lambda y^*w=0,
\]
so \(Aw\in W\). Also \(y^*x=1\), so \(x\notin W\). Since \(W\) has codimension one,
\[
\mathbb C^n=\operatorname{span}\{x\}\oplus W.
\]
:::

<1>3. Choose a matrix \(X\in M_{n,n-1}\) whose columns form a basis of \(W\). Then
\((x\ \ X)\) is nonsingular, and its inverse has the form
\[
(x\ \ X)^{-1}=\begin{pmatrix}y^*\\Y^*\end{pmatrix}
\]
for some \(Y\in M_{n,n-1}\).
::: {.proof}
By <1>2 the columns \(x\) together with a basis of \(W\) form a basis of
\(\mathbb C^n\), so \((x\ \ X)\) is nonsingular. Because \(y^*x=1\) and \(y^*X=0\), the
first row of its inverse is exactly \(y^*\); denote the remaining rows by \(Y^*\).
:::

<1>4. There is a matrix \(M\in M_{n-1}\) such that
\[
AX=XM.
\]
::: {.proof}
By <1>2, \(W=\operatorname{im}X\) is \(A\)-invariant. Hence each column of \(AX\) is a
linear combination of the columns of \(X\), and these coefficients form a unique matrix
\(M\).
:::

<1>5. Therefore
\[
A(x\ \ X)=(x\ \ X)
\begin{pmatrix}
\lambda&0\\
0&M
\end{pmatrix},
\]
and hence
\[
\begin{pmatrix}y^*\\Y^*\end{pmatrix}
A(x\ \ X)=
\begin{pmatrix}
\lambda&0\\
0&M
\end{pmatrix}.
\]
::: {.proof}
The first column identity is \(Ax=\lambda x\), and the remaining columns are <1>4.
Multiplying on the left by \((x\ \ X)^{-1}=\begin{pmatrix}y^*\\Y^*\end{pmatrix}\) gives
the required block form.
:::
:::
