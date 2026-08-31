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
---

::: problem
Let $f \in L^1(\mathbb{R})$ and $x f(x) \in L^1(\mathbb{R})$.
Prove that the Fourier transform $\hat{f}$ is differentiable at every point $\xi \in \mathbb{R}$.
:::

::: {.solution}
**Goal.** Show $\hat f$ is differentiable everywhere when $f, xf \in L^1$.

<1>1. $\hat f(\xi) = \int f(x) e^{-2\pi i x\xi}\,dx$.
::: {.proof}
definition.
:::

<1>2. The integrand is differentiable in $\xi$ with derivative $-2\pi i x f(x) e^{-2\pi i x\xi}$.
::: {.proof}
differentiate $e^{-2\pi i x\xi}$ with respect to $\xi$.
:::

<1>3. The derivative is dominated by $2\pi |x f(x)| \in L^1$.
::: {.proof}
$|{-2\pi i x f(x) e^{-2\pi i x\xi}}| = 2\pi |x f(x)|$, and $xf \in L^1$ by hypothesis.
:::

<1>4. Hence $\hat f$ is differentiable and $\hat f'(\xi) = \int (-2\pi i x) f(x) e^{-2\pi i x\xi}\,dx = -2\pi i \widehat{xf}(\xi)$.
::: {.proof}
differentiation under the integral sign, justified by the dominated convergence theorem (the difference quotients are dominated by $2\pi |xf| \in L^1$).
:::

<1>5. Q.E.D.
::: {.proof}
<1>4 shows $\hat f$ is differentiable at every $\xi$.
:::
:::
