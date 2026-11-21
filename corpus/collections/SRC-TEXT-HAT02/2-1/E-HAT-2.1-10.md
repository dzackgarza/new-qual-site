---
schema: qual/card@1
id: E-HAT-2.1-10
kind: problem
title: Quotient of paired triangles is a surface with a Delta-complex structure
classification:
  areas:
  - topology
  topics:
  - Homology
  - Surfaces
  - Simplicial Complexes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.1, Exercise 10; the stored statement matches the corrected online text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read (a): the link at a quotient vertex is a finite connected 2-regular graph, hence a circle, and the neighbourhood is its cone, a disk. Part (b) rests on a cited branching theorem whose hypotheses the text checks against the identification data.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Part (a) read and checked independently; part (b) read and its citation verified for scope. (a)
    The three local models are right: triangle interiors are disks, an interior point of a paired
    edge gets two half-disks glued along their diameters, and at a quotient vertex the link is a
    finite graph in which every vertex has degree two — because each triangle corner has exactly one
    partner — and which is connected, so it is a circle and its cone is a disk. This is the standard
    argument and it is complete, including the absence of boundary. (b) is not proved here: it is
    referred to a branching lemma for ideal triangulations of closed surfaces from a paper on
    deformation of hyperbolic triangulations, and the hypothesis `chi(X) - #V < 0` is discharged by
    `F = 2(#V - chi(X)) > 0`, which is `3F = 2E` substituted into `chi = V - E + F`. That is
    consistent, and the citation is to a named lemma rather than to folklore, but the result is
    research-level for an exercise the book marks as more difficult, so the claim of (b) should be
    read as a citation. No correction was needed.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure under the corrected partition rule (this card was outside the old split-on-first-hyphen residue). Part (a) is the card's own: the interior and edge-interior cases, the plain fact that the link at a vertex is finite and 2-regular (each edge-germ at v is a side of exactly two corners, possibly of the same corner for a loop), its connectivity, and the cone-on-the-link description. What I added to the argument: the counting with multiplicity in the 2-regular statement, and the reason L_v is connected (a component is a quotient of finitely many triangles glued pairwise along edge-sides, and each such gluing that puts two vertices over v joins the corresponding corners). Part (b) remains a citation, as the card had it: Benedetti arXiv:1903.12596v1 Lemma 2.14 p. 7, with the definitions on p. 1 matching this exercise, and the paper's standing hypothesis chi(S) - #V < 0 now verified on the card (F = 2k, E = 3k, chi - #V = -k). The lemma's proof is not reproduced, which the card states.
---

::: {.problem}
(a) Show the quotient space of a finite collection of disjoint 2-simplices obtained by identifying pairs of edges is always a surface, locally homeomorphic to $\RR^2$.

(b) Show the edges can always be oriented so as to define a $\Delta$-complex structure on the quotient surface.
[This is more difficult.]
:::

::: {.solution}
Part (a) is the card's own argument. Part (b) is not proved on this card: it is the published lemma cited below, whose hypotheses are checked here — **Benedetti, *On ideal triangulations of surfaces up to branched transit equivalences*, arXiv:1903.12596v1, Lemma 2.14** (with the definitions the paper fixes at its opening for these objects).

Write $X$ for the quotient of the finite disjoint union of $2$-simplices by the chosen pairs of edges, and for a point $x\in X$ let $L_v$, at a quotient vertex $v$, be the graph whose vertices are the germs at $v$ of the edges of the triangulation and whose edges are the corners of the triangles at $v$.

::: pf

::: {.pf-step #interior}
A point in the interior of a $2$-simplex, or in the interior of a quotient edge, has a neighbourhood homeomorphic to an open disc.

::: pf-proof
An interior point of a simplex has a disc neighbourhood inside that simplex, and no identification touches it. An interior point of an edge lies in the interior of exactly two edge-sides, one from each of the two triangles glued along that edge; each side contributes a half-disc whose diameter contains the point, and the two half-discs are glued along that diameter, so their union is a disc.
:::

:::

::: {.pf-step #regular}
$L_v$ is a finite graph in which every vertex has degree $2$, counted with multiplicity.

::: pf-proof
Finitely many simplices give finitely many germs and corners. A vertex of $L_v$ is a germ of an edge $e$ at $v$; the edge-sides of $e$ are exactly two, and each of them is a side of exactly one triangle corner at $v$ (possibly both are sides of the same corner, when $e$ is a loop at $v$), so exactly two corners of $L_v$ are incident with that germ.
:::

:::

::: {.pf-step #connected}
$L_v$ is connected.

::: pf-proof
Two corners at $v$ that are corners of the same triangle are joined by the edge of $L_v$ they cut out. Two triangles whose closures contain $v$ and that share an edge-side $s$ at $v$ contribute corners sharing the germ of $s$, hence lie in the same component of $L_v$. Since the component of $X$ containing $v$ is a quotient of finitely many triangles glued pairwise along edge-sides, and every such gluing that puts two triangle vertices over $v$ joins their corners in $L_v$, all corners at $v$ lie in one component.
:::

:::

::: {.pf-step #vertex}
Every point of $X$ has a neighbourhood homeomorphic to $\RR^2$, and $X$ has no boundary.

::: pf-proof
At an interior point this is step [](#interior){.pf-ref}. At a quotient vertex $v$, a small regular neighbourhood is the cone on the link $L_v$: intersecting with a small sphere about $v$ gives $L_v$ itself. By steps [](#regular){.pf-ref} and [](#connected){.pf-ref}, $L_v$ is a finite connected $2$-regular graph, hence a cycle, hence homeomorphic to $S^1$; the cone on $S^1$ is a closed disc, with $v$ mapping to its cone point. So every point has a disc neighbourhood, which is to say $X$ is locally homeomorphic to $\RR^2$ and no point has a half-disc neighbourhood. This is part (a).
:::

:::

::: {.pf-step #hypothesis}
For a component built from $2k$ triangles, $\chi-\#V=V-k<0$.

::: pf-proof
The $6k$ edge-sides are paired, so $E=3k$; $F=2k$; hence $\chi=V-E+F=V-3k+2k=V-k$ for the component's vertex set $V$, so $\chi-\#V=-k$, which is negative because $k\ge1$.
:::

:::

::: {.pf-step #partb}
The edges can be oriented so as to define a $\Delta$-complex structure on $X$.

::: pf-proof
Benedetti's *branching* of a triangulation is "a system of edge orientations which lifted to every abstract triangle of $T$ is induced by a (local) ordering of the vertices, so that every edge goes towards the biggest endpoint", and he notes that this is "equivalently $b$ promotes $T$ to be a $\Delta$-complex accordingly with Chapter 2 of [Hatcher]". His ideal triangulation is exactly the data here: abstract triangles glued along their abstract edges in pairs with no edge left unglued, self- and multiple adjacencies allowed, viewed together with its vertex set. So each component of $X$ with its quotient vertices is an ideal triangulation of a closed surface, and by step [](#hypothesis){.pf-ref} the paper's standing hypothesis $\chi(S)-\#V<0$ holds for it. Lemma 2.14 of the paper states that every ideal triangulation of $(S,V)$ can be branched; applying it to each component and orienting the edges accordingly gives exactly Hatcher's $\Delta$-complex condition, which is part (b). The proof of the lemma — flips and b-flips from one branched triangulation per surface with few vertices, then b-bubbles — is not reproduced here.
:::

:::

:::
:::
