---
schema: qual/card@1
id: P-EQGG7
kind: problem
title: $z\tan z-a$ has only real roots for $a>0$
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
  - Trigonometry
relations: []
review: draft
---

::: {.problem}
Prove that for $a> 0$, $z\tan z - a$ has only real roots.
:::

::: solution
Let
\[
z=x+iy
\]
be a zero of $z\tan z-a$, so
\[
z\tan z=a>0.
\]
Using
\[
\tan(x+iy)
=\frac{\sin 2x+i\sinh 2y}
       {\cos 2x+\cosh 2y},
\]
we obtain
\[
z\tan z
=\frac{x\sin 2x-y\sinh 2y
+i\bigl(x\sinh 2y+y\sin 2x\bigr)}
{\cos 2x+\cosh 2y}.
\]

Suppose $y\ne0$. Then
\[
\cos 2x+\cosh 2y>0,
\]
and since $z\tan z$ is real, its imaginary part vanishes:
\[
x\sinh 2y+y\sin 2x=0.
\]
Thus
\[
\sin 2x=-\frac{x}{y}\sinh 2y.
\]
Substituting this into the real part gives
\[
\operatorname{Re}(z\tan z)
=-\frac{(x^2+y^2)\sinh 2y}
{y(\cos 2x+\cosh 2y)}.
\]
For $y\ne0$,
\[
\frac{\sinh 2y}{y}>0,
\]
so the right-hand side is strictly negative. This contradicts
\[
z\tan z=a>0.
\]

Therefore $y=0$, and every zero is real.
:::
