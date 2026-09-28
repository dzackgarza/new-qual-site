---
schema: qual/card@1
id: E-KY2W7
kind: problem
title: The dictionary order plane is metrizable
classification:
  areas:
  - topology
  topics:
  - Metrizability
  - Order Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Show that $\mathbb{R} \times \mathbb{R}$ in the dictionary order topology is metrizable.
:::

::: {.solution}
By [[E-QMZO5]], the dictionary order topology on $\mathbb R\times\mathbb R$ is exactly the product topology
\[
\mathbb R_d\times\mathbb R,
\]
where $\mathbb R_d$ is discrete.

Let
\[
\delta(x,x')=\begin{cases}0,&x=x',\\1,&x\ne x',\end{cases}
\qquad
\rho(y,y')=\min\{|y-y'|,1\}.
\]
Both are metrics inducing the discrete and usual topologies respectively. Then
\[
D((x,y),(x',y'))=\delta(x,x')+\rho(y,y')
\]
is a metric on $\mathbb R^2$. For $0<r\le1$,
\[
B_D((x,y),r)=\{x\}\times(y-r,y+r),
\]
since $\delta(x,x')\ge1$ when $x'\ne x$. These sets form a basis of $\mathbb R_d\times\mathbb R$ at $(x,y)$, and every $D$-ball about $(x,y)$ contains one of them. Hence $D$ metrizes the dictionary order topology.
:::
