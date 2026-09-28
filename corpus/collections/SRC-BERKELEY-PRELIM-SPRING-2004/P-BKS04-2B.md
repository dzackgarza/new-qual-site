---
schema: qual/card@1
id: P-BKS04-2B
kind: problem
title: UC Berkeley Spring 2004 prelim 2B
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
---

::: {.problem}
Find the maximum possible value of $\vert f ^ { \prime } ( 1 ) \vert$ given that f is holomorphic on an open neighborhood of $\{ z \in \mathbb { C } : | z | \leq 2 \}$ and satisfies $| f ( z ) | \leq 1$ when $| z | = 2$ .
:::

::: {.solution}
We will use a fractional linear transformation to change the problem to one where the derivative is evaluated at the center of a disk.

The function $z \mapsto { \frac { 2 } { z } } \left( { \frac { z - 1 } { { \bar { z } } - 1 } } \right)$ on $| z | = 2$ has absolute value 1, and it extends to a fractional linear transformation $\begin{array} { r } { g ( z ) = 2 \left( \frac { z - 1 } { 4 - z } \right) } \end{array}$ Since it also maps $z = 1$ to the interior of the unit disk, it must map the region $| z | \le 2$ bijectively onto the unit disk.
We calculate $| g ^ { \prime } ( 1 ) | = 2 / 3$

Now, for any other f mapping the circle $| z | = 2$ into $| z | \leq 1$ , the composition $h : = f \circ g ^ { - 1 }$ is holomorphic on a neighborhood of $| z | \le 1$ , and maps $| z | = 1$ into $| z | \leq 1$ . Taking absolute values in

$$
h ^ { \prime } ( 0 ) = \frac { 1 } { 2 \pi i } \int _ { | z | = 1 } \frac { h ( z ) } { z ^ { 2 } } d z
$$

gives $| h ^ { \prime } ( 0 ) | \ \leq \ 1$ Since $g ^ { - 1 } ( 0 ) = 1$ , the Chain Rule gives $h ^ { \prime } ( 0 ) ~ = ~ f ^ { \prime } ( 1 ) g ^ { \prime } ( 1 ) ^ { - 1 }$ Thus $| f ^ { \prime } ( 1 ) | = | h ^ { \prime } ( 0 ) | | g ^ { \prime } ( 1 ) | \leq | g ^ { \prime } ( 1 ) | = 2 / 3$ . Thus $2 / 3$ is the maximum possible value of $\vert f ^ { \prime } ( 1 ) \vert$ .
:::
