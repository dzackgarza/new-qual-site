---
schema: qual/card@1
id: P-KSRING17-129
kind: problem
title: Localizations of a PID at nonzero primes are discrete valuation rings
classification:
  areas: [algebra]
  topics:
  - Localization
  - Discrete Valuation Rings
  - Principal Ideal Domains
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 129 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let $D$ be a principal ideal domain and let $P$ be a non-zero prime ideal. Show that $D_{P}$, the localization of $D$ at $P$, is a principal ideal domain and has a unique irreducible element, up to associates.
:::

::: {.solution}

Set
$$
S
\coloneqq
D\setminus P,
$$
so that
$$
D_P=S^{-1}D.
$$
Since $D$ is a PID and $P$ is a nonzero prime ideal, write
$$
P=(p)
$$
with
$$
p\ne0.
$$

::: pf

::: pf-step

Let
$$
J\trianglelefteq D_P.
$$
Define its contraction
$$
I
\coloneqq
\left\{
a\in D:
\frac a1\in J
\right\}.
$$
Then $I$ is an ideal of $D$.


::: pf-proof

The contraction of an ideal along any ring homomorphism is an ideal.
Explicitly, if
$$
a,b\in I,
$$
then
$$
\frac a1,\frac b1\in J,
$$
so
$$
\frac{a-b}{1}
\in
J,
$$
and therefore
$$
a-b\in I.
$$
If
$$
r\in D
$$
and
$$
a\in I,
$$
then
$$
\frac r1\frac a1
=
\frac{ra}{1}
\in
J,
$$
so
$$
ra\in I.
$$

:::

:::

