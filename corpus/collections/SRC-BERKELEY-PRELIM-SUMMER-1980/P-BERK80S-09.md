---
schema: qual/card@1
id: P-BERK80S-09
kind: problem
title: Absolute and conditional convergence of a logarithmic power series
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 9 of the vendored Berkeley Preliminary Exam, Summer 1980.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the root-test regimes, the logarithmic p-series boundary, and the exact alternating-series condition at a=-1.
---

::: {.problem}
For each $(a,b,c)\in\RR^3$, consider the series

$$
\sum_{n=3}^{\infty}\frac{a^n}{n^b(\log n)^c}.
$$

Determine the values of $(a,b,c)$ for which the series

1. converges absolutely;

2. converges but not absolutely;

3. diverges.
:::

::: {.solution}
Write
$$
u_n=\frac{a^n}{n^b(\log n)^c}.
$$

<1>1. If $\abs{a}<1$, the series converges absolutely; if $\abs{a}>1$, it
diverges.

::: {.proof}
The $n$th root of $\abs{u_n}$ satisfies
$$
\abs{u_n}^{1/n}
=\abs{a}\,n^{-b/n}(\log n)^{-c/n}
\longrightarrow \abs{a}.
$$
The root test gives absolute convergence when $\abs{a}<1$ and divergence
when $\abs{a}>1$.
:::

<1>2. For $\abs{a}=1$, the series
$$
\sum_{n=3}^\infty \abs{u_n}=\sum_{n=3}^\infty \frac1{n^b(\log n)^c}
$$
converges exactly when $b>1$, or when $b=1$ and $c>1$.

::: {.proof}
If $b=1$, the integral test compares the series with
$$
\int_3^\infty \frac{dx}{x(\log x)^c}.
$$
With $u=\log x$, this becomes
$$
\int_{\log 3}^\infty u^{-c}\,du,
$$
which converges exactly when $c>1$.

If $b>1$ and $c\ge0$, the summand is eventually bounded by $n^{-b}$. If
$b>1$ and $c<0$, choose $0<\varepsilon<b-1$. Since
$(\log n)^{\abs{c}}=o(n^\varepsilon)$, the summand is eventually bounded by
$n^{-(b-\varepsilon)}$, and $b-\varepsilon>1$. In both cases the series
converges.

If $b<1$, choose $0<\varepsilon<1-b$. When $c>0$, the estimate
$(\log n)^c=o(n^\varepsilon)$ gives, for large $n$,
$$
\frac1{n^b(\log n)^c}\ge \frac1{n^{b+\varepsilon}},
$$
and $b+\varepsilon<1$, so the series diverges. When $c\le0$, the summand
is at least $n^{-b}$ for $n\ge3$, and the series diverges because $b<1$.
:::

<1>3. For $a=1$, the series converges exactly when it converges
absolutely.

::: {.proof}
For $a=1$ every term is positive, so $u_n=\abs{u_n}$.
:::

<1>4. For $a=-1$, the series converges exactly when
$$
b>0
\qquad\text{or}\qquad
b=0,\ c>0.
$$

::: {.proof}
Write
$$
d_n=\frac1{n^b(\log n)^c}>0,
$$
so that $u_n=(-1)^nd_n$. The sequence $d_n$ tends to $0$ exactly when
$b>0$, or $b=0$ and $c>0$; otherwise $d_n\not\to0$ and the series
diverges. In the two convergent cases,
$$
\frac{d}{dx}\log\frac1{x^b(\log x)^c}
=-\frac1x\left(b+\frac{c}{\log x}\right)<0
$$
for large $x$, so $d_n$ is eventually decreasing, and the alternating
series test gives convergence.
:::

<1>5. The series
$$
\boxed{
\begin{aligned}
&\text{converges absolutely iff } \abs{a}<1, \text{ or } \abs{a}=1 \text{ and } (b>1 \text{ or } b=1,\ c>1);\\
&\text{converges but not absolutely iff } a=-1 \text{ and } (0<b<1,\ \text{or } b=1,\ c\le1,\ \text{or } b=0,\ c>0);\\
&\text{diverges in all other cases.}
\end{aligned}
}
$$

::: {.proof}
Steps <1>1 and <1>2 give the absolute-convergence region. Conditional
convergence requires convergence without absolute convergence; by step
<1>1 this forces $\abs{a}=1$, by step <1>3 it forces $a=-1$, and step <1>4
together with step <1>2 gives the listed parameters. Every other
parameter value gives a divergent series by steps <1>1--<1>4.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 answers all three parts.
:::
:::
