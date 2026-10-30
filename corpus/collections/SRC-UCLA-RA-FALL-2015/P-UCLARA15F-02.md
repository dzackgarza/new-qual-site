---
schema: qual/card@1
id: P-UCLARA15F-02
kind: problem
title: Almost everywhere convergence of $\sum_n\int_n^{n+n^{-a}}\abs{f(x+y)}\,dy$ for $f\in L^p$
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the retained UCLA Analysis Qualifying Exam Solutions compendium, Fall 2015 section; the official exam PDF is image-only.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retranscribed the font-garbled statement in LaTeX from Problem 2 on page 1 of the official analysis-15F.pdf exam, checked against the Fall 2015 section of UCLA_Solutions.pdf.
---

::: {.problem}
Let $f \in L^p(\RR)$, $1 < p < \infty$, and let $a \in \RR$ be such that $a > 1 - \frac{1}{p}$. Show that the series
$$
\sum_{n=1}^{\infty} \int_n^{n+n^{-a}} \abs{f(x+y)}\,dy
$$
converges for almost all $x \in \RR$.
:::

::: {.solution}

Let
$$
q=\frac{p}{p-1}
$$
be the conjugate exponent, so
$$
\frac1p+\frac1q=1.
$$

Define the nonnegative measurable function
$$
G(x)
=
\sum_{n=1}^{\infty}
\int_n^{n+n^{-a}}
\abs{f(x+y)}\,dy,
$$
allowing the value $+\infty$.

It suffices to prove
$$
G(x)<\infty
$$
for almost every $x$.

::: pf

::: pf-step

For each $n$,
$$
\boxed{
\int_n^{n+n^{-a}}
\abs{f(x+y)}\,dy
=
n^{-a}
\int_0^1
\abs{f(x+n+n^{-a}z)}\,dz}.
$$


::: pf-proof

Use the change of variables
$$
y=n+n^{-a}z,
\qquad
dy=n^{-a}\,dz.
$$

:::

:::

::: pf-step

Since
$$
a>\frac1q,
$$
one has
$$
\boxed{
\sum_{n=1}^{\infty}n^{-aq}<\infty}.
$$


::: pf-proof

The inequality $a>1/q$ is equivalent to
$$
aq>1,
$$
so this is a convergent $p$-series.

:::

:::

