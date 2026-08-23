---
schema: qual/card@1
id: P-TOPF23H
kind: problem
title: "Transfer map for free group actions: rational homology of the quotient is the invariant part"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Group Actions
  - Covering Spaces
  - Transfer Map
relations: []
review: draft
solved: false
---

::: problem
Let $G$ be a finite group of order $d$ acting freely on a space $X$, so that we have a covering map $\pi : X \to Y = X/G$.
By lifting singular simplexes, construct a chain map $\tau_* : C_*(Y; \mathbb{Z}) \to C_*(X; \mathbb{Z})$ such that the composite $C_*(Y; \mathbb{Z}) \xrightarrow{\tau_*} C_*(X; \mathbb{Z}) \xrightarrow{\pi_*} C_*(Y; \mathbb{Z})$ is multiplication by $d$.
Use this to show that we can identify the rational homology of $Y$ with the $G$-invariant subspace of the rational homology of $X$:
$$
H_*(Y; \mathbb{Q}) \cong H_*(X; \mathbb{Q})^G.
$$
:::
