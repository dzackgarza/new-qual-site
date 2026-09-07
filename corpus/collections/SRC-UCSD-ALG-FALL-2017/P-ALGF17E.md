---
schema: qual/card@1
id: P-ALGF17E
kind: problem
title: Companion-like matrix over $\mathbb{Q}(y)$ vs $\mathbb{F}_3(y)$; irreducibility and diagonalizability
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Field Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 5 of the official UCSD Algebra Qualifying Exam, Fall 2017; the matrix and all three parts agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the characteristic polynomial x^3+y, Eisenstein irreducibility over Q(y), separability in characteristic zero, and the single repeated eigenvalue with cubic minimal polynomial in characteristic three.
---

::: {.problem}
Consider the matrix
\[
A = \begin{pmatrix} 0 & 0 & -y \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}
\]
where $y$ is an indeterminate.

(a) Show that the characteristic polynomial $f(x)$ of $A$ is irreducible in $\mathbb{Q}(y)[x]$.

(b) Show that $A$ is diagonalisable over the algebraic closure of $\mathbb{Q}(y)$.

(c) Show that $A$ is not diagonalisable over the algebraic closure of $\mathbb{F}_3(y)$.
:::

::: {.solution}
<1>1. The characteristic polynomial of $A$ is
\[
f(x)=x^3+y.
\]
::: {.proof}
One computes
\[
xI-A=
\begin{pmatrix}
x&0&y\\
-1&x&0\\
0&-1&x
\end{pmatrix}.
\]
Expanding the determinant along the first row gives
\[
\det(xI-A)=x^3+y.
\]
:::

<1>2. The polynomial $x^3+y$ is irreducible in $\mathbb Q(y)[x]$.
::: {.proof}
Regard
\[
x^3+y
\]
as an element of the polynomial ring $\mathbb Q[y][x]$.
The coefficient ring $\mathbb Q[y]$ is a UFD, and $y$ is prime in it.
All non-leading coefficients of $x^3+y$ are divisible by $y$, while the constant coefficient $y$ is not divisible by $y^2$.
Thus Eisenstein's criterion at the prime $y$ shows that $x^3+y$ is irreducible in
\[
\mathbb Q[y][x].
\]
It is primitive as a polynomial in $x$, so Gauss's lemma implies that it remains irreducible over the fraction field
\[
\operatorname{Frac}(\mathbb Q[y])=\mathbb Q(y).
\]
This proves part (a).
:::

<1>3. Over $\mathbb Q(y)$, the minimal polynomial of $A$ equals $x^3+y$.
::: {.proof}
Let $e_1,e_2,e_3$ be the standard basis vectors.
Directly from the columns of $A$,
\[
Ae_1=e_2,
\qquad
A^2e_1=e_3.
\]
Hence
\[
e_1,Ae_1,A^2e_1
\]
is a basis.
Thus $e_1$ is a cyclic vector and the minimal polynomial of $A$ has degree $3$.
By Cayley--Hamilton it divides the characteristic polynomial, which also has degree $3$.
Therefore
\[
m_A(x)=x^3+y.
\]
:::

<1>4. The matrix $A$ is diagonalizable over the algebraic closure of $\mathbb Q(y)$.
::: {.proof}
In characteristic zero,
\[
f'(x)=3x^2.
\]
The polynomials $x^3+y$ and $3x^2$ are relatively prime in $\mathbb Q(y)[x]$, because $y\neq0$ in the field $\mathbb Q(y)$.
Thus $x^3+y$ has three distinct roots in an algebraic closure.
By <1>3, this is the minimal polynomial of $A$, so the minimal polynomial splits into distinct linear factors over the algebraic closure.
Therefore $A$ is diagonalizable there.
This proves part (b).
:::

<1>5. Over $\mathbb F_3(y)$, the minimal polynomial of $A$ is still $x^3+y$.
::: {.proof}
The cyclic-vector computation from <1>3 uses only the displayed matrix and therefore remains valid over $\mathbb F_3(y)$:
\[
e_1,Ae_1,A^2e_1
\]
is still a basis.
Hence the minimal polynomial has degree $3$.
The characteristic polynomial remains
\[
x^3+y,
\]
so Cayley--Hamilton again gives
\[
m_A(x)=x^3+y.
\]
:::

<1>6. The matrix $A$ is not diagonalizable over the algebraic closure of $\mathbb F_3(y)$.
::: {.proof}
Let $\overline F$ be an algebraic closure of $\mathbb F_3(y)$ and choose $\alpha\in\overline F$ with
\[
\alpha^3=-y.
\]
In characteristic $3$,
\[
(x-\alpha)^3=x^3-\alpha^3=x^3+y.
\]
Thus over $\overline F$ the characteristic polynomial has only the single root $\alpha$, with multiplicity $3$.
By <1>5, the minimal polynomial has degree $3$; equivalently after scalar extension it is
\[
(x-\alpha)^3.
\]
This polynomial has a repeated factor, so the minimal polynomial is not squarefree.
Therefore $A$ is not diagonalizable over $\overline F$.
This proves part (c).
:::
:::
