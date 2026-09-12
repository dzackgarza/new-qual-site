---
schema: qual/card@1
id: P-HGRO42
kind: problem
title: Six-bead necklaces with two colors
classification:
  areas: [algebra]
  topics: [Group Actions]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Group Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
How many distinct six-bead necklaces can be made with two colors, where necklaces related by a symmetry are identified?
:::

::: solution
There are $13$.

Let the dihedral group $D_{12}$ act on the $2^6=64$ two-colorings of the six
bead positions. By Burnside's lemma, the number of necklaces is the average
number of colorings fixed by the twelve symmetries.

<1>1. The six rotations fix respectively
\[
64,\ 2,\ 4,\ 8,\ 4,\ 2
\]
colorings.
::: proof
A rotation through $k$ bead positions has $\gcd(6,k)$ cycles on the six
positions, and a coloring fixed by that rotation is constant on each cycle.
Hence it fixes
\[
2^{\gcd(6,k)}
\]
colorings. For $k=0,1,2,3,4,5$ this gives the displayed numbers.
:::

<1>2. Three reflections fix $16$ colorings each and the other three fix $8$
colorings each.
::: proof
For even $6$, three reflection axes pass through a pair of opposite beads. Such
a reflection has two fixed beads and two transposed pairs, hence four orbits and
$2^4=16$ fixed colorings.

The other three axes pass through opposite gaps. Such a reflection has three
transposed pairs, hence three orbits and $2^3=8$ fixed colorings.
:::

<1>3. Burnside's lemma gives
\[
\frac{64+2+4+8+4+2+3\cdot16+3\cdot8}{12}=13.
\]
::: proof
The numerator is $156$, and $156/12=13$.
:::
:::
