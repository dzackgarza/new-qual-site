---
schema: qual/card@1
id: P-KSRING17-058
kind: problem
title: A ring in which every ideal is prime is a field
classification:
  areas: [algebra]
  topics:
  - Prime Ideals
  - Fields
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 58 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source assumes every ideal is prime, which no ring satisfies since $R$ itself is not prime. The statement now assumes $R$ nonzero and every proper ideal prime.
---

::: {.problem}
Let $R$ be a nonzero commutative ring with $1$ in which every proper ideal is a prime ideal. Prove that $R$ is a field. (Hint: For $a \neq 0$ consider the ideals $(a)$ and $(a^{2})$.)
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The zero ideal is prime.

::: pf-proof

Since $R$ is nonzero, $(0)\neq R$, so $(0)$ is a proper ideal and hence prime by hypothesis.

:::

:::

::: {.pf-step #s1-2}

The ring $R$ is an integral domain.

::: pf-proof

Since
$$
(0)
$$
is prime by step [](#s1-1){.pf-ref}, whenever
$$
ab=0,
$$
one has
$$
ab\in(0),
$$
and therefore
$$
a\in(0)
\quad\text{or}\quad
b\in(0).
$$
Thus
$$
a=0
\quad\text{or}\quad
b=0.
$$
Hence $R$ is a domain.

:::

:::

::: {.pf-step #s1-3}

Let
$$
0\ne a\in R.
$$
If
$$
(a)=R,
$$
then $a$ is a unit.

::: pf-proof

The equality
$$
(a)=R
$$
means
$$
1\in(a).
$$
Hence
$$
1=ar
$$
for some
$$
r\in R.
$$
Thus $a$ is invertible.

:::

:::

::: {.pf-step #s1-4}

Suppose instead that
$$
(a)
\subsetneq
R.
$$
Then
$$
(a^2)
\subsetneq
R
$$
and therefore
$$
(a^2)
$$
is prime.

::: pf-proof

Since
$$
(a^2)\subseteq(a)
$$
and
$$
(a)\subsetneq R,
$$
the ideal
$$
(a^2)
$$
is proper. By hypothesis, every proper ideal is prime.

:::

:::

::: {.pf-step #s1-5}

Under the assumptions of step [](#s1-4){.pf-ref},
$$
a\in(a^2).
$$

::: pf-proof

One has
$$
a\cdot a
=
a^2
\in
(a^2).
$$
Since
$$
(a^2)
$$
is prime, primality implies
$$
a\in(a^2).
$$

:::

:::

::: {.pf-step #s1-6}

The element $a$ is a unit.

::: pf-proof

By step [](#s1-5){.pf-ref}, there exists
$$
r\in R
$$
such that
$$
a
=
a^2r.
$$
Hence
$$
a(1-ar)=0.
$$
Because $R$ is an integral domain by step [](#s1-2){.pf-ref} and
$$
a\ne0,
$$
one must have
$$
1-ar=0.
$$
Thus
$$
ar=1,
$$
so $a$ is invertible.

:::

:::

::: {.pf-step #s1-7}

Every nonzero element of $R$ is a unit.

::: pf-proof

Let
$$
0\ne a\in R.
$$
If
$$
(a)=R,
$$
step [](#s1-3){.pf-ref} gives invertibility. If
$$
(a)\subsetneq R,
$$
steps [](#s1-4){.pf-ref} through [](#s1-6){.pf-ref} give invertibility. Thus every nonzero element is a unit.

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\boxed{R\text{ is a field}.}
$$

::: pf-proof

The ring is commutative with identity, and by step [](#s1-7){.pf-ref} every nonzero element is invertible.

:::

:::

:::

:::
