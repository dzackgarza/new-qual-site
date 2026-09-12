---
schema: qual/card@1
id: P-BKS04-8B
kind: problem
title: UC Berkeley Spring 2004 prelim 8B
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
For each real number x, compute

$$
\operatorname* { l i m } _ { n \to \infty } n \left( \left( 1 + { \frac { x } { n } } \right) ^ { n } - e ^ { x } \right) .
$$
:::

::: {.solution}
We have

$$
\begin{array} { c } { { n \left( \left( 1 + \displaystyle \frac { x } { n } \right) ^ { n } - e ^ { x } \right) = n \left( e ^ { n \log ( 1 + x / n ) } - e ^ { x } \right) } } \\ { { = n e ^ { x } \left( e ^ { n \log ( 1 + x / n ) - x } - 1 \right) . } } \end{array}
$$

Taylor’s Theorem with Remainder gives

$$
\log \left( 1 + { \frac { x } { n } } \right) = { \frac { x } { n } } - { \frac { 1 } { 2 } } \left( { \frac { x ^ { 2 } } { n ^ { 2 } } } \right) + O \left( { \frac { 1 } { n ^ { 3 } } } \right)
$$

where the constant in the big-O depends on x, but not on n. Substituting, we get

$$
n e ^ { x } \left( e ^ { - \frac { x ^ { 2 } } { 2 n } + O \left( \frac { 1 } { n ^ { 2 } } \right) } - 1 \right) .
$$

Since $e ^ { y } = 1 + y + O ( y ^ { 2 } )$ as $y  0$ , this becomes

$$
n e ^ { x } \left( - \frac { x ^ { 2 } } { 2 n } + O \left( \frac { 1 } { n ^ { 2 } } \right) \right) = - \frac { 1 } { 2 } x ^ { 2 } e ^ { x } + O \left( \frac { 1 } { n } \right) ,
$$

so the limit is $- { \textstyle \frac { 1 } { 2 } } x ^ { 2 } e ^ { x }$
:::
