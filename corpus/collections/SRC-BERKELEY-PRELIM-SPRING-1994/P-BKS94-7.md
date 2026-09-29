---
schema: qual/card@1
id: P-BKS94-7
kind: problem
title: Lower bound for $|1-\sum a_k e^{2\pi ikx}|$ on $[0,1]$
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
  note: Checked against the vendored UC Berkeley Spring 1994 preliminary examination.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Integrated over one period: the trigonometric polynomial has mean 1, so
    its modulus cannot be strictly less than 1 everywhere.
---

::: {.problem}
Let $a _ { 1 } , a _ { 2 } , \ldots , a _ { n }$ be complex numbers. Prove that there is a point x in [0, 1] such that

$$
\left| 1 - \sum _ { k = 1 } ^ { n } a _ { k } e ^ { 2 \pi i k x } \right| \geqslant 1 .
$$
:::

::: {.solution}
Define
$$
F(x)\coloneqq
1-\sum_{k=1}^n a_ke^{2\pi ikx}.
$$

::: pf

::: {.pf-step #s1}

One has
$$
\int_0^1F(x)\,dx=1.
$$

::: pf-proof

For every positive integer $k$,
$$
\int_0^1e^{2\pi ikx}\,dx
=
\left[\frac{e^{2\pi ikx}}{2\pi ik}\right]_0^1
=0.
$$
Therefore
$$
\int_0^1F(x)\,dx
=
1-\sum_{k=1}^n
a_k\int_0^1e^{2\pi ikx}\,dx
=1.
$$

:::

:::

::: {.pf-step #s2}

It is impossible that
$$
\abs{F(x)}<1
$$
for every $x\in[0,1]$.

::: pf-proof

Suppose the strict inequality held everywhere. Since $\abs F$ is continuous
on the compact interval $[0,1]$, it attains a maximum
$$
m<1.
$$
Then step [](#s1){.pf-ref} and the triangle inequality for integrals give
$$
1
=
\abs{\int_0^1F(x)\,dx}
\leq
\int_0^1\abs{F(x)}\,dx
\leq
m
<1,
$$
a contradiction.

:::

:::

::: {.pf-step #s3}

There exists $x\in[0,1]$ such that
$$
\abs{
1-\sum_{k=1}^n a_ke^{2\pi ikx}
}
\geq1.
$$

::: pf-proof

This is the negation of the impossible assertion in step [](#s2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the required conclusion.

:::

:::

:::
