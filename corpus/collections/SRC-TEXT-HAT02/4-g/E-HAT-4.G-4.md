---
schema: qual/card@1
id: E-HAT-4.G-4
kind: problem
title: Nerve lemma for subcomplex covers of CW complexes
classification:
  areas:
  - topology
  topics:
  - CW Complexes
  - Homotopy Equivalence
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Statement repaired against Hatcher's printed text: the card had dropped printed matter
    (a bracketed hint or pointer, or a printed sentence) that an audit located by word-by-word
    comparison with tmp/hat/AT.txt, and that this session re-verified at the cited lines before
    applying the repair. The restored text is the printed wording and the mathematics of the
    statement is otherwise unchanged.
---

::: {.problem}
Show that Proposition 4G.2 and its corollary hold also for CW complexes and covers by families of subcomplexes.
[CW complexes are paracompact; see [VBKT].]
:::

::: {.solution}
Let $X=\bigcup_{i\in I}X_i$ be a CW complex covered by subcomplexes. For each nonempty finite set $\sigma\subset I$, put $X_\sigma=\bigcap_{i\in\sigma}X_i$. Every $X_\sigma$ is again a subcomplex. Form the realization $\Delta X_{\mathcal U}$ of this diagram of intersections, and let
$$
p:\Delta X_{\mathcal U}\longrightarrow X
$$
be the map that forgets the simplex coordinate.

The map $p$ is a homotopy equivalence. To see this, build $X$ by its cells. The interior of each cell belongs to exactly the subcomplexes that contain that cell. Over the cell, the realization adds a simplex of choices of these subcomplexes; this simplex is contractible. Along the boundary, the choices can only increase, and the attaching maps are inclusions of subcomplexes. The homotopy gluing lemma therefore proves by cellular induction that $p$ is a homotopy equivalence. Equivalently, the realization of this diagram of subcomplex inclusions computes their union because all the inclusions are cofibrations. This is the subcomplex-cover version of Proposition 4G.2 (p. 459), the open-cover statement proved there for paracompact $X$; a CW complex is paracompact, which is what the printed hint points to.

If every nonempty $X_\sigma$ is contractible, the maps $X_\sigma\to *$ are homotopy equivalences. Proposition 4G.1 (p. 458), which says that a map of complexes of spaces whose maps on vertex and edge spaces are homotopy equivalences induces a homotopy equivalence of realizations, then gives a homotopy equivalence from $\Delta X_{\mathcal U}$ to the realization of the diagram of points, which is the nerve of the cover (Corollary 4G.3, p. 459). Combining this with $p$ gives
$$
X\simeq N(\mathcal U),
$$
the stated corollary.
:::
