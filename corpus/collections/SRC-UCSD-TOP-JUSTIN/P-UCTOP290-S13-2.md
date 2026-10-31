---
schema: qual/card@1
id: P-UCTOP290-S13-2
kind: problem
title: Canonical orientation of the orientation double cover
classification:
  areas:
  - topology
  topics:
  - Manifolds
  - Covering Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 13, Problem 2 in its checked-in extraction.
---

::: {.problem}
Show that the orientation double cover
$\widetilde M\to M$ of a manifold $M$ is orientable.
Show that it has a canonical orientation.
:::

::: {.solution}

A point of $\widetilde M$ is a pair $(x,o_x)$, where $x\in M$
and $o_x$ is one of the two local orientations at $x$.
At an interior point these are the two generators of
$$
H_n(M,M\setminus\{x\};\ZZ)\cong\ZZ.
$$
At a boundary point, use a collar to extend a local
orientation from the interior; the two choices extend
uniquely to the boundary point.
Over an evenly covered coordinate ball $U$, the two sheets
correspond to the two continuous choices of local orientation
on $U$.

At $(x,o_x)$, choose the local orientation of $\widetilde M$
that maps to $o_x$ under the local homeomorphism
$p:\widetilde M\to M$. This choice varies continuously on each
sheet over $U$, because that sheet was defined by a continuous
choice of local orientation on $U$. It therefore gives a global
orientation of $\widetilde M$.

The construction uses only the specified point $(x,o_x)$ and
the covering projection. It makes $p$ orientation-preserving
at every point with respect to the chosen local orientation
there. Hence the orientation is canonical. The deck
involution $(x,o_x)\mapsto(x,-o_x)$ reverses it.

:::
