---
schema: qual/card@1
id: P-WESRA12-2
kind: problem
title: 'Lebesgue-measure digit sets and a nearest-reciprocal function'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md. Flash renders the source interval as `{0,1}`; the decimal-expansion, Borel, and Lebesgue-measure context determines that the intended set is the interval $[0,1]$.
---

::: {.problem}
Let $X=[0,1]$ with its Borel $\sigma$-algebra and Lebesgue measure $\lambda$.

(a) Calculate the measure of each set:

1. $\{x\in X:\sin(2\pi/x)\le0\}$;

2. numbers $x=0.x_1x_2\cdots$ having no digit $x_i=7$;

3. numbers $x=0.x_1x_2\cdots$ for which $x_i=5$ and $x_{i+1}=6$ for some $i$.

(b) State the Dominated Convergence Theorem on $(X,\lambda)$.

(c) For $x\ne0$, choose a positive integer $n=n(x)$ for which the distance $d(x)$ from $x$ to $1/n$ is minimal, and define $f(x)=d(x)$ if $n$ is odd and $f(x)=0$ otherwise.
Explain why $f$ is integrable and calculate $\int_Xf\,d\lambda$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For
$$
x\in(0,1],
$$
set
$$
t=\frac1x.
$$
Then
$$
\sin(2\pi/x)\le0
$$
exactly when
$$
t\in
\bigcup_{k=0}^{\infty}
\left[
k+\frac12,
k+1
\right].
$$


::: pf-proof

The function
$$
\sin(2\pi t)
$$
is nonpositive precisely on the second half of each period:
$$
t\in
\left[
k+\frac12,
k+1
\right]
$$
for integers
$$
k\ge0.
$$

:::

:::

