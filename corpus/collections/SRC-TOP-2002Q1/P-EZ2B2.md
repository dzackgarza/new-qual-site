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
Fix $x\in A\cap\overline B$, and suppose $A\cup B=P\sqcup Q$ with $P$ and $Q$ disjoint and open in the subspace $A\cup B$.
It suffices to show that $P$ or $Q$ is empty.

::: pf

::: {.pf-step #a-or-b-same-side}
Each of $A$ and $B$ lies entirely in $P$ or entirely in $Q$.

::: pf-proof
The sets $A\cap P$ and $A\cap Q$ are disjoint and open in $A$, and their union is $A$.
Since $A$ is connected, one of them is empty; hence $A\subseteq P$ or $A\subseteq Q$.
The same argument applies to $B$.
:::

:::

::: {.pf-step #not-different-sides}
$A$ and $B$ do not lie in different members of $\{P,Q\}$.

::: pf-proof
Suppose, after interchanging $P$ and $Q$ if necessary, that $A\subseteq P$ and $B\subseteq Q$.
Since $x\in A\subseteq P$ and $P$ is open in $A\cup B$, there is an open set $O\subseteq X$ with $x\in O$ and $O\cap(A\cup B)=P$.
Because $x\in\overline B$, the neighborhood $O$ meets $B$.
But $O\cap B\subseteq O\cap(A\cup B)=P$ and $B\subseteq Q$, so $O\cap B\subseteq P\cap Q=\varnothing$, a contradiction.
:::

:::

::: pf-qed
By steps [](#a-or-b-same-side){.pf-ref} and [](#not-different-sides){.pf-ref}, $A$ and $B$ lie in the same member of $\{P,Q\}$, say $P$.
Then $A\cup B\subseteq P$, so $Q=\varnothing$.
Hence $A\cup B$ has no separation into two nonempty disjoint relatively open sets, and $A\cup B$ is connected.
:::

:::

:::
