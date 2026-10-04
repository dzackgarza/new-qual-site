---
schema: qual/card@1
id: P-KSRING17-100
kind: problem
title: Euclidean algorithm in $\mathbb Z[i]$ for $\gcd(5+i,13)$
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

<1>1. The norm is multiplicative:
$$
N(zw)=N(z)N(w)
$$
for all
$$
z,w\in\ZZ[i].
$$

::: {.proof}
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

<1>2. Let
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

::: {.proof}
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

<1>3. Set
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

::: {.proof}
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

<1>4. Define
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

::: {.proof}
One has
$$
r
=
\beta
\left(
\frac{\alpha}{\beta}-q
\right).
$$
By multiplicativity of the norm and step <1>3,
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

<1>5. Therefore
$$
\boxed{
\ZZ[i]
\text{ is a Euclidean domain with Euclidean function }N.
}
$$

::: {.proof}
Step <1>4 gives Euclidean division with remainder of strictly smaller norm whenever the remainder is nonzero.
:::

<1>6. For the elements
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

::: {.proof}
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

<1>7. The next division is exact:
$$
\boxed{
5+i
=
(1-i)(2+3i).
}
$$

::: {.proof}
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

<1>8. Therefore
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

::: {.proof}
In a Euclidean domain, the last nonzero remainder in the Euclidean algorithm is a greatest common divisor.
By steps <1>6--<1>7, the last nonzero remainder is
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

<1>9. Q.E.D.

::: {.proof}
Step <1>5 proves that
$$
\ZZ[i]
$$
is Euclidean, and step <1>8 gives the requested greatest common divisor.
:::
:::
