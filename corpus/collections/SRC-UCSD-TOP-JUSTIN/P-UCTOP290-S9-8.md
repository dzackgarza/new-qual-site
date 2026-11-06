---
schema: qual/card@1
id: P-UCTOP290-S9-8
kind: problem
title: A torus triangulation needs at least fourteen triangles
classification:
  areas:
  - topology
  topics:
  - Triangulations
  - Euler Characteristic
  - Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 9, Problem 8 in its checked-in extraction.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against UCSD Math 290 Fall 2014 problem sheet 9, problem 8
    (assets/attachments/UCSD_290_F14_sheet9.pdf, printed page 267), from the
    checked-in extraction and a 300 dpi render. The printed problem asks for a
    proof that there are no triangulations of the torus with fewer than fourteen
    2-simplices and for one with fourteen. The card states exactly this, so no
    repair was needed. Checked in the render: the printed sentence begins "A
    triangulation of a topological space X is a simplicial complex K together
    with a homeomorphism h: X -> |K|", which is what the card's hypothesis uses.
---

::: {.problem}
Prove that a simplicial triangulation of the
torus has at least fourteen two-simplices,
and exhibit one with fourteen.
:::

::: {.solution}

Let $K$ be a simplicial complex triangulating the torus, with $V$ vertices,
$E$ edges and $F$ faces.

::: pf

::: {.pf-step #count}

$3F=2E$ and, since $\chi(T^2)=0$, $E=3V$ and $F=2V$.

::: pf-proof

A triangulation of a closed surface has every edge in exactly two triangles,
since the link of an edge must be a circle; counting incidences of edges with
triangles gives $2E=3F$. The Euler characteristic of a triangulated torus is
$V-E+F=0$, so substituting $E=3F/2$ gives $V=F/2$, that is $F=2V$ and $E=3V$.

:::

:::

::: {.pf-step #bound}

$V\ge7$, hence $F=2V\ge14$.

::: pf-proof

In a simplicial complex a set of two vertices spans at most one edge, so
$E\le\binom{V}{2}=V(V-1)/2$. With $E=3V$ this gives $6V\le V(V-1)$, and since
$V>0$ we may divide by $V$ to get $6\le V-1$, that is $V\ge7$. Then
$F=2V\ge14$ by step [](#count){.pf-ref}.

:::

:::

::: {.pf-step #example}

The seven vertices $\ZZ/7$ with the fourteen triangles $\{i,i+1,i+3\}$ and
$\{i,i+2,i+3\}$, indices modulo $7$, form a simplicial complex which is a
closed connected surface of Euler characteristic $0$.

::: pf-proof

Both families are orbits of the cyclic shift $i\mapsto i+1$, so the complex is
invariant under that shift, which permutes the vertices cyclically and hence
acts transitively on them; consequently all vertex links are isomorphic and
the edge conditions can be checked on one representative of each orbit of
edges. The pairs of vertices fall into the three orbits $\{i,i+1\}$,
$\{i,i+2\}$, $\{i,i+3\}$, which are all $\binom72=21$ pairs since the
differences $\pm1,\pm2,\pm3$ exhaust the nonzero residues modulo $7$; each
pair lies in exactly two of the listed triples, as $\{0,1\}$ lies in
$\{0,1,3\}$ and $\{5,0,1\}$, the pair $\{0,2\}$ in $\{0,2,3\}$ and
$\{6,0,2\}$, and the pair $\{0,3\}$ in $\{0,1,3\}$ and $\{0,2,3\}$. The link
of the vertex $0$ consists of the pairs opposite $0$ in the six triangles
containing it, namely $13,32,26,64,45,51$, a single six-cycle; so the link of
every vertex is a circle and the complex is a closed surface. It is connected,
since the triangles $\{0,1,3\}$ and $\{0,2,3\}$ share an edge and the shift
moves them around. Counting, $V=7$, $E=21$, $F=14$, so $\chi=7-21+14=0$.

:::

:::

::: {.pf-step #torus}

The example is orientable, hence a torus; so the torus does have a
triangulation with fourteen triangles.

::: pf-proof

Orient $\{i,i+1,i+3\}$ as $(i,i+1,i+3)$ and $\{i,i+2,i+3\}$ as $(i+3,i+2,i)$,
the reverse of its listed order. Take an edge, say $\{1,3\}$, carried by the
triangles $\{0,1,3\}$ and $\{1,3,4\}$: the first orientation induces $1\to3$
on it, and the second, being $(4,3,1)$ on $\{1,3,4\}$, induces $3\to1$; the
two induced orientations are opposite. The same computation for the
representatives $\{0,1\}$, $\{0,2\}$, $\{0,3\}$ of the three edge orbits,
together with the invariance of the orientations under the cyclic shift, shows
that every edge is induced with opposite orientations by its two triangles; so
the surface is orientable. An orientable closed connected surface with
$\chi=0$ is a torus, by the classification of surfaces.

:::

:::

:::


:::
