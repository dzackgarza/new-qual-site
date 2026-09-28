---
schema: qual/card@1
id: P-TOPF10F
kind: problem
title: 'Rank of $H_2$ of the universal cover of a $4$-manifold with finite $\pi_1$'
classification:
  areas:
  - topology
  topics:
  - Homology
  - Universal Cover
  - Manifolds
  - Fundamental Group
relations: []
review: draft
---

::: {.problem}
An orientable closed compact $4$-manifold $W^4$ has a finite fundamental group with $d$ elements, and the rank of its second homology group is $r$.
What is the rank of the second homology group of its universal cover?
:::

::: {.solution}
<1>1. Since $\pi_1(W)$ is finite, $b_1(W)=0$; by Poincaré duality $b_3(W)=0$.
::: {.proof}
The rank of $H_1$ is the rank of the abelianization of $\pi_1$, hence zero for a finite group. For a closed oriented $4$-manifold, $b_3=b_1$.
:::

<1>2. Thus
$$
\chi(W)=2+r.
$$
::: {.proof}
We have $b_0=b_4=1$, $b_1=b_3=0$, and $b_2=r$.
:::

<1>3. The universal cover $\widetilde W\to W$ has degree $d$, so
$$
\chi(\widetilde W)=d(r+2).
$$
::: {.proof}
Euler characteristic multiplies by the number of sheets of a finite covering.
:::

<1>4. The universal cover is simply connected and closed oriented, so
$$
\chi(\widetilde W)=2+b_2(\widetilde W).
$$
::: {.proof}
For $\widetilde W$, the first and third Betti numbers vanish and $b_0=b_4=1$.
:::

<1>5. Therefore
$$
\boxed{\operatorname{rank}H_2(\widetilde W;\mathbb Z)=d(r+2)-2.}
$$
::: {.proof}
Equate the expressions in <1>3 and <1>4.
:::
:::
