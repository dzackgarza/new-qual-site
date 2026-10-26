---
schema: qual/card@1
id: P-KSRING17-097
kind: problem
title: Ideals of a UFD with a single irreducible up to associates are totally ordered
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 97 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let D be a unique factorization domain such that if p and q are irreducible elements of $D$ then p and q are associates.
Show that if A and B are ideals of D, then either $A \subseteq B$ or $B \subseteq A$
:::

If $D$ is a field, then its only ideals are $(0)$ and $D$, so the conclusion is immediate.
Assume henceforth that $D$ is not a field.

::: pf

::: pf-step

Fix an irreducible element
$$
p\in D.
$$
Then every nonzero nonunit of $D$ is associate to a power of $p$.


::: pf-proof

Let
$$
0\ne a\in D
$$
be a nonunit.
Because $D$ is a UFD,
$$
a
=
u q_1q_2\cdots q_n
$$
for a unit
$$
u\in D^\times
$$
and irreducibles
$$
q_i.
$$
By hypothesis, every irreducible is associate to $p$.
Thus
$$
q_i=u_i p
$$
for units $u_i$, and therefore
$$
a
=
\left(
u\prod_{i=1}^{n}u_i
\right)
p^n.
$$
Hence $a$ is associate to $p^n$.

:::

:::

::: pf-step

Every nonzero element $a\in D$ can be written uniquely in the form
$$
a=up^n
$$
with
$$
u\in D^\times,
\qquad
n\in\ZZ_{\ge0}.
$$


::: pf-proof

Existence follows from step <1>1, with
$$
n=0
$$
for units.

For uniqueness, suppose
$$
up^m
=
vp^n
$$
with $u,v$ units.
If
$$
m<n,
$$
then cancellation of
$$
p^m
$$
in the domain gives
$$
u
=
vp^{n-m},
$$
which would make the nonunit
$$
p^{n-m}
$$
a unit.
This is impossible.
Similarly
$$
n<m
$$
is impossible.
Thus
$$
m=n.
$$

:::

:::

::: pf-step

Let
$$
I\trianglelefteq D
$$
be a nonzero ideal.
Then there is a least integer
$$
n\ge0
$$
such that
$$
up^n\in I
$$
for some unit $u.


::: pf-proof

The set
$$
\{
k\ge0:
\text{some unit multiple of }p^k\text{ lies in }I
\}
$$
is nonempty because $I$ contains a nonzero element and step <1>2 applies.
The nonnegative integers are well ordered, so this set has a least element.

:::

:::

::: pf-step

For the least exponent $n$ from step <1>3,
$$
p^n\in I.
$$


::: pf-proof

Choose
$$
up^n\in I
$$
with $u$ a unit.
Since $I$ is an ideal,
$$
u^{-1}(up^n)
=
p^n
\in
I.
$$

:::

:::

::: pf-step

Every element of $I$ lies in
$$
(p^n).
$$


::: pf-proof

Let
$$
0\ne a\in I.
$$
By step <1>2,
$$
a=vp^m
$$
for a unit $v$ and some
$$
m\ge0.
$$
By minimality of $n$ in step <1>3,
$$
m\ge n.
$$
Hence
$$
a
=
vp^{m-n}p^n
\in
(p^n).
$$
The zero element also lies in
$$
(p^n).
$$
Thus
$$
I\subseteq(p^n).
$$

:::

:::

::: pf-step

Every nonzero ideal of $D$ has the form
$$
\boxed{I=(p^n)}
$$
for some
$$
n\ge0.
$$


::: pf-proof

Step <1>4 gives
$$
(p^n)\subseteq I,
$$
and step <1>5 gives
$$
I\subseteq(p^n).
$$
Hence equality holds.

:::

:::

::: pf-step

For nonnegative integers $m,n$,
$$
(p^m)\subseteq(p^n)
\iff
m\ge n.
$$


::: pf-proof

If
$$
m\ge n,
$$
then
$$
p^m
=
p^{m-n}p^n,
$$
so every multiple of $p^m$ is a multiple of $p^n$.
Thus
$$
(p^m)\subseteq(p^n).
$$

Conversely, if
$$
(p^m)\subseteq(p^n),
$$
then
$$
p^m\in(p^n),
$$
so
$$
p^m=rp^n
$$
for some
$$
r\in D.
$$
If
$$
m<n,
$$
cancellation would make a positive power of $p$ a unit, impossible.
Hence
$$
m\ge n.
$$

:::

:::

::: pf-step

Any two ideals $A,B$ of $D$ are comparable.


::: pf-proof

If either ideal is zero, comparability is immediate.
Assume both are nonzero.
By step <1>6,
$$
A=(p^m),
\qquad
B=(p^n)
$$
for some
$$
m,n\ge0.
$$
Either
$$
m\ge n
$$
or
$$
n\ge m.
$$
By step <1>7, the first case gives
$$
A\subseteq B,
$$
and the second gives
$$
B\subseteq A.
$$
Thus
$$
\boxed{
A\subseteq B
\quad\text{or}\quad
B\subseteq A.
}
$$

:::

:::

::: pf-qed

Step <1>8 is the required conclusion.

:::

:::
