---
schema: qual/card@1
id: E-ESQ3V
kind: problem
title: The Hilbert cube is not locally compact in the uniform topology
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
---

::: {.exercise}

Show that $[0, 1]^\omega$ is not locally compact in the uniform topology.
:::

::: {.solution}
Let $X=[0,1]^\omega$ with the uniform topology. Suppose $X$ were locally compact at some point $x$. A compact neighborhood of $x$ is closed because $X$ is metric, so there would be an open neighborhood $V$ of $x$ with compact closure. Choose $\varepsilon>0$ such that
$$
B(x,\varepsilon)\subset V.
$$
Choose $0<\delta<\min\{\varepsilon/2,1/2\}$. For each $n$, define $y^{(n)}\in X$ by changing only the $n$-th coordinate of $x$ by $\delta$, choosing the sign so as to remain in $[0,1]$. Then $y^{(n)}\in B(x,\varepsilon)\subset\overline V$, while for $m\ne n$,
$$
\bar\rho(y^{(m)},y^{(n)})=\delta.
$$
Thus $\{y^{(n)}\}$ is an infinite $\delta$-separated subset of compact metric $\overline V$, impossible since compact metric spaces are totally bounded. Therefore $X$ is not locally compact at any point.
:::
