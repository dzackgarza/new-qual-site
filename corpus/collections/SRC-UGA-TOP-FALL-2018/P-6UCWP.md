---
schema: qual/card@1
id: P-6UCWP
kind: problem
title: Euler characteristic of a cylinder after identifying two disjoint closed intervals
  on the boundary, and which bordered surfaces arise
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - Surfaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $C$ be cylinder.
Let $I$ and $J$ be disjoint closed intervals contained in $\partial C$.

What is the Euler characteristic of the surface $S$ obtained by identifying $I$ and $J$?

Can all surface with nonempty boundary and with this Euler characteristic be obtained from this construction?
:::

::: {.solution}
<1>1. Computation of the Euler characteristic $\chi(S)$:
<2>1. The cylinder $C = S^1 \times [0, 1]$ deformation retracts onto $S^1$, so:
\[
\chi(C) = \chi(S^1) = 0.
\]
::: {.proof}
homotopy invariance of Euler characteristic.
:::
<2>2. $I \cong [0, 1]$ and $J \cong [0, 1]$ are disjoint closed intervals on $\partial C$, each having $\chi(I) = \chi(J) = 1$.
Their intersection is $I \cap J = \emptyset$.
::: {.proof}
contractibility of closed intervals.
:::
<2>3. The surface $S = C / (I \sim J)$ is obtained by gluing along $J \cong I$.
Using the Mayer–Vietoris / CW inclusion-exclusion principle:
\[
\chi(S) = \chi(C) - \chi(J) = 0 - 1 = -1.
\]
(Equivalently: under the identification $I \sim J$, 2 vertices merge into 2 vertices ($\Delta V = -2$) and 1 edge merges into 1 edge ($\Delta E = -1$), so $\Delta \chi = \Delta V - \Delta E = -2 - (-1) = -1$).
::: {.proof}
Euler characteristic of quotient cell complexes.
:::

<1>2. Classification of surfaces with non-empty boundary and $\chi = -1$:
<2>1. By the classification of compact connected surfaces with boundary, the Euler characteristic is:
- Orientable surfaces: $\chi = 2 - 2g - b = -1 \implies 2g + b = 3$.
  Since $b \ge 1$ and $g \ge 0$, the only solutions are:
  - $(g, b) = (0, 3)$: sphere with 3 boundary components (a pair of pants).
  - $(g, b) = (1, 1)$: torus with 1 boundary component (punctured torus).
- Non-orientable surfaces: $\chi = 2 - k - b = -1 \implies k + b = 3$.
  Since $b \ge 1$ and $k \ge 1$, the only solutions are:
  - $(k, b) = (1, 2)$: $\mathbb{RP}^2$ with 2 boundary components (Möbius strip with 1 hole).
  - $(k, b) = (2, 1)$: Klein bottle with 1 boundary component (punctured Klein bottle).
::: {.proof}
classification theorem for compact 2-manifolds with boundary.
:::

<1>3. Realizability of all connected candidate surfaces:
<2>1. The boundary of the cylinder consists of two disjoint circles: $\partial C = S_1 \sqcup S_2$.
Depending on the placement of $I, J$ and the gluing map $\phi: I \to J$:
- **Case 1 ($I, J \subset S_1$, same boundary component):**
  - Gluing with the orientation that preserves orientability splits $S_1$ into two circles while $S_2$ remains intact, producing a pair of pants ($g=0, b=3$).
  - Gluing with the opposite orientation produces a non-orientable surface with two boundary components ($k=1, b=2$).
- **Case 2 ($I \subset S_1, J \subset S_2$, different boundary components):**
  - Gluing with the orientation that preserves surface orientability merges $S_1$ and $S_2$ into a single boundary component, yielding a punctured torus ($g=1, b=1$).
  - Gluing with a twist (reversing orientation) produces a punctured Klein bottle ($k=2, b=1$).
::: {.proof}
direct topological construction by gluing.
:::
<2>2. Because $C$ is connected, any surface $S$ obtained by this construction is necessarily connected.
Thus all connected surfaces with non-empty boundary and $\chi = -1$ are realized, but disconnected surfaces with $\chi = -1$ (such as the disjoint union of a cylinder and a disk) cannot be obtained.
::: {.proof}
quotient of a connected space is connected.
:::

<1>4. Conclusion:
The Euler characteristic is $\chi(S) = -1$. All connected surfaces with non-empty boundary and $\chi = -1$ can be obtained from this construction. Q.E.D.
::: {.proof}
<1>1 through <1>3.
:::
:::
