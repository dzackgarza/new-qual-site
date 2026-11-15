---
schema: qual/card@1
id: E-LOA25
kind: problem
title: Metrizability equals paracompact Hausdorff for locally euclidean spaces
classification:
  areas:
  - topology
  topics:
  - Manifolds
  - Paracompactness
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution was located; the sets searched are listed in the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00.
    Checked against Munkres, Topology (2000), supplementary Exercise 8 of §50, printed p. 318. What was corrected:
    both directions had been attributed to "Stone's theorem", which the book does not state; they are the two
    halves of the Smirnov metrization theorem, Theorem 42.1, which the book proves, the metrizable half resting on
    Lemma 39.2 and Theorem 40.3, and the other half being exactly the statement that a paracompact Hausdorff space
    that is locally metrizable is metrizable. The local metrizability is supplied by the first supplementary
    exercise. Nothing else needed correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). Nothing located treats supplementary Exercise 8 of §50 (printed
    p. 318) as an exercise; the statement is the Smirnov metrization theorem, Theorem 42.1 of the book, and the
    card derives both directions from that theorem rather than from a located proof. Murayama's selection has
    no Chapter 8, dbFin has no chapter-8 page, the ten GitHub repositories of Munkres solutions listed in
    COMPLAINTS.md stop before §36, and the AoPS post *Topology by Munkres Chapter 8 | Day 18*
    (https://artofproblemsolving.com/community/c3401823h3647630) answers §50 with its formulas lost. The Stack
    Exchange queries of this pass are listed in the COMPLAINTS.md entry for §43--§50. Nothing needed
    correction.
---

::: {.exercise}

Let $X$ be a space that is locally $m$-euclidean.
Show that $X$ is metrizable if and only if $X$ is paracompact Hausdorff.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $X$ is metrizable, then $X$ is paracompact Hausdorff.

::: pf-proof

One direction is one half of the Smirnov metrization theorem (Theorem 42.1): a metrizable space is paracompact Hausdorff. (Distinct points of a metric space have disjoint open balls, and the paracompactness of a metrizable space is part of Theorem 42.1, whose proof uses the countably locally finite basis produced by Lemma 39.2 and Theorem 40.3.)

:::

:::

::: {.pf-step #s2}

If $X$ is paracompact Hausdorff, then $X$ is metrizable.

::: pf-proof

This is the other half of the Smirnov metrization theorem (Theorem 42.1): a paracompact Hausdorff space that is locally metrizable is metrizable. The hypothesis is supplied by the first exercise of these supplementary exercises, that a locally $m$-euclidean space is locally metrizable, since a neighbourhood homeomorphic to an open subset of $\RR^m$ is metrizable.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} give the two implications.

:::

:::

:::
