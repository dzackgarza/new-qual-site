---
schema: qual/card@1
id: E-SMI-8000E-MT5
kind: problem
title: The Cayley-Hamilton theorem
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the statement with Smith 8000 Fall 2006 midterm problem 5."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Proved Cayley--Hamilton from the adjugate identity by comparing polynomial-matrix coefficients and telescoping, avoiding the invalid direct substitution of A into a matrix polynomial with non-scalar coefficients."
---

::: {.exercise}
State and prove the Cayley-Hamilton theorem.
:::

::: solution
<1>1. State the theorem.
::: proof
Let $V$ be a finite-dimensional vector space over a field $F$, and let
$T\in\operatorname{End}_F(V)$. Its characteristic polynomial is
$$
\chi_T(x)=\det(xI-T).
$$
The Cayley--Hamilton theorem states that $T$ satisfies its own characteristic
polynomial:
$$
\boxed{\chi_T(T)=0.}
$$
Equivalently, if $A$ is any $n\times n$ matrix over $F$ and
$$
\chi_A(x)=\det(xI-A),
$$
then
$$
\chi_A(A)=0.
$$
:::

<1>2. Apply the adjugate identity to the polynomial matrix $xI-A$.
::: proof
Work in the matrix ring $M_n(F[x])$. The adjugate identity gives
$$
(xI-A)\operatorname{adj}(xI-A)
=\det(xI-A)I
=\chi_A(x)I.
$$
Write
$$
\chi_A(x)=a_0+a_1x+\cdots+a_nx^n,
\qquad a_n=1,
$$
and write the adjugate as
$$
\operatorname{adj}(xI-A)
=C_0+C_1x+\cdots+C_{n-1}x^{n-1},
$$
where $C_i\in M_n(F)$.
:::

<1>3. Compare coefficients of powers of $x$.
::: proof
Expanding the identity in step <1>2 gives
$$
\begin{aligned}
-AC_0&=a_0I,\\
C_0-AC_1&=a_1I,\\
C_1-AC_2&=a_2I,\\
&\ \vdots\\
C_{n-2}-AC_{n-1}&=a_{n-1}I,\\
C_{n-1}&=a_nI=I.
\end{aligned}
$$
These are ordinary matrix identities over $F$.
:::

<1>4. Multiply by successive powers of $A$ and telescope.
::: proof
Multiply the first identity by $I$, the second by $A$, the third by $A^2$,
and so on, always on the left. This yields
$$
\begin{aligned}
a_0I&=-AC_0,\\
a_1A&=AC_0-A^2C_1,\\
a_2A^2&=A^2C_1-A^3C_2,\\
&\ \vdots\\
a_{n-1}A^{n-1}
&=A^{n-1}C_{n-2}-A^nC_{n-1},\\
a_nA^n&=A^nC_{n-1}.
\end{aligned}
$$
Adding all of these equations cancels every term involving a $C_i$. Hence
$$
a_0I+a_1A+\cdots+a_nA^n=0.
$$
The left side is precisely $\chi_A(A)$, so
$$
\boxed{\chi_A(A)=0.}
$$
This proves the Cayley--Hamilton theorem.
:::
:::
