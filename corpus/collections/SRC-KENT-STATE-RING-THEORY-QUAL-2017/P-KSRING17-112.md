---
schema: qual/card@1
id: P-KSRING17-112
kind: problem
title: $R[x]$ is a PID only if $R$ is a field
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 112 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
[CORRECTED] Show that if R is a commutative ring with 1 that is not a field, then $R [ x ]$ is not a principal ideal domain.
:::

We prove the contrapositive.
Assume
$$
R[x]
$$
is a principal ideal domain.

::: pf

::: pf-step

The ring $R[x]$ is an integral domain.


::: pf-proof

Being an integral domain is part of the definition of a principal ideal domain.

:::

:::

::: pf-step

The coefficient ring $R$ is an integral domain.


::: pf-proof

The ring $R$ embeds in
$$
R[x]
$$
as the constant polynomials.
If
$$
ab=0
$$
in $R$, the same equality holds in
$$
R[x].
$$
Since
$$
R[x]
$$
is an integral domain by step <1>1,
$$
a=0
\quad\text{or}\quad
b=0.
$$
Thus $R$ has no zero divisors.
Also
$$
1_R\ne0
$$
because
$$
R[x]
$$
is nonzero.
Hence $R$ is an integral domain.

:::

:::

::: pf-step

Suppose, for contradiction, that $R$ is not a field.
Then there exists a nonzero nonunit
$$
c\in R.
$$


::: pf-proof

In a nonzero commutative ring with identity, being a field is equivalent to every nonzero element being a unit.
Since $R$ is not a field and is nonzero by step <1>2, some nonzero element is not invertible.

:::

:::

::: pf-step

The ideal
$$
(x,c)
\subseteq
R[x]
$$
is proper.


::: pf-proof

Suppose
$$
1\in(x,c).
$$
Then
$$
1
=
xg(x)+ch(x)
$$
for some
$$
g,h\in R[x].
$$
Evaluating at
$$
x=0
$$
gives
$$
1
=
c\,h(0).
$$
Thus $c$ is a unit of $R$, contradicting step <1>3.
Hence
$$
(x,c)\subsetneq R[x].
$$

:::

:::

::: pf-step

If
$$
(x,c)
$$
were principal, say
$$
(x,c)=(f),
$$
then $f$ would be constant.


::: pf-proof

Since
$$
c\in(f),
$$
there exists
$$
g\in R[x]
$$
such that
$$
c=fg.
$$
The polynomial
$$
c
$$
is nonzero and has degree $0$.
Because $R$ is an integral domain by step <1>2,
$$
\deg(fg)
=
\deg f+\deg g.
$$
Therefore
$$
\deg f=0.
$$
Thus
$$
f=d
$$
for some nonzero
$$
d\in R.
$$

:::

:::

::: pf-step

The constant $d$ from step <1>5 is a unit of $R$.


::: pf-proof

Since
$$
x\in(x,c)=(d),
$$
there exists
$$
h(x)\in R[x]
$$
such that
$$
x=d\,h(x).
$$
Comparing the coefficient of $x$ gives
$$
1=d h_1
$$
for the coefficient $h_1$ of $x$ in $h$.
Hence
$$
d
$$
is a unit.

:::

:::

::: pf-step

The ideal $(x,c)$ is not principal.


::: pf-proof

If it were principal, steps <1>5--<1>6 would give
$$
(x,c)=(d)=R[x],
$$
because a unit generates the whole ring.
This contradicts properness from step <1>4.
Thus
$$
\boxed{
(x,c)
\text{ is not principal}.
}
$$

:::

:::

::: pf-step

The assumption that $R$ is not a field contradicts the hypothesis that $R[x]$ is a PID.


::: pf-proof

A principal ideal domain has every ideal principal.
Step <1>7 gives a nonprincipal ideal of
$$
R[x].
$$
This contradiction shows that the assumption in step <1>3 is impossible.

:::

:::

::: pf-step

Therefore, if
$$
R[x]
$$
is a PID, then
$$
R
$$
is a field.


::: pf-proof

This is the conclusion of step <1>8.

:::

:::

::: pf-step

Equivalently,
$$
\boxed{
R\text{ not a field}
\implies
R[x]\text{ not a PID}.
}
$$


::: pf-proof

This is the contrapositive of step <1>9.

:::

:::

::: pf-qed

Step <1>10 is the required conclusion.

:::

:::
