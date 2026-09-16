---
schema: qual/card@1
id: E-HAT-4.3-16
kind: problem
title: "Whitehead theorem via homotopy fiber"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 16; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that a map $f: X \to Y$ of connected CW complexes is a homotopy equivalence if it induces an isomorphism on $\pi_1$ and its homotopy fiber $F_f$ has $\tilde{H}_*(F_f; \mathbb{Z}) = 0$.
:::

::: {.solution}
Replace \(f:X\to Y\) by its mapping-path fibration
\[
F_f\longrightarrow E_f\xrightarrow{p}Y,
\]
where \(E_f\simeq X\). The hypothesis on \(\pi_1\) says
\[
\pi_1(E_f)\xrightarrow{\cong}\pi_1(Y).
\]
The long exact sequence therefore shows that
\[
\pi_1(F_f)\to\pi_1(E_f)
\]
is the zero homomorphism.

By Exercise 10, the usual action of \(\pi_1(F_f)\) on every \(\pi_n(F_f)\), including conjugation on \(\pi_1(F_f)\), factors through \(\pi_1(E_f)\). Hence this action is trivial. In particular \(\pi_1(F_f)\) is abelian. Since
\[
\widetilde H_1(F_f;\mathbb Z)=0,
\]
its abelianization is zero, so
\[
\pi_1(F_f)=0.
\]

Now \(F_f\) is simply connected and acyclic. If \(\pi_n(F_f)\ne0\) for a least \(n\ge2\), Hurewicz would give
\[
\pi_n(F_f)\cong H_n(F_f)=0,
\]
a contradiction. Thus all homotopy groups of \(F_f\) vanish. The homotopy fiber has CW type, so Whitehead gives
\[
F_f\simeq *.
\]
The fibration long exact sequence now shows that \(f\) induces isomorphisms on every homotopy group. Since \(X,Y\) are connected CW complexes,
\[
\boxed{f\text{ is a homotopy equivalence}.}
\]
:::
