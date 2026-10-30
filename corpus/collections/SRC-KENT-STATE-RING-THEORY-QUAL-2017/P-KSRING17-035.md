---
schema: qual/card@1
id: P-KSRING17-035
kind: problem
title: The field $\QQ(\sqrt 2)$ is a principal ideal domain not containing $\sqrt 3$
classification:
  areas: [algebra]
  topics:
  - Quadratic Fields
  - Principal Ideal Domains
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 35 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let $\QQ$ be the field of rational numbers and $D = \{a + b\sqrt{2} \st a, b \in \QQ\}$.

(a) Show that $D$ is a subring of the field of real numbers.

(b) Show that $D$ is a principal ideal domain.

(c) Show that $\sqrt{3}$ is not an element of $D$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The set $D$ contains $0$ and $1$ and is closed under addition and additive inverses.


::: pf-proof

One has
$$
0=0+0\sqrt2
\qquad\text{and}\qquad
1=1+0\sqrt2.
$$
If
$$
x=a+b\sqrt2,
\qquad
y=c+d\sqrt2
$$
with
$$
a,b,c,d\in\QQ,
$$
then
$$
x+y
=
(a+c)+(b+d)\sqrt2
\in D
$$
and
$$
-x
=
(-a)+(-b)\sqrt2
\in D.
$$

:::

:::

::: {.pf-step #s1-2}

The set $D$ is closed under multiplication.


::: pf-proof

For
$$
x=a+b\sqrt2,
\qquad
y=c+d\sqrt2,
$$
one has
$$
\begin{aligned}
xy
&=
(a+b\sqrt2)(c+d\sqrt2)\\
&=
(ac+2bd)
+
(ad+bc)\sqrt2.
\end{aligned}
$$
Both coefficients are rational, so
$$
xy\in D.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{D\text{ is a subring of }\RR.}
$$


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} verify closure under the ring operations and show that the same $1$ as in $\RR$ belongs to $D$.

:::

:::

::: {.pf-step #s1-4}

If
$$
0\ne x=a+b\sqrt2\in D,
$$
then
$$
a^2-2b^2\ne0.
$$


::: pf-proof

Suppose
$$
a^2-2b^2=0.
$$
If
$$
b=0,
$$
then
$$
a=0,
$$
contrary to
$$
x\ne0.
$$
Thus
$$
b\ne0,
$$
and
$$
\left(\frac ab\right)^2=2.
$$
This would make
$$
\sqrt2
=
\abs{\frac ab}
\in\QQ,
$$
impossible. Hence
$$
a^2-2b^2\ne0.
$$

:::

:::

::: {.pf-step #s1-5}

Every nonzero element of $D$ has an inverse in $D$.


::: pf-proof

Let
$$
x=a+b\sqrt2\ne0.
$$
By step [](#s1-4){.pf-ref},
$$
a^2-2b^2\ne0.
$$
Then
$$
\begin{aligned}
x^{-1}
&=
\frac{a-b\sqrt2}{(a+b\sqrt2)(a-b\sqrt2)}\\
&=
\frac{a-b\sqrt2}{a^2-2b^2}\\
&=
\frac{a}{a^2-2b^2}
-
\frac{b}{a^2-2b^2}\sqrt2.
\end{aligned}
$$
Both coefficients are rational, so
$$
x^{-1}\in D.
$$

:::

:::

::: {.pf-step #s1-6}

Hence $D$ is a field, and therefore a principal ideal domain.


::: pf-proof

By steps [](#s1-3){.pf-ref} and [](#s1-5){.pf-ref}, $D$ is a commutative ring with identity in which every nonzero element is invertible. Thus $D$ is a field.

The only ideals of a field are
$$
(0)
\qquad\text{and}\qquad
(1)=D,
$$
both principal. Therefore
$$
\boxed{D\text{ is a PID}.}
$$

:::

:::

::: {.pf-step #s1-7}

Suppose, for contradiction, that
$$
\sqrt3\in D.
$$
Then there exist
$$
a,b\in\QQ
$$
such that
$$
\sqrt3=a+b\sqrt2.
$$


::: pf-proof

This is exactly the definition of membership in $D$.

:::

:::

::: {.pf-step #s1-8}

Under the assumption of step [](#s1-7){.pf-ref},
$$
ab=0
$$
and
$$
a^2+2b^2=3.
$$


::: pf-proof

Square the equation from step [](#s1-7){.pf-ref}:
$$
3
=
a^2+2b^2+2ab\sqrt2.
$$
Since
$$
\sqrt2\notin\QQ,
$$
the representation
$$
r+s\sqrt2
$$
with $r,s\in\QQ$ is unique. Therefore the coefficient of $\sqrt2$ must vanish:
$$
2ab=0.
$$
Thus
$$
ab=0,
$$
and comparison of rational parts gives
$$
a^2+2b^2=3.
$$

:::

:::

::: {.pf-step #s1-9}

The case
$$
b=0
$$
is impossible.


::: pf-proof

If
$$
b=0,
$$
step [](#s1-8){.pf-ref} gives
$$
a^2=3.
$$
Write
$$
a=\frac rs
$$
in lowest terms with
$$
r,s\in\ZZ,
\qquad
s\ne0.
$$
Then
$$
r^2=3s^2.
$$
Thus $3\mid r^2$, so $3\mid r$. Write
$$
r=3k.
$$
Then
$$
9k^2=3s^2,
$$
so
$$
3k^2=s^2.
$$
Hence
$$
3\mid s,
$$
contradicting the assumption that $r/s$ is in lowest terms.

:::

:::

::: {.pf-step #s1-10}

The case
$$
a=0
$$
is impossible.


::: pf-proof

If
$$
a=0,
$$
step [](#s1-8){.pf-ref} gives
$$
2b^2=3,
$$
so
$$
b^2=\frac32.
$$
Write
$$
b=\frac rs
$$
in lowest terms. Then
$$
2r^2=3s^2.
$$
The right side is even, so $s^2$ is even, hence
$$
2\mid s.
$$
Write
$$
s=2k.
$$
Then
$$
2r^2=12k^2,
$$
so
$$
r^2=6k^2,
$$
and hence
$$
2\mid r.
$$
This contradicts
$$
\gcd(r,s)=1.
$$

:::

:::

::: {.pf-step #s1-11}

Therefore
$$
\boxed{\sqrt3\notin D.}
$$


::: pf-proof

Step [](#s1-8){.pf-ref} gives
$$
ab=0,
$$
so either $a=0$ or $b=0$. Steps [](#s1-9){.pf-ref} through [](#s1-10){.pf-ref} rule out both possibilities.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves part (a), step [](#s1-6){.pf-ref} proves part (b), and step [](#s1-11){.pf-ref} proves part (c).

:::

:::

:::
