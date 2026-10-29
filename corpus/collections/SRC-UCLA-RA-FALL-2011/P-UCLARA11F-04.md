---
schema: qual/card@1
id: P-UCLARA11F-04
kind: problem
title: 'Weighted time derivative implies an $L^2$ limit'
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Fall 2011 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Let $f\in C^\infty([0,\infty)\times[0,1])$ satisfy
$$
\int_0^\infty\int_0^1 |\partial_t f(t,x)|^2(1+t^2)\,dx\,dt<\infty.
$$
Prove that there exists $g\in L^2([0,1])$ such that $f(t,\cdot)\to g$ in $L^2([0,1])$ as $t\to\infty$.
:::

::: {.solution}

For $t\ge0$, write
$$
F(t)=f(t,\cdot)\in L^2([0,1]).
$$

::: pf

::: {.pf-step #s1-1}

For $0\le s<t$ and every $x\in[0,1]$,
$$
\boxed{
f(t,x)-f(s,x)
=
\int_s^t \partial_\tau f(\tau,x)\,d\tau}.
$$


::: pf-proof

Apply the fundamental theorem of calculus in the $t$-variable, using smoothness of $f$.

:::

:::

::: {.pf-step #s1-2}

Hence
$$
\boxed{
\|F(t)-F(s)\|_{L^2}
\le
\int_s^t
\|\partial_\tau f(\tau,\cdot)\|_{L^2}\,d\tau}.
$$


::: pf-proof

Take the $L^2$-norm in $x$ of the integral in step [](#s1-1){.pf-ref} and apply Minkowski's integral inequality.

:::

:::

::: {.pf-step #s1-3}

Rewrite the integrand as
$$
\|\partial_\tau f(\tau,\cdot)\|_2
=
\sqrt{1+\tau^2}\,
\|\partial_\tau f(\tau,\cdot)\|_2
\cdot
\frac1{\sqrt{1+\tau^2}}.
$$


::: pf-proof

This is an algebraic identity.

:::

:::

::: {.pf-step #s1-4}

Cauchy--Schwarz in $\tau$ gives
$$
\boxed{
\int_s^t
\|\partial_\tau f(\tau,\cdot)\|_2\,d\tau
\le
\left(
\int_s^t
(1+\tau^2)
\|\partial_\tau f(\tau,\cdot)\|_2^2\,d\tau
\right)^{1/2}
\left(
\int_s^t
\frac{d\tau}{1+\tau^2}
\right)^{1/2}}.
$$


::: pf-proof

Apply Cauchy--Schwarz to the two factors from step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

By Fubini,
$$
\int_0^\infty
(1+\tau^2)
\|\partial_\tau f(\tau,\cdot)\|_2^2\,d\tau
=
\int_0^\infty\int_0^1
|\partial_t f(\tau,x)|^2
(1+\tau^2)\,dx\,d\tau.
$$


::: pf-proof

By definition,
$$
\|\partial_\tau f(\tau,\cdot)\|_2^2
=
\int_0^1
|\partial_t f(\tau,x)|^2\,dx.
$$
The integrand is nonnegative, so Tonelli's theorem applies.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
A:=
\int_0^\infty
(1+\tau^2)
\|\partial_\tau f(\tau,\cdot)\|_2^2\,d\tau
<\infty}.
$$


::: pf-proof

This is exactly the hypothesis, rewritten using step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

For $t\ge s$,
$$
\int_s^t
\frac{d\tau}{1+\tau^2}
\le
\int_s^\infty
\frac{d\tau}{1+\tau^2}.
$$


::: pf-proof

The integrand is nonnegative.

:::

:::

::: {.pf-step #s1-8}

One has
$$
\boxed{
\int_s^\infty
\frac{d\tau}{1+\tau^2}
=
\frac{\pi}{2}-\arctan s
\longrightarrow0}
$$
as $s\to\infty$.


::: pf-proof

An antiderivative is $\arctan\tau$, and
$$
\arctan s\to\frac\pi2.
$$

:::

:::

::: {.pf-step #s1-9}

Combining steps [](#s1-2){.pf-ref}, [](#s1-4){.pf-ref}, and [](#s1-6){.pf-ref}, and [](#s1-7){.pf-ref},
$$
\boxed{
\|F(t)-F(s)\|_2
\le
A^{1/2}
\left(
\int_s^\infty
\frac{d\tau}{1+\tau^2}
\right)^{1/2}}
$$
for every $t\ge s$.


::: pf-proof

The weighted energy integral over $[s,t]$ is at most $A$, and the second factor is bounded by the tail from step [](#s1-7){.pf-ref}.

:::

:::

::: pf-step

The right-hand side of step [](#s1-9){.pf-ref} tends to $0$ as $s\to\infty$, uniformly for all $t\ge s$.


::: pf-proof

The constant $A^{1/2}$ is finite by step [](#s1-6){.pf-ref}, and the tail factor tends to $0$ by step [](#s1-8){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

Hence $(F(t))_{t\ge0}$ is Cauchy in $L^2([0,1])$ as $t\to\infty$.


::: pf-proof

Given $\varepsilon>0$, choose $S$ so large that the right-hand side in step [](#s1-9){.pf-ref} is $<\varepsilon$ whenever $s\ge S$. Then for any $t\ge s\ge S$,
$$
\|F(t)-F(s)\|_2<\varepsilon.
$$
Interchanging $s,t$ handles the opposite order.

:::

:::

::: {.pf-step #s1-12}

Since $L^2([0,1])$ is complete, there exists
$$
g\in L^2([0,1])
$$
such that
$$
\boxed{
F(t)\to g
\text{ in }L^2([0,1])}.
$$


::: pf-proof

Every Cauchy net, and in particular every Cauchy trajectory indexed by sufficiently large real $t$, converges in the complete metric space $L^2([0,1])$. Equivalently, choose any sequence $t_n\to\infty$; step [](#s1-11){.pf-ref} gives a common Cauchy limit independent of the sequence, and the uniform tail estimate upgrades sequential convergence to full $t\to\infty$ convergence.

:::

:::

::: {.pf-step #s1-13}

Therefore
$$
\boxed{
f(t,\cdot)\to g
\quad\text{in }L^2([0,1])
\text{ as }t\to\infty}.
$$


::: pf-proof

This is step [](#s1-12){.pf-ref} in the original notation.

:::

:::

::: pf-qed

Step [](#s1-13){.pf-ref} is the required conclusion.

:::

:::

:::
