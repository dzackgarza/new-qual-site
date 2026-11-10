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
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §5 Exercise 5, printed p. 39; the four
    subsets of R^omega are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 5.5,
    printed pp. 74-75 (tmp/sources/munkres-solutions-whitman.pdf). His answers are the
    card's: (a), (b) and (c) are the products of Z, of [i, infinity) and of R up to the
    99th coordinate and Z after it; (d) fails, his witness being that two sequences in
    the set with different constant values force every factor to contain both values.
    No defect found.
---

::: {.exercise}

Which of the following subsets of $\RR^{\omega}$ can be expressed as the cartesian product of subsets of $\RR$ ?

(a) $\{x \mid x_{i} \text{ is an integer for all } i\}$ .

(b) $\{x \mid x_{i} \geq i \text{ for all } i\}$ .

(c) $\{\mathbf{x} \mid x_i$ is an integer for all $i \geq 100\}$ .

(d) $\{x \mid x_{2} = x_{3}\}$ .
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 5.5, printed pp. 74--75** (`tmp/sources/munkres-solutions-whitman.pdf`), with the same four answers; the card replaces his two constant sequences in (d) by the equivalent argument that both values must lie in every factor.

(a) Yes. The set is
$$
\prod_{i=1}^{\infty}\ZZ.
$$

(b) Yes. It is
$$
\prod_{i=1}^{\infty}[i,\infty).
$$

(c) Yes. It is
$$
\left(\prod_{i=1}^{99}\RR\right)
\times
\left(\prod_{i=100}^{\infty}\ZZ\right).
$$
Equivalently, take the $i$-th factor to be $\RR$ for $i<100$ and $\ZZ$ for $i\ge100$.

(d) No. Suppose
$$
\{x:x_2=x_3\}=\prod_i A_i.
$$
For every $r\in\RR$ there is a sequence in the set having $x_2=x_3=r$, so necessarily
$$
A_2=A_3=\RR.
$$
But then the product contains a sequence with $x_2=0$ and $x_3=1$, contradicting the defining relation $x_2=x_3$. Thus this subset is not a cartesian product of coordinate subsets.
:::
