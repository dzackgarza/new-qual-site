---
schema: qual/card@1
id: E-MUN-4-3
kind: problem
title: Inductive sets and basic properties of $\mathbb{Z}_+$
classification:
  areas:
  - topology
  topics:
  - Integers and Real Numbers
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 4, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

(a) Show that if $\mathcal{A}$ is a collection of inductive sets, then the intersection of the elements of $\mathcal{A}$ is an inductive set.

(b) Prove the basic properties (1) and (2) of $\mathbb{Z}_{+}$ .
:::

::: {.solution}
(a) Let \(\mathcal A\) be a collection of inductive subsets of \(\mathbb R\), and put
\[
I=\bigcap_{A\in\mathcal A}A.
\]
Every \(A\in\mathcal A\) contains \(1\), so \(1\in I\). If \(x\in I\), then \(x\in A\) for every \(A\in\mathcal A\). Since each \(A\) is inductive, \(x+1\in A\) for every \(A\), hence \(x+1\in I\). Thus \(I\) is inductive.

(b) By definition, \(\mathbb Z_+\) is the intersection of all inductive subsets of \(\mathbb R\). Part (a) therefore shows immediately that \(\mathbb Z_+\) is itself inductive. This is property (1).

For property (2), let \(A\subset\mathbb Z_+\) be an inductive set of positive integers. Since \(A\) is an inductive subset of \(\mathbb R\), and \(\mathbb Z_+\) is the intersection of *all* such subsets,
\[
\mathbb Z_+\subset A.
\]
But by hypothesis \(A\subset\mathbb Z_+\). Hence
\[
A=\mathbb Z_+,
\]
which is the principle of induction.
:::
