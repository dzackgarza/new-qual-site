---
schema: qual/card@1
id: P-YFZRX
kind: problem
title: $\int x\sec^{-1}(x)\,dx$ and $\int x\csc^{-1}(x)\,dx$
classification:
  areas:
  - prelim
  topics:
  - Integrals
  - Integration by Parts
  - Trigonometry
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Corrected the second mislabeled inverse-trigonometric integral and made the branch domain explicit.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    No source document is retained for this card. The collection
    SRC-PRELIM-ART-INTEGRAL-PRACTICE has an empty provenance list, its own
    remark records that the drill sheet's original paper was not found, and
    searching assets/attachments/ and the migration records finds no copy of the
    sheet, so there is no page to read and the printed statement could not be
    compared with a source document. What was checked here is the statement and
    its answer: the two inverse-trigonometric derivatives on x > 1 from the inverse function theorem, and both integration by parts results, each checked by differentiating
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet, so the value is
    derived here rather than transcribed. Two derivatives of inverse trigonometric functions, then integration by parts in each case.
---

::: {.problem}
For $x>1$, evaluate
$$
\int x\,\sec^{-1}(x)\,dx
\qquad\text{and}\qquad
\int x\,\csc^{-1}(x)\,dx.
$$
:::

::: {.solution}

For $x>1$ the principal branches of the inverse secant and cosecant are
differentiable, with the derivatives stated below, and both integrands are
continuous there.

::: pf

::: {.pf-step #derivatives}

For $x>1$, $\dfrac{d}{dx}\sec^{-1}x=\dfrac{1}{x\sqrt{x^2-1}}$ and
$\dfrac{d}{dx}\csc^{-1}x=-\dfrac{1}{x\sqrt{x^2-1}}$.

::: pf-proof

On $x>1$ the principal branch of $\sec^{-1}$ is the inverse of $\sec$
restricted to $(0,\frac\pi2)$, so by the inverse function theorem
$\frac{d}{dx}\sec^{-1}x=\frac{1}{\sec'\theta}$ with $\theta=\sec^{-1}x$, that
is $\frac{1}{\sec\theta\tan\theta}=\frac{1}{x\sqrt{x^2-1}}$ because
$\tan\theta=\sqrt{\sec^2\theta-1}$ is positive for $\theta\in(0,\frac\pi2)$.
Similarly $\csc^{-1}$ on $x>1$ is the inverse of $\csc$ restricted to
$(0,\frac\pi2)$, and $\csc'=-\csc\cot$ gives $-\frac{1}{x\sqrt{x^2-1}}$.

:::

:::

::: {.pf-step #secant}

$\displaystyle\int
x\sec^{-1}x\,dx=\frac12\left(x^2\sec^{-1}x-\sqrt{x^2-1}\right)+C$ on $x>1$.

::: pf-proof

Integrate by parts with $u=\sec^{-1}x$, $dv=x\,dx$: $\int
x\sec^{-1}x\,dx=\frac{x^2}{2}\sec^{-1}x-\int\frac{x^2}{2}\cdot\frac{dx}{x\sqrt{x^2-1}}=\frac{x^2}{2}\sec^{-1}x-\frac12\int\frac{x\,dx}{\sqrt{x^2-1}}$,
using step [](#derivatives){.pf-ref}. Since
$\frac{d}{dx}\sqrt{x^2-1}=\frac{x}{\sqrt{x^2-1}}$, the last integral is
$\sqrt{x^2-1}$, giving the stated primitive; differentiating it gives
$x\sec^{-1}x+\frac{x^2}{2}\cdot\frac{1}{x\sqrt{x^2-1}}-\frac{x}{2\sqrt{x^2-1}}=x\sec^{-1}x$.

:::

:::

::: {.pf-step #cosecant}

$\displaystyle\int
x\csc^{-1}x\,dx=\frac12\left(x^2\csc^{-1}x+\sqrt{x^2-1}\right)+C$ on $x>1$.

::: pf-proof

The same integration by parts gives
$\frac{x^2}{2}\csc^{-1}x-\int\frac{x^2}{2}\left(-\frac{dx}{x\sqrt{x^2-1}}\right)=\frac{x^2}{2}\csc^{-1}x+\frac12\sqrt{x^2-1}+C$,
with the sign because the derivative of $\csc^{-1}$ is negative by step
[](#derivatives){.pf-ref}. Differentiating gives
$x\csc^{-1}x-\frac{x^2}{2}\cdot\frac{1}{x\sqrt{x^2-1}}+\frac{x}{2\sqrt{x^2-1}}=x\csc^{-1}x$,
which checks it.

:::

:::

:::


:::
