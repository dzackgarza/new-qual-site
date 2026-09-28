---
schema: qual/card@1
id: P-TOPF25H
kind: problem
title: No closed 3-manifold homotopy equivalent to $\Sigma\mathbb{RP}^2$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Higher Homotopy Groups
relations: []
review: draft
---

::: {.problem}
Prove that there is no closed 3-manifold which is homotopy-equivalent to the suspension $\Sigma\mathbb{RP}^2$.
:::

::: {.solution}
<1>1. Suspension shifts reduced integral homology, so
$$\widetilde H_i(\Sigma\mathbb{RP}^2;\mathbb Z)\cong\widetilde H_{i-1}(\mathbb{RP}^2;\mathbb Z).$$
Thus
$$H_2(\Sigma\mathbb{RP}^2;\mathbb Z)\cong\mathbb Z/2,$$
and all other positive-degree integral homology groups vanish.
::: {.proof}
The only nonzero reduced integral homology group of $\mathbb{RP}^2$ is $H_1\cong\mathbb Z/2$.
:::

<1>2. If a closed connected $3$-manifold $M$ were homotopy equivalent to $\Sigma\mathbb{RP}^2$, then $H_3(M;\mathbb Z)=0$, so $M$ would be nonorientable.
::: {.proof}
A closed connected orientable $3$-manifold has $H_3\cong\mathbb Z$; a nonorientable one has zero integral top homology.
:::

<1>3. But every closed connected nonorientable $3$-manifold has nonzero $H_1(M;\mathbb Z)$.
::: {.proof}
The orientation character $w_1:\pi_1(M)\to\mathbb Z/2$ is nontrivial. Since its target is abelian, it factors through the abelianization $H_1(M;\mathbb Z)$, which therefore cannot vanish.
:::

<1>4. This contradicts $H_1(\Sigma\mathbb{RP}^2;\mathbb Z)=0$. Hence no such closed $3$-manifold exists.
::: {.proof}
Homotopy equivalence preserves integral homology, so <1>1 and <1>3 are incompatible.
:::
:::
