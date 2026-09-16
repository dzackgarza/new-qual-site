---
schema: qual/card@1
id: E-HAT-4.F-3
kind: problem
title: "Homotopy colimit commutes with loop space"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.F, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that for any sequence $Z_1 \to Z_2 \to \cdots$, the natural map $\operatorname{hocolim} \Omega Z_n \to \Omega \operatorname{hocolim} Z_n$ is a weak homotopy equivalence, where the direct limits mean mapping telescopes.
:::

::: {.solution}
Let
\[
T=\operatorname{hocolim}(Z_1\to Z_2\to\cdots)
\]
be the mapping telescope, and let
\[
T_\Omega=\operatorname{hocolim}(\Omega Z_1\to\Omega Z_2\to\cdots).
\]
There is a natural map
\[
\kappa:T_\Omega\longrightarrow\Omega T
\]
obtained by regarding a loop in a stage \(Z_n\) as a loop in the corresponding slice of the telescope.

For every \(j\ge0\), compactness of \(S^j\) implies
\[
\pi_j(T_\Omega)
\cong\varinjlim_n\pi_j(\Omega Z_n).
\tag{1}
\]
Indeed, a map from a compact sphere into a telescope has image in a finite subtelescope, and a finite subtelescope deformation retracts onto its last stage. The same argument gives
\[
\pi_{j+1}(T)
\cong\varinjlim_n\pi_{j+1}(Z_n).
\tag{2}
\]
Using \(\pi_j(\Omega Z_n)=\pi_{j+1}(Z_n)\), equations (1) and (2) identify both sides with the same direct limit:
\[
\pi_j(T_\Omega)
\cong
\varinjlim_n\pi_{j+1}(Z_n)
\cong
\pi_j(\Omega T).
\]
Under these identifications, \(\kappa_*\) is the identity on the direct limit. This also gives the required bijection on path components when \(j=0\).

Hence \(\kappa\) induces isomorphisms on every homotopy group and a bijection on components. Therefore
\[
\boxed{\operatorname{hocolim}\Omega Z_n\longrightarrow
\Omega\operatorname{hocolim}Z_n\text{ is a weak homotopy equivalence}.}
\]
:::
