---
schema: qual/card@1
id: E-FS7GZ
kind: problem
title: Radii of convergence of the principal $\sqrt z$ about $4+3i$ and $-4+3i$
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Convergence Tests
  - Complex Logarithm
relations: []
review: draft
---

::: {.exercise}
Find the radius of convergence of the Taylor series of the principal branch of $\sqrt z$ about $z_0=4+3i$.
Repeat with $z_1=-4+3i$.
:::

::: {.solution}
For a center $c\neq0$, the disk $\abs{z-c}<\abs c$ does not contain $0$, so it carries a holomorphic branch of $\sqrt z$ agreeing with the principal branch near $c$; the Taylor series of the principal branch at $c$ converges on this disk. It converges on no larger disk: the binomial expansion
\[
\sqrt z=\sqrt c\sum_{n\ge0}\binom{1/2}{n}\qty{z-c\over c}^n
\]
has radius of convergence exactly $\abs c$, since $\binom{1/2}{n}$ has ratio $\abs{1/2-n}/(n+1)\to1$.

For $z_0=4+3i$,
\[
R_0=|4+3i|=\boxed{5}.
\]

For $z_1=-4+3i$,
\[
R_1=|-4+3i|=\boxed{5}.
\]
The branch cut $\RR_{\le0}$ meets this disk: the sum of the series equals the principal branch only on the part of the disk above the cut, including the disk $\abs{z-z_1}<3$, and equals its analytic continuation across the cut below it.
:::
