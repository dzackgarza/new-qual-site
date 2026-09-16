---
schema: qual/card@1
id: P-PRACT20-W3-06
kind: problem
title: Convergence of $\sum n!\,x^n$ and $\sum n!\,x^{n^2}$
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
For which x does $\textstyle \sum _ { n = 1 } ^ { \infty } n ! x ^ { n }$ converge?
What about $\scriptstyle \sum _ { n = 1 } ^ { \infty } n ! x ^ { n ^ { 2 } } ?$
:::

::: {.solution}
The first series does not converge for any nonzero x since the ratio test results in

$$
\operatorname* { l i m } _ { n \to \infty } \left| { \frac { ( n + 1 ) ! x ^ { n + 1 } } { n ! x ^ { n } } } \right| = ( n + 1 ) | x | = \infty
$$

when $x \neq 0$ . The second series converges for $| x | < 1$ . Indeed, performing the ratio test we see

$$
\operatorname* { l i m } _ { n \to \infty } \frac { ( n + 1 ) ! x ^ { n ^ { 2 } + 2 n + 1 } } { n ! x ^ { n ^ { 2 } } } = \operatorname* { l i m } _ { n \to \infty } ( n + 1 ) | x | ^ { 2 n + 1 } = \operatorname* { l i m } _ { n \to \infty } ( n + 1 ) e ^ { \log | x | ( 2 n + 1 ) } = \left\{ \begin{array} { l l } { 0 , } & { | x | < 1 , } \\ { + \infty , } & { | x | \geq 1 . } \end{array} \right.
$$
:::
