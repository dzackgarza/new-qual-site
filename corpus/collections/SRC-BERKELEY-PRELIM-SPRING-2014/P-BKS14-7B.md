---
schema: qual/card@1
id: P-BKS14-7B
kind: problem
title: Compute a high power of a three-by-three matrix
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2014 preliminary examination PDF.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the characteristic and minimal polynomials and the degree-two interpolation of t^16 at eigenvalues 0, 2, and 3.
---

::: {.problem}
Let
\[
A=\begin{pmatrix}
\frac52&0&-\frac12\\
0&3&0\\
\frac52&0&-\frac12
\end{pmatrix}.
\]
Calculate \(A^{16}\). You may give your answer as a polynomial in \(A\) of degree at most \(2\).
:::

::: {.solution}
<1>1. The characteristic polynomial of $A$ is
$$
\chi_A(t)
=
t(t-2)(t-3).
$$

::: {.proof}
Because the second coordinate is separated from the first and third,
$$
\begin{aligned}
\det(tI-A)
&=
(t-3)
\det
\begin{pmatrix}
t-\frac52&\frac12\\
-\frac52&t+\frac12
\end{pmatrix}\\
&=
(t-3)
\left(
\left(t-\frac52\right)\left(t+\frac12\right)
+\frac54
\right)\\
&=
(t-3)(t^2-2t)\\
&=
t(t-2)(t-3).
\end{aligned}
$$
:::

<1>2. The minimal polynomial of $A$ is
$$
m_A(t)=t(t-2)(t-3).
$$

::: {.proof}
Step <1>1 shows that the three distinct numbers
$$
0,\ 2,\ 3
$$
are eigenvalues of $A$. Every eigenvalue is a root of the minimal
polynomial, so $m_A$ is divisible by each of the three distinct linear
factors
$$
t,\quad t-2,\quad t-3.
$$
On the other hand, the Cayley--Hamilton theorem makes $m_A$ divide
$\chi_A$. Hence equality holds.
:::

<1>3. There are unique constants $a,b,c$ such that the remainder of
$t^{16}$ upon division by $m_A(t)$ is
$$
r(t)=at^2+bt+c.
$$
They satisfy
$$
c=0,
$$
$$
4a+2b=2^{16},
$$
and
$$
9a+3b=3^{16}.
$$

::: {.proof}
Polynomial division gives a unique remainder of degree at most $2$.
Since
$$
t^{16}-r(t)
$$
is divisible by
$$
t(t-2)(t-3),
$$
the two polynomials agree at $t=0,2,3$. Substitution gives exactly the
three displayed equations.
:::

<1>4. The coefficients are
$$
a=3^{15}-2^{15}
$$
and
$$
b=3\cdot2^{15}-2\cdot3^{15}.
$$

::: {.proof}
Divide the last two equations in step <1>3 by $2$ and $3$ respectively:
$$
2a+b=2^{15},
$$
$$
3a+b=3^{15}.
$$
Subtracting gives
$$
a=3^{15}-2^{15}.
$$
Substitute this into the first equation:
$$
\begin{aligned}
b
&=
2^{15}-2a\\
&=
2^{15}-2(3^{15}-2^{15})\\
&=
3\cdot2^{15}-2\cdot3^{15}.
\end{aligned}
$$
:::

<1>5. Therefore
$$
\boxed{
A^{16}
=
(3^{15}-2^{15})A^2
+
(3\cdot2^{15}-2\cdot3^{15})A
}.
$$

::: {.proof}
There is a polynomial $q(t)$ such that
$$
t^{16}
=
q(t)m_A(t)+r(t).
$$
Evaluate this identity at $A$. By the definition of the minimal
polynomial,
$$
m_A(A)=0.
$$
Hence
$$
A^{16}=r(A).
$$
Now apply steps <1>3 and <1>4, with $c=0$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the requested calculation.
:::
:::
