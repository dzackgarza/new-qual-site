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
- event: source-checked
  by: OpenAI
  date: 2026-09-09
  note: Checked against the UCR qualifying-algebra linear algebra problem list.
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
<1>1. For a monic quadratic
\[
f(x)=x^2+a_1x+a_0,
\]
we use the companion-matrix convention
\[
C_f=\begin{pmatrix}0&-a_0\\1&-a_1\end{pmatrix}.
\]
Hence for \(f(x)=x^2-x+2\),
\[
M=\begin{pmatrix}0&-2\\1&1\end{pmatrix}.
\]
::: {.proof}
Here \(a_1=-1\) and \(a_0=2\), so substituting into the standard companion form gives the displayed matrix.
:::

<1>2. The characteristic polynomial of \(M\) is \(f\).
::: {.proof}
We compute
\[
\det(xI-M)
=\det\begin{pmatrix}x&2\\-1&x-1\end{pmatrix}
=x(x-1)+2
=x^2-x+2=f(x).
\]
:::

<1>3. The minimal polynomial of \(M\) has degree \(2\).
::: {.proof}
The vector \(e_1=(1,0)^T\) satisfies
\[
Me_1=e_2.
\]
Thus \(e_1,Me_1\) are linearly independent, so no nonzero polynomial of degree at most \(1\) can annihilate \(M\). Hence the minimal polynomial has degree at least \(2\). Since \(M\) is \(2\times2\), Cayley-Hamilton implies that its minimal polynomial has degree at most \(2\).
:::

<1>4. Therefore the minimal polynomial of \(M\) is \(f(x)=x^2-x+2\).
::: {.proof}
By <1>2, \(f(M)=0\). By <1>3, the monic minimal polynomial has degree \(2\), and it divides the characteristic polynomial \(f\), also monic of degree \(2\). Therefore they are equal.
:::
:::
