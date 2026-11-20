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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps from the retained Whitman solution (Exercise 5.5, printed pp. 74-75); statement and the four answers unchanged. Parts (a)-(c) are one step each, each showing both inclusions through the coordinate condition. Part (d) is split into the two facts the refutation needs: that every real number must occur in the second and third factor, and that a product with those factors then contains a sequence with distinct second and third coordinates -- the second fact is what actually contradicts the defining relation, and the earlier prose asserted it without saying which sequence it uses. Pages added: the product and projection notation of §5 on printed p. 36, the exercise on printed p. 39.

---

::: {.exercise}

Which of the following subsets of $\RR^{\omega}$ can be expressed as the cartesian product of subsets of $\RR$ ?

(a) $\{x \mid x_{i} \text{ is an integer for all } i\}$ .

(b) $\{x \mid x_{i} \geq i \text{ for all } i\}$ .

(c) $\{\mathbf{x} \mid x_i$ is an integer for all $i \geq 100\}$ .

(d) $\{x \mid x_{2} = x_{3}\}$ .

:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 5.5** (`tmp/sources/munkres-solutions-whitman.pdf`), with the same four answers; the card replaces his two constant sequences in (d) by the equivalent argument that both values must lie in every factor.

Throughout, a subset $S\subset\RR^\omega$ is a cartesian product of subsets of $\RR$ when $S=\prod_{i\in\ZZ_+}A_i$ with $A_i\subset\RR$, and then $A_i$ is the $i$-th projection of $S$, since $\pi_i\big(\prod_jA_j\big)=A_i$ (§5; the exercise is on printed p. 39).

::: pf

::: {.pf-step #integers}
(a) $\{x:x_i\in\ZZ$ for all $i\}=\prod_i\ZZ$.

::: pf-proof
A sequence $x$ lies in the left-hand set exactly when each of its coordinates is an integer, which is exactly the condition $x_i\in\ZZ$ for every $i$, that is $x\in\prod_i\ZZ$.

:::

:::

::: {.pf-step #lower}
(b) $\{x:x_i\ge i$ for all $i\}=\prod_i[i,\infty)$.

::: pf-proof
$x$ lies in the left-hand set exactly when $x_i\ge i$ for every $i$, which is the condition $x_i\in[i,\infty)$ for every $i$.

:::

:::

::: {.pf-step #tail}
(c) $\{x:x_i\in\ZZ$ for all $i\ge100\}=\prod_{i<100}\RR\times\prod_{i\ge100}\ZZ$, that is, the product with $i$-th factor $\RR$ for $i<100$ and $\ZZ$ for $i\ge100$.

::: pf-proof
The defining condition constrains no coordinate below $100$ and requires each coordinate from $100$ on to be an integer, which is precisely membership in the displayed product.

:::

:::

::: {.pf-step #equality}
(d) $\{x:x_2=x_3\}$ is not a cartesian product of subsets of $\RR$.

::: pf-proof

::: {.pf-step #factors}
If $\{x:x_2=x_3\}=\prod_iA_i$ then $A_2=A_3=\RR$.

::: pf-proof
For $r\in\RR$ the constant sequence $x$ with $x_i=r$ for all $i$ satisfies $x_2=x_3$, so it lies in the product and its second and third coordinates show $r\in A_2$ and $r\in A_3$. As $r$ was arbitrary, $A_2=A_3=\RR$.

:::

:::

::: {.pf-step #contradiction}
The product $\prod_iA_i$ with $A_2=A_3=\RR$ contains a sequence with $x_2\ne x_3$, so it is not $\{x:x_2=x_3\}$.

::: pf-proof
Let $x$ have $x_2=0$, $x_3=1$ and $x_i=0$ for $i\ne2,3$; then $x_i\in A_i$ for every $i$ by step [](#factors){.pf-ref}, so $x\in\prod_iA_i$, while $x_2\ne x_3$. Hence $\prod_iA_i$ strictly contains $\{x:x_2=x_3\}$, so the two sets are not equal.

:::

:::

:::

:::

:::

:::
