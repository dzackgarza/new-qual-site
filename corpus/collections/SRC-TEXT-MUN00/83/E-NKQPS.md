---
schema: qual/card@1
id: E-NKQPS
kind: problem
title: The vertex assumption in the normality proof for linear graphs
classification:
  areas:
  - topology
  topics:
  - Graphs
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Munkres §83 Exercise 1, printed p. 505. Searched outside the checkout for issue #146; the record is
    tmp/sources/mse-searches-146.md and the saved thread is tmp/sources/mse-4911475-E-NKQPS.md, read whole.
    Math StackExchange 4911475 quotes this exercise and asks why the hypothesis is without loss of generality;
    the accepted answer 4911528 by Paul Frost (2024-05-05) answers it: add the remaining vertices to B, a
    closed set by the result on printed p. 502. That is transcribed on the card with its URL. The answer does
    not say why the proof needs the hypothesis, i.e. what fails at a vertex in neither B nor C; the card's own
    proof does, and it is kept.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 83 Exercise 1, printed p. 505. Why the proof of normality of a linear graph may assume every vertex lies in B or C: vertices can be adjoined to the closed sets. Checked against the printed proof in Section 83. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Step-by-step check against the printed pages, and the repair. Citations added: the paragraph before Lemma 83.1 (printed p. 502), which proves that $X^0$ is a closed discrete subspace and that every subset of $X^0$ is closed in $X$, and the two steps of the printed proof of Lemma 83.1 (printed p. 502) in which the assumption is used. Corrected: the proof did not say why the substituted set $B\cup D$ is still disjoint from $C$ nor that its closedness is what the substitution needs; both are now stated. What the certificate does not cover: Lemma 83.1 itself is the book's, and only the reduction in its first line is discussed here.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked that every subset of the vertex set is closed
    in a linear graph, that the pair of closed sets can be enlarged so that B contains all
    vertices, and the two places where the printed proof of Lemma 83.1 (printed p. 502) uses
    that assumption: disjointness of the edgewise open sets and the equality U cap A_alpha =
    U_alpha giving openness. Paul Frost's MSE answer 4911528 supplies the enlargement; the
    location of the use is the card's own argument. The printed statement needed no repair.
---

::: {.exercise}

In the proof of normality of a linear graph $X$, why did we assume that every vertex of $X$ belongs either to $B$ or to $C$?

:::

::: {.solution}
The published answer this card rests on is **Paul Frost, answer 4911528 to Math Stack Exchange question 4911475, "Every linear graph $X$ is normal"** (posted 2024-05-05); Frost shows that the vertex assumption of the printed proof costs nothing. The argument below, which locates where the assumption is used, is the card's own.

Throughout, $X$ is a linear graph, $X^{0}$ its set of vertices, and the printed proof is that of Lemma 83.1 (printed p. 502), in which the two closed sets $B$ and $C$ are separated by open sets $U_{\alpha}\subset A_{\alpha}$ and $V_{\beta}\subset A_{\beta}$ chosen on the edges $A_{\alpha}$.

::: pf

::: {.pf-step #vertices-closed}
Every subset of $X^{0}$ is closed in $X$, and $X^{0}$ is a closed discrete subspace.

::: pf-proof
This is proved just before Lemma 83.1 (printed p. 502): each vertex is closed in $X$ and the subspace $X^{0}$ is discrete. Moreover, for any $S\subset X^{0}$ and any edge $A$ of $X$, the intersection $S\cap A$ is empty or a single point, hence closed in $A$; so $S$ is closed in $X$ by the coherent topology on a linear graph.
:::

:::

::: {.pf-step #reduce}
It suffices to separate the two closed sets under the extra assumption that every vertex of $X$ lies in $B\cup C$.

::: pf-proof
Let $D=X^{0}-(B\cup C)$ and $B'=B\cup D$. Then $D$ is closed by step [](#vertices-closed){.pf-ref}, so $B'$ is closed, and $B'\cap C=\varnothing$ because $D\cap C=\varnothing$ and $B\cap C=\varnothing$. The set $B'$ contains every vertex of $X$, since a vertex outside $B$ lies in $C$ or in $D$. A separation of the pair $B'$, $C$ separates $B\subset B'$ from $C$, so it is enough to prove the lemma for the pair $B'$, $C$.
:::

:::

::: {.pf-step #used-disjointness}
Under that assumption, $U_{\alpha}\cap V_{\beta}=\varnothing$ for distinct edges $A_{\alpha}$, $A_{\beta}$.

::: pf-proof
A point of $U_{\alpha}\cap V_{\beta}$ lies in $A_{\alpha}\cap A_{\beta}$, and distinct edges of a linear graph meet in at most one vertex, so it is a vertex. A vertex of $B$ lies in no $V_{\beta}$, because $V_{\beta}$ was chosen inside $A_{\beta}$ avoiding $C$ and the vertices of $B$ are not in $C$; symmetrically a vertex of $C$ lies in no $U_{\alpha}$. Since the assumption puts every vertex in $B$ or in $C$, no vertex lies in both, and the intersection is empty.
:::

:::

::: {.pf-step #used-openness}
Under that assumption, $U=\bigcup_{\alpha}U_{\alpha}$ and $V=\bigcup_{\beta}V_{\beta}$ are open in $X$.

::: pf-proof
By the coherent topology it suffices that $U\cap A_{\alpha}$ be open in $A_{\alpha}$ for each edge. If $x\in U\cap A_{\alpha}$ and $x\notin U_{\alpha}$, then $x$ lies in some other $U_{\beta}$ with $\beta\ne\alpha$, so $x\in A_{\beta}$ and hence $x$ is a vertex. By the assumption $x\in B$ or $x\in C$; a vertex of $B$ lies in $U_{\alpha}$ by the definition of $U_{\alpha}$, which contains $B\cap A_{\alpha}$, and a vertex of $C$ cannot lie in $U$. So every point of $U\cap A_{\alpha}$ is in $U_{\alpha}$, that is $U\cap A_{\alpha}=U_{\alpha}$, which is open in $A_{\alpha}$. The same argument with $B$, $U$ replaced by $C$, $V$ shows $V\cap A_{\alpha}=V_{\alpha}$.
:::

:::

::: {.pf-step}
The vertex assumption is what the printed proof needs, and it can always be arranged.

::: pf-proof
Steps [](#used-disjointness){.pf-ref} and [](#used-openness){.pf-ref} locate the two places where the proof uses that every vertex lies in $B\cup C$: without it, a vertex outside $B\cup C$ may lie in some $U_{\alpha}$ and some $V_{\beta}$ with $\alpha\ne\beta$, and the sets $U_{\alpha}$ are chosen only to contain $B\cap A_{\alpha}$, so such a vertex would be unaccounted for. Step [](#reduce){.pf-ref} shows the assumption can always be arranged by enlarging $B$ with the closed set of remaining vertices.
:::

:::

:::
:::
