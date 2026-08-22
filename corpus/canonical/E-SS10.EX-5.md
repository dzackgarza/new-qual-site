---
schema: qual/card@1
id: E-SS10.EX-5
kind: exercise
title: "SS 10.5: Logarithmic asymptotics of the partition generating function"
classification:
  areas:
  - complex-analysis
  topics: ['Theta Functions', 'Modular Forms', 'Partitions']
relations: []
review: draft
solved: false
---

::: exercise
5. Let

$$

F (x) = \sum_ {n = 0} ^ {\infty} p (n) x ^ {n} = \prod_ {n = 1} ^ {\infty} \frac {1}{1 - x ^ {n}}

$$

be the generating function for the partitions. Show that

$$

\log F (x) \sim \frac {\pi^ {2}}{6 (1 - x)} \quad \mathrm{as} x \to 1, \mathrm{with} 0 <   x <   1.

$$

[Hint: Use log $\textstyle F ( x ) = \sum \log ( 1 / ( 1 - x ^ { n } ) )$ and log $\textstyle ( 1 / ( 1 - x ^ { n } ) ) = \sum ( 1 / m ) x ^ { n m }$ , so

$$

\log F (x) = \sum {\frac {1}{m}} {\frac {x ^ {m}}{1 - x ^ {m}}}.

$$

Use also $m x ^ { m - 1 } ( 1 - x ) < 1 - x ^ { m } < m ( 1 - x ) . ]$
:::
