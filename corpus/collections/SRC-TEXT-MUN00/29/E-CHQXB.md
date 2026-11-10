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
---

::: {.exercise}

Theorem.
Let $A \subset X$.
Then $x \in \overline{A}$ if and only if there is a net of points of $A$ converging to $x$.

[Hint: To prove the implication $\Rightarrow$, take as index set the collection of all neighborhoods of $x$, partially ordered by reverse inclusion.]
:::

::: {.solution}
If a net $(a_\alpha)$ in $A$ converges to $x$, then every neighborhood of $x$ contains some tail point $a_\alpha\in A$; hence every neighborhood of $x$ meets $A$, so $x\in\overline A$.

Conversely, assume $x\in\overline A$. Let $J$ be the set of neighborhoods of $x$, ordered by reverse inclusion:
$$
U\preceq V\iff U\supset V.
$$
This is directed because $U\cap V$ is a neighborhood of $x$ and satisfies $U\preceq U\cap V$ and $V\preceq U\cap V$. For each $U\in J$, choose $a_U\in A\cap U$, possible because $x\in\overline A$. Then the net $(a_U)_{U\in J}$ converges to $x$: if $W$ is a neighborhood of $x$, then for every $U\succeq W$ we have $U\subset W$, so $a_U\in W$.
:::
