---
schema: qual/card@1
id: P-MZZJH
kind: problem
title: Genus of an $n$-sheeted cover of a closed surface
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Surfaces
  - Euler Characteristic
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Prove that if $p: M_g \to M_h$ is an $n$-sheeted covering space between connected, closed, orientable surfaces of genus $g$ and $h$, then:
$$g = n(h - 1) + 1.$$
:::

::: solution
**Goal:** Prove the genus formula $g = n(h-1) + 1$ (unramified Riemann–Hurwitz formula) for $n$-sheeted covering spaces $M_g \to M_h$.

<1>1. Euler Characteristic of Closed Orientable Surfaces:
    *Proof:*
    <2>1. A closed orientable surface of genus $g$, denoted $M_g$, has Euler characteristic:
        $$\chi(M_g) = 2 - 2g.$$
    <2>2. Similarly, for the base surface $M_h$ of genus $h$:
        $$\chi(M_h) = 2 - 2h.$$

<1>2. Multiplicativity of Euler Characteristic under Covering Spaces:
    *Proof:*
    <2>1. Triangulate the base surface $M_h$ with a finite CW-complex structure (simplicial complex) consisting of $V$ vertices (0-cells), $E$ edges (1-cells), and $F$ faces (2-cells), chosen fine enough so that each open cell is evenly covered by the covering projection $p: M_g \to M_h$.
    <2>2. The Euler characteristic of $M_h$ is:
        $$\chi(M_h) = V - E + F.$$
    <2>3. Because $p$ is an $n$-sheeted covering map, the preimage of each $k$-cell in $M_h$ consists of exactly $n$ disjoint, homeomorphic $k$-cells in $M_g$.
    <2>4. Thus the induced CW-decomposition on the covering space $M_g$ has:
        $$V' = n V \text{ vertices}, \quad E' = n E \text{ edges}, \quad F' = n F \text{ faces}.$$
    <2>5. The Euler characteristic of $M_g$ is:
        $$\chi(M_g) = V' - E' + F' = n V - n E + n F = n (V - E + F) = n \chi(M_h).$$

<1>3. Solving for the Genus $g$:
    *Proof:*
    <2>1. Substitute the genus-Euler characteristic formulas into $\chi(M_g) = n \chi(M_h)$:
        $$2 - 2g = n (2 - 2h).$$
    <2>2. Divide both sides by 2:
        $$1 - g = n (1 - h) = -n (h - 1).$$
    <2>3. Multiply by $-1$:
        $$g - 1 = n (h - 1).$$
    <2>4. Add 1 to both sides:
        $$g = n (h - 1) + 1.$$

<1>4. Geometric Examples and Sanity Checks:
    *Proof:*
    <2>1. For the torus $T^2$ ($h = 1$): $g = n(1 - 1) + 1 = 1$. Any $n$-fold cover of the torus is another torus $T^2$.
    <2>2. For the sphere $S^2$ ($h = 0$): $g = n(0 - 1) + 1 = 1 - n$. Since genus $g \ge 0$, this forces $n = 1$ (the sphere is simply connected, having no non-trivial connected covering spaces).
    <2>3. For genus $h = 2$ and a 3-fold cover ($n = 3$): $g = 3(2 - 1) + 1 = 4$.

<1>5. Conclusion:
    The genus of an $n$-sheeted cover is $g = n(h - 1) + 1$. Q.E.D.
:::
