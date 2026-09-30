---
schema: qual/card@1
id: P-73UFB
kind: problem
title: Unique fractional linear transformation sending a circle $C$ to $C'$ with $f(z_1)=z'_1$
  and $f(z_2)=z'_2$
classification:
  areas:
  - complex-analysis
  topics:
  - Fractional Linear Transformations
  - Conformal Maps
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $C$ and $C'$ be two circles and let $z_1 \in C$, $z_2 \notin C$, $z'_1 \in C'$, $z'_2 \notin C'$.
Show that there is a unique fractional linear transformation $f$ with $f(C) = C'$ and $f(z_1) = z'_1$, $f(z_2) = z'_2$.
:::

::: {.solution}
::: pf

::: {.pf-step #three-points-determine}
A fractional linear transformation is determined by its values at three distinct points.

::: pf-proof
a Möbius map $z \mapsto \frac{az+b}{cz+d}$ has three degrees of freedom (up to scaling), so prescribing three images determines it uniquely.
:::

:::

::: pf-step
The reflection of $z_2$ across the circle $C$ is a point $z_2^*$ (the inverse point of $z_2$ with respect to $C$), and similarly $z_2'^*$ for $z_2'$ across $C'$.

::: pf-proof
definition of the inverse point with respect to a circle.
:::

:::

::: {.pf-step #reflection-condition}
A Möbius map sends $C$ to $C'$ iff it sends the pair $\{z_2, z_2^*\}$ to the pair $\{z_2', z_2'^*\}$.

::: pf-proof
a Möbius map preserves the relation of being inverse points with respect to a circle (it preserves circles and angles, hence symmetric points).
:::

:::

::: pf-step
Hence $f$ is determined by the three conditions $f(z_1) = z_1'$, $f(z_2) = z_2'$, $f(z_2^*) = z_2'^*$.

::: pf-proof
Step [](#reflection-condition){.pf-ref} and the fact that $z_1 \in C$ maps to $z_1' \in C'$.
:::

:::

::: {.pf-step #unique-determination}
These three conditions determine $f$ uniquely.

::: pf-proof
Step [](#three-points-determine){.pf-ref} (three points determine a Möbius map).
:::

:::

::: pf-qed
Step [](#unique-determination){.pf-ref}.
:::

:::

:::
