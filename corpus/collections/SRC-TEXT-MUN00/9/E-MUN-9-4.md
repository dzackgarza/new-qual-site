---
schema: qual/card@1
id: E-MUN-9-4
kind: problem
title: Identifying implicit use of the axiom of choice
classification:
  areas:
  - topology
  topics:
  - Infinite Sets and the Axiom of Choice
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §9 Exercise 4, printed p. 61; the stored statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 9.4, printed pp. 103-104 (tmp/sources/munkres-solutions-whitman.pdf). The theorem is Theorem 7.5, a countable union of countable sets is countable, and the choice step is the selection of one surjection Z_+ -> A_n for each n, exactly as the card states; his proof composes with a surjection Z_+ -> J where the card uses the countable set I x Z_+ directly.
---

::: {.exercise}

There was a theorem in §7 whose proof involved an infinite number of arbitrary choices.
Which one was it?
Rewrite the proof so as to make explicit the use of the choice axiom.
(Several of the earlier exercises have used the choice axiom also.)
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 9.4, printed pp. 103--104** (`tmp/sources/munkres-solutions-whitman.pdf`); the identification of Theorem 7.5 as the theorem in question, and the selection of one surjection for each member of the family as the choice step, are his.


The theorem is Theorem 7.5: a countable union of countable sets is
countable. Let $\{A_n\}_{n\in\ZZ_+}$ be a family of countable sets, and put
$I=\{n:A_n\ne\varnothing\}$. If $I$ is empty, the union is empty.

For each $n\in I$, the set of surjections $\ZZ_+\to A_n$ is nonempty:
finite nonempty sets can be listed with repetitions. Apply the axiom of
choice to this family of sets of surjections, obtaining one map
$f_n:\ZZ_+\to A_n$ for every $n\in I$. This simultaneous selection is
the choice step in the proof. Countable choice suffices because $I$ is
countable.

The map
$$
I\times\ZZ_+\longrightarrow\bigcup_{n\in I}A_n,
\qquad(n,m)\longmapsto f_n(m)
$$
is surjective. Its domain is a subset of the countable set
$\ZZ_+\times\ZZ_+$, so its image is countable. Thus
$\bigcup_{n\in\ZZ_+}A_n$ is countable.
:::
