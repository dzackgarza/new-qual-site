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
<1>1. For the monic polynomial
\[
f(x)=x^2-x+2=x^2+a_1x+a_0
\]
with \(a_1=-1\) and \(a_0=2\), its companion matrix is
\[
M=\begin{pmatrix}0&-a_0\\1&-a_1\end{pmatrix}
 =\begin{pmatrix}0&-2\\1&1\end{pmatrix}.
\]
::: {.proof}
This is the standard companion matrix attached to a monic quadratic \(x^2+a_1x+a_0\).
:::

<1>2. The matrix \(M\) is annihilated by \(f\):
\[
M^2-M+2I_2=0.
\]
::: {.proof}
A direct multiplication gives
\[
M^2=
\begin{pmatrix}-2&-2\\1&-1\end{pmatrix}.
\]
Hence
\[
M^2-M+2I_2
=
\begin{pmatrix}-2&-2\\1&-1\end{pmatrix}
-
\begin{pmatrix}0&-2\\1&1\end{pmatrix}
+
\begin{pmatrix}2&0\\0&2\end{pmatrix}
=0.
\]
Thus the minimal polynomial \(m_M(x)\) divides \(f(x)\).
:::

<1>3. The minimal polynomial of \(M\) cannot have degree \(0\) or \(1\).
::: {.proof}
A nonzero constant polynomial cannot annihilate a matrix.
If a monic linear polynomial \(x-\lambda\) annihilated \(M\), then \(M=\lambda I_2\), but
\[
M=\begin{pmatrix}0&-2\\1&1\end{pmatrix}
\]
is not scalar.
:::

<1>4. Therefore \(m_M(x)=f(x)=x^2-x+2\).
::: {.proof}
By <1>2, \(m_M\mid f\), so \(\deg m_M\le2\). By <1>3, \(\deg m_M\ge2\). Both \(m_M\) and \(f\) are monic of degree \(2\), and divisibility then forces equality.
:::
:::
