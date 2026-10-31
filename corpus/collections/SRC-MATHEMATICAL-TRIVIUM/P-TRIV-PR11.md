---
schema: qual/card@1
id: P-TRIV-PR11
kind: problem
title: Exponential waiting time between collisions
classification:
  areas: [prelim]
  topics:
  - Exponential Distribution
  - Poisson Process
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 11, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider the particle moving in a gas of other particles.
Given that the last collision of the particle occurred at $t = 0$ , the probability that the next collision will occur between t and $t + \Delta t$ equals $\lambda \Delta t + o ( \Delta t )$ , when $\Delta t \to 0$ . Find the probability $P ( t )$ that the time between the nearest collisions will exceed t.
:::

::: {.solution}

Interpret the stated infinitesimal law as a constant conditional collision rate: given no collision before time $t$, the probability of a collision during $(t,t+\Delta t]$ is $\lambda\Delta t+o(\Delta t)$.

::: pf

::: {.pf-step #s1-1}

The survival probability satisfies
$$
P(t+\Delta t)
=P(t)\bigl(1-\lambda\Delta t+o(\Delta t)\bigr).
$$


::: pf-proof

For the waiting time to exceed $t+\Delta t$, it must first exceed $t$ and then no collision may occur in the following interval. Conditional on survival to $t$, the latter probability is $1-\lambda\Delta t+o(\Delta t)$.

:::

:::

::: {.pf-step #s1-2}

Hence
$$
P'(t)=-\lambda P(t).
$$


::: pf-proof

Subtract $P(t)$ from step [](#s1-1){.pf-ref}, divide by $\Delta t$, and let $\Delta t\to0$:
$$
\frac{P(t+\Delta t)-P(t)}{\Delta t}
=-\lambda P(t)+P(t)o(1).
$$

:::

:::

::: {.pf-step #s1-3}

The initial condition is
$$
P(0)=1.
$$


::: pf-proof

Immediately after the collision at time $0$, the waiting time to the next collision is nonnegative and exceeds $0$ with probability $1$ under the continuous waiting-time model.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{P(t)=e^{-\lambda t}},
\qquad t\geq0.
$$


::: pf-proof

The unique solution of the differential equation in step [](#s1-2){.pf-ref} with the initial condition in step [](#s1-3){.pf-ref} is $P(t)=e^{-\lambda t}$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the probability that the intercollision time exceeds $t$.

:::

:::

:::
