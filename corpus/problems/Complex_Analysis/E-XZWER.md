---
schema: qual/card@1
id: E-XZWER
kind: problem
title: $\sin z=z$ has infinitely many solutions in $\CC$
classification:
  areas:
  - complex-analysis
  topics:
  - Picard
  - Entire Functions
  - Trigonometry
relations: []
review: draft
---

::: {.exercise}
Show that $\sin(z) = z$ has infinitely many solutions in $\CC$.
:::

::: {.solution}
Let $f(z)\coloneqq\sin(z) - z$.

::: pf

::: {.pf-step #picard}
$f$ takes every value in $\CC$, with at most one exception, infinitely many times.

::: pf-proof
$f$ is entire and not a polynomial, since its Taylor series $-\frac{z^3}{3!} + \frac{z^5}{5!} - \cdots$ does not terminate.
So $w\mapsto f(1/w)$ has an essential singularity at $0$, and the big Picard theorem applies to it on every punctured neighbourhood of $0$.
:::

:::

::: {.pf-step #shift}
$f(z+2\pi) = f(z) - 2\pi$ for all $z$.

::: pf-proof
$\sin$ is $2\pi$-periodic.
:::

:::

::: pf-step
No value is taken only finitely often by $f$; in particular $f(z) = 0$ has infinitely many solutions.

::: pf-proof
Suppose $f$ takes the value $c$ only finitely often.
By step [](#picard){.pf-ref}, $c$ is the unique exceptional value, so $f$ takes $c+2\pi\neq c$ at infinitely many points $z_j$.
By step [](#shift){.pf-ref}, $f(z_j+2\pi) = c$ at the infinitely many distinct points $z_j + 2\pi$, a contradiction.
:::

:::

:::

:::
