---
schema: qual/card@1
id: E-HAT-3.3-23
kind: problem
title: "Simplicial vs. singular compactly supported cohomology"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 23; the stored statement matches the current online text and diagram where applicable.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that for a locally compact $\Delta$-complex $X$ the simplicial and singular cohomology groups $H_c^i(X; G)$ are isomorphic.
:::

::: {.solution}
Let $X$ be a locally compact $\Delta$-complex. A compactly supported simplicial cochain is nonzero on only finitely many simplices, since local compactness implies that each compact set meets only finitely many simplices. Hence
\[
\Delta_c^i(X;G)=\bigcup_A \Delta^i(X,A;G),
\]
where $A$ ranges over subcomplexes containing all but finitely many simplices. The same family is cofinal for compactly supported singular cochains, and
\[
C_c^i(X;G)=\bigcup_A C^i(X,A;G).
\]
These unions are filtered direct limits over $A$ ordered by reverse inclusion.

For each such subcomplex $A$, the usual comparison theorem between simplicial and singular cohomology of a $\Delta$-complex pair gives an isomorphism
\[
H^i_{\Delta}(X,A;G)\xrightarrow{\cong}H^i_{\mathrm{sing}}(X,A;G),
\]
natural with respect to inclusions of pairs. Since filtered direct limits are exact, cohomology commutes with these direct limits. Therefore
\[
H^i(\Delta_c^*(X;G))
\cong
\varinjlim_A H^i_{\Delta}(X,A;G)
\cong
\varinjlim_A H^i_{\mathrm{sing}}(X,A;G)
\cong
H^i(C_c^*(X;G)).
\]
Thus the simplicial and singular compactly supported cohomology groups are naturally isomorphic.
:::
