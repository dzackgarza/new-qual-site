---
schema: qual/card@1
id: P-BKF18-5B
kind: problem
title: Derivative at the origin for an extremal bounded entire function
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Suppose $h$ is entire, $h(0)=3+4i$, and $\abs{h(z)}\le5$ whenever $\abs{z}<1$.
What is $h'(0)$?
:::

::: {.solution}

$h'(0)=0$.

::: pf

::: {.pf-step #s1}

$h$ is constant.

::: pf-proof

$\abs{h(0)}=\sqrt{3^2+4^2}=5$, so $\abs{h}$ restricted to the open unit disk attains its maximum $5$ at the interior point $0$. By the maximum modulus principle, $h$ is constant on the disk, and by the identity theorem $h$ is constant on $\CC$.

:::

:::

::: pf-qed

By step [](#s1){.pf-ref}, $h'\equiv0$, so $h'(0)=0$.

:::

:::

:::
