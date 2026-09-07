---
schema: qual/card@1
id: P-ALGF11H
kind: problem
title: Jordan form of a companion-like $3\times 3$ matrix over $\mathbb{C}$ and $\overline{\mathbb{F}_3}$
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Jordan Canonical Form
  - Finite Fields
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 8 of the official UCSD Algebra Qualifying Exam, Fall 2011; both field cases and the matrix agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the cyclic-vector computation of the minimal polynomial and the resulting Jordan forms in characteristic 0 and characteristic 3.
---

::: {.problem}
Find the Jordan canonical form for the matrix
\[
\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix}.
\]

(a) Over the complex numbers.

(b) Over the algebraic closure of the field of three elements.
:::


::: {.solution}
Let
\[
A=
\begin{pmatrix}
0&1&0\\
0&0&1\\
1&0&0
\end{pmatrix}.
\]

<1>1. The characteristic and minimal polynomials of \(A\) are both
\[
t^3-1.
\]
::: {.proof}
A direct determinant computation gives
\[
\det(tI-A)
=
\det
\begin{pmatrix}
t&-1&0\\
0&t&-1\\
-1&0&t
\end{pmatrix}
=t^3-1.
\]
Also
\[
A^3=I,
\]
so the minimal polynomial divides \(t^3-1\).

On the other hand, if \(e_1,e_2,e_3\) are the standard basis vectors, then
\[
Ae_1=e_3,
\qquad
A^2e_1=e_2.
\]
Thus
\[
e_1,Ae_1,A^2e_1
\]
is a basis.
Hence \(e_1\) is a cyclic vector for \(A\), so the minimal polynomial has degree \(3\).
Since it divides the degree-3 polynomial \(t^3-1\), it must equal
\[
m_A(t)=t^3-1.
\]
:::

<1>2. Over \(\mathbb C\), the Jordan canonical form is
\[
\operatorname{diag}(1,\omega,\omega^2),
\]
where \(\omega=e^{2\pi i/3}\).
::: {.proof}
Over \(\mathbb C\),
\[
t^3-1=(t-1)(t-\omega)(t-\omega^2),
\]
and the three roots are distinct.
By <1>1, the minimal polynomial of \(A\) has no repeated factor over \(\mathbb C\).
Therefore \(A\) is diagonalizable.
Its eigenvalues are exactly the roots of its characteristic polynomial, namely
\[
1,\omega,\omega^2.
\]
Thus its Jordan form is
\[
\begin{pmatrix}
1&0&0\\
0&\omega&0\\
0&0&\omega^2
\end{pmatrix},
\]
up to reordering of the diagonal entries.
:::

<1>3. Over \(\overline{\mathbb F}_3\), the characteristic and minimal polynomials are
\[
(t-1)^3.
\]
::: {.proof}
In characteristic \(3\),
\[
t^3-1=(t-1)^3,
\]
because
\[
(t-1)^3=t^3-3t^2+3t-1=t^3-1.
\]
The cyclic-vector argument in <1>1 works over every field, so the minimal polynomial still has degree \(3\).
Hence over \(\overline{\mathbb F}_3\),
\[
m_A(t)=(t-1)^3.
\]
:::

<1>4. Over \(\overline{\mathbb F}_3\), the Jordan canonical form is one size-3 block
\[
J_3(1)=
\begin{pmatrix}
1&1&0\\
0&1&1\\
0&0&1
\end{pmatrix}.
\]
::: {.proof}
By <1>3, the only eigenvalue is \(1\), and the largest Jordan block has size equal to the exponent of \(t-1\) in the minimal polynomial, namely \(3\).
Since the whole vector space has dimension \(3\), there must be exactly one Jordan block, of size \(3\).
Thus the Jordan form is \(J_3(1)\).
:::
:::
