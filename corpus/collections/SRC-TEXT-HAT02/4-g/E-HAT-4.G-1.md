---
schema: qual/card@1
id: E-HAT-4.G-1
kind: problem
title: "Infinite mapping cylinder deformation retracts onto telescope"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.G, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Show that for a sequence of maps $X_0 \xrightarrow{f_1} X_1 \xrightarrow{f_2} \cdots$, the infinite iterated mapping cylinder $M(f_1, f_2, \ldots)$, which is the union of the finite iterated mapping cylinders $M(f_1, \ldots, f_n)$, deformation retracts onto the mapping telescope.

::: {.solution}
Let
\[
X_0\xrightarrow{f_1}X_1\xrightarrow{f_2}X_2\to\cdots
\]
be the sequence. For each finite stage, the iterated mapping cylinder
\[
M_n=M(f_1,\ldots,f_n)
\]
contains the finite telescope
\[
T_n=X_0\times[0,1]\cup X_1\times[1,2]\cup\cdots\cup X_{n-1}\times[n-1,n]\cup X_n
\]
with the usual identifications at integer levels.

The ordinary mapping cylinder \(M(f)\) deformation retracts onto the copy of the interval cylinder together with its target, and this retraction can be chosen fixed on the target. Apply this successively to the nested mapping-cylinder pieces of \(M_n\). This gives a deformation retraction
\[
r_n:M_n\times I\to M_n
\]
onto \(T_n\), chosen so that \(r_{n+1}\) restricts to \(r_n\) on \(M_n\). Concretely, on the new mapping-cylinder block one only straightens the extra cylinder coordinate; all earlier stages are left unchanged.

Since the finite-stage homotopies are compatible, they assemble on the union
\[
M(f_1,f_2,\ldots)=\bigcup_nM_n
\]
to a continuous homotopy
\[
r:M(f_1,f_2,\ldots)\times I\to M(f_1,f_2,\ldots).
\]
At time \(1\) its image is
\[
\bigcup_nT_n,
\]
which is exactly the mapping telescope. The homotopy fixes the telescope pointwise throughout. Hence
\[
\boxed{M(f_1,f_2,\ldots)\text{ deformation retracts onto the mapping telescope}.}
\]
:::
