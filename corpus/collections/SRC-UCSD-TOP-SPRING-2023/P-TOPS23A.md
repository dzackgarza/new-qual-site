---
schema: qual/card@1
id: P-TOPS23A
kind: problem
title: "The Hopf fibration S^3 to S^2 has no section"
classification:
  areas:
  - topology
  topics:
  - Fiber Bundles
  - Hopf Fibration
  - Homotopy
relations: []
review: draft
---

::: problem
Let $p : S^3 \to S^2$ be the Hopf mapping, defined by sending $(Z, W) \in S^3 \subseteq \mathbb{C}^2$ to $Z/W \in \mathbb{C} \cup \{\infty\}$.
Show that there does not exist a section, that is a map $s : S^2 \to S^3$ satisfying $p \circ s = \operatorname{id}_{S^2}$.
:::

::: {.solution}
<1>1. Suppose a section $s:S^2\to S^3$ existed with $p\circ s=\operatorname{id}_{S^2}$.
::: {.proof}
We derive a contradiction on second homology.
:::

<1>2. On $H_2(-;\mathbb Z)$ one would have
$$p_*\circ s_*=(p\circ s)_*=\operatorname{id}_{H_2(S^2)}.$$
::: {.proof}
Homology is functorial.
:::

<1>3. But $H_2(S^3;\mathbb Z)=0$, so $s_*=0$ and therefore $p_*s_*=0$.
::: {.proof}
The induced map $s_*$ lands in the zero group.
:::

<1>4. This contradicts <1>2 because $H_2(S^2;\mathbb Z)\cong\mathbb Z\ne0$. Hence
$$\boxed{\text{the Hopf fibration }S^3\to S^2\text{ has no section}.}$$
::: {.proof}
The identity on a nonzero group cannot be the zero map.
:::
:::
