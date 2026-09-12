---
schema: qual/card@1
id: E-HAT-4.1-7
kind: problem
title: "Change-of-basepoint for relative homotopy groups"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 7; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

---

Extend the results proved near the beginning of this section for the change-of-basepoint maps $\beta_\gamma$ to the case of relative homotopy groups.

::: {.solution}
Let \(\gamma:I\to A\) be a path from \(x_0\) to \(x_1\). For \(n\ge2\), define
\[
\beta_\gamma:\pi_n(X,A,x_1)\longrightarrow\pi_n(X,A,x_0)
\]
by attaching to the distinguished boundary point of a representative
\[
f:(D^n,S^{n-1},s_0)\to(X,A,x_1)
\]
a thin collar whose image runs along \(\gamma\), and extending this collar constantly in the transverse directions. Equivalently, in the cubical model one reserves a narrow strip adjacent to the distinguished face and maps that strip through \(\gamma\).

The usual reparametrization argument shows that this construction is independent of the width of the collar and of the chosen representative. Reversing \(\gamma\) gives the inverse:
\[
\beta_{\bar\gamma}\beta_\gamma=\operatorname{id},
\qquad
\beta_\gamma\beta_{\bar\gamma}=\operatorname{id}.
\]
Concatenating paths gives
\[
\beta_{\gamma\eta}=\beta_\gamma\beta_\eta
\]
with the corresponding convention for path order, and homotopic paths rel endpoints induce the same map.

These maps commute with the maps in the long exact sequence of the pair. In particular, if
\[
\partial:\pi_n(X,A,x_i)\to\pi_{n-1}(A,x_i),
\]
then
\[
\partial\beta_\gamma=eta_\gamma\partial,
\]
and the analogous naturality holds for \(\pi_n(A)\to\pi_n(X)\) and \(\pi_n(X)\to\pi_n(X,A)\).

Thus all change-of-basepoint results from the absolute case extend to relative homotopy groups. In particular, when \(A\) is path-connected the relative groups are independent of basepoint up to these canonical isomorphisms, with the same \(\pi_1(A)\)-ambiguity as in the absolute case.
:::
