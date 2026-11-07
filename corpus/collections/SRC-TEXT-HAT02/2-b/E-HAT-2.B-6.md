---
schema: qual/card@1
id: E-HAT-2.B-6
kind: problem
title: "Alexander horned sphere with non-simply-connected complement"
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.B, Exercise 6; the stored statement matches and the construction was compared with Hatcher's preceding Alexander-horned-sphere example.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the local van Kampen injections and the free-group bonding maps for the horned constructions.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §2.B Exercise 6, printed page
    176; the statement matches word for word. Checked: the construction localises the
    Alexander horned sphere (Example 2B.2, p. 170) in two disjoint small balls, one on
    each side of a round sphere and each meeting it in a tame disk, so each
    complementary domain acquires a copy of the wild fundamental group and neither is
    simply connected. No defect.
- event: solution-written
  by: claude
  date: 2026-11-08
  note: >-
    Replaces the local double-horn construction with the published example itself. Alexander,
    Proc. Nat. Acad. Sci. 10 (1924), pp.9-10, constructs the solid horned sphere and observes
    that its exterior is not simply connected. Bing, Examples and Counterexamples, Pi Mu Epsilon
    Journal 1 (1953), p.316, glues two reflected solid horned spheres along their common
    boundary to obtain S^3. Deleting a boundary point leaves an S^2 in R^3 whose two
    complementary components are the two non-simply-connected exteriors. This is a complete
    published route, not a citation added to the previous local construction.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Read both printed sources. Alexander's limiting surface is genus zero and its exterior has
    infinite fundamental group; Bing explicitly says that the interiors of his two solid horned
    spheres are not simply connected and that their union is S^3. Removing a single boundary
    point therefore gives precisely the requested embedding, without claiming that the bounded
    or unbounded side of the usual Alexander sphere is the tame side.
---
---

::: {.problem}
Modify the construction of the Alexander horned sphere to produce an embedding $S^2 \hookrightarrow \RR^3$ for which neither component of $\RR^3 - S^2$ is simply-connected.
:::

::: {.solution}
Use **J. W. Alexander, *An Example of a Simply Connected Surface Bounding a Region which is not Simply Connected*, pp. 9--10** (`tmp/sources/alexander-horned-sphere-1924.pdf`) and **R. H. Bing, *Examples and Counterexamples*, Pi Mu Epsilon Journal 1 (1953), p. 316** (`tmp/sources/bing-examples-counterexamples-1953.pdf`).

::: pf

::: {.pf-step #alexander}
Alexander's construction produces a solid horned sphere whose boundary is a genuine $2$-sphere and whose exterior is not simply connected.

::: pf-proof
Alexander builds a sequence of approximating surfaces by attaching successively smaller interlocking tubes. The limiting surface has genus zero and no singularities. Its exterior nevertheless contains a loop nearly coinciding with the boundary of one of the cells that cannot be deformed to a point in that exterior; in fact, its fundamental group requires infinitely many generators.
:::

:::

::: {.pf-step #double}
Glue two reflected copies of Alexander's solid horned sphere along their common boundary. The result is $S^3$, and neither complementary domain of the boundary sphere is simply connected.

::: pf-proof
This is Bing's reflected pair in the passage cited above. Each of the two solid horned spheres has a non-simply-connected interior by Alexander's construction. Their union is $S^3$, and the common boundary is homeomorphic to $S^2$.
:::

:::

::: {.pf-step #puncture}
Deleting a point of the common boundary gives the required embedding in $\RR^3$.

::: pf-proof
The punctured boundary is still homeomorphic to $S^2$, and the two complementary components are the two non-simply-connected interiors from step [](#double){.pf-ref}. Hence the limiting surface is a topological $2$-sphere in $\RR^3$ for which neither component of $\RR^3\setminus S^2$ is simply connected.
:::

:::

:::
:::
