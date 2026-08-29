---
schema: qual/card@1
id: T-6F3GO
kind: theorem
title: Arzelà-Ascoli (analog of Heine-Borel)
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

:::{.theorem}
For $X$ compact Hausdorff, consider the Banach space $C(X; \RR)$ equipped with the *uniform norm* 
\[
\norm{f}_{\infty, X} \da \sup_{x\in X} \abs{f(x)}
.\]

A subset $A \subseteq C(X; \RR)$ is compact iff $A$ is closed, uniformly bounded, and equicontinuous.

For $X = [a,b]\subseteq \RR$, if a sequence is uniformly bounded and uniformly equicontinuous, then there exists a uniformly convergent subsequence.
:::
