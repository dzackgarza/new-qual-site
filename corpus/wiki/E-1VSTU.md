---
schema: qual/card@1
id: E-1VSTU
kind: exercise
title: Net convergence generalizes sequence convergence
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


Let $X$ be a topological space. A net in $X$ is a function $f$ from a directed set $J$ into $X$. If $\alpha \in J$, we usually denote $f(\alpha)$ by $x_\alpha$. We denote the net $f$ itself by the symbol $(x_\alpha)_{\alpha \in J}$, or merely by $(x_\alpha)$ if the index set is understood.

The net $(x_\alpha)$ is said to converge to the point $x$ of $X$ (written $x_\alpha \to x$) if for each neighborhood $U$ of $x$, there exists $\alpha \in J$ such that

$$
\alpha \preceq \beta \implies x_\beta \in U.
$$

Show that these definitions reduce to familiar ones when $J = \mathbb{Z}_+$.
:::
