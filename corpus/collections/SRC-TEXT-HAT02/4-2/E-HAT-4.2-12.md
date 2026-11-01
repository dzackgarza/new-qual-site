---
schema: qual/card@1
id: E-HAT-4.2-12
kind: problem
title: "Whitehead theorem via universal covers"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 12; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Statement repaired against Hatcher's printed text: the card had dropped printed matter
    (a bracketed hint or pointer, or a printed sentence) that an audit located by word-by-word
    comparison with tmp/hat/AT.txt, and that this session re-verified at the cited lines before
    applying the repair. The restored text is the printed wording and the mathematics of the
    statement is otherwise unchanged.
---

::: {.problem}
Show that a map $f: X \to Y$ of connected CW complexes is a homotopy equivalence if it induces an isomorphism on $\pi_1$ and if a lift $\tilde{f}: \tilde{X} \to \tilde{Y}$ to the universal covers induces an isomorphism on homology. [The latter condition can be restated in terms of homology with local coefficients as saying that $f_*: H_*(X; \ZZ[\pi_1 X]) \to H_*(Y; \ZZ[\pi_1 Y])$ is an isomorphism; see §3.H.]
:::

::: {.solution}
Let
$$
f:X\to Y
$$
be as in the problem, and let
$$
\widetilde f:\widetilde X\to\widetilde Y
$$
be the chosen lift. The universal covers are simply connected CW complexes. By hypothesis $\widetilde f$ induces an isomorphism on integral homology in every degree. The homology version of Whitehead's theorem for simply connected CW complexes therefore implies
$$
\widetilde f\text{ is a homotopy equivalence}.
$$
Hence
$$
\widetilde f_*:\pi_i(\widetilde X)\xrightarrow{\cong}\pi_i(\widetilde Y)
\qquad(i\ge2).
$$
Covering maps induce isomorphisms on higher homotopy groups, so the commutative lifting square gives
$$
f_*:\pi_i(X)\xrightarrow{\cong}\pi_i(Y)
\qquad(i\ge2).
$$
By assumption $f_*$ is also an isomorphism on $\pi_1$, and connectedness gives the $\pi_0$ condition. Thus $f$ is a weak homotopy equivalence between CW complexes. Whitehead's theorem yields
$$
\boxed{f\text{ is a homotopy equivalence}.}
$$
:::
