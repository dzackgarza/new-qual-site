---
schema: qual/card@1
id: P-V33ML
kind: problem
title: Layer-cake formula for a measurable function
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Integrals
relations: []
review: draft
---


::: {.problem}

Let $f:\RR^n\to\RR$ be measurable. Show that
$$
\int_{\RR^n} \abs{ f} = \int_0^{\infty } m(A_t)\dt, \qquad A_t \coloneqq \theset{x\in \RR^n \st \abs{f(x)} > t}.
$$

:::

::: {.solution}

::: pf

::: {.pf-step #indicator}

For every $x \in \RR^n$, $\abs{f(x)} = \int_0^\infty \mathbf{1}_{A_t}(x)\dt$.

::: pf-proof

For fixed $x$, $\mathbf{1}_{A_t}(x) = 1$ exactly when $0 \le t < \abs{f(x)}$, so the integral is the length of $[0, \abs{f(x)})$.

:::

:::

::: pf-step

$\int_{\RR^n} \abs{f} = \int_0^\infty m(A_t)\dt$, where both sides may be $+\infty$.

::: pf-proof

The set $\theset{(x,t) : \abs{f(x)} > t}$ is measurable in $\RR^n\times[0,\infty)$ because $(x,t) \mapsto \abs{f(x)} - t$ is measurable, so $(x,t) \mapsto \mathbf{1}_{A_t}(x)$ is measurable and nonnegative. By step [](#indicator){.pf-ref} and Tonelli's theorem,
$$
\int_{\RR^n}\abs{f(x)}\dx
 = \int_{\RR^n}\int_0^\infty \mathbf{1}_{A_t}(x)\dt\dx
 = \int_0^\infty \int_{\RR^n}\mathbf{1}_{A_t}(x)\dx\dt
 = \int_0^\infty m(A_t)\dt.
$$
Tonelli's theorem needs no integrability hypothesis.

:::

:::

:::

:::
