---
schema: qual/card@1
id: T-BX4LD
kind: theorem
title: Lefschetz Fixed Point
classification:
  areas:
  - topology
  topics:
  - Fixed Points
  - Homology
relations: []
review: draft
---

::: {.theorem}
For $f:X\to X$, define the **trace** of $f$ to be
\[
\Lambda_f \da \sum_{k \geq 0} (-1)^k ~\mathrm{Tr}(f_* \mid H_k(X; \QQ))
\]
where $f_*: H_k(X; \QQ) \to H_k(X; \QQ)$ is the induced map on homology.
If $\Lambda_f \neq 0$ then $f$ has a fixed point.
:::
