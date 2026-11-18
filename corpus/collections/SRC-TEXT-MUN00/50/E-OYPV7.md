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
    §50 (printed p. 317). Murayama's selection has no Chapter 8, dbFin has no chapter-8 page, the ten GitHub
    repositories of Munkres solutions listed in COMPLAINTS.md stop before §36, and the AoPS post *Topology by
    Munkres Chapter 8 | Day 18* (https://artofproblemsolving.com/community/c3401823h3647630) answers §50 with
    its formulas lost. The Stack Exchange query "locally m-euclidean" returned two neighbouring statements,
    4416020 (Lindelof and locally euclidean imply second countable) and 2317193 (a Hausdorff locally euclidean
    space that is not paracompact), neither of which proves any link of the chain. The link with content is
    (i) implies (ii): compactness turns the euclidean neighbourhoods of the points into a finite family, and a
    finite union of countable bases is countable, which is what the card proves; (ii) implies (iii) is the
    Urysohn metrization theorem, (iii) implies (iv) the normality of a metric space, and (iv) implies (v) the
    $T_1$ axiom, all of which the book has. Nothing needed correction.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the four implications into numbered steps, each naming the book result it uses:
    compactness for the finite subcover in (i) implies (ii); local compactness of a locally
    euclidean space together with Exercise 3 of Section 32 (every locally compact Hausdorff space is
    regular) for the regularity needed before Urysohn applies; Theorem 34.1 for metrizability;
    Theorem 32.2 for normality of a metric space; and, for (iv) implies (v), the definitions of
    Section 32, where one-point sets closed is part of normality and a normal space is regular and
    hence Hausdorff. Checked in the retained text: Munkres's sentence that "a regular space is
    Hausdorff, and that a normal space is regular", with closedness of one-point sets part of both
    definitions. Nothing needed correction.
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

The chain is the card's own argument, each link attributed to the book result it uses; no complete published solution was located, as the card's earlier audit events record. The statement was checked against Munkres, *Topology* (2000), supplementary Exercise 2 of §50, printed p. 317.

A space is locally $m$-euclidean when each point has a neighbourhood homeomorphic to an open subset of $\RR^{m}$, and an $m$-manifold when it is also Hausdorff and second countable.

::: pf

::: {.pf-step #i-ii}
(i) implies (ii).

::: pf-proof
Let $X$ be compact Hausdorff and locally $m$-euclidean. Each point has a coordinate neighbourhood, second countable because $\RR^{m}$ has a countable basis and a subspace of a second-countable space is second countable (Theorem 30.2). These neighbourhoods form an open cover, and compactness extracts a finite subcover $V_{1},\dots,V_{k}$. The union of countable bases of the $V_{j}$, together with $X$, is then a countable basis for $X$: an open set of $X$ is the union of its intersections with the $V_{j}$, each open in $V_{j}$. So $X$ is Hausdorff, second countable and locally $m$-euclidean, an $m$-manifold.
:::

:::

::: {.pf-step #ii-iii}
(ii) implies (iii).

::: pf-proof
An $m$-manifold is locally $m$-euclidean, so each point has a neighbourhood homeomorphic to an open subset of $\RR^{m}$; such a subset contains a ball, which is locally compact, so $X$ is locally compact. Being second countable and Hausdorff, $X$ is regular by Exercise 3 of §32 ("every locally compact Hausdorff space is regular"). A regular space with a countable basis is metrizable by the Urysohn metrization theorem (Theorem 34.1).
:::

:::

::: {.pf-step #iii-iv}
(iii) implies (iv).

::: pf-proof
Theorem 32.2 states that every metrizable space is normal.
:::

:::

::: {.pf-step #iv-v}
(iv) implies (v).

::: pf-proof
Munkres defines normality to include the closedness of one-point sets and states (printed p. 196) that a normal space is regular and a regular space is Hausdorff; being Hausdorff is condition (v).
:::

:::

::: {.pf-step}
(i) implies (ii) implies (iii) implies (iv) implies (v).

::: pf-proof
Steps [](#i-ii){.pf-ref}, [](#ii-iii){.pf-ref}, [](#iii-iv){.pf-ref}, [](#iv-v){.pf-ref} are the four implications in order.
:::

:::

:::

:::
