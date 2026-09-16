---
schema: qual/card@1
id: E-HAT-3.A-4
kind: problem
title: "Tensor product and Tor commute with direct limits"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.A, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that $\otimes$ and Tor commute with direct limits: $(\varinjlim_\alpha A_\alpha) \otimes B = \varinjlim(A_\alpha \otimes B)$ and $\operatorname{Tor}(\varinjlim A_\alpha, B) = \varinjlim \operatorname{Tor}(A_\alpha, B)$.
:::

::: {.solution}
Let $(A_\alpha)$ be a directed system of abelian groups.

For tensor products, the universal property immediately gives
\[
\left(\varinjlim_\alpha A_\alpha\right)\otimes B
\cong \varinjlim_\alpha(A_\alpha\otimes B),
\]
since $-\otimes B$ is a left adjoint and therefore preserves colimits.

For $\operatorname{Tor}$, use a functorial free presentation. Let $F(A)$ be the free abelian group on the underlying set of $A$, with its natural surjection $F(A)\to A$, and let $K(A)$ be the kernel. Thus
\[
0\to K(A)\to F(A)\to A\to0
\]
is functorial in $A$. Applying this to the directed system and taking direct limits gives an exact sequence
\[
0\to \varinjlim K(A_\alpha)
\to \varinjlim F(A_\alpha)
\to \varinjlim A_\alpha\to0,
\]
because filtered colimits are exact in the category of abelian groups. The first two terms are free-resolution terms for the colimit for purposes of computing the kernel after tensoring.

Tensor the presentations with $B$. Since tensor product commutes with direct limits and filtered colimits preserve kernels of maps occurring in these exact sequences,
\[
\begin{aligned}
\operatorname{Tor}(\varinjlim A_\alpha,B)
&=\ker\!\left((\varinjlim K(A_\alpha))\otimes B
\to(\varinjlim F(A_\alpha))\otimes B\right)\\
&\cong \varinjlim\ker\!\left(K(A_\alpha)\otimes B
\to F(A_\alpha)\otimes B\right)\\
&=\varinjlim\operatorname{Tor}(A_\alpha,B).
\end{aligned}
\]
Thus both $\otimes$ and $\operatorname{Tor}$ commute with directed limits.
:::
