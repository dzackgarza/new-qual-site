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
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §2.C Exercise 6, printed page
    184, which asks for an even-genus analog of Example 2C.4 (genus 3, p. 181) with
    the central torus replaced by a sphere and f the antipodal map there; the card's
    statement matches. Proof checked: attaching handles in m antipodal pairs with
    matching parametrizations gives a fixed-point-free homeomorphism of the genus 2m
    surface; f_* swaps the rank-two summands of H_1 pairwise, so its trace is 0; and
    on H_2 = Z it is the antipodal map of S^2, of degree -1 (Proposition 2.30,
    p. 134). Then tau(f) = 1 - 0 - 1 = 0, as the fixed-point-free map requires. No
    defect.
---
---

::: {.problem}
Do an even-genus analog of Example 2C.4 by replacing the central torus by a sphere letting $f$ be a homeomorphism that restricts to the antipodal map on this sphere.
:::

::: {.solution}
Let the desired genus be $2m$. Realize the surface $M_{2m}$ as a central sphere with $m$ symmetric pairs of handles attached in antipodal pairs.

::: pf

::: pf-step

Define a homeomorphism $f:M_{2m}\to M_{2m}$ by the antipodal map on the central sphere and by interchanging the two handles in each antipodal pair.

::: pf-proof

Choose the attaching disks in antipodal pairs and attach each pair of handles by identical parametrizations. The antipodal map carries the attaching data of one handle to that of its partner, so it extends across the handles by swapping each pair. The resulting map is a homeomorphism.

:::

:::

::: pf-step

The map $f$ has no fixed points.

::: pf-proof

The antipodal map has no fixed point on the central sphere. Every point in an attached handle is carried into the distinct partner handle. Hence no point of the whole surface is fixed.

:::

:::

::: {.pf-step #s3}

On $H_1(M_{2m};\ZZ)$, the map $f_*$ has trace zero.

::: pf-proof

Choose the standard two generators on each handle. The handles occur in $m$ pairs, and $f_*$ swaps the two corresponding rank-two summands for each pair. Relative to this basis the matrix has zero diagonal, so its trace is zero.

:::

:::

::: {.pf-step #s4}

On $H_2(M_{2m};\ZZ)\cong\ZZ$, the map $f_*$ is multiplication by $-1$.

::: pf-proof

On the central sphere $f$ restricts to the antipodal map of $S^2$, which has degree $(-1)^3=-1$. The extensions across paired handles preserve this local orientation-reversing character, so the homeomorphism is orientation reversing globally and has degree $-1$.

:::

:::

::: pf-step

Consequently
$$
\tau(f)=1-0+(-1)=0,
$$
as required by the Lefschetz theorem for a fixed-point-free map.

::: pf-proof

The trace on $H_0$ is $1$ because the surface is connected, step [](#s3){.pf-ref} gives the $H_1$ trace, and step [](#s4){.pf-ref} gives the $H_2$ trace.

:::

:::

:::

This gives the even-genus counterpart of Example 2C.4. Additional symmetric pairs of handles increase the genus by two without introducing fixed points.
:::
