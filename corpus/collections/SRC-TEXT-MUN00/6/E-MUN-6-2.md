---
schema: qual/card@1
id: E-MUN-6-2
kind: problem
title: Subsets of finite sets are finite
classification:
  areas:
  - topology
  topics:
  - Finite Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 6, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Show that if $B$ is not finite and $B \subset A$, then $A$ is not finite.
:::

::: {.solution}
Suppose, toward a contradiction, that $A$ were finite. We first prove by
induction on $n$ that every subset of $\{1,\dots,n\}$ is finite. For $n=0$,
the only subset is empty. Assume the claim for $n$ and let
$C\subset\{1,\dots,n+1\}$. If $n+1\notin C$, the induction hypothesis
applies. If $n+1\in C$, then $C-\{n+1\}$ is finite by the induction
hypothesis, and adjoining one point gives a finite set. This proves the
claim for $n+1$.

Now identify $A$ with $\{1,\dots,n\}$. The image of $B$ under this
bijection is a subset of $\{1,\dots,n\}$, hence is finite by the claim.
Thus $B$ is finite, contrary to the hypothesis.

Therefore
$$
B\subset A\text{ and }B\text{ infinite}\quad\Longrightarrow\quad A\text{ infinite}.
$$
Equivalently, this is the contrapositive of the statement that every subset of a finite set is finite.
:::
