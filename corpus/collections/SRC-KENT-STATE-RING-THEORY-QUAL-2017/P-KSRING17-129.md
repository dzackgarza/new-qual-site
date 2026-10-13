---
schema: qual/card@1
id: P-KSRING17-129
kind: problem
title: Localizations of a PID at nonzero primes are discrete valuation rings
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 129 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let D be a principal ideal domain and let P be a non-zero prime ideal.
Show that $D _ { P }$ , the localization of D at P , is a principal ideal domain and has a unique irreducible element, up to associates.
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

<1>1. Let
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

::: {.proof}
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

<1>2. One has
$$
J=S^{-1}I.
$$

::: {.proof}
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

<1>3. The ideal $J$ is principal.

::: {.proof}
Since $D$ is a PID,
$$
I=(d)
$$
for some
$$
d\in D.
$$
By step <1>2,
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

<1>4. The ring $D_P$ is an integral domain.

::: {.proof}
It is a subring of the fraction field of the integral domain $D$.
Hence it has no zero divisors.
:::

<1>5. Therefore
$$
\boxed{
D_P
\text{ is a principal ideal domain}.
}
$$

::: {.proof}
Step <1>3 shows every ideal is principal, and step <1>4 shows $D_P$ is an integral domain.
:::

<1>6. The element $p$ is irreducible in $D$.

::: {.proof}
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

<1>7. A fraction
$$
\frac as\in D_P
$$
is a unit if
$$
a\notin P.
$$

::: {.proof}
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

<1>8. A fraction
$$
\frac as\in D_P
$$
with
$$
a\in P
$$
is not a unit.

::: {.proof}
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

<1>9. Therefore
$$
\boxed{
\frac as
\text{ is a unit in }D_P
\iff
a\notin P.
}
$$

::: {.proof}
Combine steps <1>7 and <1>8.
:::

<1>10. The element
$$
\frac p1
$$
is a nonunit of $D_P$.

::: {.proof}
Its numerator
$$
p
$$
lies in
$$
P.
$$
Apply step <1>9.
:::

<1>11. The element
$$
\frac p1
$$
is irreducible in $D_P$.

::: {.proof}
Suppose
$$
\frac p1
=
\frac as\frac bt
$$
with both factors nonunits.
By step <1>9,
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

<1>12. Let
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

::: {.proof}
An irreducible element is a nonunit.
By step <1>9, a nonunit fraction must have numerator in
$$
P.
$$
:::

<1>13. Write
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

::: {.proof}
By step <1>12,
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

<1>14. The factor
$$
\frac ds
$$
is a unit.

::: {.proof}
The element
$$
\alpha
$$
is irreducible.
Step <1>13 expresses it as a product
$$
\alpha
=
\frac p1\frac ds.
$$
By step <1>10,
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

<1>15. Every irreducible element of $D_P$ is associate to
$$
p/1.
$$

::: {.proof}
Step <1>13 gives
$$
\alpha
=
\frac p1\frac ds,
$$
and step <1>14 shows
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

<1>16. Consequently,
$$
\boxed{
D_P
\text{ has a unique irreducible element up to associates}.
}
$$

::: {.proof}
Step <1>11 gives the irreducible
$$
p/1,
$$
and step <1>15 shows every irreducible is associate to it.
:::

<1>17. Q.E.D.

::: {.proof}
Step <1>5 proves that $D_P$ is a PID, and step <1>16 proves uniqueness of the irreducible up to associates.
:::
:::
