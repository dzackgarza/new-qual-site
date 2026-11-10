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
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §10 Exercise 7, printed pp. 67-68; the stored
    statement is the printed definition of inductive and the printed theorem.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 10.7, printed p. 112.
    The proof is his: the least element of J - J_0 has all its predecessors in J_0, so
    inductivity puts it in J_0, a contradiction.
---

::: {.exercise}

Let $J$ be a well-ordered set.
A subset $J_0$ of $J$ is said to be inductive if for every $\alpha \in J$,

$$
(S_\alpha \subset J_0) \Longrightarrow \alpha \in J_0.
$$

Prove the following theorem (the principle of transfinite induction).
If $J$ is a well-ordered set and $J_0$ is an inductive subset of $J$, then $J_0 = J$.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 10.7, printed p. 112** (`tmp/sources/munkres-solutions-whitman.pdf`); the proof is his.

Let $J$ be well ordered and let $J_{0}\subset J$ be inductive: for every $\alpha\in J$, if $S_{\alpha}\subset J_{0}$ then $\alpha\in J_{0}$. Suppose $J_{0}\ne J$. Then $J-J_{0}$ is a nonempty subset of the well-ordered set $J$, so it has a smallest element $\alpha$.

Let $y\in S_{\alpha}$, so $y<\alpha$. Since $\alpha$ is the smallest element of $J-J_{0}$, the element $y$ does not lie in $J-J_{0}$; as $y\in J$, this means $y\in J_{0}$. Hence $S_{\alpha}\subset J_{0}$, and since $J_{0}$ is inductive, $\alpha\in J_{0}$. This contradicts $\alpha\in J-J_{0}$. So $J_{0}=J$.
:::
