---
schema: qual/card@1
id: P-AGH258SEMICONT
kind: problem
title: Semicontinuity of the fibre dimension of a coherent sheaf
classification:
  areas:
  - algebraic-geometry
  topics:
  - Coherent Sheaves
  - Semicontinuity
  - Nakayama's Lemma
relations: []
review: draft
---

::: problem
Let $X$ be a noetherian scheme and $\mcf$ a coherent sheaf on $X$.
Consider the function
\[
\varphi(x) = \dim_{k(x)} \mcf_x \tensor_{\OO_x} k(x),
\]
where $k(x) = \OO_x / \mfm_x$ is the residue field at $x$.
Use Nakayama's lemma to prove the following.

a. The function $\varphi$ is upper semi-continuous, i.e. for any $n \in \ZZ$ the set $\ts{x \in X \st \varphi(x) \geq n}$ is closed.

b. If $\mcf$ is locally free and $X$ is connected, then $\varphi$ is a constant function.

c. Conversely, if $X$ is reduced and $\varphi$ is constant, then $\mcf$ is locally free.
:::
