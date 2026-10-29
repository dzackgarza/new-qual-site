---
schema: qual/card@1
id: P-SKT7G
kind: problem
title: $\lim_{x\to\infty}f'(x)=0$ whenever $\lim f$ and $\lim f'$ exist at infinity;
  a counterexample when $\lim f'$ fails to exist
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Limits
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $f:\RR\to\RR$ be a differentiable function with $f'\in C(\RR)$.
Assume that there are $a,b\in\RR$ with $\lim_{x\to\infty}f(x)=a$ and $\lim_{x\to\infty}f'(x)=b$.
Prove that $b=0$.
Then, find a counterexample to show that the assumption $\lim_{x\to\infty}f'(x)$ exists is necessary.
:::

::: {.solution}

::: pf

::: pf-step

$b = 0$.

::: pf-proof

By the mean value theorem applied to $f$ on $[x, x+1]$, for each $x$ there is $\xi_x \in (x, x+1)$ with $$ f(x+1) - f(x) = f'(\xi_x) . $$ As $x \to \infty$, the left side tends to $a - a = 0$, because both $f(x+1)$ and $f(x)$ tend to $a$. Also $\xi_x \to \infty$, so $f'(\xi_x) \to b$. Hence $b = 0$.

:::

:::

::: pf-step

The function $\boxed{f(x)=\sin(x^2)/\sqrt{1+x^2}}$ is continuously differentiable on $\RR$ and satisfies $\lim_{x\to\infty}f(x)=0$, but $\lim_{x\to\infty}f'(x)$ does not exist.

::: pf-proof

The function $f$ is a quotient of smooth functions with nonvanishing denominator, so $f\in C^1(\RR)$. Since $\abs{f(x)}\leq(1+x^2)^{-1/2}$, $f(x)\to0$. Differentiation gives
$$
f'(x) = \frac{2x\cos(x^2)}{\sqrt{1+x^2}} - \frac{x\sin(x^2)}{(1+x^2)^{3/2}}.
$$
The second term tends to $0$, and $2x/\sqrt{1+x^2}\to2$. Along $x_k=\sqrt{2\pi k}$ the first term tends to $2$, and along $y_k=\sqrt{(2k+1)\pi}$ it tends to $-2$. Hence $f'(x_k)\to2$ and $f'(y_k)\to-2$, so $\lim_{x\to\infty}f'(x)$ does not exist.

:::

:::

:::

:::
