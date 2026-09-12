---
schema: qual/card@1
id: E-PTY7A
kind: problem
title: Projection from a product with a discrete space is a covering map
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
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

Let $Y$ have the discrete topology.
Show that if $p: X \times Y \to X$ is projection on the first coordinate, then $p$ is a covering map.
:::

::: {.solution}
Fix \(x\in X\) and let \(U\) be any open neighborhood of \(x\) (for example \(U=X\)). Since \(Y\) is discrete, every singleton \(\{y\}\) is open, and
\[
p^{-1}(U)=U\times Y=\bigsqcup_{y\in Y}(U\times\{y\}).
\]
Each \(U\times\{y\}\) is open in \(X\times Y\), and the restriction
\[
p|_{U\times\{y\}}:U\times\{y\}\longrightarrow U
\]
is a homeomorphism with inverse \(u\mapsto(u,y)\). Thus every open \(U\) is evenly covered; in particular \(p:X\times Y\to X\) is a covering map.
:::
