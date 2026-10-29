---
schema: qual/card@1
id: P-SW2HY
kind: problem
title: $\bigl(\frac12(-1+\sqrt{3}i)\bigr)^n+\bigl(\frac12(-1-\sqrt{3}i)\bigr)^n$ equals
  $2$ if $3\mid n$ and $-1$ otherwise
classification:
  areas:
  - complex-analysis
  topics:
  - Trigonometry
  - Polynomials
relations: []
review: draft
---

::: {.problem}
Let $n$ be a natural number.
Show that

$$
\left[\tfrac12(-1+\sqrt{3} i)\right]^{n}+\left[\tfrac12(-1-\sqrt{3} i)\right]^{n}
$$

is equal to 2 if $n$ is a multiple of 3, and it is equal to $-1$ otherwise.
:::

::: {.solution}

::: pf

::: {.pf-step #cosine}

The sum equals $2\cos\frac{2\pi n}3$.

::: pf-proof

$\frac12(-1\pm\sqrt3\,i)=e^{\pm2\pi i/3}$, so the sum is $e^{2\pi in/3}+e^{-2\pi in/3}=2\cos\frac{2\pi n}3$.

:::

:::

::: pf-step

The sum is $2$ if $3\mid n$ and $-1$ otherwise.

::: pf-proof

By step [](#cosine){.pf-ref}: if $3\mid n$, then $\cos\frac{2\pi n}3=1$; if $n\equiv1$ or $2\pmod3$, then $\cos\frac{2\pi n}3=-\frac12$.

:::

:::

:::

:::
