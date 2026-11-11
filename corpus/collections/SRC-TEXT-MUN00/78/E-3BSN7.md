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
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 78 Exercise 1, printed p. 476. Part (a) is the Klein bottle: two vertex classes, chi = 0, non-orientable. What was corrected: part (b) answered S^2 disjoint union P^2, but the pair def, dfe^{-1} gives all six vertices one class, so chi = 1 - 3 + 2 = 0, and H_1 = <d,e,f | def, dfe^{-1}> = Z + Z/2, which is the Klein bottle; the glued square is efe^{-1}f. The answer is now S^2 disjoint union K, with that computation. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
---

::: {.exercise}

What space is indicated by each of the following labelling schemes for a collection of four triangular regions?

(a) $abc$, $dae$, $bef$, $cdf$

(b) $abc$, $cba$, $def$, $dfe^{-1}$
:::

::: {.solution}

::: pf

::: pf-step

Part (a): Scheme $abc, dae, bef, cdf$.
    The space is the **Klein bottle** ($K^2 \cong \#^2 \RP^2$).
    *Proof:*

::: pf-proof

::: pf-step

**Faces and Edges:** There are $F = 4$ triangular faces and $E = 6$ edge identification classes ($a, b, c, d, e, f$).

:::

::: pf-step

**Vertex counting:**
        - Label the vertices of $T_1(abc)$ as $v_1 \xrightarrow{a} v_2 \xrightarrow{b} v_3 \xrightarrow{c} v_1$.
        - Trace identifications:
          - Class 1: $\{v_1, w_2, z_2, w_1, u_3, z_3\}$.
          - Class 2: $\{v_2, w_3, u_2, v_3, z_1, u_1\}$.
        - Thus there are exactly $V = 2$ vertex equivalence classes.

:::

::: pf-step

**Euler characteristic:**
        $$\chi = V - E + F = 2 - 6 + 4 = 0.$$

:::

::: pf-step

**Orientability:** The edge $a$ appears with identical cyclic orientation in both $T_1(abc)$ and $T_2(dae)$. Gluing along $a$ creates a non-orientable Möbius band region.

:::

::: pf-step

**Classification:** The unique closed, connected non-orientable surface with Euler characteristic $\chi = 0$ is the Klein bottle $K^2$.

:::

:::

:::

::: pf-step

Part (b): Scheme $abc, cba, def, dfe^{-1}$.
    The space is the disjoint union of the **2-sphere** and the **Klein bottle**: $S^2 \sqcup K$.
    *Proof:*

::: pf-proof

::: pf-step

**Decomposition into disjoint components:** The triangles $T_1(abc)$ and $T_2(cba)$ only involve edges $\{a, b, c\}$, while $T_3(def)$ and $T_4(dfe^{-1})$ only involve edges $\{d, e, f\}$. Since no edges or vertices are shared between the two pairs, the resulting space is the topological disjoint union $X = X_1 \sqcup X_2$.

:::

::: pf-step

**Component $X_1 = T_1 \cup T_2$:**
        - $T_1$ has boundary labels in the cyclic order $a,b,c$, while $T_2$ has them in the reverse cyclic order $c,b,a$.
        - Identifying matching edges glues the two closed 2-disks along their entire boundary circles, yielding the 2-sphere $S^2$.

:::

::: pf-step

**Component $X_2 = T_3 \cup T_4$:** Glue $T_3$ to $T_4$ first along the edges labelled $d$; the result is a square whose boundary scheme is $efe^{-1}f$, read from the free edges: $e$ on $T_3$, then $f$ on $T_3$, then the edge of $T_4$ labelled $e^{-1}$, then $f$ on $T_4$. Pasting the two $f$-edges leaves the Klein bottle, whose standard scheme is $aba^{-1}b$. The counts agree with this: the identifications $d$ give $p_1\sim q_1$, $p_2\sim q_2$; $f$ gives $p_3\sim q_2$, $p_1\sim q_3$; and $e$ gives $p_2\sim q_1$, $p_3\sim q_3$, so all six vertices of the two triangles are one class, and $\chi=V-E+F=1-3+2=0$, with $H_1=\langle d,e,f\mid def,\ dfe^{-1}\rangle\cong\ZZ\oplus\ZZ/2$ — the Klein bottle, not $P^2$, whose Euler characteristic is $1$. The reason the boundary of the quad does not reduce to a single pair $e,e$ is that the two $e$-edges are glued in opposite senses, so that after the $f$-pasting the scheme $efe^{-1}f$ stands.

**Conclusion:** $X \cong S^2 \sqcup K$. Q.E.D.

:::

:::

:::

:::

:::
