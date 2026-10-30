---
schema: qual/card@1
id: P-6ET4N
kind: problem
title: Rational and Jordan canonical forms of a $3\times 3$ real matrix; abelian groups of order $360$
classification:
  areas:
  - prelim
  topics:
  - Jordan Canonical Form
  - Rational Canonical Form
  - Abelian Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---
::: {.problem}
(a) Find a rational canonical form and a Jordan canonical form for the following $3 \times 3$ matrix with real entries:
$$A = \begin{pmatrix} 0 & -1 & 2 \\ 3 & -4 & 6 \\ 2 & -2 & 3 \end{pmatrix}.$$

(b) Describe the distinct isomorphism classes of Abelian groups of order $360$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The characteristic polynomial of $A$ is
$$
\chi_A(t)=(t-1)(t+1)^2.
$$

::: pf-proof

One computes
$$
tI-A=
\begin{pmatrix}
t&1&-2\\
-3&t+4&-6\\
-2&2&t-3
\end{pmatrix},
$$
and expansion along the first row gives
$$
\begin{aligned}
\det(tI-A)
&=t\bigl((t+4)(t-3)+12\bigr)
-\bigl(-3(t-3)-12\bigr)\\
&\qquad
-2\bigl(-6+2(t+4)\bigr)\\
&=t^3+t^2-t-1\\
&=(t-1)(t+1)^2.
\end{aligned}
$$

:::

:::

::: {.pf-step #s2}

The matrix $A$ is diagonalizable over $\RR$, and its minimal
polynomial is
$$
m_A(t)=(t-1)(t+1)=t^2-1.
$$

::: pf-proof

For the eigenvalue $-1$,
$$
-I-A=
\begin{pmatrix}
-1&1&-2\\
-3&3&-6\\
-2&2&-4
\end{pmatrix}
$$
has rank $1$, because every row is a scalar multiple of the first.
Therefore
$$
\dim\ker(A+I)=2,
$$
which equals the algebraic multiplicity of $-1$ from step [](#s1){.pf-ref}. The
eigenvalue $1$ has algebraic multiplicity $1$, so its eigenspace has
dimension $1$. Hence $A$ has three linearly independent eigenvectors and
is diagonalizable. Its minimal polynomial is therefore the product of its
distinct linear eigenvalue factors, namely $(t-1)(t+1)$.

:::

:::

::: {.pf-step #s3}

For part (a), one Jordan canonical form and one rational canonical
form are
$$
J=\boxed{
\begin{pmatrix}
1&0&0\\
0&-1&0\\
0&0&-1
\end{pmatrix}},
\qquad
R=\boxed{
\begin{pmatrix}
-1&0&0\\
0&0&1\\
0&1&0
\end{pmatrix}}.
$$

::: pf-proof

The Jordan form follows immediately from diagonalizability and the
eigenvalue multiplicities in steps [](#s1){.pf-ref} and [](#s2){.pf-ref}.

For rational canonical form, let the invariant factors be
$d_1\mid d_2$. Their product is $\chi_A$ and the largest invariant
factor is the minimal polynomial. Hence
$$
d_2(t)=t^2-1,
\qquad
d_1(t)=\frac{\chi_A(t)}{d_2(t)}=t+1.
$$
The companion matrices are
$$
C(t+1)=(-1),
\qquad
C(t^2-1)=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
$$
and their block diagonal sum is the displayed matrix $R$.

:::

:::

::: {.pf-step #s4}

There are exactly six isomorphism classes of abelian groups of
order $360$.

::: pf-proof

Since
$$
360=2^3\cdot3^2\cdot5,
$$
the classification theorem for finite abelian groups decomposes such a
group uniquely into its $2$-, $3$-, and $5$-primary parts [@DF04].
There are three possibilities for the $2$-primary part,
$$
\ZZ/8,
\qquad
\ZZ/4\times\ZZ/2,
\qquad
(\ZZ/2)^3,
$$
two possibilities for the $3$-primary part,
$$
\ZZ/9,
\qquad
(\ZZ/3)^2,
$$
and one possibility for the $5$-primary part, namely $\ZZ/5$.
Thus there are $3\cdot2\cdot1=6$ isomorphism classes.

:::

:::

::: {.pf-step #s5}

In invariant-factor form, the six groups in part (b) are
$$
\boxed{
\ZZ/360,\quad
\ZZ/3\times\ZZ/120,\quad
\ZZ/2\times\ZZ/180,\quad
\ZZ/6\times\ZZ/60,\quad
(\ZZ/2)^2\times\ZZ/90,\quad
\ZZ/2\times\ZZ/6\times\ZZ/30}.
$$

::: pf-proof

Combine the primary factors from step [](#s4){.pf-ref} using
$\ZZ/m\times\ZZ/n\cong\ZZ/(mn)$ whenever $\gcd(m,n)=1$.
The six choices are
$$
\begin{aligned}
\ZZ/8\times\ZZ/9\times\ZZ/5
&\cong\ZZ/360,\\
\ZZ/8\times(\ZZ/3)^2\times\ZZ/5
&\cong\ZZ/3\times\ZZ/120,\\
\ZZ/4\times\ZZ/2\times\ZZ/9\times\ZZ/5
&\cong\ZZ/2\times\ZZ/180,\\
\ZZ/4\times\ZZ/2\times(\ZZ/3)^2\times\ZZ/5
&\cong\ZZ/6\times\ZZ/60,\\
(\ZZ/2)^3\times\ZZ/9\times\ZZ/5
&\cong(\ZZ/2)^2\times\ZZ/90,\\
(\ZZ/2)^3\times(\ZZ/3)^2\times\ZZ/5
&\cong\ZZ/2\times\ZZ/6\times\ZZ/30.
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} gives the two canonical forms required in part (a), and
steps [](#s4){.pf-ref} and [](#s5){.pf-ref} give all isomorphism classes required in part (b).

:::

:::

:::
