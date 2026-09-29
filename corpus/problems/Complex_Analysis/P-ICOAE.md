---
schema: qual/card@1
id: P-ICOAE
kind: problem
title: $\int_0^{2\pi}\frac{d\theta}{(a+b\cos\theta)^2}$ for $a>b>0$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Trigonometry
  - Poles
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Suppose $a>b>0$ and calculate
\[
\int_0^{2\pi} {1 \over (a+b\cos(\theta))^2} \,d\theta
.\]

:::

::: {.solution}
::: pf

::: {.pf-step #substitution}
Substitute $z = e^{i\theta}$, so $d\theta = \frac{dz}{iz}$ and $\cos\theta = \frac{z + z^{-1}}{2}$.

::: pf-proof
standard substitution.
:::

:::

::: {.pf-step #denominator-expression}
Then $a + b\cos\theta = a + \frac{b}{2}(z + z^{-1}) = \frac{2az + bz^2 + b}{2z}$.

::: pf-proof
Step [](#substitution){.pf-ref}.
:::

:::

::: pf-step
Hence
$$\int_0^{2\pi} \frac{d\theta}{(a + b\cos\theta)^2} = \oint_{|z|=1} \frac{1}{\left(\frac{2az + bz^2 + b}{2z}\right)^2} \frac{dz}{iz} = \oint_{|z|=1} \frac{4z}{i(2az + bz^2 + b)^2}\,dz.$$

::: pf-proof
Steps [](#substitution){.pf-ref} and [](#denominator-expression){.pf-ref}.
:::

:::

::: pf-step
The integrand has poles where $bz^2 + 2az + b = 0$, i.e. $z = \frac{-a \pm \sqrt{a^2 - b^2}}{b}$.

::: pf-proof
solve the quadratic.
:::

:::

::: pf-step
Since $a > b > 0$, one root $z_1 = \frac{-a + \sqrt{a^2 - b^2}}{b}$ has $|z_1| < 1$ and the other $z_2 = \frac{-a - \sqrt{a^2 - b^2}}{b}$ has $|z_2| > 1$.

::: pf-proof
$z_1 z_2 = 1$ (product of roots is $b/b = 1$), and $z_1$ is the one inside the unit circle.
:::

:::

::: {.pf-step #residue-value}
The integrand has a double pole at $z_1$ (inside the unit circle), and the residue there is $\frac{a}{i(a^2 - b^2)^{3/2}}$.

::: pf-proof
computing the residue of $\frac{4z}{i b^2 (z - z_1)^2 (z - z_2)^2}$ at $z = z_1$ (a double pole).
:::

:::

::: {.pf-step #integral-value}
By the residue theorem, the integral is $2\pi i \cdot \frac{a}{i(a^2 - b^2)^{3/2}} = \frac{2\pi a}{(a^2 - b^2)^{3/2}}$.

::: pf-proof
Step [](#residue-value){.pf-ref}.
:::

:::

::: {.pf-step #final-result}
Hence $\int_0^{2\pi} \frac{d\theta}{(a + b\cos\theta)^2} = \frac{2\pi a}{(a^2 - b^2)^{3/2}}$.

::: pf-proof
Step [](#integral-value){.pf-ref}.
:::

:::

::: pf-qed
Step [](#final-result){.pf-ref}.
:::

:::



