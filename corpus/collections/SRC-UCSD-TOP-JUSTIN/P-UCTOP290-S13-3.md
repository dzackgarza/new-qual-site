---
schema: qual/card@1
id: P-UCTOP290-S13-3
kind: problem
title: A compact manifold cannot retract to its boundary
classification:
  areas:
  - topology
  topics:
  - Manifolds
  - Homology
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 13, Problem 3 in its checked-in extraction.
---

::: {.problem}
Show that a compact manifold cannot retract to its boundary.
:::

::: {.solution}

Let $M$ be a nonempty compact $n$-manifold with nonempty
boundary, and work with $\ZZ/2$ coefficients so no orientation
assumption is needed. The relative fundamental class
$$
[M,\partial M]\in H_n(M,\partial M;\ZZ/2)
$$
is nonzero. The boundary map in the long exact sequence of the
pair sends it to
$$
\partial[M,\partial M]
=[\partial M]\in H_{n-1}(\partial M;\ZZ/2).
$$
This boundary class is nonzero: on every boundary component
it is that component's fundamental class. Exactness gives
$$
i_*[\partial M]=0
\quad\text{in }H_{n-1}(M;\ZZ/2),
$$
where $i:\partial M\hookrightarrow M$ is inclusion.

If a retraction $r:M\to\partial M$ existed, then
$r\circ i=\operatorname{id}_{\partial M}$, so $i_*$ would be
injective. This contradicts the nonzero boundary class in
its kernel, whether or not $M$ is connected.

:::
