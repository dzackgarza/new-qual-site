---
schema: qual/card@1
id: E-HAT-3.3-30
kind: problem
title: "Boundary of orientable manifold is orientable"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 30; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that the boundary of an $R$-orientable manifold is also $R$-orientable.
:::

::: {.solution}
Let $M^n$ be $R$-orientable. A collar identifies a neighborhood of the boundary with
\[
\partial M\times[0,\varepsilon).
\]
For $x\in\partial M$, choose a small half-ball neighborhood $B_+^n$ in $M$. The local fundamental class of $M$ determines a generator of
\[
H_n(B_+^n,B_+^n-\{x\};R)
\]
in the relative form appropriate to a boundary point. The connecting homomorphism for the local pair sends this generator to a generator of
\[
H_{n-1}(\partial M,\partial M-\{x\};R).
\]
Use this image as the local orientation of $\partial M$ at $x$.

Naturality of the connecting homomorphism shows that these boundary local classes vary locally constantly whenever the local orientation classes of $M$ do. Hence they define an $R$-orientation of $\partial M$.

Equivalently, in oriented collar charts this is the usual rule that an oriented basis of the boundary is chosen so that the outward normal followed by that basis gives the orientation of $M$. Thus
\[
\boxed{\partial M\text{ is }R\text{-orientable}.}
\]
:::
