---
schema: qual/card@1
id: P-PRECALC2-08
kind: problem
title: Integral of $\frac{1}{1+\tan^{2020}x}$ over $[0,\pi/2]$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Compute $\int _ { 0 } ^ { \pi / 2 } \frac { d x } { 1 + \tan ( x ) ^ { 2 0 2 0 } } .$
:::

::: {.solution}
Let
\[
I
=
\int_0^{\pi/2}
\frac{dx}{1+\tan^{2020}x}.
\]

<1>1. Make the substitution
\[
\boxed{
u=\frac{\pi}{2}-x}.
\]

::: {.proof}
This substitution reflects the interval about its midpoint and exchanges
\(\tan\) with \(\cot\).
:::

<1>2. Then
\[
dx=-du,
\]
and the bounds \(x=0,\pi/2\) become \(u=\pi/2,0\).

::: {.proof}
Differentiate
\[
u=\frac{\pi}{2}-x.
\]
:::

<1>3. Therefore
\[
I
=
\int_0^{\pi/2}
\frac{du}{1+\cot^{2020}u}.
\]

::: {.proof}
Substitute step <1>2 and reverse the limits:
\[
\begin{aligned}
I
&=
\int_{\pi/2}^{0}
\frac{-du}
{1+\tan^{2020}(\pi/2-u)}\\
&=
\int_0^{\pi/2}
\frac{du}{1+\cot^{2020}u}.
\end{aligned}
\]
:::

<1>4. For \(0<u<\pi/2\),
\[
\boxed{
\frac1{1+\cot^{2020}u}
=
\frac{\tan^{2020}u}
{1+\tan^{2020}u}}.
\]

::: {.proof}
Since
\[
\cot u=\frac1{\tan u},
\]
one has
\[
\begin{aligned}
\frac1{1+\cot^{2020}u}
&=
\frac1{1+\tan^{-2020}u}\\
&=
\frac{\tan^{2020}u}
{1+\tan^{2020}u}.
\end{aligned}
\]
:::

<1>5. Adding the original and transformed integrands gives
\[
\boxed{
\frac1{1+\tan^{2020}u}
+
\frac1{1+\cot^{2020}u}
=
1}.
\]

::: {.proof}
Use step <1>4:
\[
\frac1{1+t}
+
\frac{t}{1+t}
=
1,
\]
with
\[
t=\tan^{2020}u.
\]
:::

<1>6. Hence
\[
2I
=
\int_0^{\pi/2}1\,du.
\]

::: {.proof}
Add the original representation of \(I\) to the representation in step
<1>3 and use step <1>5.
:::

<1>7. Therefore
\[
2I
=
\frac{\pi}{2}.
\]

::: {.proof}
\[
\int_0^{\pi/2}1\,du
=
\frac{\pi}{2}.
\]
:::

<1>8. Thus
\[
\boxed{
I=\frac{\pi}{4}}.
\]

::: {.proof}
Divide step <1>7 by \(2\).
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 is the requested value.
:::
:::
