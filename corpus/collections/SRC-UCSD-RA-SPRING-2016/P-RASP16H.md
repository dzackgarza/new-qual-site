---
schema: qual/card@1
id: P-RASP16H
kind: problem
title: "First moment condition makes the Fourier transform differentiable"
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Transform
  - Differentiation
  - Dominated Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 8 of the official UCSD Spring 2016 real-analysis qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Existing dominated-difference-quotient proof reviewed as correct; normalized legacy solution/proof block syntax.
---

::: {.problem}
Let $f \in L^1(\mathbb{R})$ and $x f(x) \in L^1(\mathbb{R})$.
Prove that the Fourier transform $\hat{f}$ is differentiable at every point $\xi \in \mathbb{R}$.
:::

::: {.solution}
**Goal.** Show $\hat f$ is differentiable everywhere when $f, xf \in L^1$.

::: pf

::: pf-step

$\hat f(\xi) = \int f(x) e^{-2\pi i x\xi}\,dx$.

::: pf-proof

definition.

:::

:::

::: pf-step

The integrand is differentiable in $\xi$ with derivative $-2\pi i x f(x) e^{-2\pi i x\xi}$.

::: pf-proof

differentiate $e^{-2\pi i x\xi}$ with respect to $\xi$.

:::

:::

::: pf-step

The derivative is dominated by $2\pi |x f(x)| \in L^1$.

::: pf-proof

$|{-2\pi i x f(x) e^{-2\pi i x\xi}}| = 2\pi |x f(x)|$, and $xf \in L^1$ by hypothesis.

:::

:::

::: {.pf-step #s4}

Hence $\hat f$ is differentiable and $\hat f'(\xi) = \int (-2\pi i x) f(x) e^{-2\pi i x\xi}\,dx = -2\pi i \widehat{xf}(\xi)$.

::: pf-proof

differentiation under the integral sign, justified by the dominated convergence theorem (the difference quotients are dominated by $2\pi |xf| \in L^1$).

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} shows $\hat f$ is differentiable at every $\xi$.

:::

:::

:::
