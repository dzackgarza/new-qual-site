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
By the dictionary-order calculation from §16, the dictionary order topology on $\mathbb R\times\mathbb R$ is exactly the product topology
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
is a metric on $\mathbb R^2$. Balls of radius $<1$ force $x=x'$ and impose an ordinary metric condition on $y$, so they have the same local bases as $\mathbb R_d\times\mathbb R$. Hence $D$ metrizes the dictionary order topology.
:::