::: {.pf-step #s1-2}

Intersecting with
$$
t\ge1
$$
and returning to $x=1/t$, the set in part (a1), up to the single endpoint
$$
x=1,
$$
is
$$
\bigcup_{k=1}^{\infty}
\left[
\frac1{k+1},
\frac1{k+1/2}
\right].
$$


::: pf-proof

For
$$
k\ge1,
$$
the reciprocal map is decreasing, so
$$
k+\frac12
\le
\frac1x
\le
k+1
$$
is equivalent to
$$
\frac1{k+1}
\le
x
\le
\frac1{k+1/2}.
$$
The interval with $k=0$ meets $[1,\infty)$ only at
$$
t=1,
$$
corresponding to the single point
$$
x=1,
$$
which has measure zero.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\lambda
\{x\in[0,1]:\sin(2\pi/x)\le0\}
=
\sum_{k=1}^{\infty}
\left(
\frac1{k+1/2}
-
\frac1{k+1}
\right).
$$


::: pf-proof

The intervals in step [](#s1-2){.pf-ref} have pairwise disjoint interiors, and endpoints
do not affect Lebesgue measure.
The measure is therefore the sum of their lengths.

:::

:::

::: {.pf-step #s1-4}

The series in step [](#s1-3){.pf-ref} equals
$$
\boxed{
2\log2-1.
}
$$


::: pf-proof

The classical alternating harmonic series gives
$$
\log2
=
1-\frac12+\frac13-\frac14+\cdots.
$$
Equivalently,
$$
2\log2
=
\sum_{k=0}^{\infty}
\left(
\frac1{k+1/2}
-
\frac1{k+1}
\right).
$$
The $k=0$ term is
$$
2-1=1.
$$
Removing it leaves
$$
2\log2-1.
$$

:::

:::

::: {.pf-step #s1-5}

For part (a2), let
$$
E_m
$$
be the set of numbers in $[0,1]$ whose first $m$ decimal digits contain no
digit $7$.
Then
$$
\lambda(E_m)
=
\left(
\frac9{10}
\right)^m.
$$


::: pf-proof

Ignoring the countable set of numbers having two decimal expansions, fixing
the first $m$ decimal digits determines an interval of length
$$
10^{-m}.
$$
For each of the $m$ positions there are $9$ allowed digits.
Thus there are
$$
9^m
$$
allowed digit blocks, giving total measure
$$
9^m10^{-m}
=
\left(
\frac9{10}
\right)^m.
$$

:::

:::

::: {.pf-step #s1-6}

The set
$$
E
$$
of numbers having no digit $7$ satisfies
$$
E
=
\bigcap_{m=1}^{\infty}E_m
$$
up to the countable decimal-expansion ambiguity.


::: pf-proof

A decimal expansion contains no digit $7$ exactly when none of its finite
initial blocks contains a $7$.
The numbers with two decimal expansions form a countable set, hence have
measure zero.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{
\lambda(E)=0.
}
$$


::: pf-proof

The sets $E_m$ decrease with $m$ and have finite measure.
By continuity from above,
$$
\lambda(E)
=
\lim_{m\to\infty}
\lambda(E_m)
=
\lim_{m\to\infty}
\left(
\frac9{10}
\right)^m
=
0.
$$

:::

:::

::: {.pf-step #s1-8}

For part (a3), for each
$$
k\ge1,
$$
let $F_k$ be the set of numbers whose digits in positions
$$
2k-1
\quad\text{and}\quad
2k
$$
are respectively
$$
5
\quad\text{and}\quad
6.
$$
Then
$$
\lambda(F_k)=\frac1{100}.
$$


::: pf-proof

Fixing two prescribed decimal digits reduces measure by a factor of
$$
10^{-2}.
$$
Again the countable set of ambiguous decimal expansions is irrelevant.

:::

:::

::: {.pf-step #s1-9}

The measure of numbers for which none of the first $m$ disjoint digit
pairs equals $56$ is
$$
\left(
\frac{99}{100}
\right)^m.
$$


::: pf-proof

Among the
$$
100
$$
possible two-digit blocks in each pair of positions, exactly one is
forbidden.
For $m$ disjoint pairs there are
$$
99^m
$$
allowed blocks out of
$$
100^m.
$$
Thus the measure is
$$
\frac{99^m}{100^m}.
$$

:::

:::

::: {.pf-step #s1-10}

Hence the set of numbers containing the consecutive digits
$$
56
$$
somewhere has measure
$$
\boxed{1}.
$$


::: pf-proof

Let $G$ be the set of numbers that never contain $56$.
In particular, no disjoint pair
$$
(2k-1,2k)
$$
can equal $56$.
Thus for every $m$,
$$
G
$$
is contained in the set from step [](#s1-9){.pf-ref}.
Therefore
$$
\lambda(G)
\le
\left(
\frac{99}{100}
\right)^m
$$
for every $m$.
Letting
$$
m\to\infty
$$
gives
$$
\lambda(G)=0.
$$
Its complement, the set containing $56$ somewhere, has measure $1$.

:::

:::

::: {.pf-step #s1-11}

**Dominated Convergence Theorem.**

Let
$$
f_n:X\to\RR
$$
be measurable functions such that
$$
f_n(x)\to f(x)
$$
for almost every $x$.
Suppose there exists
$$
g\in L^1(X,\lambda)
$$
with
$$
\abs{f_n(x)}
\le
g(x)
$$
for almost every $x$ and every $n$.
Then
$$
f\in L^1(X,\lambda)
$$
and
$$
\boxed{
\lim_{n\to\infty}
\int_X f_n\,d\lambda
=
\int_X f\,d\lambda.
}
$$


::: pf-proof

This is the Dominated Convergence Theorem on the measure space
$$
([0,1],\mathcal B,\lambda).
$$

:::

:::

::: {.pf-step #s1-12}

For part (c), set
$$
a_n
\coloneqq
\frac1n.
$$
For
$$
n\ge2,
$$
the points closer to $a_n$ than to its neighboring reciprocals form the
interval
$$
I_n
=
\left[
\frac12
\left(
\frac1n+\frac1{n+1}
\right),
\frac12
\left(
\frac1{n-1}+\frac1n
\right)
\right].
$$
For $n=1$,
$$
I_1
=
\left[
\frac34,1
\right].
$$


::: pf-proof

The nearest-reciprocal boundary between
$$
\frac1n
\quad\text{and}\quad
\frac1{n+1}
$$
is their midpoint.
For $n\ge2$, the Voronoi cell of $1/n$ is therefore bounded by the
midpoints with
$$
\frac1{n+1}
$$
and
$$
\frac1{n-1}.
$$
For $n=1$, only the neighbor
$$
\frac12
$$
occurs inside $[0,1]$, and the midpoint is
$$
\frac34.
$$

:::

:::

::: {.pf-step #s1-13}

The midpoint tie set is countable and therefore has measure zero.


::: pf-proof

There is one tie point between each consecutive pair
$$
\frac1n,
\frac1{n+1}.
$$
Thus the set of ties is countable.
Any ambiguity in the choice of $n(x)$ affects $f$ only on this null set and
does not affect the integral.

:::

:::

::: {.pf-step #s1-14}

On
$$
I_n,
$$
the distance function is
$$
d(x)
=
\abs{
x-\frac1n
}.
$$
For
$$
n\ge2,
$$
the left and right half-widths are
$$
L_n
=
\frac1{2n(n+1)}
$$
and
$$
R_n
=
\frac1{2n(n-1)}.
$$


::: pf-proof

The left endpoint is
$$
\frac12
\left(
\frac1n+\frac1{n+1}
\right).
$$
Subtracting it from
$$
\frac1n
$$
gives
$$
L_n
=
\frac12
\left(
\frac1n-\frac1{n+1}
\right)
=
\frac1{2n(n+1)}.
$$
Similarly,
$$
R_n
=
\frac12
\left(
\frac1{n-1}-\frac1n
\right)
=
\frac1{2n(n-1)}.
$$

:::

:::

::: {.pf-step #s1-15}

For
$$
n\ge2,
$$
$$
\int_{I_n}
d(x)\,dx
=
\frac1{8n^2}
\left(
\frac1{(n+1)^2}
+
\frac1{(n-1)^2}
\right).
$$


::: pf-proof

The graph of
$$
d(x)
=
\abs{
x-\frac1n
}
$$
on $I_n$ consists of two triangles.
Therefore
$$
\int_{I_n}d(x)\,dx
=
\frac12L_n^2
+
\frac12R_n^2.
$$
Substitute the values from step [](#s1-14){.pf-ref}.

:::

:::

::: {.pf-step #s1-16}

For
$$
n=1,
$$
$$
\int_{I_1}d(x)\,dx
=
\frac1{32}.
$$


::: pf-proof

On
$$
I_1=[3/4,1],
$$
$$
d(x)=1-x.
$$
Thus
$$
\int_{3/4}^1(1-x)\,dx
=
\frac12
\left(
\frac14
\right)^2
=
\frac1{32}.
$$

:::

:::

::: {.pf-step #s1-17}

The function $f$ is measurable and integrable.


::: pf-proof

Up to the countable tie set, $f$ is given on each interval $I_n$ by either
$$
\abs{
x-\frac1n
}
$$
when $n$ is odd or by $0$ when $n$ is even.
Thus $f$ is measurable.

Also
$$
0\le f(x)\le1
$$
on $[0,1]$.
Therefore
$$
\abs{f}
\le
1\in L^1([0,1]).
$$
Hence $f$ is integrable.

:::

:::

::: {.pf-step #s1-18}

Its integral is
$$
\int_0^1f(x)\,dx
=
\frac1{32}
+
\sum_{\substack{n\ge3\\n\text{ odd}}}
\frac1{8n^2}
\left(
\frac1{(n+1)^2}
+
\frac1{(n-1)^2}
\right).
$$


::: pf-proof

The intervals $I_n$ partition $(0,1]$ up to their shared endpoints.
The function vanishes on even-indexed cells and equals the distance function
on odd-indexed cells.
Apply steps [](#s1-15){.pf-ref} through [](#s1-16){.pf-ref}.

:::

:::

::: {.pf-step #s1-19}

For
$$
n\ge2,
$$
$$
\frac1{8n^2}
\left(
\frac1{(n+1)^2}
+
\frac1{(n-1)^2}
\right)
=
\frac1{4(n+1)}
+
\frac1{8(n+1)^2}
-
\frac1{4(n-1)}
+
\frac1{8(n-1)^2}
+
\frac1{4n^2}.
$$


::: pf-proof

Bring the right-hand side over the common denominator
$$
8n^2(n-1)^2(n+1)^2
$$
and simplify.
Both sides reduce to
$$
\frac{n^2+1}
{4n^2(n^2-1)^2}.
$$

:::

:::

::: {.pf-step #s1-20}

Summing the first-order terms in step [](#s1-19){.pf-ref} over odd
$$
n\ge3
$$
gives
$$
-\frac18.
$$


::: pf-proof

Write
$$
n=2k+1,
\qquad
k\ge1.
$$
Then
$$
\frac1{4(n+1)}
-
\frac1{4(n-1)}
=
\frac1{8(k+1)}
-
\frac1{8k}.
$$
The series telescopes:
$$
\sum_{k=1}^{\infty}
\left(
\frac1{8(k+1)}
-
\frac1{8k}
\right)
=
-\frac18.
$$

:::

:::

::: {.pf-step #s1-21}

Summing the two shifted-square terms gives
$$
\frac{\pi^2}{96}
-
\frac1{32}.
$$


::: pf-proof

Again set
$$
n=2k+1.
$$
Then
$$
\begin{aligned}
&\sum_{\substack{n\ge3\\n\text{ odd}}}
\left(
\frac1{8(n+1)^2}
+
\frac1{8(n-1)^2}
\right)\\
&=
\frac1{32}
\sum_{k=1}^{\infty}
\left(
\frac1{(k+1)^2}
+
\frac1{k^2}
\right)\\
&=
\frac1{32}
\left(
2\sum_{k=1}^{\infty}\frac1{k^2}
-1
\right).
\end{aligned}
$$
Using
$$
\sum_{k=1}^{\infty}\frac1{k^2}
=
\frac{\pi^2}{6},
$$
this becomes
$$
\frac1{32}
\left(
\frac{\pi^2}{3}
-1
\right)
=
\frac{\pi^2}{96}
-
\frac1{32}.
$$

:::

:::

::: {.pf-step #s1-22}

Summing the final term
$$
\frac1{4n^2}
$$
over odd
$$
n\ge3
$$
gives
$$
\frac{\pi^2}{32}
-
\frac14.
$$


::: pf-proof

The sum of reciprocal squares over positive odd integers is
$$
\sum_{\substack{n\ge1\\n\text{ odd}}}
\frac1{n^2}
=
\left(
1-\frac1{2^2}
\right)
\frac{\pi^2}{6}
=
\frac{\pi^2}{8}.
$$
Removing the
$$
n=1
$$
term gives
$$
\frac{\pi^2}{8}-1.
$$
Multiply by
$$
\frac14.
$$

:::

:::

::: {.pf-step #s1-23}

Therefore
$$
\boxed{
\int_0^1f(x)\,dx
=
\frac{\pi^2}{24}
-
\frac38
=
\frac{\pi^2-9}{24}.
}
$$


::: pf-proof

By steps [](#s1-18){.pf-ref} through [](#s1-22){.pf-ref},
$$
\begin{aligned}
\int_0^1f(x)\,dx
&=
\frac1{32}
-
\frac18
+
\left(
\frac{\pi^2}{96}
-
\frac1{32}
\right)
+
\left(
\frac{\pi^2}{32}
-
\frac14
\right)\\
&=
\frac{\pi^2}{24}
-
\frac38.
\end{aligned}
$$
Finally,
$$
\frac{\pi^2}{24}
-
\frac38
=
\frac{\pi^2-9}{24}.
$$

:::

:::

::: pf-step

The answers to part (a) are
$$
\boxed{
2\log2-1,
\qquad
0,
\qquad
1.
}
$$


::: pf-proof

These are steps [](#s1-4){.pf-ref} and [](#s1-7){.pf-ref}, and [](#s1-10){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-10){.pf-ref} solve part (a), step [](#s1-11){.pf-ref} states the Dominated
Convergence Theorem for part (b), and steps [](#s1-12){.pf-ref} through [](#s1-23){.pf-ref} solve part (c).

:::

:::

:::
