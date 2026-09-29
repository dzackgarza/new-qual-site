---
schema: qual/card@1
id: P-UCTOP-SU14-6
kind: problem
title: QP^2 ∨ S^3 and RP^3 are not homotopy-equivalent
classification:
  areas:
  - topology
  topics:
  - Homotopy
relations: []
review: draft
---

::: {.problem}
Prove that $\mathbb{QP}^2 \vee S^3$ and $\mathbb{RP}^3$ are not homotopy-equivalent.
:::

::: {.solution}

::: pf

::: pf-step
The space $\mathbb{QP}^2$ has one cell in dimensions $0,4,8$, so
$$
H_4(\mathbb{QP}^2;\mathbb Z)\cong\mathbb Z,
\qquad H_8(\mathbb{QP}^2;\mathbb Z)\cong\mathbb Z.
$$

::: pf-proof
Quaternionic projective $n$-space has the standard CW decomposition with one cell in each dimension $0,4,8,\dots,4n$.
:::

:::

::: {.pf-step #h4-wedge}
Therefore
$$
H_4(\mathbb{QP}^2\vee S^3;\mathbb Z)\cong\mathbb Z.
$$

::: pf-proof
Reduced homology of a wedge is the direct sum of the reduced homologies of its summands, and $S^3$ contributes nothing in degree $4$.
:::

:::

::: {.pf-step #h4-rp3-zero}
But
$$
H_4(\mathbb{RP}^3;\mathbb Z)=0.
$$

::: pf-proof
The space $\mathbb{RP}^3$ is a $3$-dimensional CW complex.
:::

:::

::: pf-step
Hence $\mathbb{QP}^2\vee S^3$ and $\mathbb{RP}^3$ are not homotopy-equivalent.

::: pf-proof
Homotopy-equivalent spaces have isomorphic integral homology groups in every degree, contradicting steps [](#h4-wedge){.pf-ref} and [](#h4-rp3-zero){.pf-ref}.
:::

:::

:::

:::
