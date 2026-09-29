---
schema: qual/card@1
id: E-HAT-1.2-17
kind: problem
title: $\pi_1(\mathbb{R}^2 - \mathbb{Q}^2)$ is uncountable
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - van Kampen
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Show that $\pi_1(\mathbb{R}^2 - \mathbb{Q}^2)$ is uncountable.
:::

::: {.solution}

::: pf

::: pf-step

$\mathbb{R}^2 - \mathbb{Q}^2$ is the plane with the countable dense set $\mathbb{Q}^2$ removed.

::: pf-proof

$\mathbb{Q}^2$ is countable.

:::

:::

::: pf-step

For each irrational $\alpha$, the vertical line $L_\alpha = \{(\alpha, y) : y \in \mathbb{R}\}$ is contained in $\mathbb{R}^2 - \mathbb{Q}^2$ (since $\alpha \notin \mathbb{Q}$).

::: pf-proof

a point $(\alpha, y)$ is in $\mathbb{Q}^2$ only if $\alpha \in \mathbb{Q}$.

:::

:::

::: pf-step

For each irrational $\alpha$, choose a basepoint $p_\alpha = (\alpha, 0)$ and a loop $\gamma_\alpha$ that goes around the point $(\alpha, 0)$ once (a small circle).

::: pf-proof

construct a loop.

:::

:::

::: {.pf-step #s4}

The loops $\gamma_\alpha$ for distinct irrationals $\alpha$ represent distinct elements of $\pi_1(\mathbb{R}^2 - \mathbb{Q}^2)$.

::: pf-proof

the winding number of $\gamma_\alpha$ around a point $(\beta, 0)$ is $1$ if $\beta = \alpha$ and $0$ otherwise; since winding number is a homotopy invariant, distinct $\alpha$ give non-homotopic loops.

:::

:::

::: {.pf-step #s5}

There are uncountably many irrationals $\alpha$.

::: pf-proof

$\mathbb{R} \setminus \mathbb{Q}$ is uncountable.

:::

:::

::: {.pf-step #s6}

Hence $\pi_1(\mathbb{R}^2 - \mathbb{Q}^2)$ contains uncountably many distinct elements, so it is uncountable.

::: pf-proof

Steps [](#s4){.pf-ref} and [](#s5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref}.

:::

:::

:::
