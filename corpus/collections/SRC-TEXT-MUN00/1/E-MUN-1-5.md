---
schema: qual/card@1
id: E-MUN-1-5
kind: problem
title: Membership in unions and intersections of collections
classification:
  areas:
  - topology
  topics:
  - Fundamental Concepts
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
    Read against Munkres, Topology (2000), §1 Exercise 5, printed p. 14: the four
    statements (a)-(d) and their converses, for a nonempty collection of sets, are
    stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 1.5,
    printed pp. 7-8 (tmp/sources/munkres-solutions-whitman.pdf). His verdicts are the
    card's - (a) and (d) true with their converses, (b) false with a true converse, (c)
    true with a false converse - and the nonemptiness of the collection is used exactly
    where he uses it, in the two converses that go from "x in A for every A" to the
    union and from the intersection to a member.
---

::: {.exercise}

Let $\mathcal{A}$ be a nonempty collection of sets.
Determine the truth of each of the following statements and of their converses:

(a) $x \in \bigcup_{A \in \mathcal{A}} A \Rightarrow x \in A$ for at least one $A \in \mathcal{A}$ .

(b) $x \in \bigcup_{A \in \mathcal{A}} A \Rightarrow x \in A$ for every $A \in \mathcal{A}$ .

(c) $x \in \bigcap_{A \in \mathcal{A}} A \Rightarrow x \in A$ for at least one $A \in \mathcal{A}$ .

(d) $x \in \bigcap_{A \in \mathcal{A}} A \Rightarrow x \in A$ for every $A \in \mathcal{A}$ .
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 1.5, printed pp. 7--8** (`tmp/sources/munkres-solutions-whitman.pdf`), which decides each implication and each converse; the verdicts below are his.

The counterexamples take $\mathcal A=\{\{1\},\{2\}\}$ and $x=1$, so that $\bigcup_{A\in\mathcal A}A=\{1,2\}$ and $\bigcap_{A\in\mathcal A}A=\varnothing$.

::: pf

::: {.pf-step #statement-a}
Statement (a) and its converse are both true.

::: pf-proof
By the definition of the union, $x\in\bigcup_{A\in\mathcal A}A$ if and only if $x\in A$ for at least one $A\in\mathcal A$.
:::

:::

::: {.pf-step #statement-b}
Statement (b) is false, and its converse is true.

::: pf-proof
For the counterexample, $x\in\bigcup_{A\in\mathcal A}A$ but $x\notin\{2\}$.
For the converse, if $x\in A$ for every $A\in\mathcal A$, then, since $\mathcal A$ is nonempty, $x$ lies in at least one member of $\mathcal A$, hence in the union.
:::

:::

::: {.pf-step #statement-c}
Statement (c) is true, and its converse is false.

::: pf-proof
If $x\in\bigcap_{A\in\mathcal A}A$, then $x$ lies in every member of $\mathcal A$, hence, since $\mathcal A$ is nonempty, in at least one.
For the converse, the counterexample has $x\in\{1\}$ but $x\notin\bigcap_{A\in\mathcal A}A=\varnothing$.
:::

:::

::: {.pf-step #statement-d}
Statement (d) and its converse are both true.

::: pf-proof
By the definition of the intersection, $x\in\bigcap_{A\in\mathcal A}A$ if and only if $x\in A$ for every $A\in\mathcal A$.
:::

:::

::: pf-qed
Steps [](#statement-a){.pf-ref} through [](#statement-d){.pf-ref} decide each of the four statements and its converse.
:::

:::

:::
