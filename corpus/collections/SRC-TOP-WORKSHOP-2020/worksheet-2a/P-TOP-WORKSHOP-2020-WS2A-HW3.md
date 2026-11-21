---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS2A-HW3
kind: problem
title: Compact subsets of Hausdorff spaces are closed; closed subsets of compact spaces are compact
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose, and the two implications are now proved
    rather than named: for a compact subset K of a Hausdorff space, the point-separating open sets
    about a fixed x outside K, the finite subcover of K, and the intersection of the finitely many
    x-neighbourhoods give a neighbourhood of x disjoint from K; for a closed subset F of a compact
    space, the cover of X obtained by adjoining X - F has a finite subcover from which X - F is
    discarded. Added the sentence recording that the two hypotheses are not interchangeable, since a
    compact non-Hausdorff space has compact non-closed subsets and a non-compact Hausdorff space has
    closed non-compact subsets. Not checked: the printed worksheet.
---

::: {.problem}
What property on a space guarantees that compact sets are closed?
What property on a space guarantees that closed sets are compact?
:::

::: {.solution}
This is a worksheet question of the 2020 topology workshop (`SRC-TOP-WORKSHOP-2020`, worksheet 2A), whose collection `provenance` lists the worksheets as `assets/attachments/Topology_Workshop_Worksheet_*.pdf`. No solution set is retained for it and the worksheet itself was not re-read in this pass; the argument is the card's own, and both implications are proved rather than cited.

::: pf

::: {.pf-step #hausdorff}
If $X$ is Hausdorff then every compact subset $K\subset X$ is closed.

::: pf-proof
Let $x\in X\setminus K$. For each $y\in K$ the Hausdorff property gives disjoint open sets $U_{y}\ni x$ and $V_{y}\ni y$. The family $\theset{V_{y}\mid y\in K}$ covers the compact set $K$, so finitely many of them, say $V_{y_{1}},\dots,V_{y_{n}}$, cover $K$. Then $U=U_{y_{1}}\cap\cdots\cap U_{y_{n}}$ is an open neighbourhood of $x$ disjoint from $V_{y_{1}}\cup\cdots\cup V_{y_{n}}\supset K$. So $X\setminus K$ is open and $K$ is closed.
:::
:::

::: {.pf-step #compact}
If $X$ is compact then every closed $F\subset X$ is compact.

::: pf-proof
Let $\theset{U_{\alpha}}$ be a cover of $F$ by open sets of $X$. Then $\theset{U_{\alpha}}\cup\{X\setminus F\}$ is an open cover of $X$, since $X\setminus F$ is open when $F$ is closed; compactness gives a finite subcover, and discarding $X\setminus F$ from it if present leaves finitely many $U_{\alpha}$ covering $F$. So $F$ is compact.
:::
:::

::: {.pf-step #answers}
The property that guarantees compact subsets are closed is Hausdorffness, and the property that guarantees closed subsets are compact is compactness of the space.

::: pf-proof
The two implications are steps [](#hausdorff){.pf-ref} and [](#compact){.pf-ref}. Neither can be weakened to the other's hypothesis in general: a space that is compact but not Hausdorff has compact subsets that are not closed, and a Hausdorff space that is not compact has closed subsets that are not compact, so the two answers name genuinely different hypotheses.
:::
:::
:::

:::
