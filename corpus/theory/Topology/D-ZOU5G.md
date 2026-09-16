---
schema: qual/card@1
id: D-ZOU5G
kind: definition
title: CW complex
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
relations: []
review: draft
---

::: {.definition}
A \dfn{CW complex} is a topological space $X$ together with subspaces $X^0\subseteq X^1\subseteq\cdots$ constructed as follows.

1. $X^0$ is a discrete space; its points are the $0$-cells.

2. For $n\geq 1$, the \dfn{$n$-skeleton} $X^n$ is obtained from $X^{n-1}$ by [[D-MMDM3|attaching]] a family of $n$-cells $e^n_\alpha$ along continuous maps $\varphi_\alpha\colon S^{n-1}\to X^{n-1}$:
$$
X^n = \qty{X^{n-1} \disjoint \Disjoint_\alpha D^n_\alpha} / \qty{x \sim \varphi_\alpha(x) \text{ for } x \in \del D^n_\alpha},
$$
with the quotient topology.

3. Either $X = X^n$ for some $n$, or $X = \Union_{n\geq 0} X^n$ with the weak topology: a subset $A\subseteq X$ is closed if and only if $A \intersect X^n$ is closed in $X^n$ for every $n$.
:::

::: {.concept}
[@Hat02, p. 5].
:::
