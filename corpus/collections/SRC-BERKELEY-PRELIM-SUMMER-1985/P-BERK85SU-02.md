---
schema: qual/card@1
id: P-BERK85SU-02
kind: problem
title: A sine lower bound and decay of a Laplace-type integral
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Concavity of sin on [0,pi/2] puts its graph above the chord from
    (0,0) to (pi/2,1), giving sin(theta)>=2theta/pi. Hence the integral is
    at most integral_0^{pi/2} exp(-2R theta/pi)dtheta <= pi/(2R), and
    multiplication by R^lambda tends to zero for lambda<1.
---

::: {.problem}
1. For $0\le\theta\le\pi/2$, prove
\[
\sin\theta\ge \frac{2}{\pi}\theta.
\]

2. Using part 1 or otherwise, prove that if $\lambda<1$, then
\[
\lim_{R\to\infty}R^\lambda\int_0^{\pi/2}e^{-R\sin\theta}\,d\theta=0.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For $0\le\theta\le\pi/2$,
$$
\sin\theta
\ge
\frac{2}{\pi}\theta.
$$

::: pf-proof

On $[0,\pi/2]$,
$$
\frac{d^2}{d\theta^2}\sin\theta
=
-\sin\theta
\le
0,
$$
so $\sin\theta$ is concave. A concave function lies above the chord
joining any two points of its graph. The chord joining
$$
(0,0)
\qquad\text{and}\qquad
(\pi/2,1)
$$
has equation
$$
y=\frac{2}{\pi}\theta.
$$
Thus the displayed inequality holds.

:::

:::

::: {.pf-step #s2}

For every $R>0$,
$$
0
\le
\int_0^{\pi/2}e^{-R\sin\theta}\,d\theta
\le
\frac{\pi}{2R}.
$$

::: pf-proof

By step [](#s1){.pf-ref},
$$
e^{-R\sin\theta}
\le
e^{-2R\theta/\pi}.
$$
Therefore
$$
\begin{aligned}
\int_0^{\pi/2}e^{-R\sin\theta}\,d\theta
&\le
\int_0^{\pi/2}e^{-2R\theta/\pi}\,d\theta\\
&=
\frac{\pi}{2R}(1-e^{-R})\\
&\le
\frac{\pi}{2R}.
\end{aligned}
$$
The lower bound is immediate from positivity of the integrand.

:::

:::

::: {.pf-step #s3}

If $\lambda<1$, then
$$
\boxed{
\lim_{R\to\infty}
R^\lambda
\int_0^{\pi/2}e^{-R\sin\theta}\,d\theta
=
0
}.
$$

::: pf-proof

Multiplying step [](#s2){.pf-ref} by $R^\lambda$ gives
$$
0
\le
R^\lambda
\int_0^{\pi/2}e^{-R\sin\theta}\,d\theta
\le
\frac\pi2 R^{\lambda-1}.
$$
Since $\lambda-1<0$, the right-hand side tends to $0$. The squeeze
theorem gives the displayed limit.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves part 1, and step [](#s3){.pf-ref} proves part 2.

:::

:::

:::
