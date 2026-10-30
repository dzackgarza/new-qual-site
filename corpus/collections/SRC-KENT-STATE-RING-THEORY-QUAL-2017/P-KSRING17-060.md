---
schema: qual/card@1
id: P-KSRING17-060
kind: problem
title: Prime ideals of a finite commutative ring are maximal
classification:
  areas: [algebra]
  topics:
  - Finite Rings
  - Prime Ideals
  - Maximal Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 60 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Show that if R is a finite commutative ring with identity then every prime ideal of R is a maximal ideal.
:::

::: {.solution}

Let
$$
P
$$
be a prime ideal of the finite commutative ring $R$.

::: pf

::: pf-step

The quotient
$$
R/P
$$
is an integral domain.


::: pf-proof

Because
$$
P
$$
is prime, the prime-ideal quotient criterion gives that
$$
R/P
$$
is an integral domain.

:::

:::

::: {.pf-step #s1-2}

The quotient
$$
R/P
$$
is finite.


::: pf-proof

The quotient set
$$
R/P
$$
is the set of cosets of $P$ in the finite set $R$. Hence it has finitely many elements.

:::

:::

::: {.pf-step #s1-3}

The finite integral domain
$$
R/P
$$
is a field.


::: pf-proof

Let
$$
0\ne a+P\in R/P.
$$
Multiplication by this element defines a map
$$
\mu_{a+P}:R/P\to R/P,
\qquad
x+P\longmapsto(a+P)(x+P).
$$
Since
$$
R/P
$$
is an integral domain, this map is injective.
Because the quotient is finite by step [](#s1-2){.pf-ref}, the map is therefore surjective.
Hence
$$
1+P
$$
lies in its image, so there exists
$$
b+P
$$
with
$$
(a+P)(b+P)
=
1+P.
$$
Thus every nonzero element of $R/P$ is invertible.
Therefore
$$
R/P
$$
is a field.

:::

:::

::: pf-step

The ideal
$$
P
$$
is maximal.


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
R/P
$$
is a field.
The maximal-ideal quotient criterion therefore implies that
$$
P
$$
is maximal.

:::

:::

::: {.pf-step #s1-5}

Hence every prime ideal of $R$ is maximal.


::: pf-proof

The prime ideal $P$ was arbitrary.
Therefore
$$
\boxed{
\text{every prime ideal of }R\text{ is maximal}.
}
$$

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
