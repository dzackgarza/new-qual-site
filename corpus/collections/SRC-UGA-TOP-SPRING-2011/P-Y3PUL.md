---
schema: qual/card@1
id: P-Y3PUL
kind: problem
title: $\RP^2\vee S^1$ is not homotopy equivalent to a compact surface
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Surfaces
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Show that $\RP^2 \lor S^1$ is *not* homotopy equivalent to a compact surface (possibly with boundary).
:::

::: solution
**Goal:** Show no compact surface $S$ is homotopy equivalent to $\RP^2\vee S^1$.

<1> Assume a compact surface $S$ is homotopy equivalent to $X:=\RP^2\vee S^1$.
    *Proof:*
    <2>1. Then $\pi_1(S)\cong \pi_1(X)$ and
        $$\pi_1(X)\cong \pi_1(\RP^2)*\pi_1(S^1)\cong \ZZ/2 * \ZZ.$$
    <2>2. Abelianizing gives
        $$H_1(X)\cong \ZZ/2\oplus \ZZ.$$

<1> Exclude surfaces with boundary.
    *Proof:*
    <2>1. If a compact surface has non-empty boundary, its fundamental group is free.
    <2>2. A free group has no nontrivial torsion elements, but $\ZZ/2 * \ZZ$ does.
    <2>3. So $S$ has empty boundary.

<1> Exclude closed orientable and closed non-orientable possibilities.
    *Proof:*
    <2>1. For closed orientable surfaces of genus $g\ge1$, $\pi_1$ is torsion-free.
    <2>2. For closed non-orientable surfaces of genus $\ge2$, $\pi_1$ is torsion-free as well.
    <2>3. The group $\ZZ/2*\ZZ$ has a torsion element of order $2$, so these cases are impossible.
    <2>4. The remaining closed surfaces are $S^2$ and $\RP^2$.
    <2>5. $H_1(S^2)=0$ and $H_1(\RP^2)\cong \ZZ/2$, neither matches $H_1(X)\cong \ZZ/2\oplus\ZZ$.

<1> Therefore no compact surface has the same homotopy type as $X$.

Authored by **Codex 5.3 Spark Extra High**.
:::

::: {.solution}
<1>1. $X$ CW.
Proof: cellular.

<1>2. Q.E.D.
Proof: <1>1.
:::
