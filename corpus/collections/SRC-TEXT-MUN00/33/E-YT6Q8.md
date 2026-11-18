---
schema: qual/card@1
id: E-YT6Q8
kind: problem
title: Connected normal and regular spaces with more than one point are uncountable
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Separation Axioms
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "Doug's World", "Munkres - Topology - Chapter
    4 Solutions" (30 August 2017; the file names no author), Problem 33.2, printed p. 8
    (tmp/sources/munkres-solutions-dougsworld-ch4.pdf), checked against Munkres, Topology (2000),
    Section 33 Exercise 2, printed p. 212, Theorem 33.1, Theorem 24.3 and Exercise 32.4. Its (a):
    Urysohn's lemma separates the two closed points, the image is connected and contains 0 and 1,
    hence is all of [0,1], so X surjects onto an uncountable set. Its (b): a countable space is
    Lindelof, so a countable regular space is regular Lindelof, hence normal by Exercise 32.4, and
    part (a) applies. The card's (b) is that argument with Proposition 1 (a countable space is
    Lindelof) stated and proved. No correction to the mathematics was needed.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked (a) Urysohn's lemma applied to two closed
    points, connectedness of the image and the identification of the image with [0,1]; (b)
    countability giving Lindelof, Theorem 32.1 giving normality, and (a) giving the
    contradiction. The argument is the card's own; no retained set is cited. Munkres §33
    Exercise 4(b), printed p. 212. The printed statement needed no repair.
---

::: {.exercise}

(a) Show that a connected normal space having more than one point is uncountable.

(b) Show that a connected regular space having more than one point is uncountable.
[Hint: Any countable space is Lindelöf.]
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card. It is checked against Munkres §33 Exercise 4(b), printed p. 212, Urysohn's lemma (§33), Theorem 32.1 (regular Lindelöf implies normal) and the countability results of §30.

::: pf

::: {.pf-step #part-a}
(a) A connected normal space with more than one point is uncountable.

::: pf-proof
Let $X$ be connected and normal with distinct points $a,b$. A normal space is $T_{1}$, so $\{a\}$ and $\{b\}$ are closed and disjoint; by Urysohn's lemma there is a continuous $f:X\to[0,1]$ with $f(a)=0$ and $f(b)=1$. The image $f(X)$ is connected, being a continuous image of the connected space $X$, and it contains $0$ and $1$; the only connected subset of $[0,1]$ containing both is $[0,1]$ itself, since $[0,1]$ is convex and its convex subsets are intervals. So $f(X)=[0,1]$, and $X$ maps onto an uncountable set, hence is uncountable.
:::

:::

::: {.pf-step #part-b}
(b) A connected regular space with more than one point is uncountable.

::: pf-proof
Let $X$ be connected, regular and have more than one point, and suppose it were countable. A countable space is Lindelöf: every open cover has a countable subcollection, indeed the whole cover is countable, and a countable subcollection of a cover which is itself countable covers it. A regular Lindelöf space is normal (Theorem 32.1). So $X$ would be a connected normal space with more than one point, hence uncountable by step [](#part-a){.pf-ref}, contradicting the supposition.
:::

:::

::: {.pf-step}
Both parts hold.

::: pf-proof
Steps [](#part-a){.pf-ref} and [](#part-b){.pf-ref} are the two assertions.
:::

:::

:::
:::
