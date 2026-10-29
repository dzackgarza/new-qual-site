---
schema: qual/card@1
id: P-UCLAB08F-10
kind: problem
title: Norm inequality for vector-valued integrals
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
  note: Checked against Problem 10 of the retained UCLA Basic Examination, Fall 2008.
---

::: {.problem}
For $v=(v_1,\ldots,v_n)\in\RR^n$, let
\[
\|v\|=\left(\sum_{j=1}^n|v_j|^2\right)^{1/2}.
\]
If $f=(f_1,\ldots,f_n)\colon[a,b]\to\RR^n$ is continuous, define
\[
\int_a^b f(t)\,dt
=\left(\int_a^b f_1(t)\,dt,\ldots,\int_a^b f_n(t)\,dt\right).
\]
Prove that
\[
\left\|\int_a^b f(t)\,dt\right\|\le \int_a^b\|f(t)\|\,dt.
\]
:::

::: {.solution}

Let
\[
I=\int_a^b f(t)\,dt\in\RR^n.
\]

::: pf

::: {.pf-step #s1-1}

If $I=0$, then the desired inequality holds.


::: pf-proof

The left side is $0$, while the right side is nonnegative because $\|f(t)\|\ge0$.

:::

:::

::: {.pf-step #s1-2}

Suppose $I\ne0$ and define
\[
u=\frac{I}{\|I\|}.
\]
Then
\[
\|u\|=1
\]
and
\[
\|I\|=u\mathbin{\cdot} I.
\]


::: pf-proof

By construction,
\[
\|u\|=\frac{\|I\|}{\|I\|}=1.
\]
Also
\[
u\mathbin{\cdot}I
=
\frac{I\mathbin{\cdot}I}{\|I\|}
=
\frac{\|I\|^2}{\|I\|}
=
\|I\|.
\]

:::

:::

::: {.pf-step #s1-3}

One has
\[
u\mathbin{\cdot}I
=
\int_a^b u\mathbin{\cdot}f(t)\,dt.
\]


::: pf-proof

Writing
\[
u=(u_1,\ldots,u_n),
\qquad
f=(f_1,\ldots,f_n),
\]
linearity of the scalar integral gives
\[
\begin{aligned}
u\mathbin{\cdot}I
&=
\sum_{j=1}^n
u_j\int_a^b f_j(t)\,dt\\
&=
\int_a^b
\sum_{j=1}^n u_jf_j(t)\,dt\\
&=
\int_a^b u\mathbin{\cdot}f(t)\,dt.
\end{aligned}
\]

:::

:::

::: {.pf-step #s1-4}

For every $t\in[a,b]$,
\[
u\mathbin{\cdot}f(t)\le\|f(t)\|.
\]


::: pf-proof

By the Cauchy--Schwarz inequality,
\[
u\mathbin{\cdot}f(t)
\le
|u\mathbin{\cdot}f(t)|
\le
\|u\|\,\|f(t)\|
=
\|f(t)\|,
\]
using step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

One has
\[
\boxed{
\left\|\int_a^b f(t)\,dt\right\|
\le
\int_a^b\|f(t)\|\,dt
}.
\]


::: pf-proof

If $I=0$, apply step [](#s1-1){.pf-ref}. If $I\ne0$, steps [](#s1-2){.pf-ref} through [](#s1-4){.pf-ref} give
\[
\begin{aligned}
\|I\|
&=
u\mathbin{\cdot}I\\
&=
\int_a^b u\mathbin{\cdot}f(t)\,dt\\
&\le
\int_a^b\|f(t)\|\,dt.
\end{aligned}
\]

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required inequality.

:::

:::

:::
