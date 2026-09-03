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

Show that $\pi_1(\mathbb{R}^2 - \mathbb{Q}^2)$ is uncountable.

::: {.solution}
<1>1. $\mathbb{R}^2 - \mathbb{Q}^2$ is the plane with the countable dense set $\mathbb{Q}^2$ removed.
::: {.proof}
$\mathbb{Q}^2$ is countable.
:::

<1>2. For each irrational $\alpha$, the vertical line $L_\alpha = \{(\alpha, y) : y \in \mathbb{R}\}$ is contained in $\mathbb{R}^2 - \mathbb{Q}^2$ (since $\alpha \notin \mathbb{Q}$).
::: {.proof}
a point $(\alpha, y)$ is in $\mathbb{Q}^2$ only if $\alpha \in \mathbb{Q}$.
:::

<1>3. For each irrational $\alpha$, choose a basepoint $p_\alpha = (\alpha, 0)$ and a loop $\gamma_\alpha$ that goes around the point $(\alpha, 0)$ once (a small circle).
::: {.proof}
construct a loop.
:::

<1>4. The loops $\gamma_\alpha$ for distinct irrationals $\alpha$ represent distinct elements of $\pi_1(\mathbb{R}^2 - \mathbb{Q}^2)$.
::: {.proof}
the winding number of $\gamma_\alpha$ around a point $(\beta, 0)$ is $1$ if $\beta = \alpha$ and $0$ otherwise; since winding number is a homotopy invariant, distinct $\alpha$ give non-homotopic loops.
:::

<1>5. There are uncountably many irrationals $\alpha$.
::: {.proof}
$\mathbb{R} \setminus \mathbb{Q}$ is uncountable.
:::

<1>6. Hence $\pi_1(\mathbb{R}^2 - \mathbb{Q}^2)$ contains uncountably many distinct elements, so it is uncountable.
::: {.proof}
<1>4 and <1>5.
:::

<1>7. Q.E.D.
::: {.proof}
<1>6.
:::
:::