::: {.pf-step #s1-2}

One has
$$
J=S^{-1}I.
$$


::: pf-proof

Let
$$
\frac as\in J.
$$
Since
$$
\frac s1
\in
D_P,
$$
the ideal property gives
$$
\frac s1\frac as
=
\frac a1
\in
J.
$$
Hence
$$
a\in I,
$$
so
$$
\frac as
\in
S^{-1}I.
$$
Thus
$$
J\subseteq S^{-1}I.
$$

Conversely, if
$$
\frac as\in S^{-1}I,
$$
then
$$
a\in I,
$$
so
$$
\frac a1\in J.
$$
Multiplying by
$$
\frac1s
\in
D_P
$$
gives
$$
\frac as\in J.
$$
Therefore
$$
S^{-1}I\subseteq J.
$$

:::

:::

::: {.pf-step #s1-3}

The ideal $J$ is principal.


::: pf-proof

Since $D$ is a PID,
$$
I=(d)
$$
for some
$$
d\in D.
$$
By step [](#s1-2){.pf-ref},
$$
J
=
S^{-1}(d)
=
\left(
\frac d1
\right)
$$
as an ideal of $D_P$.
Thus every ideal of $D_P$ is principal.

:::

:::

::: {.pf-step #s1-4}

The ring $D_P$ is an integral domain.


::: pf-proof

It is a subring of the fraction field of the integral domain $D$.
Hence it has no zero divisors.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
D_P
\text{ is a principal ideal domain}.
}
$$


::: pf-proof

Step [](#s1-3){.pf-ref} shows every ideal is principal, and step [](#s1-4){.pf-ref} shows $D_P$ is an integral domain.

:::

:::

::: pf-step

The element $p$ is irreducible in $D$.


::: pf-proof

Suppose
$$
p=ab.
$$
Then
$$
ab\in(p)=P.
$$
Since $P$ is prime,
$$
a\in P
\quad\text{or}\quad
b\in P.
$$
If
$$
a\in P,
$$
then
$$
a=pc
$$
for some
$$
c\in D.
$$
Thus
$$
p=pcb.
$$
Since $D$ is a domain and
$$
p\ne0,
$$
cancellation gives
$$
1=cb,
$$
so $b$ is a unit.
The other case similarly makes $a$ a unit.
Thus $p$ is irreducible.

:::

:::

::: {.pf-step #s1-7}

A fraction
$$
\frac as\in D_P
$$
is a unit if
$$
a\notin P.
$$


::: pf-proof

If
$$
a\notin P,
$$
then
$$
a\in S.
$$
Hence
$$
\frac sa
\in
D_P,
$$
and
$$
\frac as\frac sa
=
1.
$$

:::

:::

::: {.pf-step #s1-8}

A fraction
$$
\frac as\in D_P
$$
with
$$
a\in P
$$
is not a unit.


::: pf-proof

Suppose it were a unit.
Then for some
$$
\frac bt\in D_P,
$$
$$
\frac{ab}{st}
=
1.
$$
Because $D$ is a domain,
$$
ab=st.
$$
The left-hand side lies in
$$
P
$$
because
$$
a\in P.
$$
Thus
$$
st\in P.
$$
But
$$
s,t\notin P
$$
and $P$ is prime, contradiction.

:::

:::

::: {.pf-step #s1-9}

Therefore
$$
\boxed{
\frac as
\text{ is a unit in }D_P
\iff
a\notin P.
}
$$


::: pf-proof

Combine steps [](#s1-7){.pf-ref} and [](#s1-8){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

The element
$$
\frac p1
$$
is a nonunit of $D_P$.


::: pf-proof

Its numerator
$$
p
$$
lies in
$$
P.
$$
Apply step [](#s1-9){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

The element
$$
\frac p1
$$
is irreducible in $D_P$.


::: pf-proof

Suppose
$$
\frac p1
=
\frac as\frac bt
$$
with both factors nonunits.
By step [](#s1-9){.pf-ref},
$$
a,b\in P=(p).
$$
Write
$$
a=pa',
\qquad
b=pb'.
$$
The equality of fractions in the fraction field gives
$$
pst=ab
=
p^2a'b'.
$$
Since $D$ is a domain and
$$
p\ne0,
$$
cancellation gives
$$
st
=
pa'b'
\in
P.
$$
But
$$
s,t\notin P,
$$
contradicting primality of $P$.
Thus in every factorization of
$$
p/1
$$
one factor is a unit.
Hence
$$
p/1
$$
is irreducible.

:::

:::

::: {.pf-step #s1-12}

Let
$$
\alpha
=
\frac as
$$
be any irreducible element of $D_P$.
Then
$$
a\in P.
$$


::: pf-proof

An irreducible element is a nonunit.
By step [](#s1-9){.pf-ref}, a nonunit fraction must have numerator in
$$
P.
$$

:::

:::

::: {.pf-step #s1-13}

Write
$$
a=pd
$$
for some
$$
d\in D.
$$
Then
$$
\alpha
=
\frac p1\frac ds.
$$


::: pf-proof

By step [](#s1-12){.pf-ref},
$$
a\in P=(p).
$$
Hence
$$
a=pd
$$
for some $d$.
Substituting gives
$$
\frac as
=
\frac{pd}{s}
=
\frac p1\frac ds.
$$

:::

:::

::: {.pf-step #s1-14}

The factor
$$
\frac ds
$$
is a unit.


::: pf-proof

The element
$$
\alpha
$$
is irreducible.
Step [](#s1-13){.pf-ref} expresses it as a product
$$
\alpha
=
\frac p1\frac ds.
$$
By step [](#s1-10){.pf-ref},
$$
p/1
$$
is a nonunit.
Therefore irreducibility of $\alpha$ forces
$$
d/s
$$
to be a unit.

:::

:::

::: {.pf-step #s1-15}

Every irreducible element of $D_P$ is associate to
$$
p/1.
$$


::: pf-proof

Step [](#s1-13){.pf-ref} gives
$$
\alpha
=
\frac p1\frac ds,
$$
and step [](#s1-14){.pf-ref} shows
$$
d/s
$$
is a unit.
Thus
$$
\alpha
$$
differs from
$$
p/1
$$
by multiplication by a unit.

:::

:::

::: {.pf-step #s1-16}

Consequently,
$$
\boxed{
D_P
\text{ has a unique irreducible element up to associates}.
}
$$


::: pf-proof

Step [](#s1-11){.pf-ref} gives the irreducible
$$
p/1,
$$
and step [](#s1-15){.pf-ref} shows every irreducible is associate to it.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves that $D_P$ is a PID, and step [](#s1-16){.pf-ref} proves uniqueness of the irreducible up to associates.

:::

:::

:::
