---
schema: qual/card@1
id: D-JDDCP
kind: definition
title: Free product of groups
classification:
  areas:
  - topology
  topics:
  - Groups
  - van Kampen
relations: []
review: draft
---

::: {.definition}
Let $(G_\alpha)_{\alpha\in A}$ be a family of groups.
A \dfn{reduced word} is a finite sequence $g_1g_2\cdots g_k$, $k\geq 0$, in which each letter $g_i$ lies in $G_{\alpha_i}\sm\ts{1}$ for some $\alpha_i\in A$ and $\alpha_i\neq\alpha_{i+1}$ for $1\leq i<k$.
The \dfn{free product} $\ast_{\alpha\in A} G_\alpha$ is the set of reduced words, with product given by concatenating two words and then reducing: adjacent letters from the same $G_\alpha$ are replaced by their product in $G_\alpha$, and letters equal to $1$ are deleted, until the word is reduced.
:::

::: {.proposition}
The free product $\ast_\alpha G_\alpha$ is a group whose identity is the empty word, and each $G_\beta$ is a subgroup via one-letter words.
For every group $H$ and homomorphisms $\varphi_\alpha\colon G_\alpha\to H$ there is a unique homomorphism $\varphi\colon\ast_\alpha G_\alpha\to H$ restricting to $\varphi_\alpha$ on each $G_\alpha$, so $\ast_\alpha G_\alpha$ is the [[D-COC6C|coproduct]] of the $G_\alpha$ in $\Grp$.
:::

::: {.example}
For a set $S$, the free group on $S$ is isomorphic to $\ast_{s\in S}\ZZ$.
:::

::: {.concept}
See [@Hat02, §1.2, p. 41].
:::
