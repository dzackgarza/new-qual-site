---
schema: qual/card@1
id: E-HAT-4.K-1
kind: problem
title: "Mayer--Vietoris for CW subcomplexes"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.K, Exercise 1 and the corrected current statement of Lemma 4K.3 where relevant; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that Corollary 4K.2 remains valid when $X$ and $Y$ are CW complexes and the subspaces $U_i$ and $V_i$ are subcomplexes rather than open sets.
:::

::: {.solution}
Let
\[
f:X\to Y
\]
be the map in Corollary 4K.2, and suppose the covering families \(\{U_i\}\) of \(X\) and \(\{V_i\}\) of \(Y\) consist of CW subcomplexes, with
\[
f(U_i)\subset V_i,
\]
and with the required weak equivalences on all finite intersections.

Replace each subcomplex by a standard open regular neighborhood in a sufficiently fine barycentric subdivision. Thus for every finite set \(J\) of indices we can choose open sets
\[
N(U_J)\supset U_J,
\qquad
N(V_J)\supset V_J,
\qquad
U_J=\bigcap_{j\in J}U_j,\quad V_J=\bigcap_{j\in J}V_j,
\]
such that
\[
N(U_J)\simeq U_J,
\qquad
N(V_J)\simeq V_J,
\]
and the choices are compatible with finite intersections. After shrinking the target neighborhoods if necessary, continuity of \(f\) and the subcomplex condition give
\[
f(N(U_i))\subset N(V_i).
\]

For each finite \(J\), the commutative square
\[
\begin{array}{ccc}
U_J&\longrightarrow&V_J\\
\downarrow&&\downarrow\\
N(U_J)&\longrightarrow&N(V_J)
\end{array}
\]
has vertical homotopy equivalences. Since the top map is a weak homotopy equivalence by hypothesis, so is the bottom map. Hence the open covers \(\{N(U_i)\}\), \(\{N(V_i)\}\) satisfy the hypotheses of Corollary 4K.2. It follows that
\[
\boxed{f:X\to Y\text{ is a weak homotopy equivalence}.}
\]
Thus Corollary 4K.2 remains valid when the covering sets are subcomplexes rather than open sets.
:::
