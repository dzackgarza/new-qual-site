---
schema: qual/card@1
id: P-TRIV-PR21
kind: problem
title: Expected area of the projection of a randomly oriented unit cube
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 21, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. Flash contains one or more nonprinting control bytes at this source position; they were removed from the authored card as nonsemantic extraction artifacts.
---

::: {.problem}
Find the expectation value of the area of the projection of a 3-dimensional randomly oriented cube with edge of length 1 onto a given plane.
:::

::: {.solution}

Let $n$ be a unit normal to the fixed projection plane, and let $u_1,u_2,u_3$ be the orthonormal directions normal to the three pairs of opposite cube faces.

::: pf

::: {.pf-step #s1-1}

For a fixed orientation of the cube, the area of its orthogonal projection is
$$
A=\abs{n\cdot u_1}+\abs{n\cdot u_2}+\abs{n\cdot u_3}.
$$


::: pf-proof

For a convex polyhedron, the projected area equals the sum over the faces visible from direction $n$ of the area of each face times the absolute cosine of the angle between its normal and $n$. For each pair of opposite unit-area cube faces, exactly one face is visible except on a measure-zero edge-on orientation, and its contribution is $\abs{n\cdot u_i}$. Summing the three pairs gives the formula.

:::

:::

::: pf-step

Under a uniformly random orientation, each $u_i$ is uniformly distributed on the unit sphere $S^2$.


::: pf-proof

Haar-uniform rotation of any fixed unit vector has the rotation-invariant probability distribution on $S^2$, which is the uniform surface-area distribution.

:::

:::

::: {.pf-step #s1-3}

If $U$ is uniform on $S^2$, then
$$
\mathbf E\abs{n\cdot U}=\frac12.
$$


::: pf-proof

By rotational invariance take $n$ as the north-pole direction. Writing $n\cdot U=\cos\theta$, the normalized surface measure is
$$
\frac1{4\pi}\sin\theta\,d\theta\,d\phi.
$$
Hence
$$
\mathbf E\abs{n\cdot U}
=\frac1{4\pi}\int_0^{2\pi}\int_0^\pi
\abs{\cos\theta}\sin\theta\,d\theta\,d\phi
=\frac12.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{\mathbf EA=\frac32}.
$$


::: pf-proof

By linearity of expectation, independence of the three $u_i$ is unnecessary. Apply step [](#s1-3){.pf-ref} separately to each term in step [](#s1-1){.pf-ref}:
$$
\mathbf EA
=\sum_{i=1}^3\mathbf E\abs{n\cdot u_i}
=3\cdot\frac12
=\frac32.
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the expected projected area of the randomly oriented unit cube.

:::

:::

:::
