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
Compute $H_*(X,\ZZ)$.
:::

::: {.solution}
The quotient collapses $T\times\{-1\}$ to one point and $T\times\{1\}$ to another, so it is precisely the unreduced suspension $\Sigma T$. Suspension shifts reduced homology by one:
$$
\widetilde H_n(\Sigma T;\ZZ)\cong \widetilde H_{n-1}(T;\ZZ).
$$
For the torus,
$$
H_0(T)=\ZZ,\qquad H_1(T)=\ZZ^2,\qquad H_2(T)=\ZZ,
$$
and all other homology groups vanish. Since $\Sigma T$ is connected, we obtain
$$
H_n(X;\ZZ)\cong
\begin{cases}
\ZZ,&n=0,\\
0,&n=1,\\
\ZZ^2,&n=2,\\
\ZZ,&n=3,\\
0,&n\ge4.
\end{cases}
$$
:::
