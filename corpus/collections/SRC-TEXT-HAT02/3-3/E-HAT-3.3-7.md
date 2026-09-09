---
schema: qual/card@1
id: E-HAT-3.3-7
kind: problem
title: "Degree 1 maps to $S^n$"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 7; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

For a map $f: M \to N$ between connected closed orientable $n$-manifolds with fundamental classes $[M]$ and $[N]$, the degree of $f$ is defined to be the integer $d$ such that $f_*([M]) = d[N]$, so the sign of the degree depends on the choice of fundamental classes.
Show that for any connected closed orientable $n$-manifold $M$ there is a degree 1 map $M \to S^n$.

::: {.solution}
Choose an embedded closed $n$-ball $B\subset M$ whose interior is orientation-compatible with the chosen fundamental class $[M]$. Collapse the complement of the interior of $B$ to a point:
\[
q:M\longrightarrow M/(M-\operatorname{int}B).
\]
The quotient is naturally homeomorphic to
\[
B/\partial B\cong S^n.
\]
Choose the final homeomorphism $B/\partial B\to S^n$ to preserve orientation on the interior of $B$.

Let $f:M\to S^n$ be the resulting map. For a point $y$ in the image of $\operatorname{int}B$, the preimage $f^{-1}(y)$ consists of one point and $f$ is an orientation-preserving local homeomorphism there. By the local-degree formula, $\deg f=1$. Equivalently, the quotient map sends $[M]$ to the fundamental class of $B/\partial B$.

Thus every connected closed orientable $n$-manifold admits a degree-$1$ map to $S^n$.
:::
