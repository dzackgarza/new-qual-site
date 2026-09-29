---
schema: qual/card@1
id: P-OZXEA
kind: problem
title: An entire function with $f(z)/z\to 0$ as $z\to\infty$ is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Entire Functions
  - Cauchy Estimates
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Suppose $f(z)$ is entire and 
\[
\lim_{z\to\infty} {f(z) \over z} = 0
.\]

Show that $f(z)$ is a constant.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

$f(z)/z\to0$ as $z\to\infty$ implies $f$ bounded: for $|z|>R$, $|f(z)|\le|z|$.

::: pf-proof

limit.

:::

:::

::: pf-step

Cauchy estimate for $f'$: $|f'(0)|\le \max_{|z|=R}|f(z)|/R$.

::: pf-proof

Cauchy.

:::

:::

::: pf-step

For large $R$, $\max_{|z|=R}|f(z)|\le2R$, so $|f'(0)|\le2$.

::: pf-proof

Step [](#s1){.pf-ref}.

:::

:::

::: pf-step

More generally $f(z)-f(0)$ satisfies same condition, and $g(z)=(f(z)-f(0))/z$ entire? Actually consider $g(z)=(f(z)-f(0))/z$ entire (removable at $0$).

::: pf-proof

$g$ entire.

:::

:::

::: {.pf-step #s5}

$g(z)\to0$ as $z\to\infty$ (since $f(z)/z\to0$), so $g$ bounded entire, hence constant $0$ by Liouville.

::: pf-proof

$g$ bounded.

:::

:::

::: {.pf-step #s6}

Hence $f(z)=f(0)$ constant.

::: pf-proof

Step [](#s5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref}.

:::

:::

:::
