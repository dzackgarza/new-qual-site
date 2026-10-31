---
schema: qual/card@1
id: E-HAT-2.3-3
kind: problem
title: Reduced homology theory vanishes on point; suspension isomorphism follows
classification:
  areas:
  - topology
  topics:
  - Homology
  - Axiomatic Homology
  - Suspension
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.3, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that if $\tilde{h}$ is a reduced homology theory, then $\tilde{h}_n(\text{point}) = 0$ for all $n$.
Deduce that there are suspension isomorphisms $\tilde{h}_n(X) \approx \tilde{h}_{n+1}(SX)$ for all $n$.
:::

::: {.solution}
Apply the exactness axiom to the CW pair $(*,*)$. The inclusion $*\to *$ and the quotient map $*\to */*=*$ are both the identity. Thus the exact sequence contains
$$
\widetilde h_n(*)\xrightarrow{\mathrm{id}}\widetilde h_n(*)
\xrightarrow{\mathrm{id}}\widetilde h_n(*).
$$
The image of the first map is the whole group, while the kernel of the second is zero. Exactness forces $\widetilde h_n(*)=0$ for every $n$.

Let $CX$ be the cone on $X$. It is contractible, so homotopy invariance gives $\widetilde h_k(CX)=0$ for every $k$. The exact sequence of the CW pair $(CX,X)$ therefore contains
$$
0=\widetilde h_{n+1}(CX)
\longrightarrow\widetilde h_{n+1}(CX/X)
\xrightarrow{\partial}\widetilde h_n(X)
\longrightarrow\widetilde h_n(CX)=0.
$$
Since $CX/X\cong SX$, the boundary map gives the required suspension isomorphism.
:::
