---
schema: qual/card@1
id: E-MUN-2-3
kind: problem
title: Preimage and image for arbitrary unions and intersections
classification:
  areas:
  - topology
  topics:
  - Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 2, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Show that (b), (c), (f), and (g) of Exercise 2 hold for arbitrary unions and intersections.
:::

::: {.solution}
Let \(\{B_i\}_{i\in I}\) be subsets of \(B\) and \(\{A_i\}_{i\in I}\) subsets of \(A\).

Preimages commute with arbitrary unions:
\[
\begin{aligned}
x\in f^{-1}\!\left(\bigcup_i B_i\right)
&\iff f(x)\in B_i\text{ for some }i\\
&\iff x\in\bigcup_i f^{-1}(B_i).
\end{aligned}
\]
Hence
\[
f^{-1}\!\left(\bigcup_iB_i\right)=\bigcup_i f^{-1}(B_i).
\]
Similarly,
\[
f^{-1}\!\left(\bigcap_iB_i\right)=\bigcap_i f^{-1}(B_i).
\]

Images commute with arbitrary unions:
\[
f\!\left(\bigcup_i A_i\right)=\bigcup_i f(A_i).
\]
For intersections one always has
\[
f\!\left(\bigcap_i A_i\right)\subset\bigcap_i f(A_i),
\]
since a point of the common domain intersection maps into every \(f(A_i)\). Equality can fail for noninjective \(f\), exactly as in Exercise 2(g). If \(f\) is injective and the index set is nonempty, equality holds: if \(y\in\bigcap_i f(A_i)\), then for each \(i\) there is \(a_i\in A_i\) with \(f(a_i)=y\); injectivity forces all \(a_i\) to be the same point, lying in \(\bigcap_iA_i\).
:::
