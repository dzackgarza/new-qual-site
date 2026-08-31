---
schema: qual/card@1
id: E-SS3.EX-7
kind: exercise
title: "SS 3.7: The integral of dtheta over (a+cos theta)^2"
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

::: exercise
7. Prove that

$$
\int_ {0} ^ {2 \pi} \frac {d \theta}{(a + \cos \theta) ^ {2}} = \frac {2 \pi a}{(a ^ {2} - 1) ^ {3 / 2}}, \quad \text { whenever } a > 1.
$$

::: {.solution}
<1>1. Put $z = e^{i\theta}$, so $\cos\theta = \frac{z+z^{-1}}{2}$ and $d\theta = \frac{dz}{iz}$.
::: {.proof}
standard substitution.
:::

<1>2. Then $$\int_0^{2\pi} \frac{d\theta}{(a+\cos\theta)^2} = \oint_{|z|=1} \frac{1}{\left(a+\frac{z+z^{-1}}{2}\right)^2}\frac{dz}{iz} = \oint_{|z|=1} \frac{4z}{i(z^2+2az+1)^2}\,dz.$$ Proof: <1>1.

<1>3. The poles are at $z = -a \pm \sqrt{a^2-1}$; for $a>1$ exactly one, $z_0 = -a+\sqrt{a^2-1}$, lies inside $|z|=1$ (with $|z_0|<1$).
::: {.proof}
product of roots $=1$, and $|z_0|<1<|z_1|$.
:::

<1>4. The integrand has a double pole at $z_0$; the residue is $$\operatorname{Res}_{z_0}\frac{4z}{i(z-z_0)^2(z-z_1)^2} = \frac{4}{i}\cdot\frac{-(z_0+z_1)}{(z_0-z_1)^3} = \frac{a}{i(a^2-1)^{3/2}}.$$ Proof: residue of double pole (derivative of $\frac{4z}{i(z-z_1)^2}$ at $z_0$).

<1>5. By the residue theorem the integral equals $2\pi i$ times the residue, i.e. $\frac{2\pi a}{(a^2-1)^{3/2}}$.
::: {.proof}
<1>4.
:::

<1>6. Q.E.D.
::: {.proof}
<1>5.
:::
:::
:::
