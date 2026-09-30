---
schema: qual/card@1
id: E-AMD-ON37VIEN
kind: problem
title: $\nilrad{R}=\rad(0)$
classification:
  areas:
  - algebra
  topics:
  - Nilpotence
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: Claude Opus 5
  date: 2026-08-30
---

::: {.exercise}
Show that the nilradical is given by $\nilrad{R} = \rad(0)$.
:::

::: {.solution}

::: pf

::: pf-step
Write $\rad{I} = \theset{ x \in R \st x^n \in I \text{ for some } n \geq 1 }$ for the radical of an ideal $I$, and $\nilrad{R} = \theset{ x \in R \st x^n = 0 \text{ for some } n \geq 1 }$ for the nilradical.
:::

::: {.pf-step #nilrad-subset-rad-zero}
$\nilrad{R} \subseteq \rad{(0)}$.

::: pf-proof
If $x^n = 0$ then $x^n \in (0)$, since $(0) = \theset 0$.
:::

:::

::: {.pf-step #rad-zero-subset-nilrad}
$\rad{(0)} \subseteq \nilrad{R}$.

::: pf-proof
If $x^n \in (0)$ then $x^n = 0$, since $(0)$ has $0$ as its only element.
:::

:::

::: pf-qed
Steps [](#nilrad-subset-rad-zero){.pf-ref} and [](#rad-zero-subset-nilrad){.pf-ref} give the two inclusions, so $\nilrad{R} = \rad{(0)}$.
:::

:::

:::
