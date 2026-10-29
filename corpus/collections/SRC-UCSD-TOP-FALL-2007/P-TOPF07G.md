---
schema: qual/card@1
id: P-TOPF07G
kind: problem
title: "Second homology of a closed 1-connected 4-manifold is free abelian"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Manifolds
relations: []
review: draft
---

::: {.problem}
Let $W$ be a closed (i.e. compact, without boundary) $4$-manifold which is $1$-connected (i.e. is path-connected and simply-connected).
Show that its second homology group is a free abelian group (in other words, has no finite cyclic summands).
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Since $W$ is simply connected,
$$
H_1(W;\ZZ)=0.
$$

::: pf-proof

The first homology group is the abelianization of the fundamental group.

:::

:::

::: {.pf-step #s2}

The universal coefficient theorem gives
$$
H^2(W;\ZZ)\cong\operatorname{Hom}(H_2(W;\ZZ),\ZZ).
$$

::: pf-proof

The UCT exact sequence has left term $\operatorname{Ext}(H_1(W),\ZZ)=0$ by step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s3}

Poincaré duality gives
$$
H^2(W;\ZZ)\cong H_2(W;\ZZ).
$$

::: pf-proof

A simply connected closed manifold is orientable, so integral Poincaré duality applies in dimension $4$.

:::

:::

::: pf-step

The group $\operatorname{Hom}(H_2(W),\ZZ)$ is free abelian, hence so is $H_2(W)$.

::: pf-proof

The homology of a compact manifold is finitely generated. For a finitely generated abelian group $A\cong\ZZ^r\oplus T$, one has $\operatorname{Hom}(A,\ZZ)\cong\ZZ^r$. Combine with steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::

:::
