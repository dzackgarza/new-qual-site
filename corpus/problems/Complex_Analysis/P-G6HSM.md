---
schema: qual/card@1
id: P-G6HSM
kind: problem
title: The modulus of $\frac{z_1-z_2}{1-\bar z_1z_2}$ is less than $1$ on the disc and equal to $1$ on the circle
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.problem}
Let $z_1,z_2\in\CC$.

(a) Prove that
$$
\abs{1-\bar z_1z_2}^2-\abs{z_1-z_2}^2
=(1-\abs{z_1}^2)(1-\abs{z_2}^2).
$$

(b) Deduce that if $\abs{z_1},\abs{z_2}<1$, then
$$
\abs{\frac{z_1-z_2}{1-\bar z_1z_2}}<1.
$$

(c) If $z_1\ne z_2$, prove that the last modulus equals $1$ if and only
if $|z_1|=1$ or $|z_2|=1$.
:::

::: {.solution}
::: pf

::: {.pf-step #identity}
(a) $\abs{1-\bar z_1z_2}^2-\abs{z_1-z_2}^2=(1-\abs{z_1}^2)(1-\abs{z_2}^2)$.

::: pf-proof
Expanding, $\abs{1-\bar z_1z_2}^2 = 1-\bar z_1 z_2 - z_1\bar z_2+\abs{z_1}^2\abs{z_2}^2$ and $\abs{z_1-z_2}^2=\abs{z_1}^2+\abs{z_2}^2-\bar z_1 z_2-z_1\bar z_2$. The difference is $1-\abs{z_1}^2-\abs{z_2}^2+\abs{z_1}^2\abs{z_2}^2$, which factors as stated.
:::

:::

::: pf-step
(b) If $\abs{z_1},\abs{z_2}<1$, then $\abs{\frac{z_1-z_2}{1-\bar z_1z_2}}<1$.

::: pf-proof
The denominator is nonzero because $\abs{\bar z_1 z_2}<1$. The right side of step [](#identity){.pf-ref} is positive, so $\abs{z_1-z_2}<\abs{1-\bar z_1z_2}$.
:::

:::

::: pf-step
(c) If $z_1\neq z_2$ and $\bar z_1 z_2\neq 1$, then $\abs{\frac{z_1-z_2}{1-\bar z_1z_2}}=1$ if and only if $\abs{z_1}=1$ or $\abs{z_2}=1$.

::: pf-proof
When the denominator is nonzero, the modulus equals $1$ exactly when the left side of step [](#identity){.pf-ref} is zero, that is, when $(1-\abs{z_1}^2)(1-\abs{z_2}^2)=0$.
If $\abs{z_1}=1$, then $\bar z_1 z_2 = 1$ would force $z_2 = 1/\bar z_1 = z_1$; likewise if $\abs{z_2}=1$. So under the hypothesis $z_1\neq z_2$ the quotient is defined whenever $\abs{z_1}=1$ or $\abs{z_2}=1$.
:::

:::

:::

:::
