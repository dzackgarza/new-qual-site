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

::: {.pf-step #s1-1}

The ring $R[x]$ is an integral domain.


::: pf-proof

Being an integral domain is part of the definition of a principal ideal domain.

:::

:::

::: {.pf-step #s1-2}

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
is an integral domain by step [](#s1-1){.pf-ref},
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

::: {.pf-step #s1-3}

Suppose, for contradiction, that $R$ is not a field.
Then there exists a nonzero nonunit
$$
c\in R.
$$


::: pf-proof

In a nonzero commutative ring with identity, being a field is equivalent to every nonzero element being a unit.
Since $R$ is not a field and is nonzero by step [](#s1-2){.pf-ref}, some nonzero element is not invertible.

:::

:::

::: {.pf-step #s1-4}

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
Thus $c$ is a unit of $R$, contradicting step [](#s1-3){.pf-ref}.
Hence
$$
(x,c)\subsetneq R[x].
$$

:::

:::

::: {.pf-step #s1-5}

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
Because $R$ is an integral domain by step [](#s1-2){.pf-ref},
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

::: {.pf-step #s1-6}

The constant $d$ from step [](#s1-5){.pf-ref} is a unit of $R$.


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

::: {.pf-step #s1-7}

The ideal $(x,c)$ is not principal.


::: pf-proof

If it were principal, steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref} would give
$$
(x,c)=(d)=R[x],
$$
because a unit generates the whole ring.
This contradicts properness from step [](#s1-4){.pf-ref}.
Thus
$$
\boxed{
(x,c)
\text{ is not principal}.
}
$$

:::

:::

::: {.pf-step #s1-8}

The assumption that $R$ is not a field contradicts the hypothesis that $R[x]$ is a PID.


::: pf-proof

A principal ideal domain has every ideal principal.
Step [](#s1-7){.pf-ref} gives a nonprincipal ideal of
$$
R[x].
$$
This contradiction shows that the assumption in step [](#s1-3){.pf-ref} is impossible.

:::

:::

::: {.pf-step #s1-9}

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

This is the conclusion of step [](#s1-8){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

Equivalently,
$$
\boxed{
R\text{ not a field}
\implies
R[x]\text{ not a PID}.
}
$$


::: pf-proof

This is the contrapositive of step [](#s1-9){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is the required conclusion.

:::

:::
