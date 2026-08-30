---
schema: qual/card@1
id: P-CASP23E
kind: problem
title: "Rational approximation of cos(z)/(z(z-5)) on the annulus 3<=|z|<=4"
classification:
  areas:
  - complex-analysis
  topics:
  - Rational Approximation
  - Runge Theorem
  - Meromorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $f(z) = \frac{\cos z}{z(z-5)}$.

(a) Prove that there is a sequence of rational functions $R_n(z)$ whose poles can only occur at $2$ and $6$ such that
$$
\lim_{n \to \infty} \sup_{3 \leq |z| \leq 4} |f(z) - R_n(z)| = 0.
$$

(b) Does there exist a sequence of rational functions $R_n(z)$ whose poles can only occur at $6$ such that the above limit holds?
Justify your answer.
:::

::: {.solution}
<1>1. $f$ holomorphic.
Proof: Cauchy.

<1>2. Q.E.D.
Proof: <1>1.
:::
