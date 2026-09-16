---
schema: qual/card@1
id: E-HAT-4.2-13
kind: problem
title: "Isomorphism on $\\pi_i$ for $i \\leq n$ in $n$-dimensional complexes"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 13; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

---

::: {.problem}
Show that a map between connected $n$-dimensional CW complexes is a homotopy equivalence if it induces an isomorphism on $\pi_i$ for $i \leq n$.
:::

::: {.solution}
Let
\[
f:X\to Y
\]
be a map of connected \(n\)-dimensional CW complexes inducing isomorphisms on \(\pi_i\) for \(i\le n\). In particular it is an isomorphism on \(\pi_1\), so it lifts to a map of universal covers
\[
\widetilde f:\widetilde X\to\widetilde Y.
\]
The universal covers are simply connected \(n\)-dimensional CW complexes, and \(\widetilde f\) is an isomorphism on \(\pi_i\) for \(2\le i\le n\).

Consider its mapping-cylinder pair \((M_{\widetilde f},\widetilde X)\). The long exact sequence of homotopy groups shows that this pair is \(n\)-connected. Relative Hurewicz therefore gives
\[
H_i(M_{\widetilde f},\widetilde X)=0
\qquad(i\le n).
\]
Equivalently,
\[
\widetilde f_*:H_i(\widetilde X)\xrightarrow{\cong}H_i(\widetilde Y)
\qquad(i\le n).
\]
For \(i>n\), both homology groups vanish because the two universal covers are \(n\)-dimensional CW complexes. Hence \(\widetilde f\) is a homology isomorphism in all degrees.

Exercise 12 now applies: since \(f\) is an isomorphism on \(\pi_1\) and its lift is a homology equivalence,
\[
\boxed{f\text{ is a homotopy equivalence}.}
\]
:::
