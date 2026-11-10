---
schema: qual/card@1
id: E-HAT-2.C-8
kind: problem
title: At most countably many homotopy classes of maps between simplicial spaces
classification:
  areas:
  - topology
  topics:
  - Simplicial Approximation
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.C, Exercise 8; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the simplicial, Lefschetz-trace, or surface argument against the preceding section results.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §2.C Exercise 8, printed page
    184; the statement matches word for word. Proof checked: K is a finite simplicial
    complex and L finite or countable, a simplicial map from a subdivision of K is
    determined by its values on the finitely many vertices, so for each r there are
    at most countably many such maps and the union over r is countable, and every map
    K → L is homotopic to one of these by the simplicial approximation theorem
    (Theorem 2C.1, p. 179). No defect.
- event: solution-written
  by: claude
  date: 2026-11-08
  note: >-
    Makes the published argument explicit in the solution: Theorem 2C.1 on pp.178-179 supplies
    a simplicial representative after finitely many barycentric subdivisions of the finite
    domain. Each sd^rK has finitely many vertices, so there are countably many maps into L for
    each r, and the union over r is countable. Homotopy equivalences X ≃ K and Y ≃ L transfer
    this bound to [X,Y]. The source paragraph is kept with the mathematics, as in Hatcher's
    own remark that a simplicial map is determined by its vertex images.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Identified and read the complete published solution: Morten Poulsen, Allen Hatcher: Algebraic
    Topology (3 November 2006), Ex.2.C.8, printed p.30, in the 33-page archived AT-ex.pdf.
    Its argument is the bijection [X,Y] with [K,L], the simplicial representatives over all
    iterated subdivisions, and the countable union of countable vertex-map sets. Checked the
    rendered PDF page directly against Hatcher p.184. Poulsen's K in the clashing typo for the
    codomain of psi_Y is corrected to L here; the four steps otherwise retain his proof verbatim
    in expanded form. The complete #105 source obligation is discharged, not merely a theorem
    citation supplied by the agent.
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Re-read against the readable copy of the set, `tmp/sources/poulsen-at-ex.pdf` (33 pages, 441,762
    bytes; the earlier `hatcher-solutions-morten-poulsen.pdf` was a corrupt duplicate and has been
    removed). Exercise 2.C.8 sits on printed p. 30, whose folio is the last line of that PDF page, so
    the card's page locator is right. Two slips in the print, both now described on the card and
    neither reproduced by its proof: the homotopy inverse $\psi_Y$ is printed with codomain $K$
    where $L$ is required, and the countable bound's factor $V_L^{V_{\mathrm{sd}^nK}}$ is left
    unexplained although it must be read as the set of vertex functions. Every remaining step of the
    card is Poulsen's, expanded.
---
---

::: {.problem}
Let $X$ be homotopy equivalent to a finite simplicial complex and let $Y$ be homotopy equivalent to a finite or countably infinite simplicial complex.
Using the simplicial approximation theorem, show that there are at most countably many homotopy classes of maps $X \to Y$.
:::

::: {.solution}
The complete published argument is **Morten Poulsen, *Allen Hatcher: Algebraic Topology* (3 November 2006), Exercise 2.C.8, printed p. 30** — `tmp/sources/poulsen-at-ex.pdf`, 33 pages, 441,762 bytes, whose page 30 is the PDF page of the same number here (the printed folio $30$ closes the page carrying Exercises 2.C.8 and 2.C.9). It transports $[X,Y]$ to $[K,L]$, applies simplicial approximation over all iterated subdivisions, and counts the vertex maps. The theorem used for the simplicial-representative step is **Hatcher's Theorem 2C.1, printed pp. 178--179**: after finitely many barycentric subdivisions of the finite domain, every continuous map is homotopic to a simplicial map. Poulsen's text has two slips, neither of which the proof below reproduces. First, his homotopy inverse is printed as $\psi_Y:K\to Y$ although $\psi_Y$ must run $L\to Y$ for the composites $\varphi_Yf\psi_X$ and $\psi_Yf\varphi_X$ to be defined; the proof below uses the mathematically required codomain. Second, his displayed bound writes the union $\bigcup_{n\in\NN}V_L^{V_{\mathrm{sd}^nK}}$ without saying what $V_L^{V_{\mathrm{sd}^nK}}$ denotes: it is the set of vertex maps, that is, of functions from the vertices of $\mathrm{sd}^nK$ to the vertices of $L$. The proof below states this, since it is what makes each factor countable.

Choose homotopy equivalences
$$
X\simeq K,
\qquad
Y\simeq L,
$$
where $K$ is a finite simplicial complex and $L$ is finite or countable.

::: pf

::: pf-step

For each $r\ge0$, there are only countably many simplicial maps
$$
\operatorname{sd}^rK\to L.
$$

::: pf-proof

The complex $\operatorname{sd}^rK$ has finitely many vertices, while $L$ has at most countably many vertices. A simplicial map is determined by its map on vertices, and every function from the vertex set of $\operatorname{sd}^rK$ to the vertex set of $L$ determines a simplicial map, namely its linear extension. So the simplicial maps $\operatorname{sd}^rK\to L$ correspond exactly to the vertex functions $V_{\operatorname{sd}^rK}\to V_L$, a set of cardinality $|V_L|^{|V_{\operatorname{sd}^rK}|}$, which is countable because $V_{\operatorname{sd}^rK}$ is finite and $V_L$ is at most countable.

:::

:::

::: {.pf-step #s2}

The union, over all $r\ge0$, of the sets of such simplicial maps is countable.

::: pf-proof

It is a countable union of countable sets.

:::

:::

::: {.pf-step #s3}

Every homotopy class of maps $K\to L$ is represented by one of these simplicial maps.

::: pf-proof

By the simplicial approximation theorem, every continuous map $K\to L$ is homotopic to a simplicial map after some iterated barycentric subdivision of the finite domain $K$.

:::

:::

::: pf-step

Therefore there are at most countably many homotopy classes of maps $X\to Y$.

::: pf-proof

Composition with fixed homotopy equivalences and their homotopy inverses gives a bijection
$$
[X,Y]\cong[K,L].
$$
By steps [](#s2){.pf-ref} and [](#s3){.pf-ref} the latter set is at most countable.

:::

:::

:::

:::
