---
schema: qual/card@1
id: P-TOP-WORKSHOP-D9-06
kind: problem
title: Use the Meyer–Vietoris sequence to calculate the homology of a wedge
classification:
  areas:
  - topology
  topics:
  - Mayer-Vietoris
  - Homology
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
Use the Meyer-Vietoris sequence to calculate the homology of $X\vee Y$.
:::

::: remark
The source page spells the sequence name “Meyer-Vietoris”; that spelling is preserved in the statement.
:::

::: {.solution}
Assume the usual CW (or well-pointed) hypotheses so that the wedge point has contractible neighborhoods in both summands. Choose open neighborhoods \(U,V\subset X\vee Y\) deformation retracting onto \(X\) and \(Y\), respectively, with \(U\cap V\) contractible. The reduced Mayer--Vietoris sequence then has, for every \(n\),
\[
0=\widetilde H_n(U\cap V)
\longrightarrow
\widetilde H_n(U)\oplus\widetilde H_n(V)
\longrightarrow
\widetilde H_n(X\vee Y)
\longrightarrow
\widetilde H_{n-1}(U\cap V)=0.
\]
Hence
\[
\boxed{\widetilde H_n(X\vee Y)
\cong \widetilde H_n(X)\oplus\widetilde H_n(Y)}
\]
for all \(n\). In particular, when \(X\) and \(Y\) are path connected,
\[
H_0(X\vee Y)\cong\mathbb Z,
\qquad
H_n(X\vee Y)\cong H_n(X)\oplus H_n(Y)\quad(n>0).
\]
:::
