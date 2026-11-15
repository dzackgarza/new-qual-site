---
schema: qual/card@1
id: E-CHQXB
kind: problem
title: Closure points detected by convergent nets
classification:
  areas:
  - topology
  topics:
  - Nets
  - Closure
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    No published set for this exercise was located. The sources searched, the pages they
    cover and the conclusion are recorded in COMPLAINTS.md under the entry for the net
    exercises of §29; the card's own proof is kept. The statement was read against Munkres,
    Topology (2000), §29 supplementary exercises on nets, printed pp. 187-188.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Transcribed from dbFin, "Supplementary Exercises*: Nets: Problem 6 Solution",
    https://dbfin.com/topology/munkres/chapter-3/supplementary-exercises-nets/problem-6-solution/,
    read 2026-11-15, text at tmp/sources/dbfin/supplementary-exercises-nets/problem-6.md, and
    checked against freakish's accepted answer to Math StackExchange 2465829 (2017-10-10),
    https://math.stackexchange.com/questions/2465829, text at
    tmp/sources/mse-2465829-munkres-29-net-6b.md, which proves the same equivalence through
    closed sets. dbFin names Exercise 1(c) for the directedness of the neighborhoods of x under
    reverse inclusion; the card states that directedness, as freakish does. The two directions are
    those of the hint printed with the exercise. This supersedes the 2026-11-10 note above.
---

::: {.exercise}

Theorem.
Let $A \subset X$.
Then $x \in \overline{A}$ if and only if there is a net of points of $A$ converging to $x$.

[Hint: To prove the implication $\Rightarrow$, take as index set the collection of all neighborhoods of $x$, partially ordered by reverse inclusion.]
:::

::: {.solution}

::: pf

::: pf-step
If some net of points of $A$ converges to $x$, then $x \in \overline{A}$.

::: pf-proof
Let $(x_\alpha)_{\alpha \in J}$ be a net with $x_\alpha \in A$ for all $\alpha$, converging to $x$, and let $U$ be any neighborhood of $x$. There is $\alpha \in J$ with $x_\alpha \in U$, and $x_\alpha \in A$; so $U \cap A \ne \varnothing$. Every neighborhood of $x$ thus meets $A$, that is, $x \in \overline{A}$.
:::

:::

::: pf-step
The neighborhoods of $x$, ordered by reverse inclusion, form a directed set.

::: pf-proof
Reverse inclusion is a partial order: $U \supset U$, and $U \supset V \supset U$ gives $U = V$, and $U \supset V \supset W$ gives $U \supset W$. Given neighborhoods $U$ and $V$ of $x$, the intersection $U \cap V$ is a neighborhood of $x$, and $U \supset U \cap V$ and $V \supset U \cap V$; so $U \cap V$ is an upper bound for the pair. The collection is nonempty since $X$ is a neighborhood of $x$.
:::

:::

::: pf-step
If $x \in \overline{A}$, then some net of points of $A$ converges to $x$.

::: pf-proof
Use the directed set $\mathcal{U}_x$ of neighborhoods of $x$ under reverse inclusion, which is directed by step 2. For $U \in \mathcal{U}_x$ the set $A \cap U$ is nonempty, because $x$ lies in the closure of $A$; choose $x_U \in A \cap U$. Given a neighborhood $U$ of $x$ and an index $V$ with $U \preceq V$, that is $V \subset U$, the point $x_V$ lies in $V$, hence in $U$ and in $A$. So $(x_U)_{U \in \mathcal{U}_x}$ is a net of points of $A$ converging to $x$.
:::

:::

::: pf-step
$x \in \overline{A}$ if and only if some net of points of $A$ converges to $x$. $\square$

::: pf-proof
The two implications are steps 1 and 3.
:::

:::

:::

:::
