---
schema: qual/card@1
id: E-HAT-4.2-16
kind: problem
title: "Surfaces with infinite $\\pi_1$ are $K(\\pi, 1)$'s"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 16; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

---

Show that the closed surfaces with infinite fundamental group are $K(\pi, 1)$'s by showing that their universal covers are contractible, via the Hurewicz theorem and results of §3.3.

::: {.solution}
Let \(M\) be a closed surface with infinite fundamental group, and let
\[
p:\widetilde M\to M
\]
be its universal cover. Then \(\widetilde M\) is a simply-connected surface. Since \(\pi_1(M)\) is infinite, the covering has infinitely many sheets, so \(\widetilde M\) is noncompact.

A connected noncompact \(2\)-manifold has zero top-dimensional integral homology, so
\[
H_2(\widetilde M;\mathbb Z)=0.
\]
Also
\[
H_1(\widetilde M;\mathbb Z)=0
\]
because \(\widetilde M\) is simply connected, and there is no homology above degree \(2\). Thus \(\widetilde M\) is acyclic.

If some higher homotopy group of \(\widetilde M\) were nonzero, choose the least \(k\ge2\) with \(\pi_k(\widetilde M)\ne0\). Then \(\widetilde M\) would be \((k-1)\)-connected, and Hurewicz would give
\[
\pi_k(\widetilde M)\cong H_k(\widetilde M),
\]
contradicting acyclicity. Hence all homotopy groups of \(\widetilde M\) vanish. Since \(\widetilde M\) has CW type, Whitehead's theorem gives
\[
\widetilde M\simeq *.
\]
Therefore
\[
\boxed{M\text{ is a }K(\pi_1(M),1).}
\]
:::
