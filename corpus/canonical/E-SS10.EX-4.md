---
schema: qual/card@1
id: E-SS10.EX-4
kind: exercise
title: "SS 10.4: Euler's recurrence for the partition function"
classification:
  areas:
  - complex-analysis
  topics: ['Theta Functions', 'Modular Forms', 'Partitions']
relations: []
review: draft
---

::: exercise
4. Using the generating formula for $p ( n )$ , prove the recurrence formula

$$

\begin{array}{r c l} p (n) & = & p (n - 1) + p (n - 2) - p (n - 5) - p (n - 7) - \dots \\ & = & \sum_ {k \neq 0} (- 1) ^ {k + 1} p \left(n - \frac {k (3 k + 1)}{2}\right), \end{array}
$$

where the right-hand side is the finite sum taken over those $k \in \mathbb { Z } , k \neq 0$ , with $k ( 3 k + 1 ) / 2 \leq n$ . Use this formula to calculate $p ( 5 ) , p ( 6 ) , p ( 7 ) , p ( 8 ) , p ( 9 )$ , and $p ( 1 0 )$ ; check that $p ( 1 0 ) = 4 2$

The next two exercises give elementary results related to the asymptotics of the partition function.
More refined statements can be found in Appendix A.
:::
