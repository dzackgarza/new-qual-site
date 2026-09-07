---
schema: qual/card@1
id: P-ALGF10C
kind: problem
title: "Every subgroup of a cyclic normal subgroup is normal in the whole group"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Question 3 of the official UCSD Algebra Qualifying Examination, Fall 2010; the statement agrees with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified that every subgroup of a cyclic group is characteristic, hence is normal in any group in which the cyclic group is normal.
---

::: {.problem}
Show that if $H$ is a cyclic normal subgroup of $G$, then every subgroup of $H$ is normal in $G$.
:::


::: {.solution}
Let \(K\le H\), where \(H\triangleleft G\) and \(H\) is cyclic.

<1>1. The subgroup \(K\) is characteristic in \(H\).
::: {.proof}
Write
\[
H=\langle h\rangle.
\]
If \(H\) is finite of order \(n\), then every subgroup of \(H\) is uniquely determined by its order: for each divisor \(d\mid n\), there is exactly one subgroup of order \(d\), namely
\[
\langle h^{n/d}\rangle.
\]
Hence every automorphism of \(H\) preserves every subgroup.

If \(H\) is infinite cyclic, every subgroup has the form
\[
\langle h^m\rangle
\qquad(m\ge0).
\]
Every automorphism of \(H\) sends \(h\) to \(h\) or \(h^{-1}\), so it preserves \(\langle h^m\rangle\).

Thus in either case every subgroup of \(H\), and in particular \(K\), is characteristic in \(H\).
:::

<1>2. The subgroup \(K\) is normal in \(G\).
::: {.proof}
Fix \(g\in G\).
Because \(H\triangleleft G\), conjugation by \(g\) restricts to an automorphism
\[
c_g:H\longrightarrow H,
\qquad
x\longmapsto gxg^{-1}.
\]
By <1>1, \(K\) is characteristic in \(H\), so
\[
c_g(K)=K.
\]
Thus
\[
gKg^{-1}=K
\]
for every \(g\in G\).
Therefore \(K\triangleleft G\).
:::
:::
