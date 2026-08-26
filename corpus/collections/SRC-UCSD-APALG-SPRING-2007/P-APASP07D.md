---
schema: qual/card@1
id: P-APASP07D
kind: problem
title: "Trace and computation of the averaged conjugate of a matrix over a finite group"
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
relations: []
review: draft
---

::: problem
Let $B$ be a given matrix and let $V' = \mathbb{C}^n$ be an irreducible $G$-module for a finite group $G$, with $g \in G$ acting via the matrix $A_g$.
Let $$C = \frac{1}{|G|} \sum_{g} A_g B A_g^{-1}.$$

(a) Calculate $\operatorname{Tr}(C)$, where $\operatorname{Tr}$ is the usual trace.

(b) Calculate $C$.
:::

::: remark
The exam prints an explicit $3\times 3$ matrix $B$; the data is not reproduced here, so the problem is stated for a general matrix $B$.
The requested computation is unchanged: $C$ is the Reynolds projection of $B$ onto the $G$-invariant subspace, so (a) asks for $\operatorname{Tr}(C) = \dim(V')^{G}$ and (b) for the projection of $B$ onto the invariants.
:::
