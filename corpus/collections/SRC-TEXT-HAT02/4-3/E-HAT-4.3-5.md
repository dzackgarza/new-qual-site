---
schema: qual/card@1
id: E-HAT-4.3-5
kind: problem
title: "$[X, S^n] \\approx H^n(X; \\mathbb{Z})$ for $n$-dimensional $X$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 5; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that $[X, S^n] \approx H^n(X; \mathbb{Z})$ if $X$ is an $n$-dimensional CW complex.
:::

::: {.solution}
Choose a map
\[
j:S^n\to K(\mathbb Z,n)
\]
representing the generator of \(\pi_nK(\mathbb Z,n)\). It induces an isomorphism on \(\pi_i\) for \(i\le n\): both spaces have zero homotopy groups below \(n\), and \(j_*:\pi_n(S^n)\to\mathbb Z\) is an isomorphism.

If \(X\) is \(n\)-dimensional, obstruction theory or cellular induction says that an \(n\)-equivalence of targets induces a bijection
\[
j_*:[X,S^n]\xrightarrow{\cong}[X,K(\mathbb Z,n)].
\]
Indeed, maps and homotopies from an \(n\)-dimensional CW complex depend only on the homotopy groups of the target through degree \(n\).

Finally representability gives
\[
[X,K(\mathbb Z,n)]\cong H^n(X;\mathbb Z).
\]
Therefore
\[
\boxed{[X,S^n]\cong H^n(X;\mathbb Z).}
\]
:::
