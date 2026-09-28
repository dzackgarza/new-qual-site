---
schema: qual/card@1
id: E-SS3.EX-7
kind: problem
title: $\int_0^{2\pi}\frac{d\theta}{(a+\cos\theta)^2}=\frac{2\pi a}{(a^2-1)^{3/2}}$
classification:
  areas:
  - complex-analysis
  topics: ['Meromorphic Functions', 'Residue Theorem', 'Argument Principle']
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}
7. Prove that

$$
\int_ {0} ^ {2 \pi} \frac {d \theta}{(a + \cos \theta) ^ {2}} = \frac {2 \pi a}{(a ^ {2} - 1) ^ {3 / 2}}, \quad \text { whenever } a > 1.
$$
:::

::: {.solution}
Put $z = e^{i\theta}$, so $\cos\theta = \frac{z+z^{-1}}{2}$ and $d\theta = \frac{dz}{iz}$, and let $z_0 = -a+\sqrt{a^2-1}$, $z_1 = -a-\sqrt{a^2-1}$ be the roots of $z^2+2az+1$.

<1>1. $\displaystyle\int_0^{2\pi} \frac{d\theta}{(a+\cos\theta)^2} = \oint_{|z|=1} \frac{4z}{i(z-z_0)^2(z-z_1)^2}\,dz$, and $z_0$ is the only pole inside $\abs z=1$.

::: {.proof}
Since $\bigl(a+\frac{z+z^{-1}}{2}\bigr)^2=\frac{(z^2+2az+1)^2}{4z^2}$, the substitution gives the integrand $\frac{4z^2}{(z^2+2az+1)^2}\cdot\frac{1}{iz}$. For $a>1$ the roots are real with $z_0z_1=1$ and $\abs{z_1}=a+\sqrt{a^2-1}>1$, so $\abs{z_0}<1<\abs{z_1}$.
:::

<1>2. The residue at the double pole $z_0$ is $\dfrac{a}{i(a^2-1)^{3/2}}$.

::: {.proof}
The residue is the derivative of $\frac{4z}{i(z-z_1)^2}$ at $z_0$:
$$\frac{4}{i}\cdot\frac{(z_0-z_1)-2z_0}{(z_0-z_1)^3} = \frac{4}{i}\cdot\frac{-(z_0+z_1)}{(z_0-z_1)^3} = \frac4i\cdot\frac{2a}{8(a^2-1)^{3/2}},$$
using $z_0+z_1=-2a$ and $z_0-z_1=2\sqrt{a^2-1}$.
:::

<1>3. Q.E.D.

::: {.proof}
By the residue theorem and steps <1>1 and <1>2, the integral is $2\pi i\cdot\frac{a}{i(a^2-1)^{3/2}}=\boxed{\dfrac{2\pi a}{(a^2-1)^{3/2}}}$.
:::
:::
