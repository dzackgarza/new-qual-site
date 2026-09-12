---
schema: qual/card@1
id: P-BKF09-7B
kind: problem
title: Berkeley Fall 2009 prelim problem 7B
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Suppose α is a complex number, $| \alpha | \neq 1$.
Compute$$\int _ { 0 } ^ { 2 \pi } { \frac { d \theta } { 1 - 2 \alpha \cos \theta + \alpha ^ { 2 } } }$$by integrating$( z - \alpha ) ^ { - 1 } ( z - \alpha ^ { - 1 } ) ^ { - 1 }$ over the unit circle.
:::

::: {.solution}
Parameterize the unit circle C by $z ( \theta ) = e ^ { i \theta } , \theta \in [ 0 , 2 \pi ]$.
Then$z ^ { \prime } ( \theta ) = i e ^ { i \theta } =$ $i z ( \theta )$, and we have cos$\theta = { \textstyle { \frac { 1 } { 2 } } } ( e ^ { i \theta } + e ^ { - i \theta } ) = { \textstyle { \frac { 1 } { 2 } } } ( z + \dot { z ^ { - 1 } } )$.
We also have$d \theta = - i d z / z$, so we have$$\begin{array} { l } { \displaystyle \int _ { 0 } ^ { 2 \pi } \displaystyle \frac { d \theta } { 1 - 2 \alpha \cos \theta + \alpha ^ { 2 } } = \int _ { C } \displaystyle \frac { - i d z / z } { 1 - \alpha ( z + z ^ { - 1 } ) + \alpha ^ { 2 } } = \int _ { C } \displaystyle \frac { i d z \alpha ^ { - 1 } } { z ^ { 2 } - ( \alpha + \alpha ^ { - 1 } ) z + 1 } } \\ { = \displaystyle \frac { i } { \alpha } \int _ { C } \displaystyle \frac { d z } { ( z - \alpha ) ( z - \alpha ^ { - 1 } ) } . } \end{array}$$If$\alpha = 0$, then$$\int _ { 0 } ^ { 2 \pi } { \frac { d \theta } { 1 - 2 \alpha \cos \theta + \alpha ^ { 2 } } } = \int _ { 0 } ^ { 2 \pi } d \theta = 2 \pi = { \frac { 2 \pi } { 1 - \alpha ^ { 2 } } } .$$If$0 < | \alpha | < 1$, then$\frac { 1 } { z - \alpha ^ { - 1 } }$is analytic inside C since$| \alpha ^ { - 1 } | > 1$, so by Cauchy’s integral formula, we have$$i \alpha ^ { - 1 } \int _ { C } \frac { ( z - \alpha ^ { - 1 } ) ^ { - 1 } d z } { z - \alpha } = i \alpha ^ { - 1 } \frac { 2 \pi i } { \alpha - \alpha ^ { - 1 } } = \frac { 2 \pi } { 1 - \alpha ^ { 2 } } .$$If$| \alpha | > 1$, then exchanging the roles of α and$\alpha ^ { - 1 }$, we have$$i \alpha ^ { - 1 } \int _ { { \cal C } } \frac { ( z - \alpha ) ^ { - 1 } d z } { z - \alpha ^ { - 1 } } = i \alpha ^ { - 1 } \frac { 2 \pi i } { \alpha ^ { - 1 } - \alpha } = \frac { 2 \pi } { \alpha ^ { 2 } - 1 } .$$So we have for$| \alpha | \neq 1$$$\int _ { 0 } ^ { 2 \pi } { \frac { d \theta } { 1 - 2 \alpha \cos \theta + \alpha ^ { 2 } } } = { \frac { 2 \pi } { \alpha ^ { 2 } - 1 } } \cdot { \frac { | \alpha | - 1 } { | | \alpha | - 1 | } } .$$
:::
