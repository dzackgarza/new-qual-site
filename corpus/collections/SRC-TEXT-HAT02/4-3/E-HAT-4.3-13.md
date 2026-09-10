---
schema: qual/card@1
id: E-HAT-4.3-13
kind: problem
title: "Pre-composing with homotopy equivalence"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 13; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Given a map $f: A \to B$ and a homotopy equivalence $g: C \to A$, show that the fibrations $E_f \to B$ and $E_{fg} \to B$ are fiber homotopy equivalent.

::: {.solution}
Let \(g:C\to A\) be a homotopy equivalence with homotopy inverse \(h:A\to C\), and choose homotopies
\[
gh\simeq1_A,
\qquad
hg\simeq1_C.
\]
There is an evident fiber-preserving map
\[
\Phi:E_{fg}\to E_f,
\qquad
(c,\gamma)\longmapsto(g(c),\gamma).
\]

For the reverse direction, use a chosen homotopy \(K:gh\simeq1_A\). For \((a,\gamma)\in E_f\), the path
\[
t\longmapsto f(K(a,t))
\]
runs from \(f(gh(a))\) to \(f(a)\). Prepending it to \(\gamma\) defines a fiber-preserving map
\[
\Psi:E_f\to E_{fg},
\qquad
\Psi(a,\gamma)=\bigl(h(a),fK_a*\gamma\bigr).
\]
The homotopies \(gh\simeq1_A\) and \(hg\simeq1_C\), together with contraction of the resulting backtracking paths, give fiber-preserving homotopies
\[
\Phi\Psi\simeq1_{E_f},
\qquad
\Psi\Phi\simeq1_{E_{fg}}.
\]
Thus
\[
\boxed{E_f\to B\simeq_f E_{fg}\to B.}
\]
:::
