---
schema: qual/card@1
id: E-MUN-10-7
kind: problem
title: Principle of transfinite induction
classification:
  areas:
  - topology
  topics:
  - Well-Ordered Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 10, Exercise 7; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $J$ be a well-ordered set.
A subset $J_0$ of $J$ is said to be inductive if for every $\alpha \in J$,

$$
(S _ {\alpha} \subset J _ {0}) \Longrightarrow \alpha \in J _ {0}
$$

Theorem (The principle of transfinite induction).
If $J$ is a well-ordered set and $J_0$ is an inductive subset of $J$, then $J_0 = J$ .
:::

::: {.solution}
Suppose \(J_0
e J\). Since \(J\) is well-ordered, the nonempty set \(J-J_0\) has a smallest element; call it \(\alpha\). Every \(x<\alpha\) lies in \(J_0\) by minimality of \(\alpha\). Hence
\[
S_\alpha\subset J_0.
\]
Since \(J_0\) is inductive, this implies \(\alpha\in J_0\), contradicting \(\alpha\in J-J_0\). Therefore
\[
\boxed{J_0=J}.
\]
:::
