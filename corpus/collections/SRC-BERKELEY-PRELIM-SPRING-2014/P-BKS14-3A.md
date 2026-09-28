---
schema: qual/card@1
id: P-BKS14-3A
kind: problem
title: Approximate an exponential integral
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2014 preliminary examination PDF.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked termwise integration, cancellation of odd powers, the value 73/72, and an explicit geometric bound on the omitted tail.
---

::: {.problem}
Find a real number \(c\) such that
\[
\left|c-\int_{-1/2}^{1/2}\frac{e^x-1}{x}\,dx\right|<0.01.
\]
:::

::: {.solution}
Let
$$
I
\coloneqq
\int_{-1/2}^{1/2}\frac{e^x-1}{x}\,dx.
$$

<1>1. On $[-1/2,1/2]$,
$$
\frac{e^x-1}{x}
=
\sum_{m=0}^{\infty}\frac{x^m}{(m+1)!},
$$
with the value at $x=0$ understood by continuity, and the series may be
integrated term by term.

::: {.proof}
The exponential series gives
$$
e^x-1
=
\sum_{k=1}^{\infty}\frac{x^k}{k!}.
$$
For $x\neq0$, division by $x$ gives the displayed series. At $x=0$, both
sides have the continuous value $1$.

The exponential power series converges uniformly on compact intervals,
and the divided series also converges uniformly on $[-1/2,1/2]$, for
example by the Weierstrass M-test:
$$
\abs{\frac{x^m}{(m+1)!}}
\leq
\frac{2^{-m}}{(m+1)!}.
$$
Therefore termwise integration is valid.
:::

<1>2. The integral is
$$
I
=
\sum_{j=0}^{\infty}
\frac{1}{2^{2j}(2j+1)(2j+1)!}.
$$

::: {.proof}
By step <1>1,
$$
I
=
\sum_{m=0}^{\infty}
\frac{1}{(m+1)!}
\int_{-1/2}^{1/2}x^m\,dx.
$$
The integral vanishes when $m$ is odd. For $m=2j$,
$$
\begin{aligned}
\int_{-1/2}^{1/2}x^{2j}\,dx
&=
\frac{2}{2j+1}
\left(\frac12\right)^{2j+1}\\
&=
\frac{1}{2^{2j}(2j+1)}.
\end{aligned}
$$
Substitution gives the formula.
:::

<1>3. The first two terms of the series in step <1>2 sum to
$$
\boxed{
c
=
1+\frac1{72}
=
\frac{73}{72}
}.
$$

::: {.proof}
The $j=0$ term is
$$
1.
$$
The $j=1$ term is
$$
\frac{1}{2^2\cdot3\cdot3!}
=
\frac1{72}.
$$
:::

<1>4. If
$$
T_j
\coloneqq
\frac{1}{2^{2j}(2j+1)(2j+1)!},
$$
then for every $j\geq2$,
$$
0<T_{j+1}<\frac14T_j.
$$

::: {.proof}
Directly,
$$
\frac{T_{j+1}}{T_j}
=
\frac{2j+1}
{4(2j+3)^2(2j+2)}
<
\frac14.
$$
:::

<1>5. The error made by choosing $c=73/72$ satisfies
$$
\abs{I-c}
<
\frac1{7200}
<
0.01.
$$

::: {.proof}
All terms in step <1>2 are positive, so
$$
I-c
=
\sum_{j=2}^{\infty}T_j.
$$
The first omitted term is
$$
T_2
=
\frac{1}{2^4\cdot5\cdot5!}
=
\frac1{9600}.
$$
By step <1>4,
$$
\sum_{j=2}^{\infty}T_j
<
\sum_{\ell=0}^{\infty}\frac{T_2}{4^\ell}
=
\frac43T_2
=
\frac1{7200}.
$$
:::

<1>6. Therefore the real number
$$
\boxed{\frac{73}{72}}
$$
satisfies the required inequality.

::: {.proof}
This is exactly the estimate in step <1>5.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 supplies an admissible value of $c$.
:::
:::
