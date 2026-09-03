---
schema: qual/card@1
id: E-SS1.EX-14
kind: problem
title: "Summation by parts (Abel's formula)"
classification:
  areas:
  - complex-analysis
  topics: ['Complex Numbers', 'Power Series', 'Cauchy-Riemann']
relations: []
review: draft
---

::: exercise
14. Suppose $\{ a _ { n } \} _ { n = 1 } ^ { N }$ and $\{ b _ { n } \} _ { n = 1 } ^ { N }$ are two finite sequences of complex numbers.
    Let $\begin{array} { r } { B _ { k } = \sum _ { n = 1 } ^ { k } b _ { n } } \end{array}$ denote the partial sums of the series $\sum b _ { n }$ with the convention $B _ { 0 } = 0$ . Prove the summation by parts formula

$$
\sum_ {n = M} ^ {N} a _ {n} b _ {n} = a _ {N} B _ {N} - a _ {M} B _ {M - 1} - \sum_ {n = M} ^ {N - 1} (a _ {n + 1} - a _ {n}) B _ {n}.
$$
:::
