---
schema: qual/card@1
id: FT-LGWHM
kind: theorem
title: Riemann's removable singularity theorem
prompts:
- What conditions are equivalent to $f$ extending holomorphically over an isolated singularity?
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
  - Singularities
relations:
- kind: variant-of
  target: FT-5NI77
review: draft
---

::: {.theorem}
Let $U\subseteq \CC$ be open, let $a\in U$, and let $f$ be [[D-E7A5W|holomorphic]] on $U\setminus\theset{a}$.
The following are equivalent:

- $f$ extends to a holomorphic function on $U$;

- $f$ extends to a continuous function on $U$;

- there exists a neighborhood $V$ of $a$ such that $f$ is bounded on $V\setminus\theset{a}$;

- $\displaystyle\lim_{z\to a} (z-a)f(z) = 0$.
:::
