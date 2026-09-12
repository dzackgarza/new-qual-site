---
schema: qual/card@1
id: P-PRACT20-W3-02
kind: problem
title: "Week 3: Calculus II (Part 2) & Calculus III, problem 2"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
For which values of x does $\sum _ { n = 1 } ^ { \infty } { \frac { n ! x ^ { 2 n } } { n ^ { n } ( 1 + x ^ { 2 n } ) } }$ converge?
:::

::: {.solution}
Using $\frac { x ^ { 2 n } } { 1 + x ^ { 2 n } } \leq 1$ , we see that for any x,

$$
\sum _ { n = 1 } ^ { \infty } { \frac { n ! x ^ { 2 n } } { n ^ { n } ( 1 + x ^ { 2 n } ) } } \leq \sum _ { n = 1 } ^ { \infty } { \frac { n ! } { n ^ { n } } } .
$$

The latter sum converges; thus the former converges for all $x \in \mathbb { R }$ . To prove the latter converges, use the ratio test:

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { a _ { n + 1 } } { a _ { n } } } = \operatorname* { l i m } _ { n \to \infty } { \frac { ( n + 1 ) ! n ^ { n } } { n ! ( n + 1 ) ^ { n + 1 } } } = \operatorname* { l i m } _ { n \to \infty } { \frac { 1 } { \left( 1 + { \frac { 1 } { n } } \right) ^ { n } } } = { \frac { 1 } { e } } < 1 .
$$
:::
