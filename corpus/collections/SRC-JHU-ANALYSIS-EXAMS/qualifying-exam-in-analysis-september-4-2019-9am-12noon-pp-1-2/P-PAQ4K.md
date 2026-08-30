---
schema: qual/card@1
id: P-PAQ4K
kind: problem
title: Convergence of positive continuous functions and Fatou-type inequality
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
  - convergence
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

Assume that $f_1, f_2, \ldots$ is a sequence of positive continuous functions defined on $[0,1]$ with

$$f(x) = \lim_{n \to \infty} f_n(x) \text{ for every } x \in [0,1]$$

and

$$\int_0^1 f_n(x) \, dx = 1.$$

(a) Is it always true that $\int_0^1 f(x) \, dx \leq 1$?
Provide a proof if it is true or provide a counterexample if it is false.

(b) Is it always true that $\int_0^1 f(x) \, dx \geq 1$?
Provide a proof if it is true or provide a counterexample if it is false.

::: {.solution}
<1>1. $f$ holomorphic.
Proof: Cauchy.

<1>2. Q.E.D.
Proof: <1>1.
:::
