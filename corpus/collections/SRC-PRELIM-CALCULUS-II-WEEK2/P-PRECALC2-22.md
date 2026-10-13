---
schema: qual/card@1
id: P-PRECALC2-22
kind: problem
title: Integral of $\frac{\log(1+t)}{1+t^2}$ over $[0,1]$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Compute the integral $\int _ { 0 } ^ { 1 } \frac { \log ( 1 + t ) } { 1 + t ^ { 2 } } d t .$
:::

::: {.solution}
Let
\[
I
=
\int_0^1
\frac{\log(1+t)}{1+t^2}\,dt.
\]

<1>1. Set
\[
\boxed{t=\tan\theta}.
\]

::: {.proof}
This substitution removes the denominator \(1+t^2\).
:::

<1>2. Then
\[
dt=\sec^2\theta\,d\theta,
\qquad
1+t^2=\sec^2\theta.
\]

::: {.proof}
Differentiate \(t=\tan\theta\) and use the identity
\[
1+\tan^2\theta=\sec^2\theta.
\]
:::

<1>3. The bounds \(t=0,1\) become
\[
\theta=0,\frac{\pi}{4}.
\]

::: {.proof}
\[
\arctan0=0,
\qquad
\arctan1=\frac{\pi}{4}.
\]
:::

<1>4. Therefore
\[
\boxed{
I
=
\int_0^{\pi/4}
\log(1+\tan\theta)\,d\theta}.
\]

::: {.proof}
Substitute steps <1>1--<1>3 into the integral.
:::

<1>5. One has
\[
1+\tan\theta
=
\frac{\sin\theta+\cos\theta}{\cos\theta}.
\]

::: {.proof}
Use
\[
\tan\theta=\frac{\sin\theta}{\cos\theta}.
\]
:::

<1>6. The numerator satisfies
\[
\boxed{
\sin\theta+\cos\theta
=
\sqrt2\cos\left(\theta-\frac{\pi}{4}\right)}.
\]

::: {.proof}
Using
\[
\cos(\theta-\pi/4)
=
\frac{\cos\theta+\sin\theta}{\sqrt2},
\]
multiply by \(\sqrt2\).
:::

<1>7. Hence
\[
\boxed{
\log(1+\tan\theta)
=
\frac12\log2
+
\log\cos\left(\theta-\frac{\pi}{4}\right)
-
\log\cos\theta}.
\]

::: {.proof}
Combine steps <1>5--<1>6 and take logarithms. On
\[
0\le\theta\le\frac{\pi}{4},
\]
all cosine factors are positive.
:::

<1>8. Therefore
\[
\begin{aligned}
I
={}&
\frac{\pi}{8}\log2\\
&+
\int_0^{\pi/4}
\log\cos\left(\theta-\frac{\pi}{4}\right)\,d\theta
-
\int_0^{\pi/4}
\log\cos\theta\,d\theta.
\end{aligned}
\]

::: {.proof}
Integrate the identity from step <1>7. The constant term contributes
\[
\frac12\log2\cdot\frac{\pi}{4}
=
\frac{\pi}{8}\log2.
\]
:::

<1>9. The two logarithmic cosine integrals are equal:
\[
\boxed{
\int_0^{\pi/4}
\log\cos\left(\theta-\frac{\pi}{4}\right)\,d\theta
=
\int_0^{\pi/4}
\log\cos\theta\,d\theta}.
\]

::: {.proof}
Set
\[
u=\frac{\pi}{4}-\theta.
\]
Then
\[
\cos\left(\theta-\frac{\pi}{4}\right)
=
\cos(-u)
=
\cos u.
\]
Reversing the bounds yields exactly the right-hand integral.
:::

<1>10. Hence the logarithmic integrals cancel, and
\[
\boxed{
I
=
\frac{\pi}{8}\log2}.
\]

::: {.proof}
Apply step <1>9 to step <1>8.
:::

<1>11. Q.E.D.

::: {.proof}
Step <1>10 is the requested value.
:::
:::
