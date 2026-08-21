---
schema: qual/card@1
id: PR-2CZUM
kind: proposition
title: Commuting derivatives with integrals, Folland 2.27
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Convergence of Integrals
  - Integrals
relations: []
review: draft
---

:::{.proposition title="Commuting derivatives with integrals, Folland 2.27"}
If $f:X\cross I \to \CC$ where $f_t: X\to \CC$ is integrable for each $t$, then if $\abs{f(x, t)} \leq \abs{g(x)}$ for some $g\in L^1$, then
\[
\lim_{t\to t_0}\int_X f(x, t) \dmu = \int_X f(x, t_0) \dmu \da F(t_0)
,\]
and if $f_x: I\to \CC$ is continuous for all $x$, then $F: I\to \CC$ is continuous.

Moreover if $\dd{f}{t}$ exists and $\abs{\dd{f}{t}(x, t)} \leq \abs{g}$ for some $g\in L^1$, then 
\[
\dd{}{t} \int_X f(x, t) \dmu
= \int_X \dd{}{t} f(x, t) \dmu
.\]


:::
