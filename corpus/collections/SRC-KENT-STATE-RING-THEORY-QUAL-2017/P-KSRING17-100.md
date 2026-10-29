---
schema: qual/card@1
id: P-KSRING17-100
kind: problem
title: Euclidean algorithm in $\ZZ[i]$ for $\gcd(5+i,13)$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 100 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Show that the ring Z[i] of Gaussian integers is a Euclidean ring and compute the greatest common divisor of $5 + i$ and 13 using the Euclidean algorithm.
:::

::: {.solution}

Let
$$
\ZZ[i]
\coloneqq
\{a+bi:a,b\in\ZZ\},
$$
and define
$$
N(a+bi)
\coloneqq
a^2+b^2.
$$

::: pf

::: pf-step

The norm is multiplicative:
$$
N(zw)=N(z)N(w)
$$
for all
$$
z,w\in\ZZ[i].
$$


::: pf-proof

For
$$
z=a+bi,
$$
one has
$$
N(z)
=
z\overline z.
$$
Hence
$$
\begin{aligned}
N(zw)
&=
zw\,\overline{zw}\\
&=
zw\,\overline z\,\overline w\\
&=
(z\overline z)(w\overline w)\\
&=
N(z)N(w).
\end{aligned}
$$

:::

:::

::: pf-step

Let
$$
\alpha,\beta\in\ZZ[i],
\qquad
\beta\ne0.
$$
Write
$$
\frac{\alpha}{\beta}
=
x+yi
$$
with
$$
x,y\in\QQ.
$$
Choose integers
$$
m,n
$$
such that
$$
\abs{x-m}\le\frac12,
\qquad
\abs{y-n}\le\frac12.
$$


::: pf-proof

The fraction field of
$$
\ZZ[i]
$$
is
$$
\QQ(i),
$$
so the displayed representation exists.
Every real number lies within distance at most
$$
\frac12
$$
of an integer, so $m,n$ can be chosen as stated.

:::

:::

::: {.pf-step #s1-3}

Set
$$
q
\coloneqq
m+ni.
$$
Then
$$
N\left(
\frac{\alpha}{\beta}-q
\right)
\le
\frac12.
$$


::: pf-proof

One has
$$
\frac{\alpha}{\beta}-q
=
(x-m)+(y-n)i.
$$
Therefore
$$
\begin{aligned}
N\left(
\frac{\alpha}{\beta}-q
\right)
&=
(x-m)^2+(y-n)^2\\
&\le
\frac14+\frac14\\
&=
\frac12.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

Define
$$
r
\coloneqq
\alpha-q\beta.
$$
Then
$$
\alpha=q\beta+r,
$$
and if
$$
r\ne0,
$$
then
$$
N(r)<N(\beta).
$$


::: pf-proof

One has
$$
r
=
\beta
\left(
\frac{\alpha}{\beta}-q
\right).
$$
By multiplicativity of the norm and step [](#s1-3){.pf-ref},
$$
\begin{aligned}
N(r)
&=
N(\beta)
N\left(
\frac{\alpha}{\beta}-q
\right)\\
&\le
\frac12N(\beta)\\
&<
N(\beta),
\end{aligned}
$$
because
$$
N(\beta)>0.
$$

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
\ZZ[i]
\text{ is a Euclidean domain with Euclidean function }N.
}
$$


::: pf-proof

Step [](#s1-4){.pf-ref} gives Euclidean division with remainder of strictly smaller norm whenever the remainder is nonzero.

:::

:::

::: {.pf-step #s1-6}

For the elements
$$
13
\qquad\text{and}\qquad
5+i,
$$
one has
$$
\boxed{
13
=
(2-i)(5+i)
+
(2+3i).
}
$$


::: pf-proof

Compute
$$
\begin{aligned}
(2-i)(5+i)
&=
10+2i-5i-i^2\\
&=
11-3i.
\end{aligned}
$$
Hence
$$
13-(11-3i)
=
2+3i.
$$
Also,
$$
N(2+3i)
=
4+9
=
13
<
26
=
N(5+i),
$$
so this is a valid Euclidean-division step.

:::

:::

::: {.pf-step #s1-7}

The next division is exact:
$$
\boxed{
5+i
=
(1-i)(2+3i).
}
$$


::: pf-proof

Compute
$$
\begin{aligned}
(1-i)(2+3i)
&=
2+3i-2i-3i^2\\
&=
5+i.
\end{aligned}
$$
Thus the remainder is zero.

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
2+3i
$$
is a greatest common divisor of
$$
5+i
$$
and
$$
13.
$$


::: pf-proof

In a Euclidean domain, the last nonzero remainder in the Euclidean algorithm is a greatest common divisor.
By steps [](#s1-6){.pf-ref} through [](#s1-7){.pf-ref}, the last nonzero remainder is
$$
2+3i.
$$
Hence
$$
\boxed{
\gcd(5+i,13)
\sim
2+3i,
}
$$
where
$$
\sim
$$
denotes equality up to multiplication by a unit
$$
\pm1,\pm i.
$$

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves that
$$
\ZZ[i]
$$
is Euclidean, and step [](#s1-8){.pf-ref} gives the requested greatest common divisor.

:::

:::

:::
