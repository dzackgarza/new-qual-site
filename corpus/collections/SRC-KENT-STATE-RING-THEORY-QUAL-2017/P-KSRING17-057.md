---
schema: qual/card@1
id: P-KSRING17-057
kind: problem
title: Prime ideals are maximal when every $x$ satisfies $x^n=x$
classification:
  areas: [algebra]
  topics:
  - Prime Ideals
  - Maximal Ideals
  - Von Neumann Regular Rings
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 57 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let $R$ be a commutative ring with $1$ such that for every $x$ in $R$ there is an integer $n > 1$ (depending on $x$) such that $x^{n} = x$. Show that every prime ideal of $R$ is maximal.
:::

::: {.solution}

Let
$$
P
$$
be a prime ideal of $R$.

::: pf

::: {.pf-step #s1-1}

The quotient
$$
D
\coloneqq
R/P
$$
is an integral domain.


::: pf-proof

This is the prime-ideal quotient criterion: because $P$ is prime,
$$
R/P
$$
is an integral domain.

:::

:::

::: {.pf-step #s1-2}

Every element
$$
y\in D
$$
satisfies
$$
y^n=y
$$
for some integer
$$
n>1
$$
depending on $y$.


::: pf-proof

Write
$$
y=x+P
$$
for some
$$
x\in R.
$$
By hypothesis, there exists
$$
n>1
$$
such that
$$
x^n=x.
$$
Passing to the quotient gives
$$
y^n
=
(x+P)^n
=
x^n+P
=
x+P
=
y.
$$

:::

:::

::: {.pf-step #s1-3}

Every nonzero element of $D$ is invertible.


::: pf-proof

Let
$$
0\ne y\in D.
$$
By step [](#s1-2){.pf-ref}, choose
$$
n>1
$$
such that
$$
y^n=y.
$$
Then
$$
y(y^{n-1}-1)=0.
$$
Since $D$ is an integral domain and
$$
y\ne0,
$$
one must have
$$
y^{n-1}-1=0.
$$
Thus
$$
y^{n-1}=1,
$$
so
$$
y^{n-2}
$$
is a multiplicative inverse of $y$.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{D=R/P\text{ is a field}.}
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, $D$ is a nonzero commutative ring with identity. By step [](#s1-3){.pf-ref}, every nonzero element of $D$ is invertible. Hence $D$ is a field.

:::

:::

::: {.pf-step #s1-5}

Consequently
$$
\boxed{P\text{ is maximal}.}
$$


::: pf-proof

By step [](#s1-4){.pf-ref},
$$
R/P
$$
is a field. The maximal-ideal quotient criterion therefore implies that $P$ is maximal.

:::

:::

::: pf-qed

Since $P$ was an arbitrary prime ideal, step [](#s1-5){.pf-ref} proves that every prime ideal of $R$ is maximal.

:::

:::

:::
