---
schema: qual/card@1
id: P-PRACT20-W3-06
kind: problem
title: Convergence of $\sum n!\,x^n$ and $\sum n!\,x^{n^2}$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
For which $x$ does $\sum_{n=1}^{\infty} n!\, x^{n}$ converge?
What about $\sum_{n=1}^{\infty} n!\, x^{n^{2}}$?
:::

::: {.solution}
The first series does not converge for any nonzero x since the ratio test results in

$$
\operatorname* { l i m } _ { n \to \infty } \abs{ { \frac { ( n + 1 ) ! x ^ { n + 1 } } { n ! x ^ { n } } } } = ( n + 1 ) \abs{ x } = \infty
$$

when $x \neq 0$ . The second series converges for $\abs{ x } < 1$ . Indeed, performing the ratio test we see

$$
\operatorname* { l i m } _ { n \to \infty } \frac { ( n + 1 ) ! x ^ { n ^ { 2 } + 2 n + 1 } } { n ! x ^ { n ^ { 2 } } } = \operatorname* { l i m } _ { n \to \infty } ( n + 1 ) \abs{ x } ^ { 2 n + 1 } = \operatorname* { l i m } _ { n \to \infty } ( n + 1 ) e ^ { \log \abs{ x } ( 2 n + 1 ) } = \left\{ \begin{array} { l l } { 0 , } & { \abs{ x } < 1 , } \\ { + \infty , } & { \abs{ x } \geq 1 . } \end{array} \right.
$$
:::
