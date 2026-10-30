---
schema: qual/card@1
id: P-KSRING17-104
kind: problem
title: If nonzero primes of $D[x]$ are maximal then $D$ is a field
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
  note: Checked against Problem 104 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let D be an integral domain and $D [ x ]$ the polynomial ring over D in the indeterminate x. Show that if every nonzero prime ideal of $D [ x ]$ is a maximal ideal, then D is a field.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Define the evaluation homomorphism
$$
\operatorname{ev}_0:D[x]\to D
$$
by
$$
\operatorname{ev}_0(f)
\coloneqq
f(0).
$$
Then
$$
\ker\operatorname{ev}_0
=(x).
$$


::: pf-proof

The map is a surjective ring homomorphism because every
$$
d\in D
$$
is the image of the constant polynomial $d$.

A polynomial
$$
f(x)
=
a_0+a_1x+\cdots+a_nx^n
$$
lies in the kernel exactly when
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
Thus
$$
\ker\operatorname{ev}_0=(x).
$$

:::

:::

::: {.pf-step #s1-2}

Therefore
$$
\boxed{
D[x]/(x)
\cong
D.
}
$$


::: pf-proof

Apply the first isomorphism theorem to the surjective map in step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

The ideal
$$
(x)
$$
is prime in
$$
D[x].
$$


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
D[x]/(x)
\cong
D.
$$
The ring $D$ is an integral domain by hypothesis.
Hence the quotient
$$
D[x]/(x)
$$
is an integral domain.
By the prime-ideal quotient criterion,
$$
(x)
$$
is prime.

:::

:::

::: {.pf-step #s1-4}

The ideal
$$
(x)
$$
is nonzero.


::: pf-proof

The polynomial
$$
x
$$
is a nonzero element of
$$
D[x]
$$
because
$$
D
$$
is a nonzero integral domain.
Hence
$$
(x)\ne(0).
$$

:::

:::

::: {.pf-step #s1-5}

By hypothesis,
$$
(x)
$$
is maximal.


::: pf-proof

Steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} show that
$$
(x)
$$
is a nonzero prime ideal of
$$
D[x].
$$
The hypothesis says every such ideal is maximal.

:::

:::

::: {.pf-step #s1-6}

The quotient
$$
D[x]/(x)
$$
is a field.


::: pf-proof

By step [](#s1-5){.pf-ref},
$$
(x)
$$
is maximal.
The maximal-ideal quotient criterion therefore gives that
$$
D[x]/(x)
$$
is a field.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{
D
\text{ is a field}.
}
$$


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
D
\cong
D[x]/(x).
$$
Step [](#s1-6){.pf-ref} shows the quotient is a field.
Being a field is preserved under ring isomorphism.
Hence $D$ is a field.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required conclusion.

:::

:::

:::
