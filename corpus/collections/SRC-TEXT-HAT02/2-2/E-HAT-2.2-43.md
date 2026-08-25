---
schema: qual/card@1
id: E-HAT-2.2-43
kind: exercise
title: Splitting of chain complexes and universal coefficient formula for $H_n(X; G)$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Universal Coefficients
  - Chain Complexes
relations: []
review: draft
---

(a) Show that a chain complex of free abelian groups $C_n$ splits as a direct sum of subcomplexes $0 \to L_{n+1} \to K_n \to 0$ with at most two nonzero terms.
[Show the short exact sequence $0 \to \ker\partial \to C_n \to \operatorname{Im}\partial \to 0$ splits and take $K_n = \ker\partial$.]

(b) In case the groups $C_n$ are finitely generated, show there is a further splitting into summands $0 \to \mathbb{Z} \to 0$ and $0 \to \mathbb{Z} \xrightarrow{m} \mathbb{Z} \to 0$.
[Reduce the matrix of the boundary map $L_{n+1} \to K_n$ to echelon form by elementary row and column operations.]

(c) Deduce that if $X$ is a CW complex with finitely many cells in each dimension, then $H_n(X; G)$ is the direct sum of the following groups:

- a copy of $G$ for each $\mathbb{Z}$ summand of $H_n(X)$

- a copy of $G/mG$ for each $\mathbb{Z}_m$ summand of $H_n(X)$

- a copy of the kernel of $G \xrightarrow{m} G$ for each $\mathbb{Z}_m$ summand of $H_{n-1}(X)$
