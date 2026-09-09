---
schema: qual/card@1
id: P-VXX34
kind: problem
title: The stabilizer of a point under a group action is a subgroup
classification:
  areas:
  - algebra
  topics:
  - Orbit-Stabilizer
  - Subgroups
  - Group Actions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Show that if $G \curvearrowright X$ is a group action, then the stabilizer $G_x = \operatorname{Stab}_G(x)$ of any point $x \in X$ is a subgroup of $G$.
:::

::: solution
By definition,
\[
G_x=\{g\in G:g\cdot x=x\}.
\]
The identity lies in $G_x$ because $e\cdot x=x$. If $g,h\in G_x$, then
\[
(gh^{-1})\cdot x
=g\cdot(h^{-1}\cdot x)
=g\cdot x
=x,
\]
because $h\cdot x=x$ implies $h^{-1}\cdot x=x$. Thus $gh^{-1}\in G_x$.
By the subgroup criterion, $G_x\le G$.
:::
