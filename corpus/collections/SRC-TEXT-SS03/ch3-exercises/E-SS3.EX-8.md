---
schema: qual/card@1
id: E-SS3.EX-8
kind: problem
title: $\int_0^{2\pi}\frac{d\theta}{a+b\cos\theta}=\frac{2\pi}{\sqrt{a^2-b^2}}$
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
8. Prove that

$$
\int_ {0} ^ {2 \pi} \frac {d \theta}{a + b \cos \theta} = \frac {2 \pi}{\sqrt {a ^ {2} - b ^ {2}}}
$$

if $a > | b |$ and $a , b \in \mathbb { R }$
:::

::: {.solution}
<1>1. If $b = 0$, the integral is $\frac{2\pi}{a}=\frac{2\pi}{\sqrt{a^2-b^2}}$.

::: {.proof}
The integrand is the constant $1/a$.
:::

<1>2. If $b\ne0$, then $\displaystyle\int_0^{2\pi} \frac{d\theta}{a + b\cos\theta} = \frac{2}{i} \oint_{|z|=1} \frac{dz}{b z^2 + 2az + b}$.

::: {.proof}
With $z = e^{i\theta}$ on the positively oriented unit circle, $d\theta = \frac{dz}{iz}$ and $\cos \theta = \frac{z + z^{-1}}{2}$, so the integrand becomes $\frac{1}{a + b(z + z^{-1})/2}\cdot\frac{1}{iz}=\frac2i\cdot\frac{1}{bz^2+2az+b}$.
:::

<1>3. For $b\ne0$, $bz^2+2az+b=b(z-z_1)(z-z_2)$ with $z_1 = \frac{-a + \sqrt{a^2 - b^2}}{b}$ inside and $z_2 = \frac{-a - \sqrt{a^2 - b^2}}{b}$ outside the unit circle, and the residue of $\frac{1}{b(z - z_1)(z - z_2)}$ at $z_1$ is $\frac{1}{2\sqrt{a^2 - b^2}}$.

::: {.proof}
The roots satisfy $z_1 z_2 = 1$, and $|z_2| = \frac{a + \sqrt{a^2 - b^2}}{|b|} > \frac{a}{|b|} > 1$, so $|z_1| < 1$. The pole at $z_1$ is simple with residue $\frac{1}{b(z_1 - z_2)} = \frac{1}{2\sqrt{a^2 - b^2}}$.
:::

<1>4. Q.E.D.

::: {.proof}
For $b\ne0$, the residue theorem and steps <1>2 and <1>3 give
$$\int_0^{2\pi} \frac{d\theta}{a + b\cos\theta} = \frac{2}{i}\cdot 2\pi i\cdot\frac{1}{2\sqrt{a^2 - b^2}} = \frac{2\pi}{\sqrt{a^2 - b^2}},$$
and step <1>1 covers $b=0$.
:::
:::
