---
schema: qual/card@1
id: P-CASP19A
kind: problem
title: "Entire function bounded by log(|f| + 2) is constant"
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Liouville's Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $f$ be an entire function.
Assume $|f| \leq \log(|f| + 2)$ on $\mathbb{C}$.
Prove $f$ is constant.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The inequality $|f(z)| \le \log(|f(z)| + 2)$ holds for all $z \in \mathbb{C}$.

::: pf-proof

hypothesis.

:::

:::

::: {.pf-step #s2}

The function $h(t) = t - \log(t + 2)$ satisfies $h(0) = -\log 2 < 0$ and $h(t) \to \infty$ as $t \to \infty$, and $h'(t) = 1 - 1/(t+2) > 0$ for $t > 0$.

::: pf-proof

calculus.

:::

:::

::: {.pf-step #s3}

Hence the set $\{t \ge 0 : t \le \log(t + 2)\}$ is bounded.

::: pf-proof

Step [](#s2){.pf-ref} ($h(t) \le 0$ only for bounded $t$).

:::

:::

::: {.pf-step #s4}

Therefore $|f(z)|$ is uniformly bounded (there is $M$ with $|f(z)| \le M$ for all $z$).

::: pf-proof

Steps [](#s1){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

::: {.pf-step #s5}

By Liouville's theorem, a bounded entire function is constant.

::: pf-proof

Liouville's theorem.

:::

:::

::: {.pf-step #s6}

Hence $f$ is constant.

::: pf-proof

Steps [](#s4){.pf-ref} and [](#s5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref}.

:::

:::

:::
