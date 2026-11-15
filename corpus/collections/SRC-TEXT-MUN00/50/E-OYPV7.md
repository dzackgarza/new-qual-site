---
schema: qual/card@1
id: E-OYPV7
kind: problem
title: The hierarchy of conditions on locally euclidean spaces
classification:
  areas:
  - topology
  topics:
  - Manifolds
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution was located; the sets searched are listed in the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00.
    Checked against Munkres, Topology (2000), supplementary Exercise 2 of §50, printed p. 317, with Theorem 34.1
    (Urysohn metrization), Theorem 32.2 (metrizable spaces are normal) and Theorem 30.2. The chain: a compact
    Hausdorff locally euclidean space is covered by finitely many coordinate neighbourhoods, each second
    countable, so it is second countable and hence a manifold; a manifold is locally compact Hausdorff, hence
    regular, and with a countable basis metrizable by Theorem 34.1; a metrizable space is normal; a normal space
    is T1 and separates points from closed sets, so it is Hausdorff. Nothing needed correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). Nothing located proves the chain of supplementary Exercise 2 of
    §50 (printed p. 316). Murayama's selection has no Chapter 8, dbFin has no chapter-8 page, the ten GitHub
    repositories of Munkres solutions listed in COMPLAINTS.md stop before §36, and the AoPS post *Topology by
    Munkres Chapter 8 | Day 18* (https://artofproblemsolving.com/community/c3401823h3647630) answers §50 with
    its formulas lost. The Stack Exchange query "locally m-euclidean" returned two neighbouring statements,
    4416020 (Lindelof and locally euclidean imply second countable) and 2317193 (a Hausdorff locally euclidean
    space that is not paracompact), neither of which proves any link of the chain. The link with content is
    (i) implies (ii): compactness turns the euclidean neighbourhoods of the points into a finite family, and a
    finite union of countable bases is countable, which is what the card proves; (ii) implies (iii) is the
    Urysohn metrization theorem, (iii) implies (iv) the normality of a metric space, and (iv) implies (v) the
    $T_1$ axiom, all of which the book has. Nothing needed correction.
---

::: {.exercise}

Consider the following conditions on a locally $m$-euclidean space $X$:

(i) $X$ is compact Hausdorff.

(ii) $X$ is an $m$-manifold.

(iii) $X$ is metrizable.

(iv) $X$ is normal.

(v) $X$ is Hausdorff.

Show that (i) $\Rightarrow$ (ii) $\Rightarrow$ (iii) $\Rightarrow$ (iv) $\Rightarrow$ (v).
:::

::: {.solution}
We prove the implications successively.

$(i)\Rightarrow(ii)$. A compact Hausdorff locally $m$-euclidean space has a finite atlas. Each coordinate neighborhood has a countable basis, and the union of finitely many such bases is a countable basis for $X$. Thus $X$ is Hausdorff, second-countable, and locally $m$-euclidean, hence an $m$-manifold.

$(ii)\Rightarrow(iii)$. An $m$-manifold is Hausdorff and second-countable, hence regular (indeed locally compact Hausdorff spaces are regular). By the Urysohn metrization theorem, a regular second-countable space is metrizable.

$(iii)\Rightarrow(iv)$. Every metrizable space is normal.

$(iv)\Rightarrow(v)$. A normal space is $T_1$ by definition, so two distinct points are disjoint closed sets, and normality separates them by disjoint open sets.

Hence
$$
(i)\Longrightarrow(ii)\Longrightarrow(iii)\Longrightarrow(iv)\Longrightarrow(v).
$$
:::
