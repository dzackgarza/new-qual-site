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

::: {.solution}
<1>1. $f$ maps closed subsets of $X$ to closed subsets of $Y$.

::: {.proof}
Let $C\subseteq X$ be closed.
A closed subset of the compact space $X$ is compact, so $C$ is compact.
The image $f(C)$ is compact because $f$ is continuous, and a compact subset of the Hausdorff space $Y$ is closed.
:::

<1>2. $f^{-1}\colon Y\to X$ is continuous.

::: {.proof}
For a closed set $C\subseteq X$, $(f^{-1})^{-1}(C)=f(C)$ because $f$ is bijective, and $f(C)$ is closed by step <1>1.
:::

<1>3. Q.E.D.

::: {.proof}
$f$ is a continuous bijection whose inverse is continuous by step <1>2, so $f$ is a homeomorphism.
:::
:::
