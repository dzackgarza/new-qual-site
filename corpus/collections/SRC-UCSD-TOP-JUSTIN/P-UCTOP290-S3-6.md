---
schema: qual/card@1
id: P-UCTOP290-S3-6
kind: problem
title: Fundamental group of a face-identified prism
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - van Kampen
relations: []
review: draft
---

::: {.problem}
Compute the fundamental group of the space obtained by identifying the faces of the solid prism shown in Problem 6 of the source sheet.
:::

::: {.remark}
The face-identification diagram appears on page 1 of the source sheet.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The $Q$-labelled top and bottom triangular faces are identified preserving their markings, so before the side-face identifications the quotient is $\Delta^2\times S^1$.

::: pf-proof

This is the mapping torus of the identity on the triangular cross-section.

:::

:::

::: {.pf-step #s2}

The three side faces carry the same $F$ marking. Their identification is constant in the $S^1$ direction and, on the boundary of the triangular cross-section, is precisely the standard dunce-cap identification of all three sides.

::: pf-proof

The common face marking identifies corresponding vertical coordinates, while the three edges of the triangular cross-section are identified with the orientations encoded by the repeated $F$ glyph. This is the same three-edge pattern as the source sheet's triangle example.

:::

:::

::: pf-step

Hence the quotient is homeomorphic to
$$D\times S^1,$$
where $D$ is the dunce cap.

::: pf-proof

The identifications in steps [](#s1){.pf-ref} and [](#s2){.pf-ref} are products of the cross-section identifications with the circle coordinate.

:::

:::

::: pf-step

The dunce cap is contractible, so
$$\boxed{\pi_1(X)\cong\pi_1(S^1)\cong\mathbb Z.}$$

::: pf-proof

Projection $D\times S^1\to S^1$ is a homotopy equivalence because $D$ is contractible.

:::

:::

:::

:::
