---
schema: qual/card@1
id: P-TOPF09G
kind: problem
title: "Suspension of a homology 3-sphere is homotopy equivalent to S^4"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Suspensions
  - Homotopy Type
  - Manifolds
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Let $M^3$ be a homology sphere: a connected closed compact $3$-manifold with the same homology groups as $S^3$.
Calculate the fundamental group and homology of the suspension $\Sigma M$.
Use this to show that the suspension is homotopy-equivalent to $S^4$.
:::

::: solution
**Goal:** Compute $\Sigma M$ homology and fundamental group, then identify it by Whitehead-type comparison with $S^4$.

<1> For any connected space $M$,
    $$
    \widetilde H_i(\Sigma M)\cong \widetilde H_{i-1}(M)\quad (i\ge1).
    $$
    Since $M$ is a homology $3$-sphere,
    $$
    \widetilde H_3(M)\cong\mathbb Z,\qquad \widetilde H_i(M)=0\ (i\ne3),
    $$
    so
    $$
    H_0(\Sigma M)=\mathbb Z,\quad
    H_i(\Sigma M)=0\ (i=1,2,3),\quad
    H_4(\Sigma M)\cong\mathbb Z.
    $$

<1> Write $\Sigma M=C_+M\cup C_-M$ as union of two contractible cones.
    Their intersection is path-connected, so van Kampen gives
    $$
    \pi_1(\Sigma M)=1.
    $$

<1> The reduced homology computation gives $H_2=H_3=0$ and $H_4\cong\mathbb Z$.
    Since $\pi_1(\Sigma M)=0$, Hurewicz gives $\pi_2(\Sigma M)=\pi_3(\Sigma M)=0$ and $\pi_4(\Sigma M)\cong\mathbb Z$.
    The induced map $f:\Sigma M\to S^4$ on $H_4$ is then an isomorphism on homotopy groups through degree $4$ by Whitehead.
    With $\Sigma M$ a $4$-dimensional CW-complex, $f$ is a homotopy equivalence.

Authored by **Codex 5.3 Spark Extra High**.
:::
