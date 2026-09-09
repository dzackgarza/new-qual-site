---
schema: qual/card@1
id: E-HAT-2.2-23
kind: problem
title: If $M_g$ covers $M_h$ then $g = n(h-1)+1$
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - Covering Spaces
  - Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 23; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete cellular/Euler-characteristic computation checked.
---

Show that if the closed orientable surface $M_g$ of genus $g$ is a covering space of $M_h$, then $g = n(h-1)+1$ for some $n$, namely, $n$ is the number of sheets in the covering.
[Conversely, if $g = n(h-1)+1$ then there is an $n$ sheeted covering $M_g \to M_h$, as we saw in Example 1.41.]

::: {.solution}
For a closed orientable surface $M_g$ of genus $g$,
\[
\chi(M_g)=2-2g.
\]
Suppose
\[
p:M_g\to M_h
\]
is an $n$-sheeted covering. By Exercise 22,
\[
\chi(M_g)=n\chi(M_h).
\]
Hence
\[
2-2g=n(2-2h).
\]
Dividing by $-2$ gives
\[
g-1=n(h-1),
\]
so
\[
\boxed{g=n(h-1)+1}.
\]
The integer $n$ is exactly the number of sheets of the covering.
:::
