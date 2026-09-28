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
The counterexamples take $\mathcal A=\{\{1\},\{2\}\}$ and $x=1$, so that $\bigcup_{A\in\mathcal A}A=\{1,2\}$ and $\bigcap_{A\in\mathcal A}A=\varnothing$.

<1>1. Statement (a) and its converse are both true.

::: {.proof}
By the definition of the union, $x\in\bigcup_{A\in\mathcal A}A$ if and only if $x\in A$ for at least one $A\in\mathcal A$.
:::

<1>2. Statement (b) is false, and its converse is true.

::: {.proof}
For the counterexample, $x\in\bigcup_{A\in\mathcal A}A$ but $x\notin\{2\}$.
For the converse, if $x\in A$ for every $A\in\mathcal A$, then, since $\mathcal A$ is nonempty, $x$ lies in at least one member of $\mathcal A$, hence in the union.
:::

<1>3. Statement (c) is true, and its converse is false.

::: {.proof}
If $x\in\bigcap_{A\in\mathcal A}A$, then $x$ lies in every member of $\mathcal A$, hence, since $\mathcal A$ is nonempty, in at least one.
For the converse, the counterexample has $x\in\{1\}$ but $x\notin\bigcap_{A\in\mathcal A}A=\varnothing$.
:::

<1>4. Statement (d) and its converse are both true.

::: {.proof}
By the definition of the intersection, $x\in\bigcap_{A\in\mathcal A}A$ if and only if $x\in A$ for every $A\in\mathcal A$.
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>1 through <1>4 decide each of the four statements and its converse.
:::
:::
