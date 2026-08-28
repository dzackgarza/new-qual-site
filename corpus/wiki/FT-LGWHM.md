---
schema: qual/card@1
id: FT-LGWHM
kind: theorem
title: Riemann's Removable Singularity Theorem
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
Let $U\subset \CC$ be open, $a\in U$, and $f$ holomorphic on $U\setminus\theset{a}$. 
Then TFAE

- $f$ extends holomorphically to all of $U$
- $f$ extends continuously to all of $U$
- There exists a neighborhood of $a$ on which $f$ is bounded.
- The limit characterization:
$$
\lim_{z\to a} (z-a)f(z) = 0
.$$
:::
