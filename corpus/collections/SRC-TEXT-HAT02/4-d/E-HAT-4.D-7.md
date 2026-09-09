---
schema: qual/card@1
id: E-HAT-4.D-7
kind: problem
title: "Thom class implies orientability"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.D, Exercise 7; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Show that if a disk bundle $D^n \to E \to B$ has a Thom class with $\mathbb{Z}$ coefficients, then it is orientable.

::: {.solution}
Let
\[
(D^n,S^{n-1})\longrightarrow(E,E')\longrightarrow B
\]
be the disk-bundle pair and let
\[
c\in H^n(E,E';\mathbb Z)
\]
be a Thom class. For each \(b\in B\), its restriction
\[
c_b\in H^n(D_b^n,S_b^{n-1};\mathbb Z)\cong\mathbb Z
\]
is a generator, hence determines an orientation of the fiber.

Let \(\gamma\) be a path in \(B\). Fiber transport along \(\gamma\) gives a homotopy equivalence of pairs
\[
L_\gamma:(D^n_{\gamma(0)},S^{n-1}_{\gamma(0)})
\longrightarrow(D^n_{\gamma(1)},S^{n-1}_{\gamma(1)}).
\]
Since \(c\) is one global relative cohomology class, naturality of restriction gives
\[
L_\gamma^*(c_{\gamma(1)})=c_{\gamma(0)}.
\]
Thus every transport map preserves the chosen generator of the top relative cohomology, so it has degree \(+1\). In particular transport around every loop preserves orientation. Therefore the bundle is orientable:
\[
\boxed{\text{an integral Thom class forces orientability}.}
\]
:::
