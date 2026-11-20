---
schema: qual/card@1
id: FF-6WY3L
kind: fact
title: Local homology of a manifold
slogan: 'At a point of an $n$-manifold the local homology is $\ZZ$ in degree $n$ and vanishes elsewhere.'
prompts:
- What are the local homology groups of an $n$-manifold at a point?
classification:
  areas:
  - topology
  topics:
  - Homology
  - Manifolds
relations: []
review: draft
---

::: {.fact}
Let $M$ be an $n$-manifold and $x\in M$.
Then
$$
H_k(M, M\sm\theset{x};\ZZ) \cong H_k(\RR^n,\RR^n\sm\theset{0};\ZZ) \cong \tilde H_{k-1}(S^{n-1};\ZZ),
$$
which is $\ZZ$ for $k=n$ and $0$ otherwise [@Hat02, §3.3].
A space with a point at which these local homology groups differ from those of $\RR^n$ is not a manifold near that point.
:::
