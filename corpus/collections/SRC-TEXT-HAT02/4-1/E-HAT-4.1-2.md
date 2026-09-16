---
schema: qual/card@1
id: E-HAT-4.1-2
kind: problem
title: "Functoriality of $\\pi_n$ under homotopy equivalence"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

---

::: {.problem}
Show that if $\varphi: X \to Y$ is a homotopy equivalence, then the induced homomorphisms $\varphi_*: \pi_n(X, x_0) \to \pi_n(Y, \varphi(x_0))$ are isomorphisms for all $n$.
:::

::: {.solution}
Let \(\varphi:X\to Y\) be a homotopy equivalence, with homotopy inverse \(\psi:Y\to X\). Choose a path \(\eta\) from \(x_0\) to \(\psi\varphi(x_0)\) supplied by the homotopy \(\psi\varphi\simeq\operatorname{id}_X\). Naturality of homotopy groups under a homotopy gives
\[
\beta_\eta\circ(\psi\varphi)_*=\operatorname{id}_{\pi_n(X,x_0)},
\]
where \(\beta_\eta\) is the appropriate change-of-basepoint isomorphism. Similarly, from \(\varphi\psi\simeq\operatorname{id}_Y\) one gets a change-of-basepoint isomorphism making \(\varphi_*\psi_*\) the identity.

Thus \(\varphi_*\) has a two-sided inverse after the canonical basepoint changes. In particular
\[
\boxed{\varphi_*:\pi_n(X,x_0)\xrightarrow{\cong}\pi_n(Y,\varphi(x_0))}
\]
for every \(n\ge1\). (For \(n=0\), the same argument says that a homotopy equivalence induces a bijection on path components.)
:::
