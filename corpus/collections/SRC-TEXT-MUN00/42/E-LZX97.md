---
schema: qual/card@1
id: E-LZX97
kind: problem
title: Local metrizability criteria as cases of the Smirnov metrization theorem
classification:
  areas:
  - topology
  topics:
  - Metrizability
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    No complete published solution was located for this exercise, so the proof is checked line by line
    against the book and the search is recorded in the COMPLAINTS.md entry for §39--§42 of SRC-TEXT-MUN00.
    Searched: the sets listed in that entry --- Aleksey Zinger's MAT 530 sheets, the *Praying For Stockholm*
    posts, Moller's S38, the Riverside Math 205A solutions, Orellana, Doug's World, Whitman,
    "positron0802", "shenapse", "9beach", "kyp44", the seven further GitHub manuals, dbfin and Gardner's
    ETSU notes --- none of which solves this exercise.
    Checked against Munkres, Topology (2000), Section 42 Exercise 1, printed p. 262, with Theorem 42.1, Theorem 41.4 and Theorem 41.5 (which supply the paracompactness that Exercises 34.7 and 34.8 do not state), and the two exercises themselves. What was corrected: the card now names Theorem 41.5 for the paracompactness of a regular Lindelof space, where it previously referred only to the construction on the card of E-KVFCT.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Issue #184: the page locators in the card's text are removed and the citation is made by
    number --- §42 Exercise 1, Theorem 42.1 (Smirnov), Theorems 41.4 and 41.5, the remark on
    compact spaces in the introduction to §41, and the definition of regularity in §31 --- each
    read in `tmp/sources/munkres-2000-topology.md`. The earlier events keep their text (QUAL-11);
    these numbered citations supersede their page locators. No step changes.

---

::: {.exercise}

Compare Theorem 42.1 (the Smirnov metrization theorem) with Exercises 7 and 8 of §34.
:::

::: {.solution}

No retained solution set covers this exercise: it is a comparison the book asks for and no sheet in `tmp/sources` treats §42 Exercise 1, so the comparison below is the card's own. The statements compared were checked against Munkres, *Topology* (2000), §42 Exercise 1, the Smirnov metrization theorem, Theorem 42.1, Theorem 41.5, the remark that every compact space is paracompact in the introduction to §41, and the definition of regularity in §31.

Throughout, the two criteria of §34 are those of [[E-MQTBP]] (compact Hausdorff and locally metrizable) and [[E-KK77N]] (regular, Lindelöf and locally metrizable).

::: pf

::: {.pf-step #smirnov}
Smirnov's theorem reads: $X$ is metrizable if and only if $X$ is paracompact Hausdorff and locally metrizable.

::: pf-proof
This is Theorem 42.1. Its forward implication uses that a metrizable space is paracompact, Theorem 41.4, and locally metrizable; its converse is the substance of the theorem.
:::

:::

::: {.pf-step #compact-case}
A compact Hausdorff space that is locally metrizable is metrizable.

:::: pf-proof

::: {.pf-step #compact-paracompact}
Every compact space is paracompact.

::: pf-proof
Given an open cover of a compact space, it contains a finite subcover, and a finite family of open sets is a locally finite open refinement of any cover it refines: each point has the neighbourhood $X$ itself, which meets only the finitely many members of the family. Munkres records this fact in the introduction to §41 as an immediate consequence of the definition.
:::

:::

::: {.pf-step}
The hypotheses of step [](#smirnov){.pf-ref} are met, so the space is metrizable.

::: pf-proof
It is compact by hypothesis, hence paracompact by step [](#compact-paracompact){.pf-ref}; it is Hausdorff and locally metrizable by hypothesis. Step [](#smirnov){.pf-ref} then gives metrizability.
:::

:::

::::

:::

::: {.pf-step #lindelof-case}
A regular Lindelöf space that is locally metrizable is metrizable.

:::: pf-proof

::: {.pf-step #lindelof-paracompact}
A regular Lindelöf space is paracompact.

::: pf-proof
This is Theorem 41.5.
:::

:::

::: {.pf-step #regular-hausdorff}
A regular space is Hausdorff.

::: pf-proof
In Munkres's sense regularity presupposes that one-point sets are closed (§31). Given distinct points $x\neq y$, the set $\theset{y}$ is closed and does not contain $x$, so regularity gives disjoint open sets containing $x$ and $\theset{y}$ respectively, which separates the two points.
:::

:::

::: {.pf-step}
The hypotheses of step [](#smirnov){.pf-ref} are met, so the space is metrizable.

::: pf-proof
It is regular and Lindelöf by hypothesis, hence paracompact by step [](#lindelof-paracompact){.pf-ref} and Hausdorff by step [](#regular-hausdorff){.pf-ref}, and it is locally metrizable by hypothesis; step [](#smirnov){.pf-ref} gives metrizability.
:::

:::

::::

:::

::: pf-step
Therefore both §34 criteria are special cases of the Smirnov theorem, and the theorem's hypothesis is strictly broader than either.

::: pf-proof
Steps [](#compact-case){.pf-ref} and [](#lindelof-case){.pf-ref} derive the two criteria from step [](#smirnov){.pf-ref}: in each case the only thing supplied by the §34 hypothesis beyond local metrizability is paracompactness, obtained from compactness in the first case and from regularity together with the Lindelöf property in the second, and the Hausdorff condition is either assumed or is a consequence of regularity. The inclusion is strict: an uncountable set with the discrete topology is metrizable, hence paracompact Hausdorff and locally metrizable, and it is neither compact nor Lindelöf, since the cover by its one-point sets has no countable subcover. So the Smirnov theorem covers spaces that neither §34 criterion reaches.
:::

:::

:::

:::
