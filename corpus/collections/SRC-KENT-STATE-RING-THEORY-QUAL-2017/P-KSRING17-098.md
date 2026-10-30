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
Let $D$ be a unique factorization domain and $p$ a fixed irreducible element of $D$ such that if $q$ is any irreducible element of $D$, then $q$ is an associate of $p$. Show the following.

(a) If $d$ is a nonzero element of $D$, then $d$ is uniquely expressible in the form $up^{n}$, where $u$ is a unit of $D$ and $n$ is a non-negative integer.

(b) $D$ is a Euclidean domain.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

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

::: {.pf-step #s1-2}

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

::: {.pf-step #s1-3}

Every irreducible factor $q_i$ in step [](#s1-2){.pf-ref} is associate to $p$.


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

::: {.pf-step #s1-4}

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

For units, use step [](#s1-1){.pf-ref}.
For nonunits, substitute
$$
q_i=u_ip
$$
from step [](#s1-3){.pf-ref} into the factorization in step [](#s1-2){.pf-ref}:
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

::: {.pf-step #s1-5}

The exponent $n$ in step [](#s1-4){.pf-ref} is unique.


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

::: {.pf-step #s1-6}

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

::: {.pf-step #s1-7}

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

Existence is step [](#s1-4){.pf-ref}, and uniqueness is steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref}.

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

Step [](#s1-7){.pf-ref} makes this definition unambiguous.

:::

:::

::: {.pf-step #s1-9}

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

::: {.pf-step #s1-10}

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
as in step [](#s1-7){.pf-ref}.
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

::: {.pf-step #s1-11}

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

::: {.pf-step #s1-12}

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
use step [](#s1-9){.pf-ref}.
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
step [](#s1-10){.pf-ref} gives division with remainder zero.
If
$$
m<n,
$$
step [](#s1-11){.pf-ref} gives a remainder of strictly smaller $\delta$-value.
Thus the Euclidean division axiom holds.

:::

:::

::: {.pf-step #s1-13}

Therefore
$$
\boxed{
D
\text{ is a Euclidean domain}.
}
$$


::: pf-proof

The ring $D$ is already an integral domain because it is a UFD.
Step [](#s1-12){.pf-ref} supplies a Euclidean function.
Hence $D$ is Euclidean.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} proves part (a), and step [](#s1-13){.pf-ref} proves part (b).

:::

:::

:::
