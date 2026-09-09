---
schema: qual/card@1
id: P-AMD-HYX4PDY2
kind: problem
title: Conjugation automorphism of $\pi_1(T^2)$ induced by a loop
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Surfaces
relations: []
review: draft
---

::: {.problem}
Let $X = S^1\times S^1$ and $\gamma$ a loop based at $x_0$.
What is the induced map $\gamma_\sharp$?
:::

::: {.solution}
<1>1. The basepoint-change automorphism associated to the loop $\gamma$ is conjugation by $[\gamma]$:
$$
\gamma_\sharp([\alpha])=[\gamma]^{-1}[\alpha][\gamma]
$$
(up to the opposite conjugation convention for basepoint change).
::: {.proof}
Changing the basepoint along a path $\gamma$ sends a loop $\alpha$ to the concatenation $\gamma^{-1}*\alpha*\gamma$ under this convention. For a loop beginning and ending at the same basepoint, this is an automorphism of the same fundamental group.
:::

<1>2. Since
$$
\pi_1(T^2,x_0)\cong\mathbb Z^2
$$
is abelian, this conjugation is trivial.
::: {.proof}
For any $g,h$ in an abelian group, $g^{-1}hg=h$.
:::

<1>3. Therefore
$$
\boxed{\gamma_\sharp=\operatorname{id}_{\mathbb Z^2}.}
$$
::: {.proof}
Apply <1>2 to every element of $\pi_1(T^2,x_0)$.
:::
:::
