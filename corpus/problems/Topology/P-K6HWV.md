---
schema: qual/card@1
id: P-K6HWV
kind: problem
title: Homology of $(S^1\times S^1)\vee S^1$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
relations: []
review: draft
---

::: {.problem}
Compute the homology of the one-point union of $S^1 \times S^1$ and $S^1$.
:::

::: {.solution}
<1>1. Reduced homology of a wedge of connected CW complexes is the direct sum of the reduced homologies of the summands.
::: {.proof}
This follows from the cellular chain complex of the wedge, or from Mayer--Vietoris using neighborhoods whose intersection is contractible.
:::

<1>2. The torus has $H_0=H_2=\mathbb Z$ and $H_1=\mathbb Z^2$, while $S^1$ has $H_0=H_1=\mathbb Z$.
::: {.proof}
These are the standard homology computations.
:::

<1>3. Therefore
$$\boxed{H_k((S^1\times S^1)\vee S^1;\mathbb Z)\cong\begin{cases}\mathbb Z,&k=0,2,\\\mathbb Z^3,&k=1,\\0,&\text{otherwise.}\end{cases}}$$
::: {.proof}
Add the reduced homology groups in positive degrees and retain one copy of $\mathbb Z$ in degree zero because the wedge is connected.
:::
:::
