---
schema: qual/card@1
id: E-71YOD
kind: problem
title: Regular spaces have disjoint closure neighborhoods of points
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solutions: Ana Emilia de Orellana, "Solutions -
    Topology Munkres", Section 31 Exercise 1, printed p. 32
    (tmp/sources/munkres-solutions-anadeore.pdf), and "Doug's World", "Munkres - Topology -
    Chapter 4 Solutions" (30 August 2017; the file names no author), Problem 31.1, printed p. 4
    (tmp/sources/munkres-solutions-dougsworld-ch4.pdf); checked against Munkres, Topology (2000),
    Section 31 Exercise 1, printed p. 199, and Lemma 31.1(a), printed p. 196. What was corrected:
    Doug's World writes that the two shrunken neighbourhoods V_x and V_y "are disjoint", whereas
    what its own construction gives is that their closures lie in the disjoint open sets U_x and
    U_y, which is the disjointness of the closures that the exercise asks for; the card states the
    conclusion at the level of closures.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Ten steps asserted their claim with no justification and the card is now three steps each deriving its
    claim: the separation of the two points by disjoint open sets, from the $T_1$ axiom of a regular space
    and the separation of a point from a closed set not containing it; the shrinking to neighbourhoods with
    closed containment, by Lemma 31.1 applied to each point and its open set; and the conclusion
    $\overline{U} \cap \overline{V} = \varnothing$ from the two inclusions into the disjoint $U_0$ and $V_0$.
    The three label-claims are replaced by the assertions their proofs establish, and the terminal step
    that only repeated the conclusion together with its literal "Q.E.D." is gone. Sources are cited by
    numbered statement: Munkres, Topology, Section 31 Exercise 1 and Lemma 31.1, as the earlier event
    records; no page reference is written in the body of this card or in the event above. The statement is
    unchanged. The transcription correction recorded above is untouched: the conclusion is stated at the
    level of closures, which is what the exercise asks for.
---

::: {.exercise}

Show that if $X$ is regular, every pair of points of $X$ have neighborhoods whose closures are disjoint.
:::

::: {.solution}

::: pf

::: {.pf-step #separate-by-disjoint-opens}
Distinct points $x \ne y$ of a regular space have disjoint open neighbourhoods $U_0 \ni x$ and $V_0 \ni y$.

::: pf-proof
A regular space is $T_1$, so one-point sets are closed and in particular $\{y\}$ is closed in $X$; since $x \ne y$, the point $x$ does not lie in it. Regularity separates a point from a closed set not containing it, so there are disjoint open sets $U_0$ containing $x$ and $V_0$ containing $\{y\}$, hence containing $y$.
:::

:::

::: {.pf-step #shrink-to-closed-containment}
There are open neighbourhoods $U$ of $x$ and $V$ of $y$ with $\overline{U} \subseteq U_0$ and $\overline{V} \subseteq V_0$.

::: pf-proof
By the characterization of regularity in Munkres Lemma 31.1, for every point $p$ and every open neighbourhood $W$ of $p$ there is an open neighbourhood $N$ of $p$ with $\overline{N} \subseteq W$. Applying it to the point $x$ and its open neighbourhood $U_0$ gives an open $U \ni x$ with $\overline{U} \subseteq U_0$, and applying it to $y$ and $V_0$ gives an open $V \ni y$ with $\overline{V} \subseteq V_0$.
:::

:::

::: pf-step

$\overline{U} \cap \overline{V} = \varnothing$.

::: pf-proof
The two closures satisfy $\overline{U} \subseteq U_0$ and $\overline{V} \subseteq V_0$ by step [](#shrink-to-closed-containment){.pf-ref}, so $\overline{U} \cap \overline{V} \subseteq U_0 \cap V_0$; and $U_0 \cap V_0 = \varnothing$ by step [](#separate-by-disjoint-opens){.pf-ref}. A subset of the empty set is empty, so the intersection of the closures is empty. Thus $U$ and $V$ are open neighbourhoods of $x$ and $y$ with disjoint closures, as required.
:::

:::

:::

:::