::: {.pf-step #s1-3}

For every $M\ge1$,
$$
\sum_{n=1}^{M}n^{-a}B_n(x)
\le
C
\left(
\sum_{n=1}^{M}B_n(x)^p
\right)^{1/p}.
$$


::: pf-proof

Apply Hölder's inequality to the finite sum with exponents $q$ and $p$:
$$
\sum_{n=1}^{M}
n^{-a}B_n
\le
\left(
\sum_{n=1}^{M}n^{-aq}
\right)^{1/q}
\left(
\sum_{n=1}^{M}B_n^p
\right)^{1/p}.
$$
Bound the first factor by $C$.

:::

:::

::: {.pf-step #s1-4}

Letting $M\to\infty$,
$$
\boxed{
G(x)^p
\le
C^p
\sum_{n=1}^{\infty}B_n(x)^p}.
$$


::: pf-proof

The partial sums on both sides increase with $M$. Raise step [](#s1-3){.pf-ref} to the $p$th power and pass to the monotone limit, allowing $+\infty$.

:::

:::

::: {.pf-step #s1-5}

For each $n$,
$$
\boxed{
B_n(x)^p
\le
\int_0^1
\abs{f(x+n+n^{-a}z)}^p\,dz}.
$$


::: pf-proof

Apply Hölder's inequality on $[0,1]$:
$$
\left(
\int_0^1 h(z)\,dz
\right)^p
\le
\left(
\int_0^1 1^q\,dz
\right)^{p/q}
\int_0^1 h(z)^p\,dz
=
\int_0^1h(z)^p\,dz.
$$
Take
$$
h(z)=\abs{f(x+n+n^{-a}z)}.
$$

:::

:::

::: {.pf-step #s1-6}

Hence
$$
\boxed{
G(x)^p
\le
C^p
\sum_{n=1}^{\infty}
\int_0^1
\abs{f(x+n+n^{-a}z)}^p\,dz}.
$$


::: pf-proof

Combine steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

Tonelli's theorem gives
$$
\begin{aligned}
\int_N^{N+1}G(x)^p\,dx
\le
C^p
\int_0^1
\sum_{n=1}^{\infty}
\int_N^{N+1}
\abs{f(x+n+n^{-a}z)}^p\,dx\,dz.
\end{aligned}
$$


::: pf-proof

Integrate step [](#s1-6){.pf-ref} over $[N,N+1]$. All terms are nonnegative, so Tonelli permits interchange of the integral and the infinite sum.

:::

:::

::: {.pf-step #s1-8}

For fixed $n,z$, the change of variables
$$
u=x+n+n^{-a}z
$$
gives
$$
\boxed{
\int_N^{N+1}
\abs{f(x+n+n^{-a}z)}^p\,dx
=
\int_{N+n+n^{-a}z}^{N+1+n+n^{-a}z}
\abs{f(u)}^p\,du}.
$$


::: pf-proof

The change of variables is a translation, so $du=dx$.

:::

:::

::: {.pf-step #s1-9}

Since
$$
a>1-\frac1p>0,
$$
one has
$$
\boxed{
0<n^{-a}\le1}
$$
for every $n\ge1$.


::: pf-proof

The exponent $a$ is positive, and $n\ge1$.

:::

:::

::: {.pf-step #s1-10}

Therefore, for $0\le z\le1$,
$$
\boxed{
[N+n+n^{-a}z,\,
N+1+n+n^{-a}z]
\subseteq
[N+n,\,
N+n+2]}.
$$


::: pf-proof

The left endpoint is at least $N+n$, and by step [](#s1-9){.pf-ref},
$$
1+n^{-a}z\le2.
$$

:::

:::

::: {.pf-step #s1-11}

Hence
$$
\int_N^{N+1}
\abs{f(x+n+n^{-a}z)}^p\,dx
\le
\int_{N+n}^{N+n+2}
\abs{f(u)}^p\,du.
$$


::: pf-proof

Use steps [](#s1-8){.pf-ref} through [](#s1-10){.pf-ref} and nonnegativity of the integrand.

:::

:::

::: {.pf-step #s1-12}

The intervals
$$
[N+n,N+n+2],
\qquad
n=1,2,\dots,
$$
have overlap multiplicity at most $2$ almost everywhere.


::: pf-proof

A point $u$ belongs to such an interval exactly when
$$
u-N-2\le n\le u-N.
$$
This interval of possible integers has length $2$, so except at endpoints it contains at most two integers. Endpoint coincidences form a null set and do not affect the integral estimate.

:::

:::

::: {.pf-step #s1-13}

Consequently,
$$
\boxed{
\sum_{n=1}^{\infty}
\int_{N+n}^{N+n+2}
\abs{f(u)}^p\,du
\le
2\norm{f}_{L^p(\RR)}^p}.
$$


::: pf-proof

By Tonelli,
$$
\sum_n
\int_{N+n}^{N+n+2}\abs{f(u)}^p\,du
=
\int_{\RR}
\abs{f(u)}^p
\left(
\sum_n
\mathbf1_{[N+n,N+n+2]}(u)
\right)
du.
$$
The multiplicity factor is at most $2$ almost everywhere by step [](#s1-12){.pf-ref}.

:::

:::

::: pf-step

Combining steps [](#s1-7){.pf-ref} and [](#s1-11){.pf-ref}, and [](#s1-13){.pf-ref},
$$
\boxed{
\int_N^{N+1}G(x)^p\,dx
\le
2C^p\norm{f}_p^p
<
\infty}.
$$


::: pf-proof

The bound in step [](#s1-13){.pf-ref} is independent of $z$, and
$$
\int_0^1dz=1.
$$

:::

:::

::: {.pf-step #s1-15}

Therefore
$$
\boxed{
G(x)<\infty
\text{ for almost every }x\in[N,N+1]}.
$$


::: pf-proof

If a nonnegative measurable function has finite $p$th power integral on a finite interval, it is finite almost everywhere there.

:::

:::

::: {.pf-step #s1-16}

Since
$$
\RR
=
\bigcup_{N\in\ZZ}[N,N+1],
$$
one has
$$
\boxed{
G(x)<\infty
\text{ for almost every }x\in\RR}.
$$


::: pf-proof

For each integer $N$, the exceptional set in $[N,N+1]$ has measure zero by step [](#s1-15){.pf-ref}. A countable union of null sets is null.

:::

:::

::: {.pf-step #s1-17}

Hence, for almost every $x$,
$$
\boxed{
\sum_{n=1}^{\infty}
\int_n^{n+n^{-a}}
\abs{f(x+y)}\,dy
\text{ converges}.}
$$


::: pf-proof

The series has nonnegative terms, so convergence is equivalent to finiteness of its sum $G(x)$. Apply step [](#s1-16){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-17){.pf-ref} is the required conclusion.

:::

:::

:::
