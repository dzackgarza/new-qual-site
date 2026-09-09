---
schema: qual/card@1
id: E-HAT-1.2-9
kind: problem
title: Surface of genus $g$ retracts onto nonseparating circle but not separating circle
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Surfaces
  - Retractions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.2, Exercise 9; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used the boundary product-of-commutators relation for the nonretraction and a standard CW structure for the retraction onto a nonseparating curve.
---

In the surface $M_g$ of genus $g$, let $C$ be a circle that separates $M_g$ into two compact subsurfaces $M'_h$ and $M'_k$ obtained from the closed surfaces $M_h$ and $M_k$ by deleting an open disk from each.
Show that $M'_h$ does not retract onto its boundary circle $C$, and hence $M_g$ does not retract onto $C$.
[Hint: abelianize $\pi_1$.] But show that $M_g$ does retract onto the nonseparating circle $C'$ in the figure.

::: {.solution}
<1>1. For $h\ge1$, the surface $M'_h$ has fundamental group
\[
\pi_1(M'_h)\cong F(a_1,b_1,\dots,a_h,b_h),
\]
and its boundary loop $C$ represents
\[
[a_1,b_1]\cdots[a_h,b_h].
\]
::: {.proof}
A genus-$h$ orientable surface with one boundary component has the standard CW description with one vertex and $2h$ one-cells
\[
a_1,b_1,\dots,a_h,b_h,
\]
but with the interior of the usual $2$-cell removed.
Hence its fundamental group is free on these $2h$ generators.
The boundary of the missing $2$-cell is the usual surface attaching word
\[
[a_1,b_1]\cdots[a_h,b_h],
\]
so this word represents the boundary circle $C$.
:::

<1>2. There is no retraction
\[
r:M'_h\to C.
\]
::: {.proof}
Suppose such a retraction existed, and let
\[
i:C\hookrightarrow M'_h
\]
be the inclusion.
Then
\[
r_*\circ i_*=\operatorname{id}_{\pi_1(C)}.
\]
Identify
\[
\pi_1(C)\cong\mathbb Z.
\]

For $h\ge1$, <1>1 says that $i_*(1)$ is a product of commutators.
Every homomorphism from a group to the abelian group $\mathbb Z$ kills every commutator, so
\[
r_*i_*(1)=0,
\]
contradicting
\[
r_*i_*(1)=1.
\]

If $h=0$, then $M'_0=D^2$, so $i_*:\pi_1(S^1)\to\pi_1(D^2)$ is the zero map and cannot possess a left inverse either.
Thus no retraction exists for any $h\ge0$.
:::

<1>3. The closed surface $M_g$ cannot retract onto the separating circle $C$.
::: {.proof}
If
\[
r:M_g\to C
\]
were a retraction, then restricting $r$ to either subsurface $M'_h\subset M_g$ would give a retraction
\[
r|_{M'_h}:M'_h\to C,
\]
because $C\subset M'_h$ and $r$ is the identity on $C$.
This contradicts <1>2.
:::

<1>4. A nonseparating simple closed curve $C'\subset M_g$ can be carried by a homeomorphism of $M_g$ to the standard loop $a_1$ in the usual one-vertex CW structure on $M_g$.
::: {.proof}
Cutting an orientable surface along a nonseparating simple closed curve produces a connected orientable surface of genus $g-1$ with two boundary components.
The same is true for the standard generator circle $a_1$.
By the classification of compact orientable surfaces with boundary, the two cut surfaces are homeomorphic by a homeomorphism matching their two boundary circles.
Regluing gives a homeomorphism of $M_g$ carrying $C'$ to $a_1$.
Thus it suffices to construct a retraction onto $a_1$.
:::

<1>5. Define a map on the $1$-skeleton
\[
q:M_g^1\to a_1\cong S^1
\]
by mapping the edge $a_1$ identically to itself and collapsing every other $1$-cell to the common vertex.
::: {.proof}
The standard $1$-skeleton is a wedge of the $2g$ circles
\[
a_1,b_1,\dots,a_g,b_g.
\]
A map from this wedge is determined continuously by its restrictions to the summand circles, and the stated restrictions agree at the wedge point.
:::

<1>6. The map $q$ extends across the $2$-cell of $M_g$.
::: {.proof}
The attaching map of the $2$-cell represents
\[
[a_1,b_1]\cdots[a_g,b_g].
\]
Under $q_*$, each $b_i$ and every $a_i$ for $i>1$ maps to the identity in
\[
\pi_1(S^1)\cong\mathbb Z,
\]
while $a_1$ maps to the generator.
Therefore every commutator maps to the identity, so the entire attaching loop maps trivially in $\pi_1(S^1)$.
Hence its composite with $q$ is null-homotopic and $q$ extends over the $2$-cell.
:::

<1>7. The extension
\[
r:M_g\to a_1
\]
is a retraction, and hence $M_g$ retracts onto $C'$.
::: {.proof}
By construction, $r$ restricts to the identity on the edge $a_1$.
Thus $r$ is a retraction onto $a_1$.
Conjugating this retraction by the homeomorphism from <1>4 gives a retraction of $M_g$ onto the original nonseparating curve $C'$.
:::
:::
