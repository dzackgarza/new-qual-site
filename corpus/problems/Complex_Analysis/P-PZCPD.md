---
schema: qual/card@1
id: P-PZCPD
kind: problem
title: Complex numbers on one side of a line through the origin have nonzero sum and
  sum of reciprocals
classification:
  areas:
  - complex-analysis
  topics:
  - Geometry
relations: []
review: draft
---

::: {.problem}
Let $z_{k}(k=1, \cdots, n)$ be complex numbers lying on the same side of a straight line passing through the origin.
Show that

$$
z_{1}+z_{2}+\cdots+z_{n} \neq 0, \quad 1 / z_{1}+1 / z_{2}+\cdots+1 / z_{n} \neq 0
$$

> Hint: Consider a special situation first.
:::

::: {.solution}
Rotate the plane so that the given line becomes the imaginary axis and all the
$z_k$ lie in the open right half-plane. Multiplication by a unimodular constant
does not affect whether either displayed sum is zero, so it is enough to treat
this case. Then
\[
\Re z_k>0
\qquad(k=1,\dots,n).
\]
Hence
\[
\Re\left(\sum_{k=1}^n z_k\right)
=\sum_{k=1}^n\Re z_k>0,
\]
and therefore $\sum z_k\ne0$.

Moreover,
\[
\Re\frac1{z_k}
=\Re\frac{\overline{z_k}}{|z_k|^2}
=\frac{\Re z_k}{|z_k|^2}>0.
\]
Thus
\[
\Re\left(\sum_{k=1}^n\frac1{z_k}\right)>0,
\]
so the sum of reciprocals is also nonzero.
:::
