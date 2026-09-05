---
schema: qual/card@1
id: P-EZ2B2
kind: problem
title: The union of connected sets is connected if one meets the closure of the other
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Closure
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked the statement against Section A, problem A3 of the January 18, 2002 topology qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Argued directly from a hypothetical separation of A union B. Connectedness
    forces A and B into opposite separation pieces, while a point of A in
    cl(B) forces every relative neighborhood on A's side to meet B.
---

::: {.problem}
Let $X$ be a topological space, and $A, B \subseteq X$ be connected subsets of $X$.
Show that if $A \cap \overline{B} \ne \varnothing$, then $A \cup B$ is a connected subset of $X$.
:::

::: {.solution}
Suppose
\[
x\in A\cap\overline B.
\]

<1>1. Assume for contradiction that $A\cup B$ is disconnected, and let
\[
A\cup B=P\sqcup Q
\]
be a separation into two nonempty sets that are open in the subspace $A\cup B$.
::: {.proof}
This is exactly the negation of connectedness of $A\cup B$.
:::

<1>2. Each of the connected sets $A$ and $B$ lies entirely in one member of the separation, and they must lie in different members.
::: {.proof}
The sets
\[
A\cap P,
\qquad
A\cap Q
\]
are disjoint and open in $A$, and their union is $A$.
Since $A$ is connected, one of them is empty; hence either $A\subseteq P$ or $A\subseteq Q$.
The same argument shows either $B\subseteq P$ or $B\subseteq Q$.

If both $A$ and $B$ were contained in the same member, say $P$, then
\[
A\cup B\subseteq P,
\]
forcing $Q=\varnothing$, contrary to the definition of a separation.
Thus, after interchanging $P$ and $Q$ if necessary,
\[
A\subseteq P,
\qquad
B\subseteq Q.
\]
:::

<1>3. The inclusion $x\in\overline B$ contradicts the separation in <1>2.
::: {.proof}
Since $x\in A\subseteq P$ and $P$ is open in the subspace $A\cup B$, there is an open set $O\subseteq X$ such that
\[
x\in O
\qquad\text{and}\qquad
O\cap(A\cup B)=P.
\]
Because $x\in\overline B$, every open neighborhood of $x$ in $X$ meets $B$, so
\[
O\cap B\neq\varnothing.
\]
But $B\subseteq Q$, whereas
\[
O\cap B
\subseteq
O\cap(A\cup B)
=P.
\]
Thus $O\cap B\subseteq P\cap Q=\varnothing$, a contradiction.
:::

<1>4. Therefore $A\cup B$ is connected.
::: {.proof}
The assumed separation in <1>1 leads to the contradiction in <1>3. Hence no separation of $A\cup B$ exists.
:::
:::
