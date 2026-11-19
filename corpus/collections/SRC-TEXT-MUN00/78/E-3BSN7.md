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
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Munkres §78 Exercise 1, printed p. 476. Searched outside the checkout for issue #146; the record is
    tmp/sources/mse-searches-146.md. No source was saved. The queries were the Stack Exchange advanced
    search "four triangular regions labelling schemes" (no hits) and the similar-question search from "What
    surface is given by labelling scheme of four triangles" (15 items), none of which treats four triangles
    in this form; the GitHub code search "munkres labelling scheme" returned no solutions file. The card
    keeps its own proof. Its answer to (b) was corrected in the pass of #129: the triangles def and dfe^{-1}
    give one vertex class, chi = 0 and H_1 = Z + Z/2, so the second component is the Klein bottle and the
    answer S^2 sqcup K; that correction stands.
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 78 Exercise 1, printed p. 476. Part (a) is the Klein bottle: two vertex classes, chi = 0, non-orientable. What was corrected: part (b) answered S^2 disjoint union P^2, but the pair def, dfe^{-1} gives all six vertices one class, so chi = 1 - 3 + 2 = 0, and H_1 = <d,e,f | def, dfe^{-1}> = Z + Z/2, which is the Klein bottle; the glued square is efe^{-1}f. The answer is now S^2 disjoint union K, with that computation. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the two containers state why their subclaims suffice, and the 8
    leaf steps that asserted a claim with no justification each carry a sentence deriving it. The
    asterisked Proof: lines inside the two part headings were removed and the trailing Q.E.D. dropped,
    because the filter labels the last step itself. Both vertex counts were re-derived this pass rather
    than trusted: for (a) the labels pair v1 with w2 and v2 with w3, v2 with u1 and v3 with u2, v3 with
    z1 and v1 with z2, w1 with z2 and w2 with z3, w3 with u2 and w1 with u3, u3 with z3 and u1 with z1,
    giving exactly two classes of six vertices, so chi = 2 - 6 + 4 = 0; for (b) the labels d, f and
    e (the last with opposite orientations) chain all six vertices into one class, so chi = 1 - 3 + 2 =
    0 and the abelianization of <d,e,f | def, dfe^{-1}> is Z + Z/2. Non-orientability of (a) is read off
    the agreeing cyclic order of the label a, and the classification is Theorem 77.5 of Munkres. Checked
    against Munkres, Topology (2000), section 78 Exercise 1, printed p. 476; no complete published
    solution is known for it, as the 2026-11-11 event records. Nothing in the statement was changed.
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

::: pf-proof
The subclaims count the cells, identify the two vertex classes, and then apply the classification of surfaces through the Euler characteristic and orientability.

::: pf-step
**Faces and Edges:** There are $F = 4$ triangular faces and $E = 6$ edge identification classes ($a, b, c, d, e, f$).

::: pf-proof
Four triangles are displayed, and the six letters $a,\dots,f$ each occur exactly twice among them, so the identifications fall into six classes of edges.
:::

:::

::: pf-step
**Vertex counting:**
        - Label the vertices of $T_1(abc)$ as $v_1 \xrightarrow{a} v_2 \xrightarrow{b} v_3 \xrightarrow{c} v_1$.
        - Trace identifications:
          - Class 1: $\{v_1, w_2, z_2, w_1, u_3, z_3\}$.
          - Class 2: $\{v_2, w_3, u_2, v_3, z_1, u_1\}$.
        - Thus there are exactly $V = 2$ vertex equivalence classes.

::: pf-proof
Write the vertices of the four triangles as $v_1,v_2,v_3$ (for $abc$), $w_1,w_2,w_3$ (for $dae$), $u_1,u_2,u_3$ (for $bef$) and $z_1,z_2,z_3$ (for $cdf$), in the cyclic order of the labels, so that in each triangle the first edge runs from the first vertex to the second, the second from the second to the third, and the third from the third to the first.

Reading the identifications off the labels, with equal orientation on both occurrences: $a$ pairs $v_1$ with $w_2$ and $v_2$ with $w_3$; $b$ pairs $v_2$ with $u_1$ and $v_3$ with $u_2$; $c$ pairs $v_3$ with $z_1$ and $v_1$ with $z_2$; $d$ pairs $w_1$ with $z_2$ and $w_2$ with $z_3$; $e$ pairs $w_3$ with $u_2$ and $w_1$ with $u_3$; $f$ pairs $u_3$ with $z_3$ and $u_1$ with $z_1$.

Chaining these gives $\{v_1, w_2, z_3, u_3, w_1, z_2\}$ as one class and $\{v_2, w_3, u_2, v_3, z_1, u_1\}$ as the other, and no relation joins the two: there are exactly two vertex classes.
:::

:::

::: pf-step
**Euler characteristic:**
        $$\chi = V - E + F = 2 - 6 + 4 = 0.$$

::: pf-proof
Substituting the three counts just made into $\chi=V-E+F$.
:::

:::

