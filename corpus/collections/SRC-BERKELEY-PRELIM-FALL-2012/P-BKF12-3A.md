---
schema: qual/card@1
id: P-BKF12-3A
kind: problem
title: Existence of the Euler--Mascheroni constant
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked against Problem 3A in the retained Fall 2012 Berkeley prelim exam
    and its retained solution packet F12_Solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked monotonicity and the positive lower bound by integral comparison.
---

::: {.problem}
Prove the existence of the limit

$$
\lim_{n\to\infty}
\left(
1+\frac12+\frac13+\cdots+\frac1n-\log n
\right).
$$
:::

::: {.solution}
Put
$$
H_n\coloneqq\sum_{k=1}^n\frac1k,
\qquad
\gamma_n\coloneqq H_n-\log n.
$$

::: pf

::: {.pf-step #s1}

The sequence $(\gamma_n)$ is decreasing.

::: pf-proof

For $n\ge1$,
$$
\begin{aligned}
\gamma_{n+1}-\gamma_n
&=\frac1{n+1}-\log\left(\frac{n+1}{n}\right)\\
&=\frac1{n+1}-\int_n^{n+1}\frac{dx}{x}.
\end{aligned}
$$
For $n<x<n+1$ one has
$$
\frac1x>\frac1{n+1}.
$$
Hence
$$
\int_n^{n+1}\frac{dx}{x}>\frac1{n+1},
$$
so $\gamma_{n+1}-\gamma_n<0$.

:::

:::

::: {.pf-step #s2}

The sequence $(\gamma_n)$ is bounded below by $0$.

::: pf-proof

For $n\ge2$ and each $k=1,\ldots,n-1$,
$$
\int_k^{k+1}\frac{dx}{x}<\frac1k.
$$
Summing these inequalities gives
$$
\log n
=\int_1^n\frac{dx}{x}
<\sum_{k=1}^{n-1}\frac1k
=H_{n-1}.
$$
Therefore
$$
\gamma_n
=H_n-\log n
>H_n-H_{n-1}
=\frac1n
>0.
$$
Also $\gamma_1=1$, so the lower bound holds for every $n\ge1$.

:::

:::

::: {.pf-step #s3}

The limit
$$
\boxed{\lim_{n\to\infty}\gamma_n}
$$
exists and is finite.

::: pf-proof

By step [](#s1){.pf-ref}, $(\gamma_n)$ is decreasing, and by step [](#s2){.pf-ref} it is
bounded below. Every monotone bounded real sequence converges.

:::

:::

::: pf-qed

By the definition of $\gamma_n$, step [](#s3){.pf-ref} is exactly the limit
whose existence was requested.

:::

:::

:::
