---
schema: qual/card@1
id: P-KSRING17-138
kind: problem
title: Hilbert basis theorem for commutative Noetherian rings
classification:
  areas: [algebra]
  topics:
  - Noetherian Rings
  - Hilbert Basis Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 138 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Show that if R is a commutative Noetherian ring with identity, then the polynomial ring R[x] is also Noetherian.
:::

::: {.solution}

Let
$$
I\trianglelefteq R[x].
$$
For
$$
n\ge0,
$$
let
$$
A_n
\subseteq
R
$$
be the set of coefficients of $x^n$ occurring in polynomials of $I$ of degree at most $n$.

::: pf

::: pf-step

Each $A_n$ is an ideal of $R$.


::: pf-proof

If
$$
a,b\in A_n,
$$
choose
$$
f,g\in I
$$
of degree at most $n$ whose coefficients of $x^n$ are $a$ and $b$.
Then
$$
f-g\in I
$$
has $x^n$-coefficient
$$
a-b.
$$
Thus
$$
a-b\in A_n.
$$

If
$$
r\in R
$$
and
$$
a\in A_n,
$$
then for such an $f$ the polynomial
$$
rf\in I
$$
has $x^n$-coefficient
$$
ra.
$$
Hence
$$
ra\in A_n.
$$

:::

:::

::: {.pf-step #s1-2}

The ideals satisfy
$$
A_0
\subseteq
A_1
\subseteq
A_2
\subseteq
\cdots.
$$


::: pf-proof

If
$$
a\in A_n
$$
comes from
$$
f\in I,
$$
then
$$
xf\in I
$$
has coefficient $a$ at
$$
x^{n+1}.
$$
Thus
$$
a\in A_{n+1}.
$$

:::

:::

::: pf-step

The chain stabilizes:
there exists
$$
N
$$
such that
$$
A_N
=
A_{N+1}
=
\cdots.
$$


::: pf-proof

Because $R$ is Noetherian, it satisfies the ascending chain condition on ideals.
Apply this to the chain from step [](#s1-2){.pf-ref}.

:::

:::

::: pf-step

For each
$$
0\le n\le N,
$$
choose generators
$$
A_n
=
(a_{n1},\ldots,a_{nr_n})
$$
and choose
$$
f_{nj}\in I
$$
of degree at most $n$ whose $x^n$-coefficient is $a_{nj}$.


::: pf-proof

Each $A_n$ is finitely generated because $R$ is Noetherian.
The definition of $A_n$ supplies the corresponding polynomials.

:::

:::

::: {.pf-step #s1-5}

Let
$$
J
\coloneqq
\left(
f_{nj}:
0\le n\le N,\ 1\le j\le r_n
\right).
$$
Then
$$
J\subseteq I.
$$


::: pf-proof

Every generator of $J$ was chosen from $I$.

:::

:::

::: {.pf-step #s1-6}

Let
$$
0\ne f\in I
$$
have degree
$$
m\le N.
$$
Then there exists
$$
g\in J
$$
such that either
$$
f=g
$$
or
$$
\deg(f-g)<m.
$$


::: pf-proof

The leading coefficient
$$
\operatorname{lc}(f)
$$
lies in $A_m$.
Write
$$
\operatorname{lc}(f)
=
\sum_j c_j a_{mj}.
$$
Set
$$
g
\coloneqq
\sum_j c_j f_{mj}.
$$
Then $g\in J$, has degree at most $m$, and has the same $x^m$-coefficient as $f$.
Thus the degree-$m$ term cancels in
$$
f-g.
$$

:::

:::

::: {.pf-step #s1-7}

Let
$$
0\ne f\in I
$$
have degree
$$
m>N.
$$
Then there exists
$$
g\in J
$$
such that either
$$
f=g
$$
or
$$
\deg(f-g)<m.
$$


::: pf-proof

The leading coefficient of $f$ lies in
$$
A_m=A_N.
$$
Write
$$
\operatorname{lc}(f)
=
\sum_j c_j a_{Nj}.
$$
Set
$$
g
\coloneqq
\sum_j c_jx^{m-N}f_{Nj}.
$$
Then
$$
g\in J
$$
and the coefficient of
$$
x^m
$$
in $g$ equals
$$
\operatorname{lc}(f).
$$
Hence the leading term cancels in
$$
f-g.
$$

:::

:::

::: {.pf-step #s1-8}

Every element of $I$ belongs to $J$.


::: pf-proof

Use induction on polynomial degree.

For degree $0$, the element is an $R$-linear combination of the chosen degree-$0$ generators
$$
f_{0j},
$$
so it lies in $J$.

Now let
$$
0\ne f\in I
$$
have positive degree.
Apply step [](#s1-6){.pf-ref} or step [](#s1-7){.pf-ref} according as
$$
\deg f\le N
$$
or
$$
\deg f>N.
$$
There is
$$
g\in J
$$
such that either
$$
f=g
$$
or
$$
f-g\in I
$$
has smaller degree.
In the latter case the induction hypothesis gives
$$
f-g\in J,
$$
and therefore
$$
f\in J.
$$

:::

:::

::: {.pf-step #s1-9}

Hence
$$
I=J.
$$


::: pf-proof

Step [](#s1-5){.pf-ref} gives
$$
J\subseteq I,
$$
and step [](#s1-8){.pf-ref} gives
$$
I\subseteq J.
$$

:::

:::

::: {.pf-step #s1-10}

The ideal $I$ is finitely generated.


::: pf-proof

The generating set used to define $J$ in step [](#s1-5){.pf-ref} is finite, because
$$
0\le n\le N
$$
and each $A_n$ has finitely many chosen generators.
Step [](#s1-9){.pf-ref} gives
$$
I=J.
$$

:::

:::

::: {.pf-step #s1-11}

Therefore every ideal of $R[x]$ is finitely generated.


::: pf-proof

The ideal
$$
I
$$
was arbitrary.
Apply step [](#s1-10){.pf-ref}.

:::

:::

::: {.pf-step #s1-12}

Hence
$$
\boxed{
R[x]
\text{ is Noetherian}.
}
$$


::: pf-proof

A commutative ring is Noetherian exactly when every ideal is finitely generated.
Step [](#s1-11){.pf-ref} verifies this for
$$
R[x].
$$

:::

:::

::: pf-qed

Step [](#s1-12){.pf-ref} is Hilbert's basis theorem.

:::

:::

:::
