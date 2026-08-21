---
schema: qual/card@1
id: E-UJAF4
kind: exercise
title: Equicontinuity + pointwise convergence implies uniform convergence
classification:
  areas:
  - complex-analysis
  topics:
  - Equicontinuity
  - Uniform Convergence
  - Sequences of Functions
  - Compactness
relations: []
review: draft
solved: true
---

:::{.exercise title="Equicontinuity + pointwise convergence implies uniform convergence"}
Prove the following: if $\ts{f_n}$ is equicontinuous on $K$ a compact set and $f_n\to f$ pointwise, then $f_n\to f$ uniformly.

:::

:::{.solution title="?"}
Fix $\eps$, it suffices to find an $n= n(\eps)$ to bound $\norm{f_n - f}_{\infty, K } < \eps$.
A standard $\eps/3$ argument works: write
\[
\abs{f_n(x) - f(x) } \leq \abs{f_n(x) - f_n(y)} + \abs{f_n(y) - f(y)} + \abs{f(y) - f_n(y)}
.\]

Use equicontinuity to bound $\abs{f_n(x) - f_n(y)}$ for all $n\geq N_0 = N_0(\eps)$, for all $x,y\in K$.
This takes care of the 1st and 3rd terms.

For the 2nd term, cover $K$ by $\delta\dash$balls and by compactness obtain a finite cover $B_{\delta}(y_k)\covers K$.
Then $x\in B_\delta(y)$ for $y=y_j$ for some $j$, and in this ball use pointwise convergence of $f_n\to f$. 

:::

