---
schema: qual/card@1
id: P-BERK87S-20
kind: problem
title: Evaluate $\int_0^\pi \cos(4\theta)/(1+\cos^2\theta)\,d\theta$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Substituted x=2 theta, divided cos(2x) by 3+cos(x), and evaluated the
    remaining reciprocal-cosine integral by symmetry and the tangent
    half-angle substitution.
---

::: {.problem}
Evaluate
\[
\int_0^\pi\frac{\cos4\theta}{1+\cos^2\theta}\,d\theta.
\]
:::

::: {.solution}
Let
$$
I\coloneqq
\int_0^\pi\frac{\cos4\theta}{1+\cos^2\theta}\,d\theta.
$$

<1>1. After the substitution $x=2\theta$,
$$
I
=
\int_0^{2\pi}\frac{\cos 2x}{3+\cos x}\,dx.
$$

::: {.proof}
Since
$$
1+\cos^2\theta
=
1+\frac{1+\cos2\theta}{2}
=
\frac{3+\cos2\theta}{2},
$$
we have
$$
I
=
2\int_0^\pi\frac{\cos4\theta}{3+\cos2\theta}\,d\theta.
$$
Setting $x=2\theta$ gives $dx=2\,d\theta$ and yields the stated
integral.
:::

<1>2. For every real $x$,
$$
\frac{\cos2x}{3+\cos x}
=
2\cos x-6+\frac{17}{3+\cos x}.
$$

::: {.proof}
Writing $c=\cos x$ and using $\cos2x=2c^2-1$,
$$
2c^2-1
=(c+3)(2c-6)+17.
$$
Since $3+\cos x\geq2>0$, division by $3+\cos x$ is valid.
:::

<1>3. One has
$$
\int_0^{2\pi}\frac{dx}{3+\cos x}
=
\frac{\pi}{\sqrt2}.
$$

::: {.proof}
The integrand is invariant under $x\mapsto2\pi-x$, so
$$
\int_0^{2\pi}\frac{dx}{3+\cos x}
=
2\int_0^\pi\frac{dx}{3+\cos x}.
$$
On $0\leq x<\pi$, set $t=\tan(x/2)$. Then
$$
\cos x=\frac{1-t^2}{1+t^2},
\qquad
dx=\frac{2\,dt}{1+t^2},
$$
and $t$ runs from $0$ to $+\infty$. Therefore
$$
\begin{aligned}
\int_0^\pi\frac{dx}{3+\cos x}
&=
\int_0^\infty
\frac{dt}{t^2+2}\\
&=
\frac1{\sqrt2}
\left[
\arctan\left(\frac{t}{\sqrt2}\right)
\right]_{0}^{\infty}
=
\frac{\pi}{2\sqrt2}.
\end{aligned}
$$
Doubling gives the claim.
:::

<1>4. The value of the integral is
$$
\boxed{
I
=
\pi\left(\frac{17}{\sqrt2}-12\right)
}.
$$

::: {.proof}
By steps <1>1 and <1>2,
$$
I
=
2\int_0^{2\pi}\cos x\,dx
-6\int_0^{2\pi}dx
+17\int_0^{2\pi}\frac{dx}{3+\cos x}.
$$
The first integral is zero, the second term is $-12\pi$, and step <1>3
evaluates the last integral. Hence
$$
I
=
-12\pi+\frac{17\pi}{\sqrt2}
=
\pi\left(\frac{17}{\sqrt2}-12\right).
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the requested value.
:::
:::
