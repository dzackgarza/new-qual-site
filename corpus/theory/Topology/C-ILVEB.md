---
schema: qual/card@1
id: C-ILVEB
kind: corollary
title: Every subgroup of a free group is free
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
  - Groups
  - Cell Complexes
relations: []
review: draft
---

::: {.corollary title="Nielsen--Schreier"}
Let $F$ be a free group and let $H \leq F$ be a subgroup.
Then $H$ is free.
:::

::: {.proof}
Let $S$ be a basis of $F$ and let $X \coloneqq \bigvee_{s\in S} S^1$ be a wedge of circles, a connected graph with one vertex $x_0$ and one edge for each $s\in S$.
Then $\pi_1(X, x_0) \cong \ast_{s\in S}\ZZ \cong F$, a [[D-JDDCP|free product]] of copies of $\ZZ$.
Since $X$ is a connected CW complex, it is path-connected, locally path-connected and semilocally simply connected, so there is a connected [[D-ANO2D|covering space]] $p\colon \tilde X\to X$ and a point $\tilde x_0 \in p^{-1}(x_0)$ with $p_*\pi_1(\tilde X, \tilde x_0) = H$, identifying $H$ with a subgroup of $\pi_1(X, x_0)$.
The cells of $X$ lift to give $\tilde X$ the structure of a connected graph.
A maximal tree $T \subseteq \tilde X$ is contractible, and the quotient $\tilde X \to \tilde X/T$ is a homotopy equivalence onto a wedge of circles, one for each edge of $\tilde X$ not in $T$.
Hence $\pi_1(\tilde X, \tilde x_0)$ is free on those edges.
Since $p_*\colon \pi_1(\tilde X, \tilde x_0)\to \pi_1(X, x_0)$ is injective, $H \cong \pi_1(\tilde X, \tilde x_0)$ is free.
:::

::: {.concept}
[@Hat02, §1.A].
:::
