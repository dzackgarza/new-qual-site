---
schema: qual/card@1
id: P-5H7FG
kind: problem
title: Rational and Jordan canonical forms of a given matrix in $M_4(\mathbb{C})$
classification:
  areas:
  - algebra
  topics:
  - Rational Canonical Form
  - Jordan Canonical Form
  - Matrices
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

::: problem
Exhibit the rational and Jordan canonical forms for the following matrix $A\in M_4(\CC)$:
  \[
  A=\left(\begin{array}{cccc}
  2 & 0 & 0 & 0 \\
  1 & 1 & 0 & 0 \\
  -2 & -2 & 0 & 1 \\
  -2 & 0 & -1 & -2
  \end{array}\right)
  .\]
:::


::: {.solution}
<1>1. The characteristic polynomial is
\[
\chi_A(x)=(x-2)(x-1)(x+1)^2.
\]
::: {.proof}
A direct determinant computation gives
\[
\det(xI-A)=(x-2)(x-1)(x+1)^2.
\]
Thus the eigenvalues are \(2,1,-1\), with algebraic multiplicities \(1,1,2\), respectively.
:::

<1>2. The eigenspace for \(-1\) has dimension \(1\).
::: {.proof}
Solving \((A+I)v=0\) gives a one-dimensional kernel. Hence the geometric multiplicity of the eigenvalue \(-1\) is \(1\).
:::

<1>3. The Jordan canonical form is
\[
J_2(-1)\oplus [1]\oplus[2].
\]
::: {.proof}
The eigenvalues \(1\) and \(2\) are simple, so each contributes a \(1\times1\) Jordan block. The eigenvalue \(-1\) has algebraic multiplicity \(2\) but geometric multiplicity \(1\), so it contributes exactly one Jordan block of size \(2\).
:::

<1>4. The minimal polynomial is
\[
m_A(x)=(x+1)^2(x-1)(x-2)=\chi_A(x).
\]
::: {.proof}
The largest Jordan block for \(-1\) has size \(2\), so \((x+1)^2\) divides the minimal polynomial. The simple eigenvalues \(1\) and \(2\) force the factors \(x-1\) and \(x-2\). Their product already has degree \(4\), equal to the characteristic polynomial, so the two polynomials coincide.
:::

<1>5. Therefore the rational canonical form consists of a single companion block for
\[
m_A(x)=x^4-x^3-3x^2+x+2.
\]
With the convention that the companion matrix of
\[
x^4+a_3x^3+a_2x^2+a_1x+a_0
\]
is
\[
\begin{pmatrix}
0&0&0&-a_0\\
1&0&0&-a_1\\
0&1&0&-a_2\\
0&0&1&-a_3
\end{pmatrix},
\]
the rational canonical form is
\[
\begin{pmatrix}
0&0&0&-2\\
1&0&0&-1\\
0&1&0&3\\
0&0&1&1
\end{pmatrix}.
\]
::: {.proof}
Since \(m_A=\chi_A\), the \(\mathbb C[x]\)-module defined by \(A\) has a single invariant factor. Rational canonical form is therefore one companion matrix for that invariant factor.
:::
:::
