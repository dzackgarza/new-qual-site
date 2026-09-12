---
schema: qual/card@1
id: P-BKF09-3B
kind: problem
title: Berkeley Fall 2009 prelim problem 3B
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Prove that the function $\begin{array} { r } { f ( z ) = \frac { z } { ( 1 - z ) ^ { 2 } } } \end{array}$is injective on the disk$B _ { 1 } ( 0 ) = \{ z \in \mathbb { C } | | z | < 1 \}$Find the Taylor series about$z = 0 ,$, and determine its radius of convergence.
What is the maximal disk$B _ { r } ( 0 ) = \{ w \in \mathbb { C } | | w | < r \}$such that$B _ { r } ( 0 ) \subset f ( B _ { 1 } ( 0 ) ) ?$
:::

::: {.solution}
Suppose that $f ( z _ { 1 } ) = f ( z _ { 2 } )$, where$| z _ { i } | < 1$.
Then$\begin{array} { r } { \frac { z _ { 1 } } { ( 1 - z _ { 1 } ) ^ { 2 } } = \frac { z _ { 2 } } { ( 1 - z _ { 2 } ) ^ { 2 } } } \end{array}$, and crossmultiplying, we have$z _ { 1 } ( 1 - z _ { 2 } ) ^ { 2 } = z _ { 2 } ( 1 - z _ { 1 } ) ^ { 2 }$.
Thus,$z _ { 1 } - z _ { 2 } = z _ { 2 } z _ { 1 } ^ { 2 } - z _ { 1 } z _ { 2 } ^ { 2 } = z _ { 1 } z _ { 2 } ( z _ { 1 } - z _ { 2 } )$ $\operatorname { I f }  z _ { 1 } \neq z _ { 2 }$, then dividing we see that$1 = z _ { 1 } z _ { 2 }$, which is impossible since then we would have$1 = | z _ { 1 } z _ { 2 } | = | z _ { 1 } | | z _ { 2 } | < 1$, a contradiction.
So$z _ { 1 } \neq z _ { 2 }$, and$f ( z )$is thus injective on$B _ { 1 } ( 0 )$Noting that$\begin{array} { r } { f ( z ) = \frac { z - 1 + 1 } { ( 1 - z ) ^ { 2 } } = \frac { - 1 } { 1 - z } + \frac { 1 } { ( 1 - z ) ^ { 2 } } } \end{array}$, and that$\scriptstyle { \frac { 1 } { ( 1 - z ) ^ { 2 } } } = { \frac { 1 } { 1 - z } } ^ { \prime } = ( 1 + z + z ^ { 2 } + \cdots ) ^ { \prime } =$ $1 + 2 z + 3 z ^ { 2 } + \cdot \cdot \cdot$, we have$f ( z ) = - 1 - z - z ^ { 2 } - \cdot \cdot \cdot + 1 + 2 z + 3 z ^ { 2 } + \cdot \cdot \cdot = z + 2 z ^ { 2 } + 3 z ^ { 3 } + \cdot \cdot \cdot$$$f ( z )$$$$B _ { 1 } ( 0 )$$Note that for$| z | = \rho < 1$, we have$\begin{array} { r } { | f ( z ) | = \left| \frac { z } { ( 1 - z ) ^ { 2 } } \right| \ge \rho / ( 1 + \rho ) ^ { 2 } } \end{array}$, since$| 1 - z | \leq 1 + | z | \leq$ $1 + \rho .$, and this is an equality if$z = - \rho .$.
Thus, the disk$B _ { \rho / ( 1 + \rho ) ^ { 2 } } ( 0 )$lies outside of the curve$f ( \rho e ^ { i \theta } ) , 0 \leq \theta < 2 \pi$.
Let$| a | < 1 / 4$, and choose$0 < \rho < 1$such that$| a | < \rho / ( 1 + \rho ) ^ { 2 }$, which we may do since$\operatorname* { l i m } _ { \rho \to 1 } \rho / ( 1 + \rho ) ^ { 2 } = 1 / 4$.
The integral$\begin{array} { r } { { \frac { 1 } { 2 \pi i } } \int _ { | z | = \rho } { \frac { f ^ { \prime } ( z ) } { f ( z ) - a } } d z } \end{array}$gives the multiplicity$| \{ z | \ f ( z ) \ = \ a , | z | \ < \ \rho \} |$by the argument principle.
Since f is injective,$f ( 0 ) = 0$, and$B _ { \rho / ( 1 + \rho ) ^ { 2 } }$lies in the complement of the contour$f ( \rho e ^ { i \theta } )$, we see that there exists$| z | < \rho ,$ $f ( z ) = a$
:::
