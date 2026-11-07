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
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Corrected the preceding revision after rereading Alexander pp.9-10 and Bing pp.315-316.
    Alexander proves non-simple-connectedness only for the exterior of his original
    outward-tube sphere. Bing separately pushes the tubes inward, explicitly states that the
    interiors of both modified spheres are not simply connected, and defines each solid horned
    sphere to be its surface together with that interior. The puncture is now chosen in one open
    complementary domain, leaving the common boundary sphere intact; van Kampen in dimension
    three shows that this puncture does not change that domain's fundamental group. Checked the
    source attribution, the two complementary fundamental groups, and the passage to R^3. Bing's
    cited theorem that the reflected gluing is S^3 is used, not re-proved here.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Rechecked the corrected topology: the embedded common boundary remains S^2 under
    stereographic projection from an interior point, its two complement components are U minus
    that point and V, and pi_1(U minus a point) is isomorphic to pi_1(U) by van Kampen. Thus both
    are non-simply-connected by Bing's explicit assertion for the inward-tube construction.
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
Glue Bing's two reflected solid horned spheres along their common boundary. The result is $S^3$, and neither complementary domain of the boundary sphere is simply connected.

::: pf-proof
For this gluing Bing uses the modified construction in which the tubes are pushed **inward**, rather than Alexander's original outward-tube construction. He defines a solid horned sphere to be such a modified sphere together with its interior, and states explicitly that the interiors of both reflected solids are not simply connected. When the two solids are sewn together along corresponding boundary points, Bing's gluing theorem says that their union $X$ is homeomorphic to $S^3$. If $K$ is their common boundary and $U,V$ are the two interiors, then $K\cong S^2$ and $X\setminus K=U\sqcup V$, with both $U$ and $V$ non-simply-connected.
:::

:::

::: {.pf-step #puncture}
Choose $p\in U$. Stereographic projection from $p$ carries the intact sphere $K\subset X\setminus\{p\}$ to the required embedding in $\RR^3$, and neither complementary component is simply connected.

::: pf-proof
The homeomorphism $X\setminus\{p\}\cong\RR^3$ leaves $K$ unchanged as a topological $2$-sphere. Its complementary components are $U\setminus\{p\}$ and $V$. The latter is non-simply-connected by step [](#double){.pf-ref}.

For the former, choose a small open $3$-ball $B\subset U$ centered at $p$. Then
$$
U=(U\setminus\{p\})\cup B,\qquad
(U\setminus\{p\})\cap B=B\setminus\{p\}.
$$
Both $B$ and $B\setminus\{p\}\cong\RR^3\setminus\{0\}$ are simply connected, and $U\setminus\{p\}$ is path connected because $U$ is a connected open $3$-manifold. Van Kampen's theorem therefore gives
$$
\pi_1(U\setminus\{p\})\cong\pi_1(U)\neq1.
$$
The images of $U\setminus\{p\}$ and $V$ in $\RR^3$ are consequently both non-simply-connected, while their common boundary is still the embedded $2$-sphere $K$.
:::

:::

:::
:::
