---
schema: qual/card@1
id: P-KSRING17-098
kind: problem
title: A UFD with a single irreducible up to associates is Euclidean
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 98 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let D be a unique factorization domain and p a fixed irreducible element of D such that if q is any irreducible element of $D ,$ then q is an associate of $p .$ Show the following.

(a) If d is a nonzero element of D, then d is uniquely expressible in the form $u p ^ { n }$ , where u is a unit of D and n is a non-negative integer.

(b) D is a Euclidean domain.
:::

::: pf

::: pf-step

Let
$$
0\ne d\in D.
$$
If $d$ is a unit, then
$$
d=dp^0.
$$


::: pf-proof

This gives the required form with
$$
u=d
\qquad\text{and}\qquad
n=0.
$$

:::

:::

::: pf-step

If $d$ is a nonunit, then
$$
d
=
u q_1q_2\cdots q_n
$$
for a unit $u$ and irreducibles $q_i$.


::: pf-proof

This is the existence part of unique factorization in the UFD $D$.

:::

:::

::: pf-step

Every irreducible factor $q_i$ in step <1>2 is associate to $p$.


::: pf-proof

This is exactly the hypothesis on the fixed irreducible element $p$.
Thus for each $i$ there is a unit
$$
u_i
$$
such that
$$
q_i=u_ip.
$$

:::

:::

::: pf-step

Every nonzero element $d\in D$ has an expression
$$
d=up^n
$$
with
$$
u\in D^\times,
\qquad
n\ge0.
$$


::: pf-proof

For units, use step <1>1.
For nonunits, substitute
$$
q_i=u_ip
$$
from step <1>3 into the factorization in step <1>2:
$$
\begin{aligned}
d
&=
u
\prod_{i=1}^{n}(u_ip)\\
&=
\left(
u\prod_{i=1}^{n}u_i
\right)
p^n.
\end{aligned}
$$
The product of units is a unit.

:::

:::

::: pf-step

The exponent $n$ in step <1>4 is unique.


::: pf-proof

Suppose
$$
up^m
=
vp^n
$$
with
$$
u,v
\in
D^\times.
$$
Assume
$$
m<n.
$$
Cancelling
$$
p^m
$$
in the domain gives
$$
u
=
vp^{n-m}.
$$
The right-hand side is a unit only if
$$
p^{n-m}
$$
is a unit, which is impossible because
$$
n-m>0
$$
and $p$ is irreducible.
Thus
$$
m<n
$$
is impossible.
By symmetry,
$$
n<m
$$
is impossible.
Hence
$$
m=n.
$$

:::

:::

::: pf-step

Once the exponent is fixed, the unit factor is also unique.


::: pf-proof

If
$$
up^n
=
vp^n,
$$
cancellation of the nonzero element
$$
p^n
$$
gives
$$
u=v.
$$

:::

:::

::: pf-step

Therefore every nonzero element has a unique expression
$$
\boxed{
d=up^n,
\qquad
u\in D^\times,
\quad
n\in\ZZ_{\ge0}.
}
$$


::: pf-proof

Existence is step <1>4, and uniqueness is steps <1>5--<1>6.

:::

:::

::: pf-step

Define
$$
\delta:D\setminus\{0\}\to\ZZ_{\ge0}
$$
by
$$
\delta(up^n)
\coloneqq
n.
$$


::: pf-proof

Step <1>7 makes this definition unambiguous.

:::

:::

::: pf-step

Let
$$
a,b\in D,
\qquad
b\ne0.
$$
If
$$
a=0,
$$
then
$$
a=0\cdot b+0.
$$


::: pf-proof

This is a valid Euclidean division with zero remainder.

:::

:::

::: pf-step

Suppose
$$
a\ne0
$$
and write
$$
a=up^m,
\qquad
b=vp^n
$$
as in step <1>7.
If
$$
m\ge n,
$$
then $b$ divides $a$.


::: pf-proof

Since
$$
m\ge n,
$$
one has
$$
a
=
up^m
=
\left(
uv^{-1}p^{m-n}
\right)
vp^n
=
\left(
uv^{-1}p^{m-n}
\right)b.
$$
Thus
$$
a=qb+0
$$
with
$$
q=uv^{-1}p^{m-n}\in D.
$$

:::

:::

::: pf-step

If
$$
m<n,
$$
then
$$
a=0\cdot b+a
$$
and
$$
\delta(a)<\delta(b).
$$


::: pf-proof

The displayed equality is immediate.
By definition,
$$
\delta(a)=m,
\qquad
\delta(b)=n.
$$
Since
$$
m<n,
$$
the remainder $a$ has strictly smaller Euclidean value than $b$.

:::

:::

::: pf-step

The function $\delta$ is a Euclidean function on $D$.


::: pf-proof

Let
$$
a,b\in D,
\qquad
b\ne0.
$$
If
$$
a=0,
$$
use step <1>9.
If
$$
a\ne0,
$$
write
$$
a=up^m,
\qquad
b=vp^n.
$$
If
$$
m\ge n,
$$
step <1>10 gives division with remainder zero.
If
$$
m<n,
$$
step <1>11 gives a remainder of strictly smaller $\delta$-value.
Thus the Euclidean division axiom holds.

:::

:::

::: pf-step

Therefore
$$
\boxed{
D
\text{ is a Euclidean domain}.
}
$$


::: pf-proof

The ring $D$ is already an integral domain because it is a UFD.
Step <1>12 supplies a Euclidean function.
Hence $D$ is Euclidean.

:::

:::

::: pf-qed

Step <1>7 proves part (a), and step <1>13 proves part (b).

:::

:::
