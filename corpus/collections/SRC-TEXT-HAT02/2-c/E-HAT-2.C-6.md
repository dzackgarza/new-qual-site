---
schema: qual/card@1
id: E-HAT-2.C-6
kind: problem
title: 'Even-genus analog of Lefschetz example: replace central torus by sphere with antipodal map'
classification:
  areas:
  - topology
  topics:
  - Lefschetz Fixed Point Theorem
  - Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.C, Exercise 6; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the simplicial, Lefschetz-trace, or surface argument against the preceding section results.
---

::: {.problem}
Do an even-genus analog of Example 2C.4 by replacing the central torus by a sphere letting $f$ be a homeomorphism that restricts to the antipodal map on this sphere.
:::

::: {.solution}
Let the desired genus be $2m$. Realize the surface $M_{2m}$ as a central sphere with $m$ symmetric pairs of handles attached in antipodal pairs.

<1>1. Define a homeomorphism $f:M_{2m}\to M_{2m}$ by the antipodal map on the central sphere and by interchanging the two handles in each antipodal pair.
::: {.proof}
Choose the attaching disks in antipodal pairs and attach each pair of handles by identical parametrizations. The antipodal map carries the attaching data of one handle to that of its partner, so it extends across the handles by swapping each pair. The resulting map is a homeomorphism.
:::

<1>2. The map $f$ has no fixed points.
::: {.proof}
The antipodal map has no fixed point on the central sphere. Every point in an attached handle is carried into the distinct partner handle. Hence no point of the whole surface is fixed.
:::

<1>3. On $H_1(M_{2m};\mathbb Z)$, the map $f_*$ has trace zero.
::: {.proof}
Choose the standard two generators on each handle. The handles occur in $m$ pairs, and $f_*$ swaps the two corresponding rank-two summands for each pair. Relative to this basis the matrix has zero diagonal, so its trace is zero.
:::

<1>4. On $H_2(M_{2m};\mathbb Z)\cong\mathbb Z$, the map $f_*$ is multiplication by $-1$.
::: {.proof}
On the central sphere $f$ restricts to the antipodal map of $S^2$, which has degree $(-1)^3=-1$. The extensions across paired handles preserve this local orientation-reversing character, so the homeomorphism is orientation reversing globally and has degree $-1$.
:::

<1>5. Consequently
\[
\tau(f)=1-0+(-1)=0,
\]
as required by the Lefschetz theorem for a fixed-point-free map.
::: {.proof}
The trace on $H_0$ is $1$ because the surface is connected, <1>3 gives the $H_1$ trace, and <1>4 gives the $H_2$ trace.
:::

This gives the even-genus counterpart of Example 2C.4. Additional symmetric pairs of handles increase the genus by two without introducing fixed points.
:::
