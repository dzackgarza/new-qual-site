---
schema: qual/card@1
id: P-JHUFA02CAJ
kind: problem
title: Simplicity and small-disk zero count for $z^7+z^3+1/16$
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros of Polynomials
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the polynomial, no-multiple-zero request and closed radius-one-half disk with Fall 2002 Complex Analysis problem 5."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Excluded common zeros of P and P' algebraically, then used a strict Rouche comparison with z^3+1/16 and checked that its three zeros lie strictly inside radius one half."
---

::: {.problem}
5. Let $\begin{array} { r } { P ( z ) = z ^ { 7 } + z ^ { 3 } + \frac { 1 } { 1 6 } } \end{array}$

(a) (5 points) Show that P has no multiple zeros.

(b) (15 points) Determine the number of zeros of P that lie in the closed disc $| z | \leq { \frac { 1 } { 2 } }$
:::

::: {.solution}
<1>1. Part (a): $P$ and $P'$ have no common zero.
::: {.proof}
Let
$$
P(z)=z^7+z^3+\frac1{16}.
$$
Then
$$
P'(z)=7z^6+3z^2=z^2(7z^4+3).
$$
A multiple zero of $P$ would be a common zero of $P$ and $P'$. The point
$z=0$ is not a zero of $P$. Hence any common zero would satisfy
$$
z^4=-\frac37.
$$
Substituting this into $P(z)=0$ gives
$$
z^3\left(z^4+1\right)+\frac1{16}=0,
$$
so
$$
\frac47 z^3=-\frac1{16},
\qquad z^3=-\frac7{64}.
$$
But then
$$
z^{12}=(z^4)^3=-\frac{27}{343}<0,
$$
while simultaneously
$$
z^{12}=(z^3)^4=\left(\frac7{64}\right)^4>0,
$$
a contradiction. Thus $P$ has no multiple zeros.
:::

<1>2. Part (b): Rouché's theorem gives exactly three zeros in the closed disk.
::: {.proof}
On $|z|=1/2$,
$$
|z^7|=\frac1{128},
$$
whereas
$$
\left|z^3+\frac1{16}\right|
\ge |z|^3-\frac1{16}
=\frac18-\frac1{16}
=\frac1{16}.
$$
Hence
$$
|z^7|<\left|z^3+\frac1{16}\right|
$$
on the entire boundary circle. Rouché's theorem shows that $P$ and
$z^3+1/16$ have the same number of zeros in $|z|<1/2$, counted with
multiplicity.

The three zeros of $z^3+1/16$ satisfy
$$
|z|=\left(\frac1{16}\right)^{1/3}=2^{-4/3}<\frac12,
$$
so all three lie inside the circle. Therefore $P$ has exactly three zeros in
$|z|<1/2$. The strict Rouché inequality also implies that $P$ has no zero on
$|z|=1/2$. Thus the closed disk $|z|\le1/2$ contains exactly
$$
\boxed{3}
$$
zeros.
:::
:::
