---
schema: qual/card@1
id: P-HQXCX
kind: problem
title: Positive integers $n$ with $(1+i)^n=(1-i)^n$
classification:
  areas:
  - complex-analysis
  topics:
  - Trigonometry
  - Geometry
relations: []
review: draft
---

::: problem
Characterize positive integers $n$ such that $(1+i)^{n}=(1-i)^{n}$
:::

::: solution
Since $1-i\ne0$, the desired equality is equivalent to
\[
\left(\frac{1+i}{1-i}\right)^n=1.
\]
But
\[
\frac{1+i}{1-i}=i,
\]
so the condition is $i^n=1$. The powers of $i$ have period $4$, hence
\[
\boxed{4\mid n}.
\]
Thus the positive integers with the required property are exactly
$n=4,8,12,\dots$.
:::
