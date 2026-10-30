---
schema: qual/card@1
id: P-KSRING17-089
kind: problem
title: Least common multiples in a principal ideal domain as intersections of ideals
classification:
  areas: [algebra]
  topics:
  - Least Common Multiples
  - Principal Ideal Domains
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 89 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let D be a principal ideal domain.

(a) For $a , b \in D$ , define a least common multiple of a and b.

(b) Show that $d \in D$ is a least common multiple of a and b if and only if $( a ) \cap ( b ) = ( d )$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A least common multiple of
$$
a,b\in D
$$
is an element
$$
d\in D
$$
such that
$$
a\mid d,
\qquad
b\mid d,
$$
and whenever
$$
a\mid c
\qquad\text{and}\qquad
b\mid c,
$$
one has
$$
d\mid c.
$$


::: pf-proof

This is the standard divisibility definition of a least common multiple in an integral domain.
As usual, least common multiples are unique only up to multiplication by a unit.

:::

:::

::: {.pf-step #s1-2}

Assume $d$ is a least common multiple of $a$ and $b$.
Then
$$
(d)\subseteq(a)\cap(b).
$$


::: pf-proof

Since
$$
a\mid d
$$
and
$$
b\mid d,
$$
one has
$$
d\in(a)
\qquad\text{and}\qquad
d\in(b).
$$
Hence
$$
d\in(a)\cap(b).
$$
Because
$$
(a)\cap(b)
$$
is an ideal containing $d$, it contains every multiple of $d$:
$$
(d)\subseteq(a)\cap(b).
$$

:::

:::

::: {.pf-step #s1-3}

Under the same hypothesis,
$$
(a)\cap(b)\subseteq(d).
$$


::: pf-proof

Let
$$
c\in(a)\cap(b).
$$
Then
$$
c\in(a)
$$
and
$$
c\in(b),
$$
so
$$
a\mid c
\qquad\text{and}\qquad
b\mid c.
$$
Since $d$ is a least common multiple,
$$
d\mid c.
$$
Thus
$$
c\in(d).
$$
Therefore
$$
(a)\cap(b)\subseteq(d).
$$

:::

:::

::: {.pf-step #s1-4}

Hence if $d$ is a least common multiple, then
$$
(a)\cap(b)=(d).
$$


::: pf-proof

Combine steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Conversely, assume
$$
(a)\cap(b)=(d).
$$
Then
$$
a\mid d
\qquad\text{and}\qquad
b\mid d.
$$


::: pf-proof

Since
$$
d\in(d)
=(a)\cap(b),
$$
one has
$$
d\in(a)
$$
and
$$
d\in(b).
$$
Thus
$$
a\mid d
\qquad\text{and}\qquad
b\mid d.
$$

:::

:::

::: {.pf-step #s1-6}

Let
$$
c\in D
$$
be any common multiple of $a$ and $b$.
Then
$$
d\mid c.
$$


::: pf-proof

Because
$$
a\mid c
\qquad\text{and}\qquad
b\mid c,
$$
one has
$$
c\in(a)
\qquad\text{and}\qquad
c\in(b).
$$
Hence
$$
c\in(a)\cap(b)
=(d).
$$
Therefore
$$
d\mid c.
$$

:::

:::

::: {.pf-step #s1-7}

Thus, if
$$
(a)\cap(b)=(d),
$$
then $d$ is a least common multiple of $a$ and $b$.


::: pf-proof

Step [](#s1-5){.pf-ref} shows that $d$ is a common multiple, and step [](#s1-6){.pf-ref} shows that $d$ divides every common multiple.
These are exactly the conditions from step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\boxed{
d\text{ is an lcm of }a,b
\iff
(a)\cap(b)=(d).
}
$$


::: pf-proof

Step [](#s1-4){.pf-ref} proves the forward implication and step [](#s1-7){.pf-ref} proves the converse.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} answers part (a), and step [](#s1-8){.pf-ref} proves part (b).

:::

:::

:::
