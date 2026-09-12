---
schema: qual/card@1
id: E-HAT-3.3-9
kind: problem
title: "Degree of covering space projections"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 9; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Show that a $p$-sheeted covering space projection $M \to N$ has degree $\pm p$, when $M$ and $N$ are connected closed orientable manifolds.

::: {.solution}
Let $p:M\to N$ be a $p$-sheeted covering between connected closed orientable $n$-manifolds. Choose an evenly covered ball $B\subset N$. Its inverse image is a disjoint union of $p$ balls
\[
p^{-1}(B)=B_1\amalg\cdots\amalg B_p,
\]
each mapped homeomorphically to $B$.

For each $i$, let $\varepsilon_i=\pm1$ be the local orientation sign of $p|_{B_i}$. Since $M$ and $N$ are connected and a covering map is locally a homeomorphism, the local sign is locally constant on $M$ and therefore constant. Thus all $\varepsilon_i$ equal a common sign $\varepsilon$.

By Exercise 8's local-degree formula,
\[
\deg p=\sum_{i=1}^p\varepsilon_i=p\varepsilon.
\]
Hence
\[
\boxed{\deg p=\pm p.}
\]
:::
