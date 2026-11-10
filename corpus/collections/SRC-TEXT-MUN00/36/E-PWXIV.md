---
schema: qual/card@1
id: E-PWXIV
kind: problem
title: Properties of eleven standard spaces
classification:
  areas:
  - topology
  topics:
  - Topological Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Checked line by line against Munkres, Topology (2000), Supplementary Exercises: Review of the
    Basics, Exercise 1, printed pp. 228-229. No published solution was located: dbFin's chapter-4
    supplementary page (https://dbfin.com/topology/munkres/chapter-4/supplementary-exercises-review-of-the-basics/,
    read 2026-11-10) carries the title and no solution, and none of its problem subpages exists;
    "Doug's World" covers the numbered exercises of §30-§36 only, Moller's files are S31, S33, S34,
    S35 and S38, and Orellana's contents run §13-§34 and §37. This exercise is in the COMPLAINTS.md
    entry. What the check confirmed against the book: S_Omega is limit point compact and not compact
    (Example 2 of §28, printed p. 181), not first- or second-countable, not separable, locally compact
    Hausdorff and hereditarily normal (Theorem 32.4), and locally metrizable because each initial
    segment [0, alpha+1) is countable; S_bar_Omega is compact (Exercise 29.7) hence Lindelof, and not
    first countable, separable, second countable or metrizable (Example 3 of §28); the product
    S_Omega x S_bar_Omega is countably compact and not normal (Example 2 of §32) and not first
    countable; the ordered square is a compact linear continuum, first countable (Exercise 21.4),
    connected and locally connected, not path connected and not separable, hence not metrizable,
    Lindelof or locally metrizable; R_l is Lindelof, separable, first countable, completely normal and
    neither second countable nor locally compact nor locally metrizable; R_l^2 is separable, first
    countable and not normal, not Lindelof; R^omega in the product topology has all the metric
    properties and none of compactness, limit point compactness or local compactness; in the uniform
    topology it is metrizable and locally path connected, balls of radius below 1 being convex,
    while it is disconnected -- the bounded and the unbounded sequences are disjoint open sets --
    and neither separable nor Lindelof (Example 2 of §30); in the box topology it is completely regular (Exercise 33.9) and nothing
    else among the countability properties, with box normality left undecided by the book (Exercise
    32.5); R^I for I = [0,1] is connected, has a countable dense subset (Exercise 30.16), is not
    first countable, and is not normal by Exercise 32.9; and R_K is connected but not path connected
    (§27), Hausdorff and second countable, and not regular (Example 31.1). The table's "?" in the box
    column is the book's own open question, so it is not a gap in the proof.
---

::: {.exercise}

Consider the following properties a space may satisfy:

(1) connected, (2) path connected, (3) locally connected, (4) locally path connected, (5) compact, (6) limit point compact, (7) locally compact Hausdorff, (8) Hausdorff, (9) regular, (10) completely regular, (11) normal, (12) first-countable, (13) second-countable, (14) Lindelöf, (15) has a countable dense subset, (16) locally metrizable, (17) metrizable.

For each of the following spaces, determine (if you can) which of these properties it satisfies.
(Assume the Tychonoff theorem if you need it.)

(a) $S_\Omega$

(b) $\overline{S}_\Omega$

(c) $S_\Omega \times \overline{S}_\Omega$

(d) The ordered square

(e) $\RR_\ell$

(f) $\RR_\ell^2$

(g) $\RR^\omega$ in the product topology

(h) $\RR^\omega$ in the uniform topology

(i) $\RR^\omega$ in the box topology

(j) $\RR^I$ in the product topology, where $I = [0, 1]$

(k) $\RR_K$
:::

::: {.solution}
Write **Y** for “yes,” **N** for “no,” and **?** for the box-product normality question not decided by the results used here. The columns are the properties (1)–(17) in the problem statement.

