---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS1-P2
kind: problem
title: Closed covering by two sets with connected intersection forces both closed sets to be connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
(May 2016) Let $X$ be a connected space and $A,B\subseteq X$ be closed subsets of $X$ with $X=A\cup B$ and $A\cap B$ a connected subset of $X$.
Show that both $A$ and $B$ are connected.
:::

::: {.solution}
We prove that \(A\) is connected; the argument for \(B\) is symmetric.

Suppose \(A\) were disconnected. Then
\[
A=C\sqcup D
\]
with \(C,D\) nonempty and both open and closed in \(A\). Since \(A\) is closed in \(X\), the sets \(C\) and \(D\), being closed in \(A\), are closed in \(X\).

The connected set \(A\cap B\) is contained in the disjoint union \(C\cup D\), so it cannot meet both \(C\) and \(D\). After relabeling, assume
\[
A\cap B\subseteq C.
\]
Then \(D\cap B=\varnothing\). Since
\[
X=A\cup B=C\cup D\cup B,
\]
we have
\[
X\setminus D=C\cup B.
\]
The right-hand side is closed in \(X\), so \(D\) is open in \(X\). We already know \(D\) is closed and nonempty. It is also proper, since \(C\ne\varnothing\). Thus \(D\) is a nontrivial clopen subset of the connected space \(X\), contradiction.

Therefore \(A\) is connected, and similarly \(B\) is connected.
:::
