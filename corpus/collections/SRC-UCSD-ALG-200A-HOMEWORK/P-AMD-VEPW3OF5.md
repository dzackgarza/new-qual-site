---
schema: qual/card@1
id: P-AMD-VEPW3OF5
kind: problem
title: Counting circular bracelets made from $r$ beads in $n$ colors
classification:
  areas:
  - algebra
  topics:
  - Burnside's Lemma
  - Group Actions
  - Partitions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 3, Exercise 8. Restored
    the source equivalence relation: two r-bead colorings are the same after
    any sequence of rotations and/or flips, so the relevant action is the
    dihedral action rather than rotations alone.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Applied Burnside's lemma to the order-2r dihedral group. A rotation by k
    positions has gcd(r,k) cycles. For reflections, odd r gives r reflections
    with (r+1)/2 cycles; even r gives r/2 vertex-axis reflections with r/2+1
    cycles and r/2 edge-axis reflections with r/2 cycles.
---

::: {.problem}
Arrange $r$ beads on a circular string and color each bead with one of $n$ colors.
Two colorings are considered the same if one can be obtained from the other by a sequence of rotations and/or flips.

How many distinct bracelets are there?
:::

::: {.solution}
Let $\mathcal C$ be the set of all colorings of the $r$ bead positions.
Then
\[
|\mathcal C|=n^r.
\]
Let $D_r$ denote the dihedral group of order $2r$ acting on the bead positions, and hence on $\mathcal C$.
The desired bracelets are exactly the $D_r$-orbits.

<1>1. A rotation through $k$ bead positions fixes exactly
\[
n^{\gcd(r,k)}
\]
colorings.
::: {.proof}
The permutation of the $r$ bead positions induced by rotation through $k$ places has exactly
\[
\gcd(r,k)
\]
cycles.
A coloring is fixed precisely when it is constant on each cycle.
There are $n$ independent choices of color for each cycle, hence
\[
|\operatorname{Fix}(\rho^k)|=n^{\gcd(r,k)}.
\]
:::

<1>2. The total fixed-coloring contribution from all rotations is
\[
\sum_{d\mid r}\varphi(d)n^{r/d}.
\]
::: {.proof}
By <1>1, the rotation contribution is
\[
\sum_{k=0}^{r-1}n^{\gcd(r,k)}.
\]
For a divisor $g\mid r$, the number of integers $k\pmod r$ satisfying
\[
\gcd(r,k)=g
\]
is
\[
\varphi(r/g).
\]
Therefore
\[
\sum_{k=0}^{r-1}n^{\gcd(r,k)}
=\sum_{g\mid r}\varphi(r/g)n^g.
\]
Reindexing by $d=r/g$ gives
\[
\sum_{d\mid r}\varphi(d)n^{r/d}.
\]
:::

<1>3. If $r$ is odd, every reflection fixes exactly
\[
n^{(r+1)/2}
\]
colorings.
::: {.proof}
For odd $r$, the axis of a reflection passes through one bead and the midpoint of the opposite edge.
Thus the induced permutation of bead positions has one fixed bead and
\[
\frac{r-1}{2}
\]
transposed pairs.
Hence it has
\[
1+\frac{r-1}{2}=\frac{r+1}{2}
\]
cycles.
A fixed coloring is constant on each cycle, giving
\[
n^{(r+1)/2}
\]
fixed colorings.
There are $r$ reflections of this type.
:::

<1>4. If $r$ is even, half the reflections fix
\[
n^{r/2+1}
\]
colorings and half fix
\[
n^{r/2}
\]
colorings.
::: {.proof}
For even $r$, there are two reflection types.

A reflection whose axis passes through two opposite beads fixes those two bead positions and pairs the other $r-2$ positions.
It therefore has
\[
2+\frac{r-2}{2}=\frac r2+1
\]
cycles and fixes
\[
n^{r/2+1}
\]
colorings.

A reflection whose axis passes through the midpoints of two opposite edges has no fixed bead positions and pairs all $r$ positions.
It therefore has
\[
\frac r2
\]
cycles and fixes
\[
n^{r/2}
\]
colorings.

There are $r/2$ reflections of each type.
:::

<1>5. If $r$ is odd, the number of distinct bracelets is
\[
\boxed{
\frac1{2r}
\left(
\sum_{d\mid r}\varphi(d)n^{r/d}
+r n^{(r+1)/2}
\right)
}.
\]
::: {.proof}
Burnside's lemma says that the number of $D_r$-orbits is the average number of fixed colorings over the $2r$ group elements.
Combine the rotation contribution from <1>2 with the $r$ equal reflection contributions from <1>3, then divide by $2r$.
:::

<1>6. If $r$ is even, the number of distinct bracelets is
\[
\boxed{
\frac1{2r}
\left(
\sum_{d\mid r}\varphi(d)n^{r/d}
+\frac r2 n^{r/2+1}
+\frac r2 n^{r/2}
\right)
}.
\]
::: {.proof}
Again apply Burnside's lemma.
Use <1>2 for the rotations and <1>4 for the two families of $r/2$ reflections, then divide their total fixed-point count by $|D_r|=2r$.
:::
:::
