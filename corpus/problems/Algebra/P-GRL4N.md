---
schema: qual/card@1
id: P-GRL4N
kind: problem
title: Jordan and rational canonical forms for $\chi_A=(x-1)^2(x+1)^2$ and $p_A=(x-1)(x+1)^2$
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Rational Canonical Form
  - Minimal and Characteristic Polynomials
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
Let $A$ be a $4\times4$ matrix over a field of characteristic not equal to $2$ with
\[
\chi_A(x)=(x-1)^2(x+1)^2
\]
and minimal polynomial
\[
m_A(x)=(x-1)(x+1)^2.
\]
Determine the Jordan canonical form and rational canonical form of $A$.
:::


::: {.solution}
<1>1. The Jordan blocks for the eigenvalue $1$ are two $1\times1$ blocks.
::: {.proof}
The algebraic multiplicity of $1$ is $2$. The exponent of $x-1$ in the minimal polynomial is $1$, so the largest Jordan block for $1$ has size $1$. Therefore both units of algebraic multiplicity occur as separate $1\times1$ blocks.
:::

<1>2. The Jordan blocks for the eigenvalue $-1$ consist of one $2\times2$ block.
::: {.proof}
The algebraic multiplicity of $-1$ is $2$, while the exponent of $x+1$ in the minimal polynomial is $2$. Hence there must be a block of size $2$, which exhausts the full algebraic multiplicity.
:::

<1>3. Thus
\[
J(A)=J_2(-1)\oplus[1]\oplus[1].
\]
::: {.proof}
Combine <1>1 and <1>2.
:::

<1>4. The invariant factors are
\[
d_1=x-1,
\qquad
d_2=(x-1)(x+1)^2.
\]
::: {.proof}
The largest invariant factor is the minimal polynomial. Their product is the characteristic polynomial, so
\[
d_1=\frac{\chi_A}{d_2}=x-1.
\]
The divisibility condition $d_1\mid d_2$ holds.
:::

<1>5. Therefore the rational canonical form is
\[
C(x-1)\oplus C((x-1)(x+1)^2).
\]
::: {.proof}
Rational canonical form is the direct sum of the companion matrices of the invariant factors. Since
\[
(x-1)(x+1)^2=x^3+x^2-x-1,
\]
one standard companion-matrix convention gives
\[
\begin{pmatrix}
0&0&1\\
1&0&1\\
0&1&-1
\end{pmatrix}
\]
for the cubic factor, together with the $1\times1$ block $[1]$.
:::
:::
