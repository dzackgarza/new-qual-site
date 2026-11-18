---
schema: qual/card@1
id: E-OR2SV
kind: problem
title: No two of the unit interval variants are homeomorphic
classification:
  areas:
  - topology
  topics:
  - Homeomorphisms
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §24 Exercise 1, printed p. 157, with Theorem 24.1
    and Example 4; the three parts and the bracketed hint are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 24.1, PDF p. 3. Three spaces are distinguished by
    how many points must be removed to disconnect them: one, two and none; and the halving
    maps give imbeddings (0,1) to (0,1] and back without a homeomorphism, and remove a point
    from R^n minus the origin versus R minus a point in (c). (tmp/sources/munkres-solutions-
    positron-ch3.pdf).
---

::: {.exercise}

(a) Show that no two of the spaces $(0, 1)$, $(0, 1]$, and $[0, 1]$ are homeomorphic.
[Hint: What happens if you remove a point from each of these spaces?]

(b) Suppose that there exist imbeddings $f: X \to Y$ and $g: Y \to X$.
Show by means of an example that $X$ and $Y$ need not be homeomorphic.

(c) Show that $\RR^n$ and $\RR$ are not homeomorphic if $n > 1$.
:::

::: {.solution}

The three parts follow the retained solution of **"positron0802"**, *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 24.1, PDF p. 3 (`tmp/sources/munkres-solutions-positron-ch3.pdf`); part (a) is reorganised below around the points whose removal leaves a connected space, which is what the book's hint points at. The statement was checked against Munkres, *Topology* (2000), §24 Exercise 1, printed p. 157, with Corollary 24.2 on printed p. 154 and Example 4 on printed p. 156.

::: pf

::: {.pf-step #cut-points}
(a) No two of $(0,1)$, $(0,1]$ and $[0,1]$ are homeomorphic.

:::: pf-proof

::: {.pf-step #cut-transport}
If $h\colon X\to Y$ is a homeomorphism and $p\in X$, then $h$ restricts to a homeomorphism $X-\theset{p}\to Y-\theset{h(p)}$; in particular $X-\theset{p}$ is connected exactly when $Y-\theset{h(p)}$ is.

::: pf-proof
The restriction of a homeomorphism to a subspace and its image is a homeomorphism of that subspace with the image, and $h(X-\theset{p})=Y-\theset{h(p)}$ because $h$ is a bijection. Connectedness is a topological property, so it is preserved in both directions.
:::

:::

::: {.pf-step #counts}
The numbers of points whose removal leaves a connected space are $0$ for $(0,1)$, $1$ for $(0,1]$, and $2$ for $[0,1]$.

::: pf-proof
In $(0,1)$, deleting $p$ leaves $(0,p)\cup(p,1)$, two nonempty disjoint sets open in the subspace, so no deletion leaves a connected space. In $(0,1]$, deleting $1$ leaves $(0,1)$, which is connected by Corollary 24.2 (printed p. 154), while deleting $p\neq1$ leaves $(0,p)\cup(p,1]$ with both members nonempty and open in the subspace. In $[0,1]$, deleting $0$ leaves $(0,1]$ and deleting $1$ leaves $(0,1)$, both connected by Corollary 24.2, while deleting $p$ with $0<p<1$ leaves $[0,p)\cup(p,1]$, again two nonempty disjoint sets open in the subspace.
:::

:::

::: {.pf-step #pairwise}
No homeomorphism exists between any two of the three spaces.

::: pf-proof
A homeomorphism $h$ carries the set of points of $X$ whose deletion leaves a connected space bijectively onto the corresponding set for $Y$, by step [](#cut-transport){.pf-ref}. By step [](#counts){.pf-ref} those sets have $0$, $1$ and $2$ elements for the three spaces, and different cardinalities admit no bijection.
:::

:::

::::

:::

::: {.pf-step #imbeddings}
(b) There are spaces $X,Y$ with imbeddings $X\to Y$ and $Y\to X$ that are not homeomorphic.

::: pf-proof
Take $X=(0,1)$, $Y=(0,1]$. The inclusion $f\colon X\to Y$, $f(x)=x$, is continuous and injective, and its inverse on the image $f(X)=(0,1)$ is the inclusion of $(0,1)$ in itself, which is continuous; so $f$ is an imbedding. The map $g\colon Y\to X$, $g(y)=y/2$, is continuous and injective with image $(0,1/2]$, and its inverse $z\mapsto2z$ is continuous on that image; so $g$ is an imbedding. By part [](#cut-points){.pf-ref} the two spaces are not homeomorphic.
:::

:::

::: pf-step
(c) $\RR^{n}$ and $\RR$ are not homeomorphic when $n>1$.

::: pf-proof
Suppose $h\colon\RR^{n}\to\RR$ were a homeomorphism and put $q\coloneqq h(0)$; by step [](#cut-transport){.pf-ref} it would restrict to a homeomorphism $\RR^{n}-\theset{0}\to\RR-\theset{q}$. But $\RR^{n}-\theset{0}$ is path connected for $n>1$ by Example 4 (printed p. 156), hence connected, while $\RR-\theset{q}=(-\infty,q)\cup(q,\infty)$ is a union of two nonempty disjoint open sets and is disconnected. A homeomorphism preserves connectedness, so no such $h$ exists.
:::

:::

:::

:::
