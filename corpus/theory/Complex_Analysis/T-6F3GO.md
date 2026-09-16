---
schema: qual/card@1
id: T-6F3GO
kind: theorem
title: Arzelà--Ascoli theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Arzelà-Ascoli
  - Equicontinuity
  - Compactness
  - Uniform Convergence
relations: []
review: draft
---

::: {.theorem}
Let $X$ be a compact Hausdorff space, and give $C(X;\RR)$ the uniform norm
$$
\norm{f}_{\infty,X}\coloneqq\sup_{x\in X}\abs{f(x)},
$$
under which it is a Banach space.
A subset $A\subseteq C(X;\RR)$ is compact if and only if $A$ is closed, uniformly bounded, and [[D-PPYCK|equicontinuous]].

In particular, for $X=[a,b]\subseteq\RR$, every uniformly bounded and uniformly equicontinuous sequence in $C([a,b];\RR)$ has a uniformly convergent subsequence.
:::
