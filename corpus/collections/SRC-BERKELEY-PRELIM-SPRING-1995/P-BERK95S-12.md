---
schema: qual/card@1
id: P-BERK95S-12
kind: problem
title: Integral of $(1-\cos n\theta)/(1-\cos\theta)$ over $[0,2\pi]$
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
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $n$ be a positive integer. Compute
\[
\int_0^{2\pi}\frac{1-\cos(n\theta)}{1-\cos\theta}\,d\theta.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For $\theta\notin2\pi\ZZ$,
$$
\frac{1-\cos(n\theta)}{1-\cos\theta}
=
\abs{\sum_{k=0}^{n-1}e^{ik\theta}}^2.
$$

::: pf-proof

Using
$$
\abs{1-e^{it}}^2=2(1-\cos t)
$$
and the geometric-sum identity,
$$
\sum_{k=0}^{n-1}e^{ik\theta}
=
\frac{1-e^{in\theta}}{1-e^{i\theta}},
$$
we obtain
$$
\abs{\sum_{k=0}^{n-1}e^{ik\theta}}^2
=
\frac{2(1-\cos(n\theta))}{2(1-\cos\theta)}.
$$
The quotient has a removable singularity at each point of $2\pi\ZZ$,
where both sides extend continuously with value $n^2$.

:::

:::

::: {.pf-step #s2}

$$
\int_0^{2\pi}
\abs{\sum_{k=0}^{n-1}e^{ik\theta}}^2\,d\theta
=2\pi n.
$$

::: pf-proof

Expand:
$$
\abs{\sum_{k=0}^{n-1}e^{ik\theta}}^2
=
\sum_{j,k=0}^{n-1}e^{i(j-k)\theta}.
$$
For an integer $m$,
$$
\int_0^{2\pi}e^{im\theta}\,d\theta
=
\begin{cases}
2\pi,&m=0,\\
0,&m\ne0.
\end{cases}
$$
Thus only the $n$ diagonal terms $j=k$ survive the integration,
giving $2\pi n$.

:::

:::

::: {.pf-step #s3}

The requested integral equals
$$
\boxed{2\pi n}.
$$

::: pf-proof

Combine steps [](#s1){.pf-ref} and [](#s2){.pf-ref}. Changing the value at the removable
singularity does not affect the integral.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} gives the value of the integral.

:::

:::

:::
