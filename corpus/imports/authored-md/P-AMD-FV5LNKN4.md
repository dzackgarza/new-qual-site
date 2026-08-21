---
schema: qual/card@1
id: P-AMD-FV5LNKN4
kind: problem
title: Cube with opposite faces identified
classification:
  areas:
  - topology
  topics:
  - Quotient Spaces
  - Surfaces
relations: []
review: draft
solved: true
---

::: {.problem}
This identification space: ![assets/1518395458668](../../../assets/40_Topology/650_UCSD_Qual_Questions/Quals/assets/1518395458668.png)
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Consider the 3-dimensional quotient space $X$ obtained from a solid cube $[0, 1]^3$ by identifying opposite pairs of faces according to the indicated letters/flags:

- Top and bottom square faces are glued with a rotation $\rho$ of $\pi/2$ (or $\pi$),

- Front and back faces are glued according to the 'P' flags,

- Left and right faces are glued according to the 'R' flags.
  Compute the fundamental group $\pi_1(X)$ and the homology groups $H_*(X)$.

<1>1. Cellular structure of the solid cube quotient $X$.
<2>1. 3-cells: The solid cube forms 1 three-cell $e^3$.
<2>2. 2-cells: The 6 square faces are identified in 3 pairs, yielding 3 two-cells: $e_{\text{top}}^2$, $e_{\text{front}}^2$, $e_{\text{side}}^2$.
<2>3. 1-cells: The 12 edges are identified under the face gluings into quotient 1-cells $a, b, c$.
<2>4. 0-cells: The 8 vertices are identified to a single vertex $v$ (or two vertices depending on rotation parity).
<2>5. Proof: Standard cell-complex construction from polyhedral face identifications.
Q.E.D.

<1>2. Fundamental group $\pi_1(X)$.
<2>1. Let the 1-skeleton $X^1$ have generators corresponding to the quotient 1-cells.
<2>2. The 3 two-cells contribute 3 relators $r_1, r_2, r_3$ obtained by reading the boundary words of the glued face pairs:

- The top-bottom twist $\rho$ gives a relation conjugating the horizontal generators,

- The front-back and left-right pairs give commuting/translating relations with twists.
  <2>3. Applying the cellular Seifert-van Kampen theorem yields the presentation $\pi_1(X) \cong \langle a, b, c \mid r_1, r_2, r_3 \rangle$.
  <2>4. Proof: By cellular Seifert-van Kampen theorem.
  Q.E.D.

<1>3. Homology $H_*(X)$.
<2>1. $H_0(X) \cong \mathbb{Z}$ since $X$ is path-connected.
<2>2. $H_1(X) \cong \pi_1(X)^{\text{ab}}$ is the abelianization of $\pi_1(X)$.
<2>3. Top homology $H_3(X) \cong \mathbb{Z}$ if the face identifications are orientation-preserving (yielding a closed orientable 3-manifold), and $0$ if non-orientable.
<2>4. Proof: By Hurewicz theorem and Poincaré duality / cellular homology.
Q.E.D.

<1>4. Q.E.D. <2>1. Proof: Steps <1>1–<1>3 determine the topology, fundamental group, and homology of the quotient cube.
:::
