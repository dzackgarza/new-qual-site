---
schema: qual/card@1
id: P-AGXNSSNONCLOSED
kind: problem
title: Failure of $I(V(J)) = \sqrt J$ over a field that is not algebraically closed
classification:
  areas:
  - algebraic-geometry
  topics:
  - Nullstellensatz
  - Maximal Ideals
  - Counterexamples
relations: []
review: draft
---

::: {.problem}
Let $J \normal k[x_1, \cdots, x_n]$ be an ideal, and find a counterexample to $I(V(J)) =\sqrt{J}$ when $k$ is not algebraically closed.
:::

::: {.solution}
Take $k = \RR$, $n = 1$, and $J = \generators{x^2 + 1} \normal \RR[x]$.

::: pf

::: {.pf-step #ivj}
$I(V(J)) = \RR[x]$.

::: pf-proof
The polynomial $x^2 + 1$ has no real root, so $V(J) = \emptyset$.
Every polynomial vanishes at every point of $\emptyset$, so $I(\emptyset) = \RR[x]$.
:::

:::

::: {.pf-step #radical}
$\sqrt{J} = J \neq \RR[x]$.

::: pf-proof
Since $\RR[x]/J \cong \CC$ is a field, $J$ is maximal and so proper.
Then $J \subseteq \sqrt{J}$, and $\sqrt{J} \neq \RR[x]$, because $1 \in \sqrt{J}$ would give $1 = 1^n \in J$.
By maximality, $\sqrt{J} = J$.
:::

:::

::: pf-step
$I(V(J)) \neq \sqrt{J}$.

::: pf-proof
Compare steps [](#ivj){.pf-ref} and [](#radical){.pf-ref}.
:::

:::

:::
:::
