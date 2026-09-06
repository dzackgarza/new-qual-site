---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F07-04
kind: problem
title: Relative openness in an open subspace
classification:
  areas:
  - topology
  topics:
  - Subspace Topology
  - Point-Set Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against Part One, question 4 of the Topology Ph.D. Qualifying Exam dated January 12, 2008 in assets/attachments/F07phdtop.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Used the definition of the subspace topology in both directions; openness of B is the step making B intersect U open in X.
---

::: {.problem}
Let $B$ be an open subset of a topological space $X$.
Prove that a subset $A\subset B$ is relatively open in $B$ if and only if $A$ is open in $X$.
:::

::: {.solution}
<1>1. If $A$ is relatively open in $B$, then $A$ is open in $X$.
::: {.proof}
By definition of the subspace topology, relative openness of $A$ in $B$ means that there is an open set $U\subseteq X$ such that
\[
A=B\cap U.
\]
The set $B$ is open in $X$ by hypothesis, and $U$ is open in $X$.
Therefore their intersection $B\cap U=A$ is open in $X$.
:::

<1>2. If $A$ is open in $X$ and $A\subseteq B$, then $A$ is relatively open in $B$.
::: {.proof}
Since $A\subseteq B$,
\[
A=B\cap A.
\]
The second factor $A$ is open in $X$.
Thus $A$ has the form $B\cap U$ for an open subset $U=A$ of $X$, which is exactly the definition of being open in the subspace $B$.
:::

<1>3. Hence
\[
A\text{ is open in }B
\quad\Longleftrightarrow\quad
A\text{ is open in }X.
\]
::: {.proof}
Combine <1>1 and <1>2.
:::
:::
