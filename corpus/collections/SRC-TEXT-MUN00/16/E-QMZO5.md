---
schema: qual/card@1
id: E-QMZO5
kind: problem
title: Dictionary order topology on the plane as a product topology
classification:
  areas:
  - topology
  topics:
  - Order Topology
  - Product Topology
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

Show that the dictionary order topology on the set $\mathbb{R} \times \mathbb{R}$ is the same as the product topology $\mathbb{R}_d \times \mathbb{R}$, where $\mathbb{R}_d$ denotes $\mathbb{R}$ in the discrete topology.
Compare this topology with the standard topology on $\mathbb{R}^2$.
:::

::: {.solution}
In the dictionary order, for every $x\in\mathbb R$ and $a<b$,
\[
\{x\}\times(a,b)=((x,a),(x,b)),
\]
so each basic set for $\mathbb R_d\times\mathbb R$ is dictionary-order open. Hence the product topology is contained in the dictionary-order topology.

Conversely, a dictionary-order interval between $(a,b)$ and $(c,d)$ is a union of vertical open pieces: if $a<c$, it is
\[
\{a\}\times(b,\infty)\;\cup\!
\bigcup_{a<x<c}\!\{x\}\times\mathbb R
\;\cup\;\{c\}\times(-\infty,d),
\]
and when $a=c$ it is simply $\{a\}\times(b,d)$. These sets are open in $\mathbb R_d\times\mathbb R$. The two topologies therefore coincide.

This topology is strictly finer than the standard topology on $\mathbb R^2$. Every ordinary open rectangle is a union of sets $\{x\}\times(c,d)$, hence is dictionary-open, while for example
\[
\{0\}\times\mathbb R
\]
is dictionary-open but not standard-open.
:::
