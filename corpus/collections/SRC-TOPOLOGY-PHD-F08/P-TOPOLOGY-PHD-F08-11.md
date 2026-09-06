---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F08-11
kind: problem
title: Connected components in a locally connected space are open
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Point-Set Topology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked against Part One, question 11 of the Topology Ph.D. Qualifying Exam
    dated January 17, 2009 in assets/attachments/F08phdtop.pdf. The source's
    phrase "connected components of each point" is malformed; the standard
    intended definition is that each point has a neighborhood base of connected
    open sets.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Rewrote the older outline as a structured proof under the standard intended
    definition. A connected open neighborhood of x lies in the connected
    component containing x by maximality, so each component is a union of open
    neighborhoods of its points.
---

::: {.problem}
A topological space $X$ is said to be locally connected if the connected components of each point form a base of neighborhoods of $X$.
Prove that in a locally connected space the connected components of $X$ are open in $X$.
:::

::: {.solution}
The source definition is malformed as printed.
We use the standard intended definition: $X$ is locally connected if every point has a neighborhood base consisting of connected open sets.

<1>1. Let $C$ be a connected component of $X$ and let $x\in C$.
There is a connected open neighborhood $U_x$ of $x$.
::: {.proof}
By local connectedness, the point $x$ has a neighborhood base of connected open sets.
In particular, taking the neighborhood $X$ itself gives a connected open neighborhood
\[
x\in U_x\subseteq X.
\]
:::

<1>2. The neighborhood $U_x$ from <1>1 satisfies
\[
U_x\subseteq C.
\]
::: {.proof}
Both $C$ and $U_x$ are connected, and they meet at $x$.
The union of two connected subsets with nonempty intersection is connected, so
\[
C\cup U_x
\]
is connected.
Since $C$ is a connected component, it is maximal among connected subsets of $X$.
Because
\[
C\subseteq C\cup U_x,
\]
maximality forces
\[
C\cup U_x=C.
\]
Hence $U_x\subseteq C$.
:::

<1>3. The component $C$ is open in $X$.
::: {.proof}
By <1>1--<1>2, for every $x\in C$ there is an open set $U_x$ satisfying
\[
x\in U_x\subseteq C.
\]
Therefore
\[
C = \bigcup_{x \in C} U_x.
\]
An arbitrary union of open sets is open, so $C$ is open.
:::

<1>4. Hence every connected component of a locally connected space is open.
::: {.proof}
The component $C$ in <1>1 was arbitrary, and <1>3 proves it is open.
:::
:::
