---
schema: qual/card@1
id: P-PRECALC1-26
kind: problem
title: Integral of $|x+1|$ over $[-3,3]$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Calculate $\int _ { - 3 } ^ { 3 } | x + 1 | d x .$
:::

::: {.solution}
<1>1. The expression \(x+1\) changes sign at
\[
\boxed{x=-1}.
\]

::: {.proof}
Solve
\[
x+1=0.
\]
:::

<1>2. For
\[
-3\le x\le-1,
\]
one has
\[
\boxed{|x+1|=-(x+1)}.
\]

::: {.proof}
On this interval,
\[
x+1\le0.
\]
:::

<1>3. For
\[
-1\le x\le3,
\]
one has
\[
\boxed{|x+1|=x+1}.
\]

::: {.proof}
On this interval,
\[
x+1\ge0.
\]
:::

<1>4. Therefore
\[
\int_{-3}^{3}|x+1|\,dx
=
\int_{-3}^{-1}-(x+1)\,dx
+
\int_{-1}^{3}(x+1)\,dx.
\]

::: {.proof}
Split the integral at the sign-change point and use steps <1>2--<1>3.
:::

<1>5. The first integral equals
\[
\boxed{2}.
\]

::: {.proof}
\[
\begin{aligned}
\int_{-3}^{-1}-(x+1)\,dx
&=
\left[
-\frac{x^2}{2}-x
\right]_{-3}^{-1}\\
&=
\left(
-\frac12+1
\right)
-
\left(
-\frac92+3
\right)\\
&=
\frac12-\left(-\frac32\right)\\
&=
2.
\end{aligned}
\]
:::

<1>6. The second integral equals
\[
\boxed{8}.
\]

::: {.proof}
\[
\begin{aligned}
\int_{-1}^{3}(x+1)\,dx
&=
\left[
\frac{x^2}{2}+x
\right]_{-1}^{3}\\
&=
\left(
\frac92+3
\right)
-
\left(
\frac12-1
\right)\\
&=
\frac{15}{2}+\frac12\\
&=
8.
\end{aligned}
\]
:::

<1>7. Hence
\[
\boxed{
\int_{-3}^{3}|x+1|\,dx=10}.
\]

::: {.proof}
Combine steps <1>4--<1>6:
\[
2+8=10.
\]
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the requested value.
:::
:::
