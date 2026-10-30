---
schema: qual/card@1
id: P-KSRING17-091
kind: problem
title: A nonzero ideal of a principal ideal domain lies in only finitely many ideals
classification:
  areas: [algebra]
  topics:
  - Principal Ideal Domains
  - Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 91 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be a principal ideal domain.
Show that if (a) is a nonzero ideal in R, then there are only finitely many ideals in R containing (a).
:::

::: {.solution}

Assume
$$
(a)\ne(0).
$$
Then
$$
a\ne0.
$$

::: pf

::: {.pf-step #s1-1}

Every ideal of $R$ containing $(a)$ has the form
$$
(d)
$$
for some divisor
$$
d\mid a.
$$


::: pf-proof

Let
$$
I
$$
be an ideal with
$$
(a)\subseteq I.
$$
Because $R$ is a principal ideal domain,
$$
I=(d)
$$
for some
$$
d\in R.
$$
The containment
$$
(a)\subseteq(d)
$$
means in particular that
$$
a\in(d).
$$
Thus
$$
a=dr
$$
for some
$$
r\in R,
$$
so
$$
d\mid a.
$$

:::

:::

::: {.pf-step #s1-2}

Conversely, if
$$
d\mid a,
$$
then
$$
(a)\subseteq(d).
$$


::: pf-proof

Write
$$
a=dr.
$$
Every element of
$$
(a)
$$
has the form
$$
sa
=
sdr
\in
(d).
$$
Hence
$$
(a)\subseteq(d).
$$

:::

:::

::: pf-step

Since $R$ is a PID, it is a UFD.


::: pf-proof

Every principal ideal domain is a unique factorization domain.
Hence every nonzero nonunit of $R$ has a factorization into irreducibles, unique up to order and associates.

:::

:::

::: pf-step

If $a$ is a unit, then the only ideal containing $(a)$ is $R$.


::: pf-proof

If $a$ is a unit, then
$$
(a)=R.
$$
The only ideal containing $R$ is $R$ itself.

:::

:::

::: {.pf-step #s1-5}

Suppose $a$ is not a unit.
Choose a factorization
$$
a
=
u
\prod_{i=1}^{r}
p_i^{e_i},
$$
where
$$
u\in R^\times,
$$
the $p_i$ are pairwise nonassociate irreducibles, and
$$
e_i\ge1.
$$
Then every divisor $d$ of $a$ is associate to an element of the form
$$
\prod_{i=1}^{r}
p_i^{f_i}
$$
with
$$
0\le f_i\le e_i.
$$


::: pf-proof

Let
$$
d\mid a.
$$
Then
$$
a=dc
$$
for some
$$
c\in R.
$$
Factor $d$ and $c$ into irreducibles.
By uniqueness of factorization, every irreducible factor of $d$ is associate to one of the $p_i$, and its exponent cannot exceed the corresponding exponent $e_i$ in the factorization of $a$.
Thus, up to multiplication by a unit,
$$
d
\sim
\prod_{i=1}^{r}
p_i^{f_i}
$$
with
$$
0\le f_i\le e_i.
$$

:::

:::

::: {.pf-step #s1-6}

There are only finitely many divisors of $a$ up to associates.


::: pf-proof

By step [](#s1-5){.pf-ref}, an associate class of a divisor is determined by the finite tuple
$$
(f_1,\ldots,f_r)
$$
with
$$
0\le f_i\le e_i.
$$
There are exactly
$$
\prod_{i=1}^{r}(e_i+1)
$$
such tuples.
Hence there are finitely many divisor classes up to associates.

:::

:::

::: {.pf-step #s1-7}

Associate elements generate the same principal ideal.


::: pf-proof

If
$$
d'=vd
$$
with
$$
v
$$
a unit, then
$$
(d')
=(vd)
=(d),
$$
because multiplication by a unit does not change the set of multiples.

:::

:::

::: {.pf-step #s1-8}

Therefore there are only finitely many ideals containing $(a)$.


::: pf-proof

By steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref}, ideals containing
$$
(a)
$$
are exactly the ideals
$$
(d)
$$
with
$$
d\mid a.
$$
Step [](#s1-6){.pf-ref} gives only finitely many divisors up to associates, and step [](#s1-7){.pf-ref} shows associates yield the same ideal.
Thus
$$
\boxed{
\text{only finitely many ideals of }R\text{ contain }(a).
}
$$

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the required conclusion.

:::

:::

:::
