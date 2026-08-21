---
schema: qual/card@1
id: E-NYYRX
kind: exercise
title: Accumulation points of nets
classification:
  areas:
  - topology
  topics:
  - Nets
relations: []
review: draft
solved: false
---

::: {.exercise title="Munkres §29 Supplementary"}


Let $(x_\alpha)_{\alpha \in J}$ be a net in $X$. We say that $x$ is an accumulation point of the net $(x_\alpha)$ if for each neighborhood $U$ of $x$, the set of those $\alpha$ for which $x_\alpha \in U$ is cofinal in $J$.

Lemma. The net $(x_\alpha)$ has the point $x$ as an accumulation point if and only if some subnet of $(x_\alpha)$ converges to $x$.

[Hint: To prove the implication $\Rightarrow$, let $K$ be the set of all pairs $(\alpha, U)$ where $\alpha \in J$ and $U$ is a neighborhood of $x$ containing $x_\alpha$. Define $(\alpha, U) \preceq (\beta, V)$ if $\alpha \preceq \beta$ and $V \subset U$. Show that $K$ is a directed set and use it to define the subnet.]
:::
