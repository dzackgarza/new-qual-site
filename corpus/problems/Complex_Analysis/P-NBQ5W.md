---
schema: qual/card@1
id: P-NBQ5W
kind: problem
title: An everywhere differentiable function whose derivative is discontinuous at
  $0$
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
f(x) \definedas
\begin{cases}
x^2\sin\qty{1\over x} & x\neq 0, \\
0 & x=0.
\end{cases}
$$

::: pf

::: {.pf-step #away-from-zero}
For $x\neq0$, $f$ is differentiable with $f'(x)=2x\sin\qty{1\over x}-\cos\qty{1\over x}$.

::: pf-proof
On $\RR\setminus\theset{0}$, $f$ is a product of $x^2$ and $\sin(1/x)$, both differentiable there; the product and chain rules give $2x\sin(1/x)+x^2\cos(1/x)\cdot(-1/x^2)$.
:::

:::

::: {.pf-step #at-zero}
$f$ is differentiable at $0$ with $f'(0)=0$.

::: pf-proof
$\abs{\frac{f(x)-f(0)}{x}}=\abs{x\sin\qty{1\over x}}\le\abs{x}\to0$ as $x\to0$.
:::

:::

::: pf-step
$f'$ is not continuous at $0$.

::: pf-proof
Let $x_n=\frac{1}{2\pi n}$. By step [](#away-from-zero){.pf-ref}, $f'(x_n)=0-\cos(2\pi n)=-1$ for every $n$, while $x_n\to0$ and $f'(0)=0$ by step [](#at-zero){.pf-ref}.
:::

:::

:::
:::
