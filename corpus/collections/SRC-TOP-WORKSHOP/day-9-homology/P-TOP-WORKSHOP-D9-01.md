---
schema: qual/card@1
id: P-TOP-WORKSHOP-D9-01
kind: problem
title: Homology of $T\times[-1,1]$ with each end $T\times\{\pm 1\}$ collapsed to a
  point
classification:
  areas:
  - topology
  topics:
  - Homology
  - Quotient Spaces
  - Surfaces
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
(Michigan Sept ’10) Consider the 2-dimensional torus $T$ and the topological space $$X=T\times[-1,1]/\sim$$ where $(x,t)\sim(x',t')$ if either $(x,t)=(x',t')$ or $t=t'\in\{-1,1\}$.
Compute $H_*(X,\mathbb Z)$.
:::

::: {.solution}
The quotient collapses \(T\times\{-1\}\) to one point and \(T\times\{1\}\) to another, so it is precisely the unreduced suspension \(\Sigma T\). Suspension shifts reduced homology by one:
\[
\widetilde H_n(\Sigma T;\mathbb Z)\cong \widetilde H_{n-1}(T;\mathbb Z).
\]
For the torus,
\[
H_0(T)=\mathbb Z,\qquad H_1(T)=\mathbb Z^2,\qquad H_2(T)=\mathbb Z,
\]
and all other homology groups vanish. Since \(\Sigma T\) is connected, we obtain
\[
H_n(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&n=0,\\
0,&n=1,\\
\mathbb Z^2,&n=2,\\
\mathbb Z,&n=3,\\
0,&n\ge4.
\end{cases}
\]
:::
