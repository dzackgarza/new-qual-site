---
schema: qual/card@1
id: E-HAT-4.I-1
kind: problem
title: "Suspension of a retract splits as a wedge"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.I, Exercise 1 and Proposition 4I.3; the stored statement matches the corrected current source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

If a connected CW complex $X$ retracts onto a subcomplex $A$, show that $\Sigma X \simeq \Sigma A \lor \Sigma(X/A)$.

::: {.solution}
Let
\[
r:X\to A
\]
be a retraction and
\[
q:X\to X/A
\]
the quotient map. Suspending and using the addition on maps out of a suspension gives
\[
F=\Sigma r+\Sigma q:\Sigma X\longrightarrow
\Sigma A\vee\Sigma(X/A).
\]
We show that \(F\) is a homology isomorphism.

Since \(r\circ i=\operatorname{id}_A\), the inclusion
\[
i_*:\widetilde H_*(A)\to\widetilde H_*(X)
\]
is split injective, with splitting \(r_*\). The long exact sequence of the pair \((X,A)\) therefore breaks into split short exact sequences
\[
0\longrightarrow\widetilde H_j(A)
\stackrel{i_*}{\longrightarrow}
\widetilde H_j(X)
\stackrel{q_*}{\longrightarrow}
\widetilde H_j(X/A)\longrightarrow0.
\]
Hence
\[
(r_*,q_*):\widetilde H_j(X)\xrightarrow{\cong}
\widetilde H_j(A)\oplus\widetilde H_j(X/A).
\tag{1}
\]
Under the suspension isomorphisms, \(F_*\) is exactly the map (1). Thus \(F\) induces an isomorphism on all reduced homology groups.

Both \(\Sigma X\) and
\[
\Sigma A\vee\Sigma(X/A)
\]
are simply connected CW complexes because \(X\) is connected. The homology version of Whitehead's theorem therefore gives
\[
\boxed{\Sigma X\simeq\Sigma A\vee\Sigma(X/A).}
\]
:::
