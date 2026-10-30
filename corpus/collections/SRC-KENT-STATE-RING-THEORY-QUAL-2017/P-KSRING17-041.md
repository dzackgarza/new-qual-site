---
schema: qual/card@1
id: P-KSRING17-041
kind: problem
title: Maximal ideals are prime, and a nonzero prime ideal that is not maximal
classification:
  areas: [algebra]
  topics:
  - Maximal Ideals
  - Prime Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 41 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
(a) Let R be a commutative ring with 1. Show that if M is a maximal ideal of R then M is a prime ideal of R.

(b) Give an example of a non-zero prime ideal in a ring R that is not a maximal ideal.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Let
$$
M
$$
be a maximal ideal of a commutative ring
$$
R
$$
with identity. Then
$$
R/M
$$
is a field.


::: pf-proof

By the maximal-ideal quotient criterion, an ideal of a commutative ring with identity is maximal exactly when its quotient is a field. Since $M$ is maximal,
$$
R/M
$$
is a field.

:::

:::

::: {.pf-step #s1-2}

Every field is an integral domain.


::: pf-proof

Let
$$
K
$$
be a field and suppose
$$
ab=0
$$
with
$$
a\ne0.
$$
Multiplying by
$$
a^{-1}
$$
gives
$$
b=0.
$$
Thus a field has no zero divisors and is therefore an integral domain.

:::

:::

::: {.pf-step #s1-3}

Therefore every maximal ideal of $R$ is prime.


::: pf-proof

By steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref},
$$
R/M
$$
is an integral domain. By the prime-ideal quotient criterion, this implies
$$
\boxed{M\text{ is prime}.}
$$

:::

:::

::: {.pf-step #s1-4}

For part (b), take
$$
\boxed{
R=\ZZ[x],
\qquad
P=(2).
}
$$


::: pf-proof

The ideal
$$
(2)
$$
is nonzero because it contains the nonzero polynomial $2$.

:::

:::

::: {.pf-step #s1-5}

The ideal
$$
P=(2)
$$
is prime in $\ZZ[x]$.


::: pf-proof

Reduction of coefficients modulo $2$ gives a ring isomorphism
$$
\ZZ[x]/(2)
\cong
\FF_2[x].
$$
The polynomial ring
$$
\FF_2[x]
$$
over a field is an integral domain. Hence, by the prime-ideal quotient criterion,
$$
(2)
$$
is prime.

:::

:::

::: {.pf-step #s1-6}

The ideal
$$
P=(2)
$$
is not maximal.


::: pf-proof

The quotient
$$
\ZZ[x]/(2)
\cong
\FF_2[x]
$$
is not a field. For example,
$$
x
$$
is a nonzero nonunit in $\FF_2[x]$, since no polynomial multiplied by $x$ can equal $1$.

By the maximal-ideal quotient criterion,
$$
(2)
$$
is therefore not maximal.

:::

:::

::: {.pf-step #s1-7}

Hence
$$
\boxed{
(2)\subset\ZZ[x]
}
$$
is a nonzero prime ideal that is not maximal.


::: pf-proof

Combine steps [](#s1-4){.pf-ref} through [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves part (a), and step [](#s1-7){.pf-ref} gives the required example for part (b).

:::

:::

:::
