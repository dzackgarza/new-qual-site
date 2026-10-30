---
schema: qual/card@1
id: P-TRIV-CA19
kind: problem
title: $\int_0^\pi \cos^{2n}\theta\,d\theta$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 19, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Compute $\int_0^{\pi} (\cos\theta)^{2n}\, \mathrm{d}\theta$.
:::

::: {.solution}

Assume $n$ is a nonnegative integer.

::: pf

::: {.pf-step #s1-1}

Since $\cos^{2n}\theta$ has period $\pi$,
$$
\int_0^{\pi}\cos^{2n}\theta\,d\theta
=
\frac12
\int_0^{2\pi}\cos^{2n}\theta\,d\theta.
$$


::: pf-proof

One has
$$
\cos(\theta+\pi)=-\cos\theta,
$$
so
$$
\cos^{2n}(\theta+\pi)=\cos^{2n}\theta.
$$
Thus the two half-period integrals over $[0,\pi]$ and $[\pi,2\pi]$ are
equal.

:::

:::

::: {.pf-step #s1-2}

Euler's formula gives
$$
\cos^{2n}\theta
=
\frac1{2^{2n}}
\sum_{k=0}^{2n}
\binom{2n}{k}
e^{i(2n-2k)\theta}.
$$


::: pf-proof

Since
$$
\cos\theta
=
\frac{e^{i\theta}+e^{-i\theta}}2,
$$
the binomial theorem gives
$$
\cos^{2n}\theta
=
\frac1{2^{2n}}
\sum_{k=0}^{2n}
\binom{2n}{k}
e^{i(2n-k)\theta}e^{-ik\theta}.
$$
Combine the exponential factors.

:::

:::

::: {.pf-step #s1-3}

For an integer $m$,
$$
\int_0^{2\pi}e^{im\theta}\,d\theta
=
\begin{cases}
2\pi,&m=0,\\
0,&m\ne0.
\end{cases}
$$


::: pf-proof

For $m=0$ the integrand is $1$. If $m\ne0$,
$$
\int_0^{2\pi}e^{im\theta}\,d\theta
=
\left[
\frac{e^{im\theta}}{im}
\right]_0^{2\pi}
=0.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\int_0^{2\pi}\cos^{2n}\theta\,d\theta
=
\frac{2\pi}{4^n}
\binom{2n}{n}.
$$


::: pf-proof

In the expansion from step [](#s1-2){.pf-ref}, step [](#s1-3){.pf-ref} kills every term except the one
with
$$
2n-2k=0,
$$
namely $k=n$. The surviving coefficient is
$$
2^{-2n}\binom{2n}{n}.
$$
Multiplying it by $2\pi$ gives the result.

:::

:::

::: {.pf-step #s1-5}

Hence
$$
\boxed{
\int_0^{\pi}\cos^{2n}\theta\,d\theta
=
\frac{\pi}{4^n}
\binom{2n}{n}.
}
$$


::: pf-proof

Apply step [](#s1-1){.pf-ref} to the value obtained in step [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the requested integral.

:::

:::

:::
