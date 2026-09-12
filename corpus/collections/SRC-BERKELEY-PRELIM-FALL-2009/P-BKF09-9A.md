---
schema: qual/card@1
id: P-BKF09-9A
kind: problem
title: Berkeley Fall 2009 prelim problem 9A
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Show that

$$\operatorname* { l i m } _ { n  \infty } ( 1 + { \frac { z } { n } } ) ^ { n } = e ^ { z }$$

uniformly on compact subsets of C.
:::

::: {.solution}
Since $\log ( 1 + u )$is holomorphic for$| u | < 1$and has Taylor expansion at 0 is$\begin{array} { r } { \sum _ { k \geq 1 } ( - 1 ) ^ { k + 1 } u ^ { k } / k } \end{array}$, we infer for$| u | \leq 1 / 2$that$$| \log ( 1 + u ) - u | \leq C | u | ^ { 2 }$$for some constant C. If$n > 2 N$and$| z | \leq N$this gives$\begin{array} { r } { \left| \log \left( 1 + \frac { z } { n } \right) - \frac { z } { n } \right| \leq C N ^ { 2 } n ^ { - 2 } } \end{array}$and$\begin{array} { r } { \left| \log \left( 1 + \frac { z } { n } \right) ^ { n } - z \right| \leq C N ^ { 2 } n ^ { - 1 } } \end{array}$. On the other hand, since$\textstyle | \sum _ { k > 0 } a ^ { k } / k ! | \leq \sum _ { k > 0 } | a | ^ { k } / k !$, we have$| e ^ { a } - 1 | \leq e ^ { | a | } - 1$. Hence if$n > 2 N$and$| z | \leq N$we find$$\left| \left( 1 + \frac { z } { n } \right) ^ { n } - e ^ { z } \right| = | e ^ { z } | \cdot \left| e ^ { \log \left( 1 + \frac { z } { n } \right) ^ { n } - z } - 1 \right| \leq e ^ { N } \cdot \left( e ^ { C N ^ { 2 } n ^ { - 1 } } - 1 \right)$$so that$\begin{array} { r } { \operatorname* { l i m } _ { n \to \infty } \left| \left( 1 + \frac { z } { n } \right) ^ { n } - e ^ { z } \right| = 0 } \end{array}$uniformly for$| z | \leq N$
:::
