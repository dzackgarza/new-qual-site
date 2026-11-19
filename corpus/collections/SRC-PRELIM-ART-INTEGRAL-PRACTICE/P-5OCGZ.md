---
schema: qual/card@1
id: P-5OCGZ
kind: problem
title: $\int\frac{x+1}{\sqrt{4-x^2}}\,dx$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Trigonometric Substitution
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the four leaf steps of the two substitutions, which asserted their
    computation with no justification, each carry a sentence deriving it, including the cancellation of
    the cosine and the identification theta = arcsin(x/2) on the chosen range. The two antiderivatives
    were checked by differentiating them back to x/sqrt(4-x^2) and 1/sqrt(4-x^2), and their sum to
    (x+1)/sqrt(4-x^2). Nothing in the statement was changed.

---

::: {.problem}
Evaluate
$$
\int\frac{x+1}{\sqrt{4-x^2}}\,dx.
$$
:::

::: {.solution}
Take $\abs{x} < 2$.

::: pf

::: pf-step

Split the integral into two parts: $$\int \frac{x+1}{\sqrt{4-x^2}} \, dx = \int \frac{x}{\sqrt{4-x^2}} \, dx + \int \frac{1}{\sqrt{4-x^2}} \, dx.$$

::: pf-proof

The integrand satisfies $\frac{x+1}{\sqrt{4-x^2}} = \frac{x}{\sqrt{4-x^2}} + \frac{1}{\sqrt{4-x^2}}$, and the integral of a sum is the sum of the integrals.

:::

:::

::: {.pf-step #s2}

$\int \frac{x}{\sqrt{4-x^2}} \, dx = -\sqrt{4-x^2} + C_1$.

::: pf-proof

::: pf-step

Substitute $u = 4 - x^2 \implies du = -2x \, dx \implies x \, dx = -\frac{1}{2} \, du$.

::: pf-proof
Differentiating $u=4-x^2$ gives $du=-2x\,dx$, so $x\,dx=-\frac12 du$; on $\abs x<2$ the quantity $u$ is positive, so the square root is differentiable there.
:::

:::

::: pf-step

$\int \frac{x}{\sqrt{4-x^2}} \, dx = -\frac{1}{2} \int u^{-1/2} \, du = -\frac{1}{2} (2 u^{1/2}) + C_1 = -\sqrt{4-x^2} + C_1$.

::: pf-proof
Substituting the preceding relations turns the integral into $-\frac12\int u^{-1/2}du$, whose antiderivative is $2u^{1/2}$; replacing $u$ by $4-x^2$ gives the displayed result.
:::

:::

:::

:::

::: {.pf-step #s3}

$\int \frac{1}{\sqrt{4-x^2}} \, dx = \arcsin\left(\frac{x}{2}\right) + C_2$.

::: pf-proof

::: pf-step

Substitute $x = 2\sin(\theta)$ for $\theta \in (-\pi/2, \pi/2)$, so $dx = 2\cos(\theta) \, d\theta$ and $\sqrt{4-x^2} = \sqrt{4 - 4\sin^2(\theta)} = 2\cos(\theta)$.

::: pf-proof
Differentiating $x=2\sin\theta$ gives $dx=2\cos\theta\,d\theta$, and $\sqrt{4-4\sin^2\theta}=2\abs{\cos\theta}=2\cos\theta$ because the cosine is positive on $(-\pi/2,\pi/2)$.
:::

:::

::: pf-step

$\int \frac{1}{\sqrt{4-x^2}} \, dx = \int \frac{2\cos(\theta)}{2\cos(\theta)} \, d\theta = \int 1 \, d\theta = \theta + C_2 = \arcsin\left(\frac{x}{2}\right) + C_2$.

::: pf-proof
The factor $2\cos\theta$ cancels, leaving the integral of $1$; and $\theta=\arcsin(x/2)$ because $\sin\theta=x/2$ with $\theta$ in the range on which arcsine is the inverse of sine.
:::

:::

:::

:::

::: pf-step

Combining results: $$\int \frac{x+1}{\sqrt{4-x^2}} \, dx = -\sqrt{4-x^2} + \arcsin\left(\frac{x}{2}\right) + C.$$

::: pf-proof

Adding the two antiderivatives from steps [](#s2){.pf-ref} and [](#s3){.pf-ref}, and absorbing the constants $C_1 + C_2$ into a single constant $C$, gives the stated result.

:::

:::

:::

:::
