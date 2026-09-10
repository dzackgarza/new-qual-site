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
Let \(X=[0,1]^\omega\) with the uniform topology. Suppose \(X\) were locally compact at some point \(x\). Then there would be a neighborhood \(V\) of \(x\) with compact closure. Choose \(\varepsilon>0\) such that
\[
B(x,\varepsilon)\subset V.
\]
For each \(n\), define \(y^{(n)}\in X\) by changing only the \(n\)-th coordinate of \(x\) by a fixed amount \(\delta>0\) with \(\delta<\varepsilon/2\), choosing the sign so as to remain in \([0,1]\). Then \(y^{(n)}\in B(x,\varepsilon)\subset\overline V\), while for \(m\ne n\),
\[
\bar\rho(y^{(m)},y^{(n)})=\delta.
\]
Thus \(\{y^{(n)}\}\) is an infinite \(\delta\)-separated subset of compact metric \(\overline V\), impossible since compact metric spaces are totally bounded. Therefore \(X\) is not locally compact at any point.
:::
