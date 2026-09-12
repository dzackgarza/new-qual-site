---
schema: qual/card@1
id: E-KADOC
kind: problem
title: Coverings over simply connected bases are homeomorphisms
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}

Let $p: E \to B$ be a covering map, with $E$ path connected.
Show that if $B$ is simply connected, then $p$ is a homeomorphism.
:::

::: {.solution}
Fix \(e_0\in E\), and let \(b_0=p(e_0)\). We show that every fiber of \(p\) has one point.

Let \(e_1\in p^{-1}(b_0)\). Since \(E\) is path connected, choose a path \(\widetilde\alpha\) in \(E\) from \(e_0\) to \(e_1\). Then \(\alpha=p\circ\widetilde\alpha\) is a loop in \(B\) at \(b_0\). Because \(B\) is simply connected, \(\alpha\) is path homotopic to the constant loop at \(b_0\). The homotopy-lifting theorem says that lifts of path-homotopic loops beginning at the same point have the same endpoint. The constant loop lifts to the constant path at \(e_0\), while \(\widetilde\alpha\) is the lift of \(\alpha\) beginning at \(e_0\). Therefore \(e_1=e_0\). Thus \(p^{-1}(b_0)=\{e_0\}\).

The same argument applies to every fiber, since \(E\) is path connected. Hence \(p\) is bijective. A covering map is a local homeomorphism, so it is open; a bijective open continuous map is a homeomorphism. Therefore \(p:E\to B\) is a homeomorphism.
:::
