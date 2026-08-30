---
schema: qual/card@1
id: E-E9PMX
kind: exercise
title: Nested closed sets in countably compact spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
review: draft
---

::: {.exercise}

Show that $X$ is countably compact if and only if every nested sequence $C_1 \supset C_2 \supset \cdots$ of closed nonempty sets of $X$ has a nonempty intersection.
:::

::: solution
**Theorem.**  
For a topological space $X$, the following are equivalent:

1. $X$ is countably compact.
2. Every nested sequence of nonempty closed sets $C_1\supseteq C_2\supseteq\cdots$ has
   $\bigcap_{n\ge1}C_n\neq\varnothing$.

*Proof.*

**Lemma 1.**  
If $X$ is countably compact, every nested nonempty closed sequence has nonempty intersection.

*Proof.*  
Assume $C_1\supseteq C_2\supseteq\cdots$ and each $C_n$ is nonempty closed.
Suppose $\bigcap_{n\ge1} C_n=\varnothing$.
Then $U_n:=X\setminus C_n$ is an increasing open cover of $X$.
If $X$ were countably compact, some finite subcover
$\bigcup_{n=1}^N U_n=X$ exists, hence
$$
X\setminus \bigcup_{n=1}^N U_n=\bigcap_{n=1}^N C_n=\varnothing,
$$
contradicting nonemptiness of each $C_n$ and especially $C_N$. ∎

**Lemma 2.**  
If every nested nonempty closed sequence has nonempty intersection, then $X$ is countably compact.

*Proof.*  
Let $\{U_n\}_{n\ge1}$ be a countable open cover.
Assume no finite subcover exists.
Define
$$
C_n:=X\setminus\bigcup_{k=1}^n U_k.
$$
Each $C_n$ is nonempty closed and $C_{n+1}\subseteq C_n$.
By hypothesis, pick $x\in\bigcap_{n\ge1} C_n$.
Then $x\notin U_n$ for all $n$, contradicting that $\{U_n\}$ covers $X$. ∎

By Lemma 1 and Lemma 2 the two conditions are equivalent. ∎
:::

::: {.solution}
<1>1. $X$ compact.
Proof: Heine-Borel.

<1>2. Q.E.D.
Proof: <1>1.
:::
