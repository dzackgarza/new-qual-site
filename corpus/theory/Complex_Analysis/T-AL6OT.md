---
schema: qual/card@1
id: T-AL6OT
kind: theorem
title: Riemann's removable singularity theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
  - Singularities
relations:
- kind: variant-of
  target: T-ZZJDP
review: draft
---

::: {.theorem}
Let $\Omega\subseteq\CC$ be open, $z_0\in\Omega$, and let $f$ be [[D-E7A5W|holomorphic]] on $\Omega\sm\ts{z_0}$.
If $f$ is bounded on some punctured neighborhood of $z_0$, then $z_0$ is a [[D-BQLJV|removable singularity]] of $f$.

More generally, the following are equivalent:

- $f$ extends holomorphically over $z_0$: there is a holomorphic $F\colon\Omega\to\CC$ with $\ro{F}{\Omega\sm\ts{z_0}}=f$;

- $f$ extends continuously over $z_0$;

- $f$ is bounded on some punctured neighborhood of $z_0$;

- $\lim_{z\to z_0}(z-z_0)f(z)=0$.
:::
