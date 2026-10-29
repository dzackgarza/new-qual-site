---
schema: qual/card@1
id: P-AGXGATHVICLOSURE
kind: problem
title: $V(I(X))$ is the Zariski closure of an arbitrary subset of $\AA^n$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Zariski Topology
  - Closure
  - Nullstellensatz
relations: []
review: draft
---

::: {.problem}
Let $X\subset \AA^n$ be an arbitrary subset and show that
$$
V(I(X)) = \bar{X}
.$$
:::

::: {.solution}
::: pf

::: {.pf-step #closure-in}
$\bar{X} \subseteq V(I(X))$.

::: pf-proof
Every $f \in I(X)$ vanishes on $X$, so $X \subseteq V(I(X))$.
The set $V(I(X))$ is Zariski closed by definition.
The closure $\bar{X}$ is the intersection of all closed sets that contain $X$, so $\bar{X} \subseteq V(I(X))$.
:::

:::

::: pf-step
$V(I(X)) \subseteq \bar{X}$, and hence $V(I(X)) = \bar{X}$.

::: pf-proof
The closed set $\bar{X}$ is $V(J)$ for some ideal $J$.
Every $f \in J$ vanishes on $\bar{X}$ and so on $X$, so $J \subseteq I(X)$.
Since $V$ reverses inclusions, $V(I(X)) \subseteq V(J) = \bar{X}$.
Together with step [](#closure-in){.pf-ref}, this gives equality.
:::

:::

:::
:::
