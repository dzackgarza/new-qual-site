---
schema: qual/card@1
id: P-EQE3U
kind: problem
title: "A degree-5 irreducible over Z/2, the field of 32 elements, and a matrix of order 31"
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Galois Theory
  - Linear Algebra
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
- Find an irreducible polynomial of degree 5 over the field $\mathbb Z/2$ of two elements and use it to construct a field of order 32 as a quotient of the polynomial ring $\mathbb Z/2[x]$.

- Using the polynomial found in part (a), find a $5\times5$ matrix $M$ over $\mathbb Z/2$ of order 31, so that $M^{31}=I$ but $M\neq I$.
:::


::: {.solution}
<1>1. The polynomial
\[
f(x)=x^5+x^2+1\in\mathbb F_2[x]
\]
is irreducible.
::: {.proof}
A reducible polynomial of degree \(5\) must have an irreducible factor of degree \(1\) or \(2\). We have
\[
f(0)=1,
\qquad
f(1)=1+1+1=1,
\]
so \(f\) has no linear factor. The only monic irreducible quadratic over \(\mathbb F_2\) is
\[
q(x)=x^2+x+1.
\]
Modulo \(q\), we have \(x^3=1\), hence \(x^5=x^2\), so
\[
f(x)\equiv x^2+x^2+1=1\pmod q.
\]
Thus \(q\nmid f\). Therefore \(f\) is irreducible.
:::

<1>2. Consequently
\[
F=\mathbb F_2[x]/(f(x))
\]
is a field with \(2^5=32\) elements.
::: {.proof}
Since \(f\) is irreducible of degree \(5\), the quotient is a field and has \(2^5\) elements as a \(5\)-dimensional vector space over \(\mathbb F_2\).
:::

<1>3. Let \(\alpha\) denote the image of \(x\) in \(F\). Then \(\alpha\) has multiplicative order \(31\).
::: {.proof}
The multiplicative group \(F^\times\) has
\[
|F^\times|=32-1=31
\]
elements. Since \(31\) is prime, every nonidentity element of \(F^\times\) has order \(31\). The element \(\alpha\) is nonzero because \(f(0)\ne0\), and \(\alpha\ne1\) because \(f(1)\ne0\). Hence \(\alpha\) has order \(31\).
:::

<1>4. With respect to the basis
\[
1,\alpha,\alpha^2,\alpha^3,\alpha^4
\]
of \(F\) over \(\mathbb F_2\), multiplication by \(\alpha\) is represented by
\[
M=
\begin{pmatrix}
0&0&0&0&1\\
1&0&0&0&0\\
0&1&0&0&1\\
0&0&1&0&0\\
0&0&0&1&0
\end{pmatrix}.
\]
::: {.proof}
The first four columns record
\[
\alpha\cdot1=\alpha,
\quad
\alpha\cdot\alpha=\alpha^2,
\quad
\alpha\cdot\alpha^2=\alpha^3,
\quad
\alpha\cdot\alpha^3=\alpha^4.
\]
Since \(f(\alpha)=0\),
\[
\alpha^5+\alpha^2+1=0,
\]
so in characteristic \(2\),
\[
\alpha^5=\alpha^2+1,
\]
which gives the last column.
:::

<1>5. The matrix \(M\) has order \(31\).
::: {.proof}
The linear transformation represented by \(M\) is multiplication by \(\alpha\). Therefore \(M^k\) represents multiplication by \(\alpha^k\). By <1>3,
\[
\alpha^{31}=1
\quad\text{and}\quad
\alpha\ne1,
\]
so
\[
M^{31}=I
\quad\text{and}\quad
M\ne I.
\]
As \(31\) is prime, the order of \(M\) is exactly \(31\).
:::
:::
