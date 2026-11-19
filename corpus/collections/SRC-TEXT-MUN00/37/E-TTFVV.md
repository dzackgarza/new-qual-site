---
schema: qual/card@1
id: E-TTFVV
kind: problem
title: The countable intersection property characterizes Lindelof spaces
classification:
  areas:
  - topology
  topics:
  - Countability
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    No complete published solution was located for this exercise, so the proof has been checked line by
    line against the book and the search is recorded in the COMPLAINTS.md entry for §37--§42 of
    SRC-TEXT-MUN00. Searched: Aleksey Zinger, "MAT 530" Problem Sets 2-9 (the only problems of Chapter 5
    or 6 among them are Munkres p235 #1, p236 #5, p260 #2 and p260 #7); "Solutions to exercises in
    Munkres", file S38.pdf (Exercise 38.4 onwards); "Solutions to exercises for Mathematics 205A" (UC
    Riverside, Fall 2014), section VI.4 (§38 Exercises 2 and 3); Orellana (whose §37 selection does not
    include this exercise), Doug's World (Chapter 4), Whitman (to §22), "positron0802" (Chapters 2 and 3),
    "shenapse" (§1--§11), "9beach" (§1--§4), "kyp44" (§1--§22); and the dbFin pages, which have no
    chapter-5 or chapter-6 section. Checked against Munkres, Topology (2000), Section 37 Exercise 2,
    printed p. 235, Definition of Lindelof and De Morgan's laws: from a countable subcover of the
    complements of the closures one gets a countable subfamily with empty intersection, and conversely an
    open cover with no countable subcover gives a family of closed sets with the countable intersection
    property and empty intersection. No correction was needed; the proof uses closedness only in the
    converse direction, where the exercise's arbitrary subsets are replaced by their closures.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the argument already on the card, whose two directions
    are correct; the audit event of 2026-11-10 records that no complete published solution was
    located and that the proof was checked against Munkres §37 Exercise 2, printed p. 235.
    Added: closedness of the complement sets is now used explicitly in the converse, which
    replaces the arbitrary subsets of the hypothesis by their closures; and the derivation of
    the countable subcover from Lindelöfness is written out rather than summarised.
---

::: {.exercise}

A collection $\mathcal{A}$ of subsets of $X$ has the countable intersection property if every countable intersection of elements of $\mathcal{A}$ is nonempty.
Show that $X$ is a Lindelöf space if and only if for every collection $\mathcal{A}$ of subsets of $X$ having the countable intersection property,

$$
\bigcap_{A \in \mathcal{A}} \overline{A}
$$

is nonempty.
:::

::: {.solution}
A collection $\mathcal{A}$ of subsets of $X$ has the countable intersection property when the intersection of any countable subcollection is nonempty, and $X$ is Lindelöf when every open cover of $X$ has a countable subcover (Munkres, *Topology* (2000), §37, printed p. 235).

::: pf

::: {.pf-step #forward}
If $X$ is Lindelöf and $\mathcal{A}$ has the countable intersection property, then $\bigcap_{A \in \mathcal{A}} \overline{A} \ne \varnothing$.

::: pf-proof
Suppose the intersection of the closures is empty. Then no point of $X$ lies in every $\overline{A}$, so each $x \in X$ has some $A$ with $x \notin \overline{A}$; the open sets $X \setminus \overline{A}$, $A \in \mathcal{A}$, therefore cover $X$. Lindelöfness gives a countable subcover $X = \bigcup_{n}(X \setminus \overline{A_{n}})$, that is $\bigcap_{n}\overline{A_{n}} = \varnothing$. Since $A_{n} \subseteq \overline{A_{n}}$, also $\bigcap_{n}A_{n} = \varnothing$, contradicting the countable intersection property of $\mathcal{A}$.

:::

:::

::: {.pf-step #closed-cover}
Assume the closure property. Let $\mathcal{U} = \theset{U_{i} \mid i \in I}$ be an open cover of $X$ with no countable subcover; then the closed sets $A_{i} \coloneqq X \setminus U_{i}$ have the countable intersection property.

::: pf-proof
For indices $i_{1}, i_{2}, \ldots$, the union $U_{i_{1}} \cup U_{i_{2}} \cup \cdots$ is not all of $X$, since it is the union of a countable subfamily; taking complements gives $A_{i_{1}} \cap A_{i_{2}} \cap \cdots \ne \varnothing$. Each $A_{i}$ is closed, being the complement of an open set.

:::

:::

::: {.pf-step #contradiction}
Assuming the closure property, no open cover of $X$ can fail to have a countable subcover.

::: pf-proof
With $\mathcal{U}$ and the $A_{i}$ as in step [](#closed-cover){.pf-ref}, the hypothesis gives $\bigcap_{i \in I}\overline{A_{i}} \ne \varnothing$. Each $A_{i}$ is closed, so $\overline{A_{i}} = A_{i}$ and the intersection is $\bigcap_{i}(X \setminus U_{i}) = X \setminus \bigcup_{i}U_{i} = \varnothing$, since $\mathcal{U}$ covers $X$. This is a contradiction, so every open cover of $X$ has a countable subcover.

:::

:::

::: pf-step
$X$ is Lindelöf if and only if for every collection $\mathcal{A}$ of subsets of $X$ with the countable intersection property, $\bigcap_{A \in \mathcal{A}}\overline{A} \ne \varnothing$.

::: pf-proof
Step [](#forward){.pf-ref} is the implication from Lindelöfness, and step [](#contradiction){.pf-ref} supplies the converse: it shows that under the closure property every open cover has a countable subcover, which is Lindelöfness.

:::

:::

:::
:::
