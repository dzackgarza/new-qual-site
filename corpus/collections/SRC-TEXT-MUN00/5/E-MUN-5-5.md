---
schema: qual/card@1
id: E-MUN-5-5
kind: problem
title: Subsets of $\RR^{\omega}$ as Cartesian products
classification:
  areas:
  - topology
  topics:
  - Cartesian Products
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 5, Exercise 5; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Which of the following subsets of $\RR^{\omega}$ can be expressed as the cartesian product of subsets of $\RR$ ?

(a) $\{x \mid x_{i} \text{ is an integer for all } i\}$ .

(b) $\{x \mid x_{i} \geq i \text{ for all } i\}$ .

(c) $\{\mathbf{x} \mid x_i$ is an integer for all $i \geq 100\}$ .

(d) $\{x \mid x_{2} = x_{3}\}$ .
:::

::: {.solution}
(a) Yes. The set is
\[
\prod_{i=1}^{\infty}\ZZ.
\]

(b) Yes. It is
\[
\prod_{i=1}^{\infty}[i,\infty).
\]

(c) Yes. It is
\[
\left(\prod_{i=1}^{99}\RR\right)
\times
\left(\prod_{i=100}^{\infty}\ZZ\right).
\]
Equivalently, take the \(i\)-th factor to be \(\RR\) for \(i<100\) and \(\ZZ\) for \(i\ge100\).

(d) No. Suppose
\[
\{x:x_2=x_3\}=\prod_i A_i.
\]
For every \(r\in\RR\) there is a sequence in the set having \(x_2=x_3=r\), so necessarily
\[
A_2=A_3=\RR.
\]
But then the product contains a sequence with \(x_2=0\) and \(x_3=1\), contradicting the defining relation \(x_2=x_3\). Thus this subset is not a cartesian product of coordinate subsets.
:::
