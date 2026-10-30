---
schema: qual/card@1
id: P-CASP09H
kind: problem
title: 'Entire functions with $\abs{f(x+iy)}\leq e^{xy}$'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Find all entire functions $f(z)$ with the property that for all $z$, $\abs{f(z)} \leq e^{xy}$, where $x$ and $y$ are the real and imaginary parts of $z$.
:::

::: {.solution}
The answer is
$$
f(z)=c\,e^{-iz^2/2},\qquad c\in\CC,\ \abs{c}\le1.
$$

::: pf

::: {.pf-step #modulus}
$\abs{e^{\pm iz^2/2}}=e^{\mp xy}$ for $z=x+iy$.

::: pf-proof
$z^2=x^2-y^2+2ixy$, so $\operatorname{Re}\bigl(\pm\tfrac i2z^2\bigr)=\mp xy$.
:::

:::

::: {.pf-step #necessary}
Every such $f$ has the stated form.

::: pf-proof
Let $g(z)=f(z)e^{iz^2/2}$. It is entire, and by step [](#modulus){.pf-ref}, $\abs{g(z)}\le e^{xy}e^{-xy}=1$ on $\CC$. Liouville's theorem makes $g$ a constant $c$, and $\abs{c}\le1$. Hence $f(z)=c\,e^{-iz^2/2}$.
:::

:::

::: {.pf-step #sufficient}
Every function of the stated form satisfies the bound.

::: pf-proof
By step [](#modulus){.pf-ref}, $\abs{c\,e^{-iz^2/2}}=\abs{c}e^{xy}\le e^{xy}$.
:::

:::

::: pf-qed
Steps [](#necessary){.pf-ref} and [](#sufficient){.pf-ref}.
:::

:::
:::
