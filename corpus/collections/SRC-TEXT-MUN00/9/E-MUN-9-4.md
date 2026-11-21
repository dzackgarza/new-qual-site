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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the rewritten proof of Theorem 7.5, which is what Queue D asks for on this card. The steps name the theorem, prove that the set of surjections from Z_+ onto a nonempty countable set is nonempty (the point the prose left as an aside about finite sets), apply the axiom of choice deliberately and record that the countable form suffices, and close with the surjectivity and countability. Statement re-read against Munkres, Topology (2000), §9 Exercise 4, printed p. 61, and the argument against Dan Whitman's set, Exercise 9.4, printed pp. 103-104. No statement repair.
---

::: {.exercise}

There was a theorem in §7 whose proof involved an infinite number of arbitrary choices.
Which one was it?
Rewrite the proof so as to make explicit the use of the choice axiom.
(Several of the earlier exercises have used the choice axiom also.)
:::

::: {.solution}
The published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 9.4, printed pp. 103--104** (`tmp/sources/munkres-solutions-whitman.pdf`); the identification of Theorem 7.5 as the theorem in question, and the selection of one surjection for each member of the family as the choice step, are his. The statement is Munkres, *Topology*, 2nd ed. (2000), §9 Exercise 4, printed p. 61.

::: pf

::: {.pf-step #theorem}
The theorem is Theorem 7.5: a countable union of countable sets is countable.

::: pf-proof
It is the one proof of §7 that selects an object for each member of an infinite family: the argument needs a surjection $\ZZ_+\to A_n$ for every $n$, and no rule produces them all at once from the hypothesis that each $A_n$ is countable.
:::

:::

::: {.pf-step #surjections}
For each $n$ with $A_n\ne\varnothing$ the set $S_n$ of surjections $\ZZ_+\to A_n$ is nonempty.

::: pf-proof
A set is countable exactly when there is a surjection from $\ZZ_+$ onto it (Lemma 7.1 of the section): for a finite nonempty set this is a listing with repetitions, and for a countably infinite set a bijection. So $S_n\ne\varnothing$ whenever $A_n\ne\varnothing$.
:::

:::

::: {.pf-step #choice}
The axiom of choice applies to the family $\{S_n\}_{n\in I}$, where $I=\{n\in\ZZ_+:A_n\ne\varnothing\}$, and yields one surjection $f_n:\ZZ_+\to A_n$ for every $n\in I$.

::: pf-proof
The index set $I$ is a subset of $\ZZ_+$, and each $S_n$ is nonempty by step [](#surjections){.pf-ref}; the axiom of choice selects an element of each member of the family, which is exactly one $f_n\in S_n$ per index. The family is indexed by a countable set, so the countable form of the axiom suffices, and no definable rule for the selection is available, which is why the axiom is needed here.
:::

:::

::: {.pf-step #countable-union}
$\bigcup_{n\in\ZZ_+}A_n$ is countable.

::: pf-proof
If $I=\varnothing$ the union is empty and hence countable. Otherwise the map $I\times\ZZ_+\to\bigcup_{n}A_n$ sending $(n,m)$ to $f_n(m)$ is surjective, because a point of the union lies in some $A_n$ with $n\in I$ and $f_n$ is surjective. Its domain is a subset of the countable set $\ZZ_+\times\ZZ_+$, so the domain is countable and a surjective image of a countable set is countable. Thus the proof of Theorem 7.5, rewritten with step [](#choice){.pf-ref} in place of the silent selection, establishes its conclusion, as the exercise asks.
:::

:::

:::
:::
