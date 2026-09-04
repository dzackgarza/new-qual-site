---
schema: qual/card@1
id: P-KSQQ5
kind: problem
title: The intersection of two topologies is a topology; the union need not be
classification:
  areas:
  - topology
  topics:
  - Point-Set Topology
  - Counterexamples
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 1 of the official UGA Fall 2016 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified all topology axioms for the intersection and checked the three-point counterexample explicitly.
---

::: {.problem}
Let $\mcs, \mct$ be topologies on a set $X$.
Show that $\mcs \cap \mct$ is a topology on $X$.

Give an example to show that $\mcs \cup \mct$ need not be a topology.
:::

::: {.solution}
<1>1. The collection $\mcs\cap\mct$ contains $\emptyset$ and $X$.
::: {.proof}
Since $\mcs$ and $\mct$ are topologies on $X$,
\[
\emptyset,X\in\mcs
\qquad\text{and}\qquad
\emptyset,X\in\mct.
\]
Hence
\[
\emptyset,X\in\mcs\cap\mct.
\]
:::

<1>2. The collection $\mcs\cap\mct$ is closed under arbitrary unions.
::: {.proof}
Let $\{U_i\}_{i\in I}$ be any family of sets in $\mcs\cap\mct$.
Then every $U_i$ belongs to both $\mcs$ and $\mct$.
Because each is a topology,
\[
\bigcup_{i\in I}U_i\in\mcs
\qquad\text{and}\qquad
\bigcup_{i\in I}U_i\in\mct.
\]
Therefore
\[
\bigcup_{i\in I}U_i\in\mcs\cap\mct.
\]
:::

<1>3. The collection $\mcs\cap\mct$ is closed under finite intersections.
::: {.proof}
If $U_1,\dots,U_r\in\mcs\cap\mct$, then all of them belong to each of $\mcs$ and $\mct$.
Thus
\[
U_1\cap\cdots\cap U_r\in\mcs
\qquad\text{and}\qquad
U_1\cap\cdots\cap U_r\in\mct,
\]
so
\[
U_1\cap\cdots\cap U_r\in\mcs\cap\mct.
\]
:::

<1>4. Hence $\mcs\cap\mct$ is a topology on $X$.
::: {.proof}
Steps <1>1--<1>3 are exactly the topology axioms.
:::

<1>5. The union of two topologies need not be a topology.
::: {.proof}
Let
\[
X=\{a,b,c\},
\]
and define
\[
\mcs=\{\emptyset,X,\{a\}\},
\qquad
\mct=\{\emptyset,X,\{b\}\}.
\]
Each collection is a topology: apart from $\emptyset$ and $X$, it has only one nontrivial open set, so it is plainly closed under arbitrary unions and finite intersections.

However,
\[
\{a\},\{b\}\in\mcs\cup\mct,
\]
while
\[
\{a\}\cup\{b\}=\{a,b\}\notin\mcs\cup\mct.
\]
Thus $\mcs\cup\mct$ is not closed under unions and is not a topology.
:::
:::
