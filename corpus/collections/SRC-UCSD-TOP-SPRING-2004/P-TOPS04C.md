---
schema: qual/card@1
id: P-TOPS04C
kind: problem
title: "Hopf fibrations do not admit a section"
classification:
  areas:
  - topology
  topics:
  - Fiber Bundles
  - Hopf Fibration
relations: []
review: draft
---

::: {.problem}
Let $\mathbb{K} = \mathbb{R}$, $\mathbb{C}$, or $\mathbb{H}$.
Show that for $n \geq 1$ the Hopf fibrations
$$
p : \mathbb{K}^{n+1} \setminus \{0\} \to \mathbb{K}P^n
$$
do not admit a section $s$ (i.e. there is no continuous $s$ satisfying $p \circ s = \operatorname{id}$).
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

A section would make $p_*:H_*(\mathbb K^{n+1}-\{0\})\to H_*(\mathbb KP^n)$ split surjective.

::: pf-proof

If $p\circ s=\operatorname{id}$, then $p_*\circ s_*=\operatorname{id}$ on homology.

:::

:::

::: {.pf-step #s2}

For $\mathbb K=\mathbb C$, no section exists.

::: pf-proof

The total space deformation-retracts onto $S^{2n+1}$, whose $H_2$ vanishes for $n\ge1$. But $H_2(\mathbb CP^n;\mathbb Z)\cong\mathbb Z$. This contradicts the split surjectivity from step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s3}

For $\mathbb K=\mathbb H$, no section exists.

::: pf-proof

The total space deformation-retracts onto $S^{4n+3}$, whose $H_4$ vanishes, whereas $H_4(\mathbb HP^n;\mathbb Z)\cong\mathbb Z$ for $n\ge1$.

:::

:::

::: {.pf-step #s4}

For $\mathbb K=\mathbb R$ and $n\ge2$, no section exists.

::: pf-proof

The total space deformation-retracts onto $S^n$, so $H_1(-;\mathbb F_2)=0$. But $H_1(\mathbb RP^n;\mathbb F_2)\cong\mathbb F_2$, contradicting step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s5}

For $\mathbb K=\mathbb R$ and $n=1$, no section exists either.

::: pf-proof

After radial deformation retraction the map is the double covering $S^1\to\mathbb RP^1\cong S^1$, whose induced map on $H_1(-;\mathbb Z)$ is multiplication by $2$. Such a map cannot have a right inverse as a homomorphism $\mathbb Z\to\mathbb Z$.

:::

:::

::: pf-step

Thus none of the stated Hopf fibrations admits a section.

::: pf-proof

Combine steps [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref}.

:::

:::

:::

:::
