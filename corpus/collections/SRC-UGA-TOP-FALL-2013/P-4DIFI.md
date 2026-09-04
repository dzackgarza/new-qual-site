---
schema: qual/card@1
id: P-4DIFI
kind: problem
title: Euler characteristic of a compact surface with $k$ boundary components is at
  most $2-k$
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Checked the statement against problem 3 of the official UGA Fall 2013 topology exam DOCX.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-04
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Verified the boundary-capping Euler-characteristic calculation and the reduction to the closed-surface classification theorem.
---

::: problem
Prove that the Euler characteristic of a compact surface with boundary which has $k$ boundary components is less than or equal to $2 - k$.
:::

::: {.solution}
<1>1. Use the compact-surface convention that a surface is connected, and let $S$ be the given compact surface with boundary components
\[
C_1,\dots,C_k.
\]
Cap each boundary component by a disk to obtain a closed connected surface
\[
\widehat S
=
S\cup_{C_1}D_1^2\cup\cdots\cup_{C_k}D_k^2.
\]
::: {.proof}
Each boundary component of a compact surface is a circle.
Gluing a copy of $D^2$ to each boundary circle removes all boundary components and does not disconnect the surface, so $\widehat S$ is a closed connected compact surface.

The connectedness convention matters here: if disconnected $2$-manifolds were allowed under the word ``surface,'' the stated inequality would not hold in general; for example, the disjoint union of two disks has $k=2$ and Euler characteristic $2$.
:::

<1>2. Capping the $k$ boundary circles increases Euler characteristic by $k$:
\[
\chi(\widehat S)=\chi(S)+k.
\]
::: {.proof}
Compact surfaces admit finite CW structures for which the boundary circles are subcomplexes.
For finite CW complexes, Euler characteristic satisfies
\[
\chi(A\cup B)
=
\chi(A)+\chi(B)-\chi(A\cap B)
\]
when the intersection is a subcomplex.

Attaching one capping disk gives
\[
\chi(S\cup_{S^1}D^2)
=
\chi(S)+\chi(D^2)-\chi(S^1)
=
\chi(S)+1-0
=
\chi(S)+1.
\]
Applying this successively to the $k$ boundary components yields
\[
\chi(\widehat S)=\chi(S)+k.
\]
:::

<1>3. Every closed connected compact surface has Euler characteristic at most $2$.
::: {.proof}
By the classification theorem for compact surfaces, a closed connected surface is either

- orientable of genus $g\ge0$, with
  \[
  \chi=2-2g\le2,
  \]
  or

- nonorientable of genus $h\ge1$, with
  \[
  \chi=2-h\le1<2.
  \]

Therefore
\[
\chi(\widehat S)\le2.
\]
:::

<1>4. Hence
\[
\boxed{\chi(S)\le2-k}.
\]
::: {.proof}
By <1>2,
\[
\chi(S)=\chi(\widehat S)-k.
\]
Using <1>3 gives
\[
\chi(S)
\le
2-k,
\]
as required.
:::
:::
