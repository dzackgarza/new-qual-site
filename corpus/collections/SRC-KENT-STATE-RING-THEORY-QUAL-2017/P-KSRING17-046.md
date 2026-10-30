---
schema: qual/card@1
id: P-KSRING17-046
kind: problem
title: When $(x)$ is prime or maximal in $R[x]$
classification:
  areas: [algebra]
  topics:
  - Polynomial Rings
  - Prime Ideals
  - Maximal Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 46 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be a commutative ring with 1.

(a) Prove that (x) is a prime ideal in $R [ x ]$ if and only if R is an integral domain.

(b) Prove that (x) is a maximal ideal in R[x] if and only if R is a field.
:::

::: {.solution}

Define the evaluation map
$$
\operatorname{ev}_0:R[x]\to R
$$
by
$$
\operatorname{ev}_0(f)
\coloneqq
f(0).
$$

::: pf

::: {.pf-step #s1-1}

The map
$$
\operatorname{ev}_0
$$
is a surjective ring homomorphism.


::: pf-proof

For
$$
f,g\in R[x],
$$
one has
$$
\operatorname{ev}_0(f+g)
=
f(0)+g(0)
$$
and
$$
\operatorname{ev}_0(fg)
=
f(0)g(0).
$$
Also,
$$
\operatorname{ev}_0(1)=1.
$$
Thus it is a unital ring homomorphism.

It is surjective because every
$$
r\in R
$$
is the image of the constant polynomial $r$.

:::

:::

::: {.pf-step #s1-2}

The kernel of
$$
\operatorname{ev}_0
$$
is exactly
$$
(x).
$$


::: pf-proof

A polynomial
$$
f(x)
=
a_0+a_1x+\cdots+a_nx^n
$$
satisfies
$$
f(0)=0
$$
if and only if
$$
a_0=0.
$$
This is equivalent to
$$
f(x)
=
x(a_1+a_2x+\cdots+a_nx^{n-1}),
$$
so
$$
f\in(x).
$$
Hence
$$
\ker\operatorname{ev}_0
=(x).
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{
R[x]/(x)
\cong
R.
}
$$


::: pf-proof

By steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref}, the first isomorphism theorem gives
$$
R[x]/\ker\operatorname{ev}_0
\cong
R.
$$
Substitute
$$
\ker\operatorname{ev}_0=(x).
$$

:::

:::

::: {.pf-step #s1-4}

The ideal
$$
(x)
$$
is prime in
$$
R[x]
$$
if and only if
$$
R
$$
is an integral domain.


::: pf-proof

By the prime-ideal quotient criterion,
$$
(x)\text{ is prime}
\iff
R[x]/(x)\text{ is an integral domain}.
$$
By step [](#s1-3){.pf-ref},
$$
R[x]/(x)
\cong
R.
$$
Being an integral domain is preserved by ring isomorphism. Therefore
$$
\boxed{
(x)\text{ is prime in }R[x]
\iff
R\text{ is an integral domain}.
}
$$

:::

:::

::: {.pf-step #s1-5}

The ideal
$$
(x)
$$
is maximal in
$$
R[x]
$$
if and only if
$$
R
$$
is a field.


::: pf-proof

By the maximal-ideal quotient criterion,
$$
(x)\text{ is maximal}
\iff
R[x]/(x)\text{ is a field}.
$$
By step [](#s1-3){.pf-ref},
$$
R[x]/(x)
\cong
R.
$$
Being a field is preserved by ring isomorphism. Hence
$$
\boxed{
(x)\text{ is maximal in }R[x]
\iff
R\text{ is a field}.
}
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves part (a), and step [](#s1-5){.pf-ref} proves part (b).

:::

:::

:::
