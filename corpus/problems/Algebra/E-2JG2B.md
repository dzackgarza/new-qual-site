---
schema: qual/card@1
id: E-2JG2B
kind: problem
title: Companion matrix of $x^{2}-x+2$ over $\mathbb{C}$
classification:
  areas:
  - algebra
  topics:
  - Rational Canonical Form
  - Minimal and Characteristic Polynomials
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
5. What is the companion matrix $M$ of the polynomial $f=x^{2}-x+2$ over $C$ ? Prove that $f$ is the minimal polynomial of $M$.
:::

::: {.solution}
<1>1. Write
\[
f(x)=x^2-x+2=x^2+a_1x+a_0
\]
with \(a_1=-1\) and \(a_0=2\). Its companion matrix is
\[
M=
\begin{pmatrix}
0&-a_0\\
1&-a_1
\end{pmatrix}
=
\begin{pmatrix}
0&-2\\
1&1
\end{pmatrix}.
\]
::: {.proof}
This is the standard companion-matrix construction for a monic quadratic polynomial \(x^2+a_1x+a_0\).
:::

<1>2. The characteristic polynomial of \(M\) is \(f\).
::: {.proof}
One computes
\[
\det(xI-M)
=
\det\begin{pmatrix}x&2\\-1&x-1\end{pmatrix}
=x(x-1)+2
=x^2-x+2=f(x).
\]
:::

<1>3. The minimal polynomial \(m_M(x)\) divides \(f(x)\).
::: {.proof}
By the Cayley--Hamilton theorem, \(f(M)=0\), since \(f\) is the characteristic polynomial of \(M\). Hence the minimal polynomial divides \(f\).
:::

<1>4. The minimal polynomial cannot have degree \(1\).
::: {.proof}
If \(m_M\) had degree \(1\), then \(m_M(x)=x-\lambda\) for some \(\lambda\in\mathbb C\), so \(M=\lambda I\). But
\[
M=
\begin{pmatrix}0&-2\\1&1\end{pmatrix}
\]
is not a scalar matrix.
:::

<1>5. Therefore \(m_M(x)=f(x)=x^2-x+2\).
::: {.proof}
By <1>3, \(m_M\mid f\), and by <1>4, \(\deg m_M\neq1\). Since \(M\) is not the zero-dimensional operator, \(m_M\) is nonconstant; thus \(\deg m_M=2=\deg f\). Both polynomials are monic, so divisibility implies equality.
:::
:::
