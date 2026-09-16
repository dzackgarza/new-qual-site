---
schema: qual/card@1
id: D-TFVPD
kind: definition
title: Mapping cone
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Homotopy
  - Quotient Spaces
relations: []
review: draft
---

::: {.definition}
Let $f\colon X\to Y$ be a continuous map with [[D-RMQ7W|mapping cylinder]] $M_f=\qty{(X\times I)\disjoint Y}/\qty{(x,1)\sim f(x)}$.
The \dfn{mapping cone} of $f$ is
$$
C_f\coloneqq M_f/(X\times\ts{0})=\qty{CX\disjoint Y}/\qty{(x,1)\sim f(x)\text{ for }x\in X},
$$
where $CX=(X\times I)/(X\times\ts{0})$ is the [[D-II4M4|cone]] on $X$; that is, $C_f$ is $Y$ with $CX$ attached along $f$ [@Hat02].
:::

::: {.proposition}
If $(X,A)$ is a CW pair and $\iota\colon A\injects X$ is the inclusion, then the mapping cone $C_\iota=X\cup CA$ is [[D-HFR32|homotopy equivalent]] to $X/A$ [@Hat02].
:::
