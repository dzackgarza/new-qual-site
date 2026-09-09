---
schema: qual/card@1
id: E-HAT-4.3-12
kind: problem
title: "Homotopic maps give fiber homotopy equivalent fibrations"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 12; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Show that for homotopic maps $f, g: A \to B$ the fibrations $E_f \to B$ and $E_g \to B$ are fiber homotopy equivalent.

::: {.solution}
Recall the mapping-path fibration
\[
E_f=\{(a,\gamma):\gamma(0)=f(a)\},
\qquad
p_f(a,\gamma)=\gamma(1).
\]
Let \(H:A\times I\to B\) be a homotopy from \(f\) to \(g\), and write \(H_a(t)=H(a,t)\). Define
\[
\Phi:E_f\to E_g,
\qquad
\Phi(a,\gamma)=(a,\overline{H_a}*\gamma),
\]
where \(\overline{H_a}\) is the reverse path from \(g(a)\) to \(f(a)\). This is fiber-preserving because the endpoint of the concatenated path is the endpoint of \(\gamma\).

Using \(H_a\) instead gives
\[
\Psi:E_g\to E_f.
\]
The composites prepend the backtracking paths
\[
H_a*\overline{H_a}
\quad\text{or}\quad
\overline{H_a}*H_a.
\]
Contract these backtracking paths to the constant path by the standard reparametrization homotopy. This produces fiber-preserving homotopies
\[
\Psi\Phi\simeq1_{E_f},
\qquad
\Phi\Psi\simeq1_{E_g}.
\]
Hence
\[
\boxed{E_f\to B\text{ and }E_g\to B\text{ are fiber homotopy equivalent}.}
\]
:::
