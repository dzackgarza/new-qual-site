---
schema: qual/card@1
id: E-HAT-4.1-6
kind: problem
title: "Covering spaces and relative homotopy groups"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 6; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

---

::: {.problem}
If $p: (\tilde{X}, \tilde{A}, \tilde{x}_0) \to (X, A, x_0)$ is a covering space with $\tilde{A} = p^{-1}(A)$, show that the map $p_*: \pi_n(\tilde{X}, \tilde{A}, \tilde{x}_0) \to \pi_n(X, A, x_0)$ is an isomorphism for all $n > 1$.
:::

::: {.solution}
Represent an element of \(\pi_n(X,A,x_0)\), \(n>1\), by a map of triples
\[
f:(D^n,S^{n-1},s_0)\longrightarrow(X,A,x_0).
\]
Since \(D^n\) is simply connected, \(f\) has a unique lift
\[
\widetilde f:(D^n,s_0)\longrightarrow(\widetilde X,\widetilde x_0).
\]
Because \(f(S^{n-1})\subset A\), we have
\[
\widetilde f(S^{n-1})\subset p^{-1}(A)=\widetilde A.
\]
Thus \(\widetilde f\) represents a class in \(\pi_n(\widetilde X,\widetilde A,\widetilde x_0)\), proving surjectivity of \(p_*\).

If two lifted maps become relatively homotopic after applying \(p\), the relative homotopy
\[
F:(D^n\times I,S^{n-1}\times I,\{s_0\}\times I)\to(X,A,x_0)
\]
has a unique lift after fixing its value at \((s_0,0)\). Uniqueness of lifting makes its two ends the prescribed lifted maps, and its boundary remains in \(p^{-1}(A)\). Hence the two lifted maps were already relatively homotopic.

Therefore
\[
\boxed{p_*:\pi_n(\widetilde X,\widetilde A,\widetilde x_0)\xrightarrow{\cong}\pi_n(X,A,x_0)}
\qquad(n>1).
\]
:::
