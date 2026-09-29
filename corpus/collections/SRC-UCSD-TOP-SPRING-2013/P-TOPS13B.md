---
schema: qual/card@1
id: P-TOPS13B
kind: problem
title: "Low-dimensional homotopy groups of S^3 x S^4 x S^5"
classification:
  areas:
  - topology
  topics:
  - Homotopy Groups
  - Spheres
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
What is $\pi_n(S^3 \times S^4 \times S^5)$ for $n \leq 3$?
:::

::: {.solution}
**Goal.** Compute $\pi_n(S^3 \times S^4 \times S^5)$ for $n \le 3$.

::: pf

::: pf-step
$\pi_n(X \times Y) \cong \pi_n(X) \times \pi_n(Y)$.

::: pf-proof
a map $S^n \to X \times Y$ is a pair of maps $S^n \to X$ and $S^n \to Y$, and homotopies correspond componentwise.
:::

:::

::: {.pf-step #pi-n-below-dim-vanishes}
$\pi_n(S^k) = 0$ for $n < k$.

::: pf-proof
any map $S^n \to S^k$ with $n < k$ is null-homotopic (cellular approximation: it factors through the $n$-skeleton of $S^k$, which is a point).
:::

:::

::: {.pf-step #pi-n-equals-n-is-z}
$\pi_n(S^n) = \ZZ$.

::: pf-proof
the Hurewicz theorem identifies $\pi_n(S^n)$ with $H_n(S^n) = \ZZ$.
:::

:::

::: pf-step
Compute each factor for $n \le 3$.

::: pf-proof

::: pf-step
$\pi_n(S^3)$: $\pi_1 = \pi_2 = 0$, $\pi_3 = \ZZ$.

::: pf-proof
by step [](#pi-n-below-dim-vanishes){.pf-ref} and step [](#pi-n-equals-n-is-z){.pf-ref}.
:::

:::

::: pf-step
$\pi_n(S^4)$: $\pi_1 = \pi_2 = \pi_3 = 0$.

::: pf-proof
by step [](#pi-n-below-dim-vanishes){.pf-ref}, since $n < 4$ for $n \le 3$.
:::

:::

::: pf-step
$\pi_n(S^5)$: $\pi_1 = \pi_2 = \pi_3 = 0$.

::: pf-proof
by step [](#pi-n-below-dim-vanishes){.pf-ref}, since $n < 5$ for $n \le 3$.
:::

:::

:::

:::

::: pf-step
Combine.

::: pf-proof

::: pf-step
$\pi_1(S^3 \times S^4 \times S^5) = 0$.

::: pf-proof
$0 \times 0 \times 0$.
:::

:::

::: pf-step
$\pi_2(S^3 \times S^4 \times S^5) = 0$.

::: pf-proof
$0 \times 0 \times 0$.
:::

:::

::: pf-step
$\pi_3(S^3 \times S^4 \times S^5) = \ZZ$.

::: pf-proof
$\ZZ \times 0 \times 0$.
:::

:::

:::

:::

::: pf-qed
$\pi_n = 0$ for $n = 1, 2$, and $\pi_3 = \ZZ$.
:::

:::

:::
