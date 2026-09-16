---
schema: qual/card@1
id: E-HAT-4.1-12
kind: problem
title: "$n$-connected $n$-dimensional CW complexes are contractible"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 12; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

---

::: {.problem}
Show that an $n$-connected, $n$-dimensional CW complex is contractible.
:::

::: {.solution}
Let \(X\) be an \(n\)-connected, \(n\)-dimensional CW complex. Thus
\[
\pi_i(X)=0\qquad(0\le i\le n).
\]
Suppose some higher homotopy group were nonzero, and let \(m>n\) be the least integer with
\[
\pi_m(X)\ne0.
\]
Then \(X\) is \((m-1)\)-connected. By the Hurewicz theorem, the Hurewicz map
\[
\pi_m(X)\longrightarrow H_m(X;\mathbb Z)
\]
is an isomorphism. Hence \(H_m(X;\mathbb Z)\ne0\).

But \(X\) has no cells in dimensions greater than \(n\), so its cellular chain complex is zero above dimension \(n\). Therefore
\[
H_m(X;\mathbb Z)=0\qquad(m>n),
\]
a contradiction. Thus every homotopy group of \(X\) is trivial.

The map \(X\to *\) is consequently an isomorphism on all homotopy groups. Since \(X\) and a point are CW complexes, Whitehead's theorem implies that \(X\to *\) is a homotopy equivalence. Hence
\[
\boxed{X\text{ is contractible}.}
\]
:::
