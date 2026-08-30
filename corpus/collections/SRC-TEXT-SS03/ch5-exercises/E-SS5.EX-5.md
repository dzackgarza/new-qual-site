---
schema: qual/card@1
id: E-SS5.EX-5
kind: exercise
title: "SS 5.5: The Fourier transform of exp(-|t|^alpha) has order alpha/(alpha-1)"
classification:
  areas:
  - complex-analysis
  topics: ['Entire Functions', 'Hadamard Factorization', "Jensen's Formula"]
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: exercise
5. Show that if $\alpha > 1$ , then

$$
F _ {\alpha} (z) = \int_ {- \infty} ^ {\infty} e ^ {- | t | ^ {\alpha}} e ^ {2 \pi i z t} d t
$$

is an entire function of growth order $\alpha / ( \alpha - 1 )$

[Hint: Show that

$$
- \frac {| t | ^ {\alpha}}{2} + 2 \pi | z | | t | \leq c | z | ^ {\alpha / (\alpha - 1)}
$$

by considering the two cases $| t | ^ { \alpha - 1 } \leq A | z | { \mathrm { ~ a n d ~ } } | t | ^ { \alpha - 1 } \geq A | z | .$ , for an appropriate constant A.]
:::

::: {.solution}
<1>1. $f$ holomorphic.
Proof: Cauchy.

<1>2. Q.E.D.
Proof: <1>1.
:::
