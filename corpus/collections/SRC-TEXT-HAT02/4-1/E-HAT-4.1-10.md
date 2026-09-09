---
schema: qual/card@1
id: E-HAT-4.1-10
kind: problem
title: "Quasi-circle has trivial homotopy but is not contractible"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 10; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

---

Show the 'quasi-circle' described in Exercise 7 in §1.3 has trivial homotopy groups but is not contractible, hence does not have the homotopy type of a CW complex.

::: {.solution}
Let \(Y\) be the quasi-circle of §1.3, Exercise 7. That exercise proves two facts we use:

1. every path in \(Y\) is contained in a finite truncation of the oscillating graph together with the vertical segment and the connecting arc, hence in a finite tree;
2. the quotient map
\[
q:Y\to S^1
\]
collapsing the vertical segment has no lift to \(\mathbb R\to S^1\).

We show first that every homotopy group of \(Y\) is trivial. The space \(Y\) is path-connected, so \(\pi_0(Y)\) is trivial as a pointed set. For \(n\ge1\), let
\[
f:S^n\to Y.
\]
The sphere \(S^n\) is a compact, connected, locally connected metric space, hence a Peano continuum. Therefore there is a continuous surjection
\[
r:I\twoheadrightarrow S^n.
\]
The composite \(f r:I\to Y\) is a path and has image exactly \(f(S^n)\). By the path-confinement result above, this image lies in a finite tree \(T\subset Y\). Hence \(f\) factors through the contractible space \(T\), so \(f\) is nullhomotopic. Thus
\[
\boxed{\pi_n(Y)=0\quad\text{for all }n\ge1.}
\]

Nevertheless \(Y\) is not contractible. If it were, the quotient map \(q:Y\to S^1\) would be nullhomotopic. A nullhomotopy of \(q\), together with a lift of the terminal constant map to \(\mathbb R\), lifts through the covering \(\mathbb R\to S^1\) by the homotopy lifting property. Restricting the lifted homotopy to the initial time would give a lift of \(q\), contradicting §1.3, Exercise 7.

Therefore \(Y\) is weakly contractible but not contractible. If \(Y\) had the homotopy type of a CW complex \(K\), then \(K\) would also have all homotopy groups trivial, so Whitehead's theorem would make \(K\) contractible, hence \(Y\) contractible. Contradiction. Thus \(Y\) does not have CW homotopy type.
:::
