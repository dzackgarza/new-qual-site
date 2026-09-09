---
schema: qual/card@1
id: E-HAT-4.2-18
kind: problem
title: "Wedge equals product for coprime homology"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 18; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

---

If $X$ and $Y$ are simply-connected CW complexes such that $\tilde{H}_i(X)$ and $\tilde{H}_j(Y)$ are finite and of relatively prime orders for all pairs $(i, j)$, show that the inclusion $X \vee Y \hookrightarrow X \times Y$ is a homotopy equivalence and $X \wedge Y$ is contractible.

::: {.solution}
By the reduced Künneth theorem for smash products,
\[
\widetilde H_k(X\wedge Y;\mathbb Z)
\]
is built from the groups
\[
\widetilde H_i(X)\otimes\widetilde H_j(Y)
\quad\text{and}\quad
\operatorname{Tor}(\widetilde H_i(X),\widetilde H_j(Y)).
\]
Each \(\widetilde H_i(X)\) and \(\widetilde H_j(Y)\) is finite, and their orders are relatively prime. Therefore both the tensor product and Tor vanish for every pair \((i,j)\). Hence
\[
\widetilde H_*(X\wedge Y)=0.
\]

Since \(X\) and \(Y\) are simply connected, the smash product is simply connected as well. Thus the map
\[
X\wedge Y\to *
\]
is a homology equivalence between simply-connected CW complexes. The homology Whitehead theorem gives
\[
\boxed{X\wedge Y\simeq *.}
\]

The inclusion
\[
X\vee Y\hookrightarrow X\times Y
\]
is a cofibration with quotient \(X\wedge Y\). Since the quotient is acyclic, the relative homology groups
\[
H_*(X\times Y,X\vee Y)
\]
vanish. Both \(X\vee Y\) and \(X\times Y\) are simply connected, so the inclusion is a homology equivalence between simply-connected CW complexes. Again by homology Whitehead,
\[
\boxed{X\vee Y\simeq X\times Y.}
\]
:::
