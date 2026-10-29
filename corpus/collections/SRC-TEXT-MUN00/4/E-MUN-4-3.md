---
schema: qual/card@1
id: E-MUN-4-3
kind: problem
title: Inductive sets and basic properties of $\ZZ_+$
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

(b) Prove the basic properties (1) and (2) of $\ZZ_{+}$ .
:::

::: {.solution}
(a) Let \(\mathcal A\) be a collection of inductive subsets of \(\RR\), and put
\[
I=\bigcap_{A\in\mathcal A}A.
\]
Every \(A\in\mathcal A\) contains \(1\), so \(1\in I\). If \(x\in I\), then \(x\in A\) for every \(A\in\mathcal A\). Since each \(A\) is inductive, \(x+1\in A\) for every \(A\), hence \(x+1\in I\). Thus \(I\) is inductive.

(b) By definition, \(\ZZ_+\) is the intersection of all inductive subsets of \(\RR\). By part (a), \(\ZZ_+\) is itself inductive. This is property (1).

For property (2), let \(A\subset\ZZ_+\) be an inductive set of positive integers. Since \(A\) is an inductive subset of \(\RR\), and \(\ZZ_+\) is the intersection of all such subsets,
\[
\ZZ_+\subset A.
\]
But by hypothesis \(A\subset\ZZ_+\). Hence
\[
A=\ZZ_+,
\]
which is the principle of induction.
:::
