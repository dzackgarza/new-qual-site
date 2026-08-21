---
schema: qual/card@1
id: T-LDJNS
kind: theorem
title: Fatou
classification:
  areas:
  - real-analysis
  topics:
  - Fatou
  - Convergence of Integrals
relations: []
review: draft
---

:::{.theorem title="Fatou"}
If $f_n$ is a sequence of nonnegative measurable functions, then
\[
\liminf_n \int f_n 
&\geq \int \liminf_n f_n \\
\limsup_n \int f_n &\leq \int \limsup_n f_n
.\]
:::
