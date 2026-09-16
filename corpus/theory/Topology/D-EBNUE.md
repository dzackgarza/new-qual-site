---
schema: qual/card@1
id: D-EBNUE
kind: definition
title: Fundamental group
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homotopy
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space and $x_0\in X$, and let $I = [0,1]$.
The \dfn{fundamental group} $\pi_1(X, x_0)$ is the set of classes of [[D-J6XOC|loops]] $\gamma\colon I\to X$ based at $x_0$ under [[D-Z7I7F|homotopy rel endpoints]], with multiplication
$$
[\gamma][\eta]\coloneqq[\gamma\cdot\eta],
$$
where $\gamma\cdot\eta$ is the [[D-J6XOC|concatenation]] of $\gamma$ and $\eta$.
:::

::: {.proposition}
The multiplication on $\pi_1(X, x_0)$ is well defined and makes $\pi_1(X, x_0)$ a group.
Its identity is the class of the constant loop at $x_0$, and $[\gamma]\inv = [\bar\gamma]$, where $\bar\gamma(s)\coloneqq\gamma(1-s)$.
:::

::: {.proposition}
Let $h\colon I\to X$ be a path from $x_0$ to $x_1$, with reverse $\bar h$.
Then $\beta_h\colon\pi_1(X, x_1)\to\pi_1(X, x_0)$, $\beta_h[\gamma]\coloneqq[h\cdot\gamma\cdot\bar h]$, is a group isomorphism.
It depends only on the homotopy class of $h$ rel endpoints, and for a second path $h'$ from $x_0$ to $x_1$, $\beta_{h'} = c\circ\beta_h$, where $c$ is conjugation by $[h'\cdot\bar h]\in\pi_1(X, x_0)$.
In particular, if $X$ is [[D-X73EB|path connected]], the groups $\pi_1(X, x)$ for $x\in X$ are all isomorphic.
:::

::: {.concept}
See [@Hat02, §1.1, pp. 26--28, Propositions 1.3 and 1.5].
:::
