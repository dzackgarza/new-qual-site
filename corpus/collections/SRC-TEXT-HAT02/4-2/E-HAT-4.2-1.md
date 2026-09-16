---
schema: qual/card@1
id: E-HAT-4.2-1
kind: problem
title: "No retraction $\\mathbb{RP}^n \\to \\mathbb{RP}^k$ via homotopy groups"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

---

::: {.problem}
Use homotopy groups to show there is no retraction $\mathbb{RP}^n \to \mathbb{RP}^k$ if $n > k > 0$.
:::

::: {.solution}
Suppose there were a retraction
\[
r:\mathbb{RP}^n\to\mathbb{RP}^k,
\qquad n>k>0,
\]
of the standard inclusion \(i:\mathbb{RP}^k\hookrightarrow\mathbb{RP}^n\). Then
\[
r_*i_*=\operatorname{id}
\]
on every homotopy group, so \(i_*\) would be injective.

If \(k\ge2\), covering-space invariance of higher homotopy groups gives
\[
\pi_k(\mathbb{RP}^k)\cong\pi_k(S^k)\cong\mathbb Z,
\]
whereas, since \(k<n\),
\[
\pi_k(\mathbb{RP}^n)\cong\pi_k(S^n)=0.
\]
Thus \(i_*:\mathbb Z\to0\) cannot be injective.

If \(k=1\), then \(\mathbb{RP}^1\cong S^1\), so
\[
\pi_1(\mathbb{RP}^1)\cong\mathbb Z,
\qquad
\pi_1(\mathbb{RP}^n)\cong\mathbb Z_2
\quad(n>1).
\]
Again no injection \(\mathbb Z\hookrightarrow\mathbb Z_2\) exists.

Therefore
\[
\boxed{\mathbb{RP}^n\text{ does not retract onto }\mathbb{RP}^k\text{ for }n>k>0.}
\]
:::
