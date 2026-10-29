---
schema: qual/card@1
id: P-PSTM-01
kind: problem
title: Continuity descended through a closed quotient map
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $f \colon X \to Y$ be a continuous surjection, and suppose f is a closed map.
Let $g \colon Y \to Z$ be a function so that $g \circ f \colon X \to Z$ is continuous.
Show that g is continuous.
:::

::: {.solution}
Let $F \subseteq Z$ be closed.
It is enough to show that $g^{-1}(F)$ is closed in $Y$.

::: pf

::: {.pf-step #preimage}
$f^{-1}(g^{-1}(F))$ is closed in $X$.

::: pf-proof
It equals $(g \circ f)^{-1}(F)$, which is closed because $g \circ f$ is continuous.
:::

:::

::: pf-step
$g^{-1}(F)$ is closed in $Y$, so $g$ is continuous.

::: pf-proof
Since $f$ is surjective, $f(f^{-1}(A)) = A$ for every $A \subseteq Y$, so $g^{-1}(F) = f\bigl(f^{-1}(g^{-1}(F))\bigr)$.
This is the image of the closed set of step [](#preimage){.pf-ref} under the closed map $f$, so it is closed.
:::

:::

:::
:::
