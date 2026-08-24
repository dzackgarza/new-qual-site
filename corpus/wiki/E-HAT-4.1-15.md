---
schema: qual/card@1
id: E-HAT-4.1-15
kind: exercise
title: "Every self-map of $S^n$ is a multiple of the identity"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
---

Show that every map $f: S^n \to S^n$ is homotopic to a multiple of the identity map by the following steps.

(a) Use Lemma 4.10 (or simplicial approximation, Theorem 2C.1) to reduce to the case that there exists a point $q \in S^n$ with $f^{-1}(q) = \{p_1, \ldots, p_k\}$ and $f$ is an invertible linear map near each $p_i$.

(b) For $f$ as in (a), consider the composition $gf$ where $g: S^n \to S^n$ collapses the complement of a small ball about $q$ to the basepoint.
Use this to reduce (a) further to the case $k = 1$.

(c) Finish the argument by showing that an invertible $n \times n$ matrix can be joined by a path of such matrices to either the identity matrix or the matrix of a reflection.
