---
schema: qual/card@1
id: P-BKS06-7B
kind: problem
title: UC Berkeley Spring 2006 prelim 7B
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let m be a fixed positive integer.

(a) Show that if an entire function $f \colon \mathbb { C } \to \mathbb { C }$ satisfies $| f ( z ) | \leq e ^ { | z | }$ for all $z \in \mathbb { C }$ , then

$$
\vert f ^ { ( m ) } ( 0 ) \vert \leq \frac { m ! e ^ { m } } { m ^ { m } } .
$$

(b) Prove that there exists an entire function $f$ such that $| f ( z ) | \leq e ^ { | z | }$ for all z and

$$
\vert f ^ { ( m ) } ( 0 ) \vert = \frac { m ! e ^ { m } } { m ^ { m } } .
$$
:::

::: {.solution}
(a) Write $\begin{array} { r } { f ( z ) = \sum _ { n > 0 } a _ { n } z ^ { n } } \end{array}$ with $a _ { n } \in \mathbb { C }$ . Then $a _ { m }$ is the coefficient of $z ^ { - 1 }$ in the Laurent series of $f ( z ) / z ^ { m + 1 }$ , so

$$
a _ { m } = \frac { 1 } { 2 \pi i } \int _ { | z | = R } \frac { f ( z ) } { z ^ { m } } \frac { d z } { z } ,
$$

for any $R > 0$ , and we get

$$
| a _ { m } | \leq \frac { 1 } { 2 \pi } \left( \frac { e ^ { R } } { R ^ { m } } \right) \frac { 2 \pi R } { R } = \frac { e ^ { R } } { R ^ { m } } .
$$

Taking $R = m$ (which calculus shows minimizes the right hand side) and multiplying by m! gives

$$
| f ^ { ( m ) } ( 0 ) | = | m ! a _ { m } | \leq \frac { m ! e ^ { m } } { m ^ { m } } .
$$

(b) Examining the proof of part (a) shows also that in order to have equality, $\frac { f ( z ) } { z ^ { m } }$ must have constant modulus $e ^ { m } / m ^ { m }$ and constant argument on the circle $| z | = m$ . Thus we guess $\begin{array} { r } { f ( z ) = \frac { e ^ { m } } { m ^ { m } } z ^ { m } } \end{array}$ , and it remains to prove that $| f ( z ) | \leq e ^ { | z | }$ for all $z \in \mathbb { C }$ . Equivalently, we must show that the minimum value of $e ^ { x } / x ^ { m }$ on $( 0 , \infty )$ is $e ^ { m } / m ^ { m }$ . This can be seen by observing that the only zero of the derivative of log $\ u _ { \ u { \ u { \ u { \ u { \ u { \ u { \chi } } } } } } } ( e ^ { x } / x ^ { m } ) = x - m$ log x is at $x = m$ , while the second derivative is positive everywhere (it is $m / x ^ { 2 } )$
:::