| space |1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| (a) $S_\Omega$ |N|N|N|N|N|Y|Y|Y|Y|Y|Y|Y|N|N|N|Y|N|
| (b) $\overline S_\Omega$ |N|N|N|N|Y|Y|Y|Y|Y|Y|Y|N|N|Y|N|N|N|
| (c) $S_\Omega\times\overline S_\Omega$ |N|N|N|N|N|Y|Y|Y|Y|Y|N|N|N|N|N|N|N|
| (d) ordered square |Y|N|Y|N|Y|Y|Y|Y|Y|Y|Y|Y|N|Y|N|N|N|
| (e) $\RR_\ell$ |N|N|N|N|N|N|N|Y|Y|Y|Y|Y|N|Y|Y|N|N|
| (f) $\RR_\ell^2$ |N|N|N|N|N|N|N|Y|Y|Y|N|Y|N|N|Y|N|N|
| (g) $\RR^\omega$, product |Y|Y|Y|Y|N|N|N|Y|Y|Y|Y|Y|Y|Y|Y|Y|Y|
| (h) $\RR^\omega$, uniform |N|N|Y|Y|N|N|N|Y|Y|Y|Y|Y|N|N|N|Y|Y|
| (i) $\RR^\omega$, box |N|N|N|N|N|N|N|Y|Y|Y|?|N|N|N|N|N|N|
| (j) $\RR^I$, product |Y|Y|Y|Y|N|N|N|Y|Y|Y|N|N|N|N|Y|N|N|
| (k) $\RR_K$ |Y|N|N|N|N|N|N|Y|N|N|N|Y|Y|Y|Y|Y|N|

The principal reasons are as follows.

**Ordinal spaces.** $S_\Omega=[0,\omega_1)$ is countably compact (hence limit point compact), locally compact Hausdorff, hereditarily normal, first countable, and locally metrizable; it is not compact, Lindelöf, separable, second countable, or metrizable. Its one-point compactification $\overline S_\Omega=[0,\omega_1]$ is compact Hausdorff and normal, but fails first countability and local metrizability at $\omega_1$. Neither ordinal space is connected or locally connected. The product in (c) is locally compact Hausdorff and completely regular, and every countable subset lies in a compact bounded rectangle, so it is limit point compact. It is not normal: the diagonal and the top edge give the standard nonseparable closed pair. This also forces failure of Lindelöfness; first countability already fails because of the second factor.

**Ordered square.** It is a compact linear continuum, hence connected, locally connected, compact Hausdorff, and normal. Its path components are the vertical fibers, so it is neither path connected nor locally path connected. It is first countable but not separable or second countable. Since a compact Hausdorff locally metrizable space would be metrizable, its nonmetrizability also implies it is not locally metrizable.

**Sorgenfrey spaces.** The Sorgenfrey line is completely normal, first countable, Lindelöf, and separable, but it is disconnected, not locally connected, not locally compact, not second countable, and not metrizable. Its square remains Hausdorff, regular, completely regular, first countable, and separable, but is not normal or Lindelöf; hence it is not metrizable. Neither space is locally metrizable.

**Infinite powers of $\RR$.** In the product topology on $\RR^\omega$, coordinatewise straight-line paths show path connectedness and local path connectedness, while the standard product metric gives all metric/countability properties; it is not compact, limit point compact, or locally compact. In the uniform topology, components are the bounded-difference classes; uniform balls of radius $<1$ are convex, so the space is locally path connected but globally disconnected. It is metrizable but nonseparable and non-Lindelöf. In the box topology, components/path components are the classes of points differing in only finitely many coordinates, so it is neither connected nor locally connected. It is completely regular but not first countable, separable, Lindelöf, or metrizable. The normality entry is left **?** here: the source notes the classical CH-positive result rather than a ZFC theorem.

For $\RR^I$ with $I=[0,1]$, the product is path connected and locally path connected, Hausdorff and completely regular, and has a countable dense subset by §30. It is not first countable, locally compact, or metrizable. Stone's theorem gives nonnormality; regular Lindelöf spaces are normal, so it is not Lindelöf either.

**The $K$-topology.** $\RR_K$ is connected but not path connected (§27), and it is not locally connected at $0$. It is Hausdorff and second countable, hence first countable, Lindelöf, and separable. It is not regular, so it is neither completely regular, normal, nor metrizable; in particular it is not locally compact Hausdorff. It is nevertheless locally metrizable: near $0$, a basic neighborhood $(a,b)-K$ has the usual subspace topology, and near a point of $K$ one can choose a small interval meeting $K$ in at most that point, again giving the usual metrizable subspace topology.
:::
