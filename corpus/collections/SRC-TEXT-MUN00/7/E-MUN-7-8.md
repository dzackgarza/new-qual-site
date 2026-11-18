---
schema: qual/card@1
id: E-MUN-7-8
kind: problem
title: Cardinality of countable subsets of $X^{\omega}$
classification:
  areas:
  - topology
  topics:
  - Countable and Uncountable Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 7, Exercise 8; the stored statement matches. The proof requires a choice principle to choose enumerations simultaneously for all countable subsets, which is stated explicitly in the solution.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §7 Exercise 8, printed p. 52; the stored
    statement matches, with B the set of countable subsets of X^omega.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 7.8,
    printed pp. 90-92 (tmp/sources/munkres-solutions-whitman.pdf). His two injections are
    the card's: singletons into the power set, and the passage from a countable subset to
    a chosen enumeration of it, which lands in (X^omega)^omega and then in X^omega because
    omega x omega is countably infinite. He also flags the choice used, as the card does.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps, transcribing the cited published solution: Dan Whitman,
    Topology, Second Edition by James Munkres: Solutions Manual (2019), Exercise 7.8, printed
    pp. 90-92. Checked against Munkres §7 Exercise 8, whose number is read from the collection
    index. Each step re-read: singletons inject X^omega into the countable subsets; choosing an
    enumeration of each nonempty countable subset is a genuine choice, and the range of the chosen
    surjection recovers the subset, so the tagged assignment is injective; and
    {0} + (Z_+ x Z_+) is countably infinite, so X times (X^omega)^omega is X^omega. Schroeder-
    Bernstein closes. The remark that the argument uses choice is kept, and the card does not claim
    the result in ZF alone. Not claimed: any statement about the cardinality of the set of all
    subsets of X^omega, which is larger by Cantor's theorem.
---

::: {.exercise}

Let $X$ denote the two-element set $\{0,1\}$ ; let $\mathcal{B}$ be the set of countable subsets of $X^{\omega}$ . Show that $X^{\omega}$ and $\mathcal{B}$ have the same cardinality.
:::

::: {.solution}
The argument is transcribed from the published solution of Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 7.8, printed pp. 90--92 (`tmp/sources/munkres-solutions-whitman.pdf`); the two injections, the choice of an enumeration for each countable subset and the remark that the choice is genuine are his. It is checked against Munkres, Topology (2000), §7 Exercise 8.

::: pf

::: {.pf-step #oneway}
$X^{\omega}$ injects into $\mathcal B$, the set of countable subsets of $X^{\omega}$.

::: pf-proof
$X=\{0,1\}$, so each $x\in X^{\omega}$ determines the countable subset $\{x\}$, and distinct points give distinct singletons.
:::

:::

::: {.pf-step #otherway}
$\mathcal B$ injects into $X\times(X^{\omega})^{\omega}$.

:::: pf-proof

::: {.pf-step #enumerations}
For every nonempty $S\in\mathcal B$ there is a surjection $e_{S}:\ZZ_{+}\to S$, and one may be chosen for each $S$ simultaneously.

::: pf-proof
$S$ is nonempty and countable, so an enumeration of its elements by positive integers exists; choosing one for each $S$ is an application of the axiom of choice to the family of nonempty sets of enumerations, and the card records that this is a genuine choice step.
:::

:::

::: {.pf-step #injective}
$S\mapsto e_{S}$ is injective on nonempty subsets, so the tagged assignment is injective on $\mathcal B$.

::: pf-proof
The range of $e_{S}$ is exactly $S$, so $S$ can be recovered from $e_{S}$; hence distinct nonempty $S$ give distinct sequences. Sending $\varnothing$ to $(0,e_{\varnothing})$ for a fixed $e_{\varnothing}\in(X^{\omega})^{\omega}$ and nonempty $S$ to $(1,e_{S})$ separates the two cases by the first coordinate and is injective within each by the previous sentence.
:::

:::

:::

:::

::: {.pf-step #identify}
$X\times(X^{\omega})^{\omega}\cong X^{\omega}$.

::: pf-proof
$X\times(X^{\omega})^{\omega}=X^{\{0\}}\times X^{\ZZ_{+}\times\ZZ_{+}}=X^{\{0\}\sqcup(\ZZ_{+}\times\ZZ_{+})}$, and $\{0\}\sqcup(\ZZ_{+}\times\ZZ_{+})$ is countably infinite, so there is a bijection with the index set $\omega$; a bijection of index sets induces a bijection of the function spaces, by composing with it and its inverse.
:::

:::

::: {.pf-step #schroeder}
$\cardinality{\mathcal B}=\cardinality{X^{\omega}}$.

::: pf-proof
Steps [](#oneway){.pf-ref}, [](#otherway){.pf-ref} and [](#identify){.pf-ref} exhibit injections in both directions, so the Schröder--Bernstein theorem gives
$$
\boxed{\cardinality{\mathcal B}=\cardinality{X^{\omega}}=2^{\aleph_{0}}.}
$$
The statement depends on the choice made in step [](#enumerations){.pf-ref}; in ZF alone this form of the cardinality statement is not available.
:::

:::

:::
:::
