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
---

::: {.problem}
(a) Show the quotient space of a finite collection of disjoint 2-simplices obtained by identifying pairs of edges is always a surface, locally homeomorphic to $\RR^2$.

(b) Show the edges can always be oriented so as to define a $\Delta$-complex structure on the quotient surface.
[This is more difficult.]
:::

::: {.solution}
Let $X$ be the quotient. A point in the interior of a triangle has a disk neighborhood. An interior point of a quotient edge has two half-disk neighborhoods, one from each paired edge, glued along their diameter; their union is a disk.

At a quotient vertex $v$, take a short segment across each triangle corner mapping to $v$. These segments form the link $L_v$. Each endpoint is paired with exactly one other endpoint by an edge identification, so every vertex of this finite graph has degree two. The graph is connected: the paired-edge identifications that make the original triangle vertices represent the same quotient vertex also join their corner segments. Hence $L_v$ is a connected finite $2$-regular graph, so $L_v\cong S^1$. A small neighborhood of $v$ is the cone on $L_v$ and is a disk. Thus every point of $X$ has a neighborhood homeomorphic to $\RR^2$, and there is no boundary. This proves (a).

Statement (b) is Lemma 2.14 of Benedetti, arXiv:1903.12596v1, p. 7, whose definitions are those of this exercise (p. 1); the proof is not reproduced here. In Benedetti, *On ideal triangulations of surfaces up to branched transit equivalences*, arXiv:1903.12596v1, p. 1, a **branching** of a triangulation is "a system of edge orientations which lifted to every abstract triangle of $T$ is induced by a (local) ordering of the vertices, so that every edge goes towards the biggest endpoint", and the author adds that "equivalently $b$ promotes $T$ to be a $\Delta$-complex accordingly with Chapter 2 of [Hatcher]". An **ideal triangulation** there is a possibly loose triangulation, self- and multiple edge adjacency allowed, with vertex set $V$, viewed as "assembling abstract triangles by gluing their abstract edges in pairs in such a way that no edge remains unglued" (p. 1); that is exactly the data of this exercise, so each connected component of $X$ with its quotient vertices is an ideal triangulation of a closed surface.

With those definitions, the existence of the orientations required in (b) is Lemma 2.14 of that paper, p. 7: *every ideal triangulation $T$ of $(S,V)$ can be branched.* The proof reduces by Theorem 1.1 (connectivity of ideal triangulations under flips, p. 1) and by the fact that every naked flip can be enhanced to a b-flip, to exhibiting one branched triangulation for each surface with the minimal number of vertices, and then raises the number of vertices by b-bubbles; the individual constructions are given for the sphere, the projective plane, the Klein bottle, the torus and, through the "bricks" of Figures 3 and 4 (pp. 6–7), for all remaining orientable and non-orientable surfaces. The figures carry those constructions and are not reproduced here.

The paper's standing hypothesis $\chi(S)-\#V<0$ holds for every component of $X$: a component built from $2k$ triangles whose $6k$ edge-sides are paired into edges has $F=2k$, $E=3k$, hence $\chi=V-3k+2k=V-k$ and $\chi-\#V=-k<0$. Applying Lemma 2.14 to each component gives the edge orientations, and by the definition quoted above those orientations satisfy Hatcher's $\Delta$-complex condition, which is statement (b).
:::
