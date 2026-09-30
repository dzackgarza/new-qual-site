---
schema: qual/card@1
id: E-QF7KI
kind: problem
title: Residues at infinity
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Singularities
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}
Use residues at infinity to evaluate
\[
\int_{|z|=1} \frac{1}{(z-2)(1+2 z)^{4}(1-3 z)^{7}} \dz
.\]

:::

::: {.solution}
**Goal.** Evaluate $\oint_{|z|=1} \frac{1}{(z-2)(1+2z)^4(1-3z)^7}\,dz$ using residues at infinity.

::: pf

::: pf-step
The integrand $f(z) = \frac{1}{(z-2)(1+2z)^4(1-3z)^7}$ has poles inside $|z| = 1$ at $z = -1/2$ (order $4$) and $z = 1/3$ (order $7$), and a simple pole at $z = 2$ outside.

::: pf-proof
$1 + 2z = 0$ at $z = -1/2$ and $1 - 3z = 0$ at $z = 1/3$, both inside the unit circle; $z = 2$ is outside.
:::

:::

::: {.pf-step #sum-of-all-residues-zero}
The sum of all residues over the extended plane is $0$.

::: pf-proof
for a rational function, $\sum_{\text{finite poles}} \operatorname{Res}(f, z_j) + \operatorname{Res}(f, \infty) = 0$.
:::

:::

::: pf-step
Compute $\operatorname{Res}(f, \infty)$.

::: pf-proof

::: {.pf-step #res-infinity-def}
$\operatorname{Res}(f, \infty) = -\operatorname{Res}\qty(\frac{1}{z^2} f(1/z), 0)$.

::: pf-proof
definition of the residue at infinity.
:::

:::

::: pf-step
$\frac{1}{z^2} f(1/z) = \frac{1}{z^2} \cdot \frac{1}{(1/z - 2)(1 + 2/z)^4(1 - 3/z)^7} = \frac{z^{10}}{(1-2z)(z+2)^4(z-3)^7}$.

::: pf-proof
substitute $z \mapsto 1/z$ and simplify (multiply numerator and denominator by $z^{12}$).
:::

:::

::: {.pf-step #res-infinity-analytic-zero}
This is analytic at $z = 0$ (numerator has $z^{10}$), so $\operatorname{Res}\qty(\frac{1}{z^2}f(1/z), 0) = 0$.

::: pf-proof
no $1/z$ term in the Laurent expansion at $0$.
:::

:::

::: {.pf-step #res-infinity-value}
Hence $\operatorname{Res}(f, \infty) = 0$.

::: pf-proof
Steps [](#res-infinity-def){.pf-ref} and [](#res-infinity-analytic-zero){.pf-ref}.
:::

:::

:::

:::

::: pf-step
Compute $\operatorname{Res}(f, 2)$.

::: pf-proof

::: {.pf-step #res-at-2-value}
$z = 2$ is a simple pole, so $\operatorname{Res}(f, 2) = \lim_{z \to 2} (z-2) f(z) = \frac{1}{(1+2\cdot 2)^4 (1 - 3\cdot 2)^7} = \frac{1}{5^4 \cdot (-5)^7} = -\frac{1}{5^{11}}$.

::: pf-proof
the residue at a simple pole is the limit of $(z-2)f(z)$.
:::

:::

:::

:::

::: pf-step
Sum of residues inside $|z| = 1$.

::: pf-proof

::: pf-step
$\sum_{\text{inside}} \operatorname{Res} = -(\operatorname{Res}(f, 2) + \operatorname{Res}(f, \infty))$.

::: pf-proof
by step [](#sum-of-all-residues-zero){.pf-ref}, the total is zero, and the poles outside are $z = 2$ and $\infty$.
:::

:::

::: pf-step
$= -\qty(-\frac{1}{5^{11}} + 0) = \frac{1}{5^{11}}$.

::: pf-proof
substitute step [](#res-infinity-value){.pf-ref} and step [](#res-at-2-value){.pf-ref}.
:::

:::

:::

:::

::: pf-step
$\oint_{|z|=1} f(z)\,dz = 2\pi i \cdot \frac{1}{5^{11}}$.

::: pf-proof
the residue theorem.
:::

:::

::: pf-qed
the integral equals $\frac{2\pi i}{5^{11}}$.
:::

:::


:::
