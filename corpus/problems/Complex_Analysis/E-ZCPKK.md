---
schema: qual/card@1
id: E-ZCPKK
kind: problem
title: Purely imaginary if on circle
classification:
  areas:
  - complex-analysis
  topics:
  - Geometry
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.exercise}
For $z\in\CC\smts{-1}$, show that
\[
\frac{z-1}{z+1}\in i\RR
\iff
\abs z=1.
\]

> Hint: $z$ is real iff $\bar{z} = z$ and purely imaginary iff $\bar{z} = -z$.
:::

::: {.solution}
Write $w=(z-1)/(z+1)$.
Then
\[
w\in i\RR
&\iff w=-\overline w \\
&\iff \frac{z-1}{z+1}=\frac{1-\bar z}{1+\bar z} \\
&\iff (z-1)(1+\bar z)=(1-\bar z)(1+z) \\
&\iff 2\abs z^2-2=0 \\
&\iff \abs z=1.
\]
:::
