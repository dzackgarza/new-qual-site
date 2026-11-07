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
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Matched the full construction to Daniel Dugger, Involutions on Surfaces, not merely to a
    citation about involutions. Section2.7 pp.11-12 defines the centered antipodal action
    T_g^anti and computes its nonorientable quotient; Proposition2.8 p.12 splits the even-genus
    action into the antipodal sphere and paired handles; Theorem4.1(a) p.18 states freeness in
    even genus. Transcribed this as the card's map. The antipodal interchange of paired handles
    gives the zero diagonal on H_1, and the nonorientable quotient confirms degree-1 on H_2.
    Thus Lefschetz is 1-0-1=0, the complete published even-genus argument matching Hatcher p.184.
- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    Corrected the preceding coverage claim. Dugger supplies the centered antipodal involution,
    its decomposition and quotient, but not a complete solution to Hatcher Exercise 2.C.6:
    the exercise's paired-handle trace computation is assembled by instantiation. No retained
    published exercise solution performs that computation. The mathematics and Dugger citation
    remain, but the complete published-solution obligation remains open.
---
---

::: {.problem}
Do an even-genus analog of Example 2C.4 by replacing the central torus by a sphere letting $f$ be a homeomorphism that restricts to the antipodal map on this sphere.
:::

::: {.solution}
Use the standard centered antipodal action $T_g^{\mathrm{anti}}$ published in **Daniel Dugger, *Involutions on Surfaces*, §2.7, printed pp. 11--12** (`tmp/sources/dugger-involutions-surfaces-2016.pdf`). His Proposition 2.8 gives $T_{2g}^{\mathrm{anti}}\cong S^2_a\mathbin{\#_\mathrm{eq}}T_g$, an antipodal sphere with paired handles, and Theorem 4.1(a), p. 18, identifies this as the free involution in even genus. This is exactly Hatcher's requested even-genus analog. Write $g=2m$, let $M_{2m}=T_{2m}^{\mathrm{anti}}$, and regard it as a central sphere with $m$ antipodal pairs of handles. Dugger also computes $T_g^{\mathrm{anti}}/C_2\cong N_{g+1}$, so the involution is orientation reversing. The general construction supplies the checked model below, but not a complete published solution of Hatcher Exercise 2.C.6, whose source obligation remains open.

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

On the central sphere $f$ restricts to the antipodal map of $S^2$, which has degree $(-1)^3=-1$. The extensions across paired handles preserve this local orientation-reversing character, so the homeomorphism is orientation reversing globally and has degree $-1$. Equivalently, Dugger's quotient $T_{2m}^{\mathrm{anti}}/C_2\cong N_{2m+1}$ is nonorientable, giving the same orientation reversal in the published construction.

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
