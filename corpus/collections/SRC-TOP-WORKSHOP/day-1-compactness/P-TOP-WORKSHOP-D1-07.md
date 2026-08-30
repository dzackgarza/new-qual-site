---
schema: qual/card@1
id: P-TOP-WORKSHOP-D1-07
kind: problem
title: A continuous bijection from compact to Hausdorff is a homeomorphism
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
  - Homeomorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.problem}
Suppose that $X$ is compact and $Y$ is Hausdorff.
Prove that every one-to-one, onto, continuous map $f:X\to Y$ is a homeomorphism.
:::

::: solution
**Goal:** Show that continuity plus bijective compact-to-Hausdorff implies open and hence homeomorphic.

<1>1. Continuity of inverse from closed sets: *Proof:*\
Let $C\subseteq X$ be closed.
Since $X$ is compact, $C$ is compact.
The image $f(C)$ is compact because $f$ is continuous, and compact subsets of Hausdorff spaces are closed.
So $f$ sends closed sets in $X$ to closed sets in $Y$.

<1>2. Inverse image of open sets: *Proof:*\
For any open $U\subseteq X$, $$f^{-1}(f(U))=U.$$ Its complement in $Y$ is $$Y\setminus f(U)=f(X\setminus U),$$ because $f$ is bijective.
Since $X\setminus U$ is closed in compact $X$, $f(X\setminus U)$ is closed in Hausdorff $Y$.
Hence $Y\setminus f(U)$ is closed, so $f(U)$ is open.

<1>3. Conclusion: *Proof:*\
$f$ is continuous, bijective, and open, so $f^{-1}$ is continuous.
Therefore $f$ is a homeomorphism.
:::
