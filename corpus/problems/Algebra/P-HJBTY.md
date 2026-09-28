---
schema: qual/card@1
id: P-HJBTY
kind: problem
title: Rational canonical forms of $3\times 3$ matrices over $\QQ$ annihilated by
  $(x^2+2)(x-1)^3$
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
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
What $3 \times 3$ matrices over $\mathbb{Q}$ (up to similarity) satisfy $f(A) = 0$, where $f(x) = (x^2 + 2)(x - 1)^3$?
List all possible invariant factor lists and rational canonical forms.
:::

::: {.solution}
Let
\[
f(x)=(x^2+2)(x-1)^3.
\]
For $A\in M_3(\mathbb Q)$, the condition $f(A)=0$ is equivalent to $\mu_A\mid f$. Since $x^2+2$ and $x-1$ are the irreducible factors of $f$, and $\deg\chi_A=3$, there are two possible characteristic-polynomial types.

If
\[
\chi_A=(x^2+2)(x-1),
\]
then both coprime irreducible factors must occur in the minimal polynomial, so
\[
\mu_A=(x^2+2)(x-1)=\chi_A.
\]
Thus the invariant-factor list is
\[
[(x^2+2)(x-1)],
\]
and the rational canonical form is
\[
C(x^3-x^2+2x-2)
=\begin{pmatrix}
0&0&2\\
1&0&-2\\
0&1&1
\end{pmatrix}.
\]

If
\[
\chi_A=(x-1)^3,
\]
the invariant factors are powers of $x-1$ whose degrees sum to $3$ and form a divisibility chain. Hence exactly three lists occur:
\[
[x-1,x-1,x-1],
\]
\[
[x-1,(x-1)^2],
\]
and
\[
[(x-1)^3].
\]
Their rational canonical forms are respectively
\[
I_3,
\]
\[
\operatorname{diag}\!\left(1,
\begin{pmatrix}0&-1\\1&2\end{pmatrix}\right),
\]
and
\[
\begin{pmatrix}
0&0&1\\
1&0&-3\\
0&1&3
\end{pmatrix}.
\]

Therefore there are exactly four similarity classes satisfying $f(A)=0$.
:::
