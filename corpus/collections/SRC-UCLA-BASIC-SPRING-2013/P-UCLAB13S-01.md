---
schema: qual/card@1
id: P-UCLAB13S-01
kind: problem
title: Riemann integrability of monotone functions
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 1 of the retained UCLA Basic Examination, Spring 2013.
---

::: {.problem}
(a) Define what it means for a function on $[0,1]$ to be Riemann integrable.

(b) Show that every monotone increasing function on $[0,1]$ is Riemann integrable.

(c) Use part (b) to give an example of a Riemann integrable function on $[0,1]$ which has infinitely many discontinuities.
:::

::: {.solution}

::: pf

::: pf-step

Let
\[
P:\quad 0=x_0<x_1<\cdots<x_m=1
\]
be a partition of $[0,1]$.
For each subinterval
\[
I_i=[x_{i-1},x_i],
\]
define
\[
M_i=\sup_{x\in I_i}f(x),
\qquad
m_i=\inf_{x\in I_i}f(x),
\]
and the upper and lower Darboux sums
\[
U(f,P)
=
\sum_{i=1}^m
M_i(x_i-x_{i-1}),
\]
\[
L(f,P)
=
\sum_{i=1}^m
m_i(x_i-x_{i-1}).
\]


::: pf-proof

These are the standard Darboux sums associated to a bounded function and a partition.

:::

:::

::: {.pf-step #s1-2}

A bounded function
\[
f:[0,1]\to\RR
\]
is Riemann integrable if
\[
\boxed{
\inf_P U(f,P)
=
\sup_P L(f,P).
}
\]
Equivalently, for every $\varepsilon>0$ there exists a partition $P$ with
\[
U(f,P)-L(f,P)<\varepsilon.
\]


::: pf-proof

The equality of the upper and lower Darboux integrals is the definition of Riemann integrability.

The equivalent criterion follows because
\[
L(f,P)
\le
\underline{\int_0^1}f
\le
\overline{\int_0^1}f
\le
U(f,P)
\]
for every partition $P$, while passing to a common refinement can only increase lower sums and decrease upper sums.
This answers part (a).

:::

:::

::: {.pf-step #s1-3}

Let $f$ be monotone increasing on $[0,1]$.
Then for every partition $P$,
\[
M_i=f(x_i)
\qquad\text{and}\qquad
m_i=f(x_{i-1}).
\]


::: pf-proof

If
\[
x_{i-1}\le x\le x_i,
\]
monotonicity gives
\[
f(x_{i-1})
\le
f(x)
\le
f(x_i).
\]
Thus the infimum and supremum on $I_i$ are attained at the endpoints.

:::

:::

::: {.pf-step #s1-4}

For a monotone increasing $f$,
\[
U(f,P)-L(f,P)
=
\sum_{i=1}^m
\bigl(
f(x_i)-f(x_{i-1})
\bigr)
(x_i-x_{i-1}).
\]


::: pf-proof

Substitute the formulas from step [](#s1-3){.pf-ref} into the definitions of the Darboux sums.

:::

:::

::: {.pf-step #s1-5}

If the mesh of $P$ is at most $\delta$, then
\[
U(f,P)-L(f,P)
\le
\delta\bigl(f(1)-f(0)\bigr).
\]


::: pf-proof

Every increment
\[
f(x_i)-f(x_{i-1})
\]
is nonnegative.
Hence step [](#s1-4){.pf-ref} gives
\[
\begin{aligned}
U(f,P)-L(f,P)
&\le
\delta
\sum_{i=1}^m
\bigl(
f(x_i)-f(x_{i-1})
\bigr)\\
&=
\delta
\bigl(
f(1)-f(0)
\bigr),
\end{aligned}
\]
because the sum telescopes.

:::

:::

::: {.pf-step #s1-6}

Every monotone increasing function on $[0,1]$ is Riemann integrable.


::: pf-proof

If
\[
f(1)=f(0),
\]
then monotonicity forces $f$ to be constant, hence integrable.

Otherwise, given
\[
\varepsilon>0,
\]
choose
\[
0<\delta
<
\frac{\varepsilon}{f(1)-f(0)}.
\]
Take a partition with mesh at most $\delta$.
Then step [](#s1-5){.pf-ref} gives
\[
U(f,P)-L(f,P)<\varepsilon.
\]
By the criterion in step [](#s1-2){.pf-ref}, $f$ is Riemann integrable.
This proves part (b).

:::

:::

::: {.pf-step #s1-7}

Define
\[
\boxed{
g(x)
=
\sum_{n=1}^{\infty}
2^{-n}
\mathbf 1_{[1/n,1]}(x).
}
\]
Then $g$ is monotone increasing on $[0,1]$.


::: pf-proof

Each summand
\[
x\longmapsto
\mathbf 1_{[1/n,1]}(x)
\]
is monotone increasing.
All coefficients
\[
2^{-n}
\]
are positive.
Therefore the pointwise sum is monotone increasing.

The series converges for every $x$ because
\[
0
\le
2^{-n}\mathbf 1_{[1/n,1]}(x)
\le
2^{-n},
\]
and
\[
\sum_{n=1}^{\infty}2^{-n}=1.
\]

:::

:::

::: {.pf-step #s1-8}

The function $g$ is Riemann integrable.


::: pf-proof

By step [](#s1-7){.pf-ref}, $g$ is monotone increasing.
Apply part (b), proved in step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

For every positive integer $m$, the function $g$ is discontinuous at
\[
x=\frac1m.
\]


::: pf-proof

At
\[
x=\frac1m,
\]
the $m$th summand
\[
2^{-m}\mathbf 1_{[1/m,1]}(x)
\]
jumps upward by
\[
2^{-m}.
\]
All other summands are monotone increasing and cannot cancel this jump.

More explicitly, as $x\uparrow1/m$, the $m$th summand is $0$, while at $x=1/m$ it equals $2^{-m}$.
Thus
\[
g(1/m)
-
\lim_{x\uparrow1/m}g(x)
\ge
2^{-m}
>
0.
\]
Hence $g$ is discontinuous at $1/m$.

:::

:::

::: {.pf-step #s1-10}

Therefore $g$ is a Riemann integrable function with infinitely many discontinuities.


::: pf-proof

Step [](#s1-8){.pf-ref} gives Riemann integrability.
Step [](#s1-9){.pf-ref} gives a discontinuity at every point
\[
1,\frac12,\frac13,\ldots,
\]
which is an infinite set.
This proves part (c).

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} answers part (a), step [](#s1-6){.pf-ref} proves part (b), and step [](#s1-10){.pf-ref} gives the example required in part (c).

:::

:::

:::
