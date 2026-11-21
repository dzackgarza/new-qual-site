---
schema: qual/card@1
id: E-MUN-1-6
kind: problem
title: Contrapositives of quantified subset statements
classification:
  areas:
  - topology
  topics:
  - Fundamental Concepts
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 1, Exercise 6; the stored statement matches.
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
    Read against Munkres, Topology (2000), §1 Exercise 6, printed p. 14; the stored
    statement matches, and the reference to Exercise 5 is to the four statements stored
    on E-MUN-1-5.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 1.6,
    printed p. 8 (tmp/sources/munkres-solutions-whitman.pdf). His four contrapositives
    agree with the card's, and the observation that a statement and its contrapositive
    have the same truth value, used to read the truth values off Exercise 5, is his.
---

::: {.exercise}

Write the contrapositive of each of the statements of Exercise 5.
:::

::: {.solution}

The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 1.6, printed p. 8** (`tmp/sources/munkres-solutions-whitman.pdf`); the four contrapositives below are his.

::: pf

::: {.pf-step #definition}

The contrapositive of $P\Rightarrow Q$ is $\neg Q\Rightarrow\neg P$, and the two implications have the same truth value.

::: pf-proof

$P\Rightarrow Q$ is equivalent to $\neg P\lor Q$, and $\neg Q\Rightarrow\neg P$ is equivalent to $\neg\neg Q\lor\neg P=Q\lor\neg P$, the same disjunction. So an implication and its contrapositive are true under exactly the same assignments, and a false implication has a true contrapositive only if the original was true: replacing a statement of Exercise 5 by its contrapositive preserves its truth value.

:::

:::

::: {.pf-step #contrapositives}

Applying this to the statements of [[E-MUN-1-5]] gives the four implications (a)--(d) displayed below.

::: pf-proof

The statements of [[E-MUN-1-5]] are implications about a point $x$ and a family $\mathcal A$ of sets; negating the hypothesis and the conclusion and reversing the arrow in each yields
(a) $\bigl(x\notin A$ for every $A\in\mathcal A\bigr)\Longrightarrow x\notin\bigcup_{A\in\mathcal A}A$;
(b) $\bigl(x\notin A$ for at least one $A\in\mathcal A\bigr)\Longrightarrow x\notin\bigcup_{A\in\mathcal A}A$;
(c) $\bigl(x\notin A$ for every $A\in\mathcal A\bigr)\Longrightarrow x\notin\bigcap_{A\in\mathcal A}A$;
(d) $\bigl(x\notin A$ for at least one $A\in\mathcal A\bigr)\Longrightarrow x\notin\bigcap_{A\in\mathcal A}A$.
Each is obtained from the corresponding statement of Exercise 5 by the rule of step [](#definition){.pf-ref}, interchanging "for every" with "for at least one" as negation requires and replacing $\in$ by $\notin$ and $\bigcup$ by $\bigcap$ where the negated conclusion demands.

:::

:::

::: {.pf-step #truth}

(a), (c) and (d) are true and (b) is false.

::: pf-proof

By step [](#definition){.pf-ref} each of (a)--(d) has the truth value of the statement of Exercise 5 it came from, and by [[E-MUN-1-5]] those four statements have truth values true, false, true, true in the order (a)--(d). So (a), (c) and (d) are true, while (b) is false: a point lying in some but not all members of the family has $x\notin A$ for at least one $A$ and yet $x\in\bigcup_{A}A$. So
$$
\boxed{\text{(a), (c), (d) true};\quad\text{(b) false},}
$$
and the truth values agree with those of the statements of Exercise 5.

:::

:::

:::

:::
