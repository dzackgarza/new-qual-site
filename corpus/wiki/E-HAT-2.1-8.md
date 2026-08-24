---
schema: qual/card@1
id: E-HAT-2.1-8
kind: exercise
title: Simplicial homology of lens space from cyclic tetrahedra
classification:
  areas:
  - topology
  topics:
  - Homology
  - Simplicial Homology
  - Lens Spaces
relations: []
review: draft
---

Construct a 3 dimensional $\Delta$-complex $X$ from $n$ tetrahedra $T_1, \cdots, T_n$ by the following two steps.
First arrange the tetrahedra in a cyclic pattern as in the figure, so that each $T_i$ shares a common vertical face with its two neighbors $T_{i-1}$ and $T_{i+1}$, subscripts being taken mod $n$.
Then identify the bottom face of $T_i$ with the top face of $T_{i+1}$ for each $i$.
Show the simplicial homology groups of $X$ in dimensions 0, 1, 2, 3 are $\mathbb{Z}$, $\mathbb{Z}$, $\mathbb{Z}_n$, $0$, $\mathbb{Z}$, respectively.
[The space $X$ is an example of a lens space; see Example 2.43 for the general case.]
