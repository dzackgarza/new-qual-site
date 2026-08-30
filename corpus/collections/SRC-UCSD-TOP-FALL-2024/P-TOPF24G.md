---
schema: qual/card@1
id: P-TOPF24G
kind: problem
title: 'Fundamental group and $\pi_2$ of $\mathbb{RP}^3 \# \mathbb{RP}^3$'
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
What is the fundamental group of $X = \mathbb{RP}^3 \# \mathbb{RP}^3$?
Give a description of the universal cover $\widetilde{X}$ of $X$ and use this to calculate $\pi_2(X)$.
:::

::: solution
**Goal:** Compute $\pi_1(X)$, describe $\widetilde X$, and deduce $\pi_2(X)$.

<1> Compute $\pi_1(X)$.
    Remove a small open ball from each summand and glue along the resulting
    $S^2$ boundaries.
    Van Kampen gives
    $$
    \pi_1(X)\cong \pi_1(\RP^3)\ast \pi_1(\RP^3)\cong \mathbf Z/2\ast\mathbf Z/2.
    $$

<1> Describe the universal cover.
    Let $A=\RP^3\setminus\operatorname{int}(D^3)$ and $E=A\cup_{S^2}A$.
    The universal cover of $A$ is $\widetilde A=S^3\setminus\operatorname{int}(D_1^3\cup D_2^3)$, which deformation retracts to $S^2$.
    The lifts of the two copies of $\pi_1(\RP^3)$ inside $X$ are arranged along the Cayley tree of $\mathbf Z/2\ast\mathbf Z/2$ (an infinite line).
    Hence $\widetilde X$ is an infinite chain of copies of $\widetilde A$ glued along boundary spheres.

<1> Collapse each $\widetilde A$ to its deformation-retraction spine $S^2$ and each collar to intervals.
    The resulting deformation retract of $\widetilde X$ is $S^2\times\mathbf R$.
    Therefore
    $$
    \widetilde X\simeq S^2\times\mathbf R.
    $$

<1> Compute $\pi_2$.
    Since covering maps induce isomorphisms on homotopy groups in degrees $\ge2$,
    $$
    \pi_2(X)\cong \pi_2(\widetilde X)\cong\pi_2(S^2\times\mathbf R)\cong\pi_2(S^2)=\mathbf Z.
    $$

Authored by **Codex 5.3 Spark Extra High**.
:::
