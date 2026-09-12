---
schema: qual/card@1
id: E-HAT-1.3-28
kind: problem
title: "Fundamental group of an orbit space"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.3, Exercise 28; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Identified the orbit map as the universal cover and its deck group with G.
---

Show that for a covering space action of a group $G$ on a simply-connected space $Y$, $\pi_1(Y/G)$ is isomorphic to $G$.
[If $Y$ is locally path-connected, this is a special case of part (c) of Proposition 1.40.]


::: {.solution}
Let
\[
q:Y\to Y/G
\]
be the orbit map.

<1>1. The map $q$ is a covering map with deck transformation group $G$.
::: {.proof}
This is exactly the definition and basic property of a covering space action: the translates of a suitable neighborhood are pairwise disjoint and map homeomorphically to one neighborhood in the quotient.
Since $Y$ is path connected, every deck transformation of $q$ is determined by the image of one point, and Proposition 1.40 gives
\[
\operatorname{Deck}(Y/(Y/G))\cong G.
\]
:::

<1>2. Since $Y$ is simply connected, $q$ is the universal covering map of $Y/G$.
::: {.proof}
A simply connected covering space is universal.
:::

<1>3. Therefore
\[
\boxed{\pi_1(Y/G)\cong G.}
\]
::: {.proof}
For a universal cover, the deck transformation group is canonically isomorphic to the fundamental group of the base, after choosing a basepoint in the fiber.
Combining this with <1>1 gives the displayed isomorphism.
:::
:::
