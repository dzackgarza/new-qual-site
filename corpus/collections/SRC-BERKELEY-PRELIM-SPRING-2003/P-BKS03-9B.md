---
schema: qual/card@1
id: P-BKS03-9B
kind: problem
title: An uncountable subset of $\mathbb R$ has uncountably many accumulation points
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Let $A\subseteq\mathbb R$ be uncountable.

(a) Show that $A$ has at least one accumulation point.

(b) Show that $A$ has uncountably many accumulation points.
:::

::: {.solution}
(a) For $n\in\mathbb{Z}$ let $A_n=A\cap[n,n+1)$.
Then $A=\bigcup_{n\in\mathbb{Z}}A_n$.
Since $A$ is uncountable, at least one of the sets $A_n$ needs to be uncountable.
Then we can find a sequence in $A_n$ with distinct terms.
This sequence is bounded, so it has a convergent subsequence.
The limit of the subsequence is an accumulation point for $A$.

(b) Denote by $B$ the set of accumulation points.
Assume by contradiction that $B$ is at most countable.
The set $B$ is closed, so its complement $\mathbb{R}\setminus B$ is open.
Then we can represent it as a countable union of closed sets, $\mathbb{R}\setminus B=\bigcup_n C_n$.
If $B$ is at most countable then $A$ must have uncountably many elements in $\mathbb{R}\setminus B$, therefore in one of the sets $C_n$.
By part (a), $A\cap C_n$ has at least one accumulation point.
$C_n$ is closed, so this accumulation point is in $C_n$.
This contradicts the fact that all accumulation points of $A$ are in $B$, which does not intersect $C_n$.
:::
