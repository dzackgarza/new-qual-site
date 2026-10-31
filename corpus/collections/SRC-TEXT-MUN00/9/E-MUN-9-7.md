---
schema: qual/card@1
id: E-MUN-9-7
kind: problem
title: Strict cardinality ordering and iterated power sets
classification:
  areas:
  - topology
  topics:
  - Infinite Sets and the Axiom of Choice
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 9, Exercise 7; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $A$ and $B$ be two nonempty sets.
If there is an injection of $B$ into $A$, but no injection of $A$ into $B$, we say that $A$ has greater cardinality than $B$ .

(a) Conclude from Theorem 9.1 that every uncountable set has greater cardinality than $\ZZ_{+}$ .

(b) Show that if $A$ has greater cardinality than $B$, and $B$ has greater cardinality than $C$, then $A$ has greater cardinality than $C$ .

(c) Find a sequence $A_1, A_2, \ldots$ of infinite sets, such that for each $n \in \ZZ_+$, the set $A_{n+1}$ has greater cardinality than $A_n$ .

(d) Find a set that for every $n$ has cardinality greater than $A_{n}$ .
:::

::: {.solution}
(a) Let $A$ be uncountable. Since $A$ is infinite, Theorem 9.1 gives an injection
$$
\ZZ_+\hookrightarrow A.
$$
There cannot be an injection $A\hookrightarrow\ZZ_+$, for then $A$ would be countable by Theorem 7.1. Hence $A$ has greater cardinality than $\ZZ_+$.

(b) Suppose $A$ has greater cardinality than $B$, and $B$ greater cardinality than $C$. There are injections
$$
C\hookrightarrow B\hookrightarrow A,
$$
so there is an injection $C\hookrightarrow A$. If there were an injection $A\hookrightarrow C$, composing with $C\hookrightarrow B$ would give an injection $A\hookrightarrow B$, contradicting that $A$ has greater cardinality than $B$. Thus $A$ has greater cardinality than $C$.

(c) Let
$$
A_1=\ZZ_+,
\qquad
A_{n+1}=\mathcal P(A_n).
$$
The map $a\mapsto\{a\}$ injects $A_n$ into $A_{n+1}$, while Cantor's theorem says there is no injection $A_{n+1}\to A_n$. Hence $A_{n+1}$ has greater cardinality than $A_n$ for every $n$.

(d) Set
$$
A=\bigcup_{n\ge1}A_n.
$$
Each $A_n$ injects into $A$ by inclusion. For a fixed $n$, if there were an injection $A\to A_n$, then restricting it to the subset $A_{n+1}\subset A$ would give an injection $A_{n+1}\to A_n$, contradicting part (c). Hence $A$ has greater cardinality than every $A_n$.

:::
