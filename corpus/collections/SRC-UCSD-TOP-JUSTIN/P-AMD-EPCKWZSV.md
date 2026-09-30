---
schema: qual/card@1
id: P-AMD-EPCKWZSV
kind: problem
title: $S^1 \times I \simeq$ the Möbius strip
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Retracts
  - Surfaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Show that $S^1 \times I \simeq M$, the Mobius strip.
:::

::: {.solution}
**Goal:** Prove that the cylinder $S^1 \times [0, 1]$ is homotopy equivalent to the Möbius strip $M = ([0, 1] \times [0, 1]) / ((0, y) \sim (1, 1-y))$.

::: pf

::: {.pf-step #s1}
Show that the cylinder $S^1 \times [0, 1]$ deformation retracts to the circle $S^1$.

::: pf-proof

::: pf-step
Realize $S^1 \times [0, 1]$ with inclusion $\iota_1 \colon S^1 \hookrightarrow S^1 \times [0, 1]$ given by $z \mapsto (z, 1/2)$, and retraction $r_1 \colon S^1 \times [0, 1] \to S^1$ given by $(z, t) \mapsto z$.
:::

::: pf-step
Define the straight-line homotopy $H_1 \colon (S^1 \times [0, 1]) \times [0, 1] \to S^1 \times [0, 1]$ by $H_1((z, t), s) = (z, (1-s)t + s(1/2))$.
:::

::: {.pf-step #s1-3}
$H_1$ is continuous, $H_1((z, t), 0) = (z, t) = \operatorname{id}_{S^1 \times I}$, $H_1((z, t), 1) = (z, 1/2) = \iota_1(r_1(z, t))$, and $H_1((z, 1/2), s) = (z, 1/2)$ for all $s \in [0, 1]$.
:::

::: pf-step
Thus $H_1$ is a strong deformation retraction of $S^1 \times [0, 1]$ onto the circle $S^1 \times \{1/2\} \cong S^1$.

::: pf-proof
The three identities in step [](#s1-3){.pf-ref} are exactly the defining conditions of a strong deformation retraction, so $H_1$ is a strong deformation retraction of $S^1 \times [0, 1]$ onto $S^1 \times \{1/2\} \cong S^1$.
:::

:::

::: pf-step
Consequently, $S^1 \times [0, 1] \simeq S^1$.
:::

:::

:::

::: {.pf-step #s2}
Show that the Möbius strip $M$ deformation retracts to the circle $S^1$.

::: pf-proof

::: pf-step
Let $M = ([0, 1] \times [0, 1]) / ((0, y) \sim (1, 1-y))$, and let $C = \{[(x, 1/2)] \mid x \in [0, 1]\} \subset M$ be the core circle.
:::

::: pf-step
The map $\gamma \colon [0, 1] / (0 \sim 1) \to C$ given by $x \mapsto [(x, 1/2)]$ is a homeomorphism, so $C \cong S^1$.
:::

::: pf-step
Define $H_2 \colon M \times [0, 1] \to M$ by $H_2([(x, y)], s) = [(x, (1-s)y + s(1/2))]$.
:::

::: {.pf-step #s2-4}
$H_2$ respects the quotient identification because at $x = 1$, $H_2([(1, 1-y)], s) = [(1, (1-s)(1-y) + s/2)] = [(0, 1 - ((1-s)(1-y) + s/2))] = [(0, (1-s)y + s/2)] = H_2([(0, y)], s)$.
:::

::: pf-step
$H_2$ is a strong deformation retraction of $M$ onto the core circle $C \cong S^1$.

::: pf-proof
The map $H_2$ is well-defined by step [](#s2-4){.pf-ref} and satisfies the defining conditions of a strong deformation retraction, so it is a strong deformation retraction of $M$ onto the core circle $C \cong S^1$.
:::

:::

::: pf-step
Consequently, $M \simeq S^1$.
:::

:::

:::

::: {.pf-step #s3}
Combine homotopy equivalences.

::: pf-proof

::: pf-step
Homotopy equivalence ($\simeq$) is an equivalence relation on topological spaces.
:::

::: pf-step
By step [](#s1){.pf-ref}, $S^1 \times [0, 1] \simeq S^1$.
:::

::: pf-step
By step [](#s2){.pf-ref}, $M \simeq S^1$.
:::

::: pf-step
By transitivity and symmetry, $S^1 \times [0, 1] \simeq M$.
:::

::: pf-qed
Since $\simeq$ is an equivalence relation, $S^1 \times [0, 1] \simeq S^1$ and $M \simeq S^1$ together imply $S^1 \times [0, 1] \simeq M$.
:::

:::

:::

::: pf-qed
Step [](#s3){.pf-ref} establishes $S^1 \times [0, 1] \simeq M$.
:::

:::
:::