::: pf-step
**Orientability:** The edge $a$ appears with identical cyclic orientation in both $T_1(abc)$ and $T_2(dae)$. Gluing along $a$ creates a non-orientable Möbius band region.

::: pf-proof
A triangulated surface is orientable only if every edge identification reverses the cyclic order of the two triangles along it, since an orientation would have to agree on the two sides of each edge. Along $a$ the two orders agree, so a neighbourhood of that edge is a Möbius band and the surface is non-orientable.
:::

:::

::: pf-step
**Classification:** The unique closed, connected non-orientable surface with Euler characteristic $\chi = 0$ is the Klein bottle $K^2$.

::: pf-proof
By the classification of closed surfaces (Munkres, Theorem 77.5), a closed connected surface is determined up to homeomorphism by its orientability and its Euler characteristic. The connected sum of $k$ projective planes has $\chi = 2-k$, so $\chi=0$ forces $k=2$, which is the Klein bottle.
:::

:::

:::

:::

::: pf-step
Part (b): Scheme $abc, cba, def, dfe^{-1}$.
The space is the disjoint union of the **2-sphere** and the **Klein bottle**: $S^2 \sqcup K$.

::: pf-proof
The subclaims split the scheme into its two independent halves and identify each.

::: pf-step
**Decomposition into disjoint components:** The triangles $T_1(abc)$ and $T_2(cba)$ only involve edges $\{a, b, c\}$, while $T_3(def)$ and $T_4(dfe^{-1})$ only involve edges $\{d, e, f\}$. Since no edges or vertices are shared between the two pairs, the resulting space is the topological disjoint union $X = X_1 \sqcup X_2$.

::: pf-proof
No letter occurs in both groups, so no edge of the first pair is identified with an edge of the second, and no vertex of one is identified with a vertex of the other; the quotient is therefore the disjoint union of the two quotients.
:::

:::

::: pf-step
**Component $X_1 = T_1 \cup T_2$:**
        - $T_1$ has boundary labels in the cyclic order $a,b,c$, while $T_2$ has them in the reverse cyclic order $c,b,a$.
        - Identifying matching edges glues the two closed 2-disks along their entire boundary circles, yielding the 2-sphere $S^2$.

::: pf-proof
The three edges of one triangle are matched with the three edges of the other in the opposite cyclic order, so the gluing identifies the two boundary circles by an orientation-reversing homeomorphism. Gluing two closed disks along their boundaries by such a homeomorphism gives the sphere: the three vertices of each become one vertex, and $V-E+F=1-3+2=0$, which for a closed connected orientable surface is $S^2$.
:::

:::

::: pf-step
**Component $X_2 = T_3 \cup T_4$:** Glue $T_3$ to $T_4$ first along the edges labelled $d$; the result is a square whose boundary scheme is $efe^{-1}f$, read from the free edges: $e$ on $T_3$, then $f$ on $T_3$, then the edge of $T_4$ labelled $e^{-1}$, then $f$ on $T_4$. Pasting the two $f$-edges leaves the Klein bottle, whose standard scheme is $aba^{-1}b$. The counts agree with this: the identifications $d$ give $p_1\sim q_1$, $p_2\sim q_2$; $f$ gives $p_3\sim q_2$, $p_1\sim q_3$; and $e$ gives $p_2\sim q_1$, $p_3\sim q_3$, so all six vertices of the two triangles are one class, and $\chi=V-E+F=1-3+2=0$, with $H_1=\langle d,e,f\mid def,\ dfe^{-1}\rangle\cong\ZZ\oplus\ZZ/2$ — the Klein bottle, not $P^2$, whose Euler characteristic is $1$. The reason the boundary of the quad does not reduce to a single pair $e,e$ is that the two $e$-edges are glued in opposite senses, so that after the $f$-pasting the scheme $efe^{-1}f$ stands.

::: pf-proof
Gluing along $d$ leaves the four free edges in the cyclic order $e$, $f$, $e^{-1}$, $f$, which is the word displayed. The vertex identifications listed are exactly those read off the three letters: matching $d$ joins the first vertex of $T_3$ to the first of $T_4$ and the second to the second, $f$ joins the third of $T_3$ to the second of $T_4$ and the first of $T_3$ to the third of $T_4$, and $e$, which occurs with opposite orientations, joins the second of $T_3$ to the first of $T_4$ and the third of $T_3$ to the third of $T_4$. Chaining them gives one class of all six vertices, hence $\chi=1-3+2=0$. The presentation is that of the fundamental group of the resulting 2-complex, and its abelianization is $\ZZ\oplus\ZZ/2$: the relation $def=1$ gives $f=e^{-1}d^{-1}$, and substituting into $dfe^{-1}=1$ gives $d^{-1}e=e^{-1}d^{-1}$, which abelianized reads $2e=0$ with $d$ free. A closed connected surface with $\chi=0$ is the torus or the Klein bottle, and the torsion in $H_1$ excludes the torus, so the component is the Klein bottle. The last sentence records why the word $efe^{-1}f$ cannot be shortened to a single pair.
:::

:::

:::

:::

:::

:::
