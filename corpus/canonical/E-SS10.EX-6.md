---
schema: qual/card@1
id: E-SS10.EX-6
kind: exercise
title: "SS 10.6: Exponential square-root bounds for the partition function"
classification:
  areas:
  - complex-analysis
  topics: ['Theta Functions', 'Modular Forms', 'Partitions']
relations: []
review: draft
solved: false
---

::: exercise
6. Show as a consequence of Exercise 5 that

$$

e ^ {c _ {1} n ^ {1 / 2}} \leq p (n) \leq e ^ {c _ {2} n ^ {1 / 2}}

$$

for two positive constants $c _ { 1 }$ and $c _ { 2 }$ .

[Hint: $\begin{array} { r } { F ( e ^ { - y } ) = \sum p ( n ) e ^ { - n y } \le C e ^ { c / y } } \end{array}$ as $y \to 0$ . So $p ( n ) e ^ { - n y } \leq c e ^ { c / y }$ . Take $y =$ $1 / n ^ { 1 / 2 }$ to get $p ( n ) \leq c ^ { \prime } e ^ { c ^ { \prime } n ^ { 1 / 2 } }$ . In the opposite direction

$$

\sum_ {n = 0} ^ {m} p (n) e ^ {- n y} \geq C (e ^ {c / y} - \sum_ {n = m + 1} ^ {\infty} e ^ {c n ^ {1 / 2}} e ^ {- n y}),

$$

and it sufices to take $y = A m ^ { - 1 / 2 }$ where A is a large constant, and use the fact that the sequence $p ( n )$ is increasing.]
:::
