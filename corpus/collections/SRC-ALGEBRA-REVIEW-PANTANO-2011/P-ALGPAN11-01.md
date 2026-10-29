---
schema: qual/card@1
id: P-ALGPAN11-01
kind: problem
title: Inverse of a product in a group with torsion relations
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Reversed and inverted the product and reduced exponents modulo the given element orders.
---

::: {.problem}
If $b$ and $c$ are elements in a group $G$, and if $b^5=c^3=e$, where $e$ is the unit element of $G$, then the inverse of $b^2cb^4c^2$ must be

(A) $b^3c^2bc$
(B) $b^4c^2b^2c$
(C) $c^2b^4cb^2$
(D) $cb^2c^2b^4$
(E) $cbc^2b^3$
:::

::: {.solution}

::: pf

::: {.pf-step #reverse}
$(b^2cb^4c^2)^{-1}=c^{-2}b^{-4}c^{-1}b^{-2}$.

::: pf-proof
In a group, $(x_1x_2\cdots x_r)^{-1}=x_r^{-1}\cdots x_2^{-1}x_1^{-1}$, because the product of the two sides telescopes to $e$.
:::

:::

::: {.pf-step #reduce}
$c^{-2}=c$, $b^{-4}=b$, $c^{-1}=c^2$, and $b^{-2}=b^3$.

::: pf-proof
From $c^3=e$ we get $c^{-2}=c^{3-2}=c$ and $c^{-1}=c^{3-1}=c^2$.
From $b^5=e$ we get $b^{-4}=b^{5-4}=b$ and $b^{-2}=b^{5-2}=b^3$.
:::

:::

::: pf-step
$(b^2cb^4c^2)^{-1}=\boxed{cbc^2b^3}$, choice (E).

::: pf-proof
Substitute step [](#reduce){.pf-ref} into step [](#reverse){.pf-ref}.
:::

:::

:::

:::
