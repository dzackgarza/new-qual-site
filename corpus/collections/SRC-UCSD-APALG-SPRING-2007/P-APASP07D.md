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
The source prints an explicit $3\times 3$ matrix $B$, but its entries are illegible in the available scan, so the problem is stated here for a general given matrix $B$.
The method requested is unchanged: $C$ is the Reynolds projection of $B$ onto the $G$-invariant subspace, so (a) asks for $\operatorname{Tr}(C) = \dim(V')^{G}$ and (b) for the projection of $B$ onto the invariants.
:::
