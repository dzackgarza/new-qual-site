---
schema: qual/card@1
id: P-DS4D6
kind: problem
title: "Show that a continuous function on a compact set is uniformly continuo\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - uniform-continuity
  - compactness
  - continuity
relations: []
review: draft
---
:::{.problem title="?"}
Show that a continuous function on a compact set is uniformly continuous.
:::

:::{.solution}
Use a stronger result: a continuous function on a compact metric is uniformly continuous.
Fix $\eps$. 
Suppose $f$ is continuous, then for each $z\in X$ choose $\delta_z = \delta(\eps, z)$ to ensure $B_\delta(z) \injects B_\eps(f(z))$ and form the cover $\ts{B_{\delta_z} (z)}_{x\in X}\covers X$.
By compactness, choose a finite subcover corresponding to $\ts{z_1, \cdots, z_m}$ and choose $\delta = \min \ts{\delta_1, \cdots, \delta_m}$.
The claim is that this $\delta$ works for uniform continuity: if $\abs{x-y} < \delta$ then $\abs{x-y} < \delta_i$ for all $i$.
Note that $x\in B_{\delta_z}(z)$ for one of the finitely many $z$ above, and if we adjust $\delta$ to $\delta/2$, we can arrange so that both $x, y\in B_{\delta_z}(z)$ for some $z$, since
\[
  \abs{x-y} = \abs{x-z+z-y} \leq \abs{x-z} + \abs{z-y} < {\delta \over 2 } + {\delta \over 2} = \delta < \delta_{z}
,\]
and similarly
\[
  \abs{f(x)-f(y) } \leq \abs{f(x)-f(z)} + \abs{f(z)-f(y)} < \eps + \eps 
,\]
so just adjust the original $\eps$ chosen by the continuity of $f$ to $\eps/2$.
:::


