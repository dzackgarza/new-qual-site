---
schema: qual/card@1
id: P-MMAQ-YQU7AEUCMW
kind: problem
title: Let
classification:
  areas:
  - topology
  topics:
  - fundamental-group
relations: []
review: draft
---

::: problem
Let
$$
V = \DD^2 \times S^1 = \theset{ (z, e^{it}) \suchthat \norm z \leq 1,~~ 0 \leq t < 2\pi}
$$
be the "solid torus" with boundary given by the torus $T = S^1 \times S^1$ .

For $n \in Z$ define `\begin{align*} \phi_n : T &\to T \\ (e^{is} , e^{it} ) &\mapsto (e^{is} , e^{i(ns+t)}) .\end{align*}`{=tex}

Find the fundamental group of the identification space
$$
V_n = {V\disjoint V \over \sim n}
$$
where the equivalence relation $\sim_n$ identifies a point $x$ on the boundary $T$ of the first copy of $V$ with the point $\phi_n (x)$ on the boundary of the second copy of $V$.
:::
