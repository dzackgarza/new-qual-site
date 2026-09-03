---
schema: qual/card@1
id: E-3BSN7
kind: problem
title: Triangular schemes for two collections of four triangles
classification:
  areas:
  - topology
  topics:
  - Classification of Surfaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

What space is indicated by each of the following labelling schemes for a collection of four triangular regions?

(a) $abc$, $dae$, $bef$, $cdf$

(b) $abc$, $cba$, $def$, $dfe^{-1}$
:::

::: solution
**Goal:** Identify the topological surfaces represented by each of the two triangular labeling schemes.

<1>1. Part (a): Scheme $abc, dae, bef, cdf$.
    The space is the **Klein bottle** ($K^2 \cong \#^2 \mathbb{R}P^2$).
    *Proof:*
    <2>1. **Faces and Edges:** There are $F = 4$ triangular faces and $E = 6$ edge identification classes ($a, b, c, d, e, f$).
    <2>2. **Vertex counting:**
        - Label the vertices of $T_1(abc)$ as $v_1 \xrightarrow{a} v_2 \xrightarrow{b} v_3 \xrightarrow{c} v_1$.
        - Trace identifications:
          - Class 1: $\{v_1, w_2, z_2, w_1, u_3, z_3\}$.
          - Class 2: $\{v_2, w_3, u_2, v_3, z_1, u_1\}$.
        - Thus there are exactly $V = 2$ vertex equivalence classes.
    <2>3. **Euler characteristic:**
        $$\chi = V - E + F = 2 - 6 + 4 = 0.$$
    <2>4. **Orientability:** The edge $a$ appears with identical cyclic orientation in both $T_1(abc)$ and $T_2(dae)$. Gluing along $a$ creates a non-orientable Möbius band region.
    <2>5. **Classification:** The unique closed, connected non-orientable surface with Euler characteristic $\chi = 0$ is the Klein bottle $K^2$.

<1>2. Part (b): Scheme $abc, cba, def, dfe^{-1}$.
    The space is the disjoint union of the **2-sphere** and the **real projective plane**: $S^2 \sqcup \mathbb{R}P^2$.
    *Proof:*
    <2>1. **Decomposition into disjoint components:** The triangles $T_1(abc)$ and $T_2(cba)$ only involve edges $\{a, b, c\}$, while $T_3(def)$ and $T_4(dfe^{-1})$ only involve edges $\{d, e, f\}$. Since no edges or vertices are shared between the two pairs, the resulting space is the topological disjoint union $X = X_1 \sqcup X_2$.
    <2>2. **Component $X_1 = T_1 \cup T_2$:**
        - $T_1$ has boundary word $abc$ and $T_2$ has boundary word $cba = (abc)^{-1}$.
        - Identifying the three boundary edges of $T_1$ with the oppositely oriented boundary edges of $T_2$ glues two closed 2-disks along their boundary circles via an orientation-reversing homeomorphism, yielding the 2-sphere $S^2$.
    <2>3. **Component $X_2 = T_3 \cup T_4$:**
        - Gluing $T_3(def)$ and $T_4(dfe^{-1})$ along the shared edges $d$ and $f$ produces a 2-gon with remaining boundary edges identified as $e e$ (or $e \sim e^{-1}$).
        - A 2-gon with boundary scheme $e^2$ is the standard polygonal presentation of the real projective plane $\mathbb{R}P^2$.
    <2>4. **Conclusion:** $X \cong S^2 \sqcup \mathbb{R}P^2$. Q.E.D.
:::
