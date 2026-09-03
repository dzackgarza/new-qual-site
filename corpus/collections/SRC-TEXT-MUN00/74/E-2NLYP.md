---
schema: qual/card@1
id: E-2NLYP
kind: problem
title: A presentation for the fundamental group of the connected sum of the projective plane and the torus
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Find a presentation for the fundamental group of $P^2 \# T$.
:::

::: solution
**Goal:** Compute a presentation for the fundamental group of the connected sum $P^2 \# T$ of the real projective plane $P^2$ and the 2-torus $T = T^2$.

<1>1. Cell complex and polygonal scheme construction:
    *Proof:*
    <2>1. The standard polygonal scheme for $P^2$ is a 2-gon with boundary word $a^2$, deformation retracting on a punctured disk to the loop $a$.
    <2>2. The standard polygonal scheme for $T^2$ is a 4-gon with boundary word $b c b^{-1} c^{-1}$, deformation retracting on a punctured disk to the wedge of loops $b$ and $c$.
    <2>3. The connected sum $P^2 \# T$ is formed by removing an open 2-disk from each surface and gluing along the resulting boundary circles $S^1$.
    <2>4. The resulting 2-manifold has a CW structure with:
        - One 0-cell $x_0$.
        - Three 1-cells (generating loops) $a, b, c$.
        - One 2-cell attached along the boundary path obtained by concatenating the original boundary schemes:
          $$w = a^2 b c b^{-1} c^{-1}.$$

<1>2. Presentation via Seifert-van Kampen Theorem:
    $\pi_1(P^2 \# T) \cong \langle a, b, c \mid a^2 b c b^{-1} c^{-1} = 1 \rangle$.
    *Proof:*
    <2>1. Decompose $P^2 \# T = U \cup V$ where $U \simeq P^2 \setminus \{\text{pt}\}$ and $V \simeq T^2 \setminus \{\text{pt}\}$.
    <2>2. $U$ deformation retracts to $S^1$ with $\pi_1(U) = \langle a \mid - \rangle$, and the boundary cycle corresponds to $a^2$.
    <2>3. $V$ deformation retracts to $S^1 \vee S^1$ with $\pi_1(V) = \langle b, c \mid - \rangle$, and the boundary cycle corresponds to $b c b^{-1} c^{-1}$.
    <2>4. The intersection $U \cap V \simeq S^1$ is connected, with generator $\gamma$ mapping to $a^2 \in \pi_1(U)$ and $(b c b^{-1} c^{-1})^{-1} \in \pi_1(V)$.
    <2>5. By the Seifert-van Kampen theorem, the amalgamated free product is:
        $$\pi_1(P^2 \# T) \cong \pi_1(U) *_{\pi_1(U \cap V)} \pi_1(V) \cong \langle a, b, c \mid a^2 = c b c^{-1} b^{-1} \rangle \cong \langle a, b, c \mid a^2 b c b^{-1} c^{-1} = 1 \rangle.$$

<1>3. Equivalent presentation via Dyck's Theorem:
    By Dyck's Theorem, $P^2 \# T \cong \#^3 \mathbb{R}P^2$ (the non-orientable surface of genus 3), which has the equivalent standard presentation:
    $$\pi_1(P^2 \# T) \cong \langle x, y, z \mid x^2 y^2 z^2 = 1 \rangle.$$

<1>4. Conclusion:
    A presentation for $\pi_1(P^2 \# T)$ is $\langle a, b, c \mid a^2 b c b^{-1} c^{-1} = 1 \rangle$. Q.E.D.
:::
