---
schema: qual/card@1
id: P-RYJ3K
kind: problem
title: An everywhere differentiable function with $f'$ discontinuous at $0$
classification:
  areas:
  - complex-analysis
  topics:
  - Calculus
  - Counterexamples
  - Continuity
relations: []
review: draft
---

::: {.problem}
Give an example of a function $f:\RR\to \RR$ that is everywhere differentiable but $f'$ is not continuous at 0.
:::

::: {.solution}
Let
$$
\boxed{f(x)=\begin{cases}x^2\sin(1/x),&x\ne0,\\0,&x=0.\end{cases}}
$$

::: pf

::: {.pf-step #at-zero}

$f'(0)=0$.

::: pf-proof

$$
f'(0)=\lim_{h\to0}\frac{h^2\sin(1/h)}h=\lim_{h\to0}h\sin(1/h)=0,
$$
since $\abs{h\sin(1/h)}\le\abs h$.

:::

:::

::: {.pf-step #away}

For $x\ne0$, $f'(x)=2x\sin(1/x)-\cos(1/x)$.

::: pf-proof

This is the product and chain rule.

:::

:::

::: pf-step

$f$ is differentiable everywhere and $f'$ is not continuous at $0$.

::: pf-proof

Differentiability follows from steps [](#at-zero){.pf-ref} and [](#away){.pf-ref}. In step [](#away){.pf-ref}, $2x\sin(1/x)\to0$ as $x\to0$, while $\cos(1/x)$ equals $1$ at $x=1/(2\pi k)$ and $-1$ at $x=1/((2k+1)\pi)$. So $f'(x)$ has no limit as $x\to0$.

:::

:::

:::

:::
