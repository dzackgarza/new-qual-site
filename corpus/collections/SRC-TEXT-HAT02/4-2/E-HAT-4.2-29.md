---
schema: qual/card@1
id: E-HAT-4.2-29
kind: problem
title: "Homotopy classification of lens spaces"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 29; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Finish the homotopy classification of lens spaces begun in Exercise 2 of §3.E by showing that two lens spaces $L_m(\ell_1, \ldots, \ell_n)$ and $L_m(\ell_1', \ldots, \ell_n')$ are homotopy equivalent if $\ell_1 \cdots \ell_n \equiv \pm k^n \ell_1' \cdots \ell_n' \pmod{m}$ for some integer $k$.
:::

::: {.solution}
Put
\[
P=\ell_1\cdots\ell_n,
\qquad
P'=\ell_1'\cdots\ell_n'.
\]
Assume
\[
P\equiv \pm k^nP'\pmod m.
\]
Since \(P\) and \(P'\) are units modulo \(m\), so is \(k\). Replacing the chosen generator of the \(\mathbb Z_m\)-action on the target by its \(k\)-th power replaces every \(\ell_j'\) by \(k\ell_j'\) without changing the lens space. Thus we may reduce to the case
\[
P\equiv\pm P'\pmod m.
\]

Choose nonzero integers \(k_j\) satisfying
\[
k_j\ell_j\equiv\ell_j'\pmod m.
\]
Exercise 2 of §3.E constructs an equivariant map of universal covers and hence a map
\[
f:L_m(\ell_1,\dots,\ell_n)\to L_m(\ell_1',\dots,\ell_n')
\]
that induces an isomorphism on \(\pi_1\) and has degree
\[
d_0=k_1\cdots k_n.
\]
Modulo \(m\),
\[
d_0P\equiv P',
\]
so the reduced congruence gives
\[
d_0\equiv\pm1\pmod m.
\]
Choose \(d\in\mathbb Z\) with
\[
d_0+dm=\pm1.
\]

Modify \(f\) inside a small ball in the source as follows. Pinch that ball to add an \(S^{2n-1}\)-summand, map this new sphere to \(S^{2n-1}\) with degree \(d\), then compose with the \(m\)-sheeted covering
\[
S^{2n-1}\to L_m(\ell_1',\dots,\ell_n').
\]
The resulting map \(g\) agrees with \(f\) on the \(1\)-skeleton, so it induces the same isomorphism on \(\pi_1\), while its degree is
\[
\deg g=d_0+dm=\pm1.
\]

Lift \(g\) to universal covers. Since the covering maps on both sides have degree \(m\), the lift
\[
\widetilde g:S^{2n-1}\to S^{2n-1}
\]
has degree \(\pm1\), hence is a homotopy equivalence. Therefore \(g\) induces isomorphisms on all higher homotopy groups as well as on \(\pi_1\). Lens spaces are CW complexes, so Whitehead's theorem gives
\[
\boxed{L_m(\ell_1,\dots,\ell_n)\simeq L_m(\ell_1',\dots,\ell_n').}
\]
This proves the converse and completes the classification.
:::
