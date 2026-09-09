---
schema: qual/card@1
id: E-HAT-3.3-17
kind: problem
title: "Direct limits commute with homology"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 17; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Show that a direct limit of exact sequences is exact.
More generally, show that homology commutes with direct limits: If $\{C_\alpha, f_{\alpha\beta}\}$ is a directed system of chain complexes, with the maps $f_{\alpha\beta}: C_\alpha \to C_\beta$ chain maps, then $H_n(\varinjlim C_\alpha) = \varinjlim H_n(C_\alpha)$.

::: {.solution}
For a directed system of abelian groups, recall that
\[
\varinjlim A_\alpha
\]
is the disjoint union of the $A_\alpha$ modulo the relation that $a_\alpha$ and $a_\beta$ are equal when their images agree at some later stage.

Consider a directed system of exact sequences
\[
A_\alpha\xrightarrow{u_\alpha}B_\alpha\xrightarrow{v_\alpha}C_\alpha.
\]
Certainly $\operatorname{im}(\varinjlim u_\alpha)\subseteq\ker(\varinjlim v_\alpha)$. Conversely, let a class $[b_\alpha]$ map to zero in $\varinjlim C_\alpha$. Then for some $\beta\ge\alpha$, the image $b_\beta$ maps to zero in $C_\beta$. Exactness at stage $\beta$ gives $a_\beta\in A_\beta$ with
\[
u_\beta(a_\beta)=b_\beta.
\]
Thus $[b_\alpha]$ lies in the image of $\varinjlim A_\alpha$. Hence filtered direct limits preserve exact sequences.

Now let $C_\alpha$ be a directed system of chain complexes. Since direct limits are exact, they commute with kernels, images, and cokernels occurring in the short exact sequences
\[
0\to Z_n(C_\alpha)\to C_{\alpha,n}\to B_{n-1}(C_\alpha)\to0
\]
and
\[
0\to B_n(C_\alpha)\to Z_n(C_\alpha)\to H_n(C_\alpha)\to0.
\]
Therefore
\[
Z_n(\varinjlim C_\alpha)\cong\varinjlim Z_n(C_\alpha),
\qquad
B_n(\varinjlim C_\alpha)\cong\varinjlim B_n(C_\alpha),
\]
and taking the quotient gives
\[
\boxed{H_n(\varinjlim C_\alpha)\cong\varinjlim H_n(C_\alpha).}
\]
:::
