---
schema: qual/card@1
id: P-PRECALC2-22
kind: problem
title: Integral of $\frac{\log(1+t)}{1+t^2}$ over $[0,1]$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Symmetry
relations: []
review: draft
---

::: {.problem}
Compute the integral $\displaystyle \int_{0}^{1} \frac{\log(1 + t)}{1 + t^{2}}\, dt$.
:::

::: {.solution}

Let
$$
I
=
\int_0^1
\frac{\log(1+t)}{1+t^2}\,dt.
$$

::: pf

::: {.pf-step #s1-1}

Set
$$
\boxed{t=\tan\theta}.
$$


::: pf-proof

This substitution removes the denominator $1+t^2$.

:::

:::

::: {.pf-step #s1-2}

Then
$$
dt=\sec^2\theta\,d\theta,
\qquad
1+t^2=\sec^2\theta.
$$


::: pf-proof

Differentiate $t=\tan\theta$ and use the identity
$$
1+\tan^2\theta=\sec^2\theta.
$$

:::

:::

::: {.pf-step #s1-3}

The bounds $t=0,1$ become
$$
\theta=0,\frac{\pi}{4}.
$$


::: pf-proof

$$
\arctan0=0,
\qquad
\arctan1=\frac{\pi}{4}.
$$

:::

:::

::: pf-step

Therefore
$$
\boxed{
I
=
\int_0^{\pi/4}
\log(1+\tan\theta)\,d\theta}.
$$


::: pf-proof

Substitute steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} into the integral.

:::

:::

::: {.pf-step #s1-5}

One has
$$
1+\tan\theta
=
\frac{\sin\theta+\cos\theta}{\cos\theta}.
$$


::: pf-proof

Use
$$
\tan\theta=\frac{\sin\theta}{\cos\theta}.
$$

:::

:::

::: {.pf-step #s1-6}

The numerator satisfies
$$
\boxed{
\sin\theta+\cos\theta
=
\sqrt2\cos\left(\theta-\frac{\pi}{4}\right)}.
$$


::: pf-proof

Using
$$
\cos(\theta-\pi/4)
=
\frac{\cos\theta+\sin\theta}{\sqrt2},
$$
multiply by $\sqrt2$.

:::

:::

::: {.pf-step #s1-7}

Hence
$$
\boxed{
\log(1+\tan\theta)
=
\frac12\log2
+
\log\cos\left(\theta-\frac{\pi}{4}\right)
-
\log\cos\theta}.
$$


::: pf-proof

Combine steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref} and take logarithms. On
$$
0\le\theta\le\frac{\pi}{4},
$$
all cosine factors are positive.

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
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
$$


::: pf-proof

Integrate the identity from step [](#s1-7){.pf-ref}. The constant term contributes
$$
\frac12\log2\cdot\frac{\pi}{4}
=
\frac{\pi}{8}\log2.
$$

:::

:::

::: {.pf-step #s1-9}

The two logarithmic cosine integrals are equal:
$$
\boxed{
\int_0^{\pi/4}
\log\cos\left(\theta-\frac{\pi}{4}\right)\,d\theta
=
\int_0^{\pi/4}
\log\cos\theta\,d\theta}.
$$


::: pf-proof

Set
$$
u=\frac{\pi}{4}-\theta.
$$
Then
$$
\cos\left(\theta-\frac{\pi}{4}\right)
=
\cos(-u)
=
\cos u.
$$
Reversing the bounds yields exactly the right-hand integral.

:::

:::

::: {.pf-step #s1-10}

Hence the logarithmic integrals cancel, and
$$
\boxed{
I
=
\frac{\pi}{8}\log2}.
$$


::: pf-proof

Apply step [](#s1-9){.pf-ref} to step [](#s1-8){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is the requested value.

:::

:::

:::
