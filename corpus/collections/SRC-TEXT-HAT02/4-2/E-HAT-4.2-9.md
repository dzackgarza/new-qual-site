---
schema: qual/card@1
id: E-HAT-4.2-9
kind: problem
title: "Contractible mapping cone implies homotopy equivalence"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 9; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

---

Show that a map between simply-connected CW complexes is a homotopy equivalence if its mapping cone is contractible.
Use the preceding exercise to give an example where this fails in the nonsimply-connected case.

::: {.solution}
Let $f:X\to Y$ be a map of simply-connected CW complexes and suppose its mapping cone $C_f$ is contractible. The cofibration sequence
\[
X\xrightarrow f Y\longrightarrow C_f
\]
gives the long exact sequence in reduced homology. Since $\widetilde H_*(C_f)=0$, the map
\[
f_*:H_i(X;\mathbb Z)\xrightarrow{\cong}H_i(Y;\mathbb Z)
\]
is an isomorphism for every $i$. The homology Whitehead theorem for simply-connected CW complexes then implies that $f$ is a homotopy equivalence.

The simply-connected hypothesis is essential. Let $A$ be any acyclic, noncontractible CW complex (for example an acyclic $K(G,1)$ for a nontrivial acyclic group $G$), and take the constant map
\[
f:A\longrightarrow *.
\]
Its mapping cone is
\[
C_f=CA/A\cong\Sigma A.
\]
By the preceding exercise the suspension of an acyclic CW complex is contractible. Thus $C_f$ is contractible, while $f$ is not a homotopy equivalence because $A$ is not contractible. This gives the required nonsimply-connected counterexample.
:::
