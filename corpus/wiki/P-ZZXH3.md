---
schema: qual/card@1
id: P-ZZXH3
kind: problem
title: The Fourier transform of a compactly supported continuous real function is
  entire
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Morera
  - Integrals
relations: []
review: draft
---

:::{.problem}
Suppose that $f: \RR\to\RR$ is a continuous function that vanishes outside of some finite interval.
For each $z\in \CC$, define
\[
g(z) = \int_{-\infty}^\infty f(t) e^{-izt} \,dt
.\]

Show that $g$ is entire.

:::

:::{.solution}
By Fubini:
\[
\oint_T g(z)\dz 
&\da \oint_T \int_\RR f(t)e^{-izt} \dt\dz \\
&\da \int_\RR \oint_T f(t)e^{-izt} \dz\dt \\
&\da \int_\RR f(t) \qty{ \oint_T e^{-izt} \dz } \dt \\
&\da \int_\RR f(t) \cdot 0 \dt \\
&= 0
,\]
where the inner integral vanishes because $z\mapsto e^{-izt}$ is entire by Goursat's theorem.
So $g$ is entire by Morera.
:::






