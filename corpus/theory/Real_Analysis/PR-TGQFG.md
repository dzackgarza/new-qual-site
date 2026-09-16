---
schema: qual/card@1
id: PR-TGQFG
kind: proposition
title: Volume of a rectangle is additive over almost disjoint decompositions and subadditive over covers
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Euclidean Spaces
relations: []
review: draft
---

::: {.proposition}
A closed rectangle in $\RR^n$ is a product $R=\prod_{i=1}^n[a_i,b_i]$ with $a_i\leq b_i$, with volume $\abs{R}\coloneqq\prod_{i=1}^n(b_i-a_i)$.
Let $R$ and $R_1,R_2,\ldots$ be closed rectangles in $\RR^n$, finitely or countably many.

(a) If $R=\bigcup_j R_j$ and the $R_j$ are pairwise [[FD-5T3HX|almost disjoint]], then $\abs{R}=\sum_j\abs{R_j}$.

(b) If $R\subseteq\bigcup_j R_j$, then $\abs{R}\leq\sum_j\abs{R_j}$.
:::
