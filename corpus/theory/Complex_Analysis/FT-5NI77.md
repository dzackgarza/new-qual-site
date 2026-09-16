---
schema: qual/card@1
id: FT-5NI77
kind: theorem
title: Riemann's removable singularity theorem
prompts:
- State Riemann's removable singularity theorem.
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
  - Singularities
relations: []
review: draft
---

::: {.theorem}
Let $U\subseteq \CC$ be open, let $a\in U$, and let $f$ be [[D-E7A5W|holomorphic]] on $U\setminus\theset{a}$.
The following are equivalent:

- $f$ extends to a holomorphic function on $U$;

- $f$ extends to a continuous function on $U$;

- there exists a neighborhood $V$ of $a$ such that $f$ is bounded on $V\setminus\theset{a}$;

- $\lim_{z\to a} (z-a)f(z) = 0$.
:::
