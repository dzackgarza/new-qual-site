---
schema: qual/card@1
id: D-MEPE3
kind: definition
title: Cells of a CW complex
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
relations: []
review: draft
---

::: {.definition}
Let $X$ be a [[D-ZOU5G|CW complex]] whose $n$-skeleton $X^n$ is obtained from $X^{n-1}$ by attaching $n$-disks $D^n_\alpha$ along attaching maps $\varphi_\alpha\colon S^{n-1}\to X^{n-1}$.
The \dfn{characteristic map} of $D^n_\alpha$ is the composite $\Phi_\alpha\colon D^n_\alpha\hookrightarrow X^{n-1}\sqcup\coprod_\beta D^n_\beta\to X^n\hookrightarrow X$, whose restriction to $S^{n-1}$ is $\varphi_\alpha$.
The \dfn{$n$-cell} $e^n_\alpha$ is the image $\Phi_\alpha(D^n\sm S^{n-1})$.
:::

::: {.proposition}
Each $n$-cell $e^n_\alpha$ is homeomorphic to the open disk $D^n\sm S^{n-1}\cong\RR^n$, and the underlying set of $X$ is the disjoint union of the cells $e^n_\alpha$ over all $n$ and $\alpha$.
:::

::: {.concept}
See [@Hat02, pp. 5 and 7].
:::
