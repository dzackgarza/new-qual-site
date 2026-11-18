---
schema: qual/card@1
id: E-SS5.EX-6
kind: problem
title: Wallis's product formula
classification:
  areas:
  - complex-analysis
  topics:
  - Infinite Products
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
Prove Wallis's product formula
$$
\frac{\pi}{2} = \frac{2\cdot2}{1\cdot3}\cdot\frac{4\cdot4}{3\cdot5}\cdots\frac{2m\cdot2m}{(2m-1)\cdot(2m+1)}\cdots .
$$

[Hint: Use the product formula for $\sin z$ at $z = \pi/2$.]
:::

::: {.solution}

The argument is the card's own: the Euler product for $\sin z$ at $z=\pi/2$ and taking reciprocals.

::: pf

::: {.pf-step #product}

$\displaystyle\frac{\sin z}{z}=\prod_{n=1}^{\infty}\Bigl(1-\frac{z^{2}}{\pi^{2}n^{2}}\Bigr)$ for all $z\in\CC$, the product converging absolutely and locally uniformly.

::: pf-proof

This is the Euler product formula for the sine function, which follows from the partial-fraction expansion of $\pi\cot(\pi z)$ by term-by-term integration, or equivalently from the Hadamard factorisation of the entire function $\sin z/z$, whose zeros are exactly $\pm\pi n$ and which is of order $1$ with no exponential factor.

:::

:::

::: {.pf-step #halfpi}

$\displaystyle\frac{2}{\pi}=\prod_{n=1}^{\infty}\frac{(2n-1)(2n+1)}{(2n)^{2}}$.

::: pf-proof

Substituting $z=\pi/2$ in step [](#product){.pf-ref} and using $\sin(\pi/2)=1$ gives $\frac{1}{\pi/2}=\frac{2}{\pi}$ for the left side, while each factor is
$$
1-\frac{(\pi/2)^{2}}{\pi^{2}n^{2}}=1-\frac{1}{4n^{2}}=\frac{4n^{2}-1}{4n^{2}}=\frac{(2n-1)(2n+1)}{(2n)^{2}}.
$$
Since the product converges to a nonzero limit, the identity may be inverted.

:::

:::

::: {.pf-step #wallis}

$\displaystyle\frac{\pi}{2}=\prod_{m=1}^{\infty}\frac{2m\cdot2m}{(2m-1)(2m+1)}$.

::: pf-proof

Inverting both sides of step [](#halfpi){.pf-ref} — legitimate because every factor $\frac{(2n-1)(2n+1)}{(2n)^{2}}$ is nonzero and the product converges to $\frac{2}{\pi}\ne0$ — and writing $n$ as $m$ gives
$$
\boxed{\frac{\pi}{2}=\prod_{m=1}^{\infty}\frac{2m\cdot2m}{(2m-1)(2m+1)},}
$$
that is, the partial products $\frac{2\cdot2}{1\cdot3}\cdot\frac{4\cdot4}{3\cdot5}\cdots\frac{2m\cdot2m}{(2m-1)(2m+1)}$ tend to $\frac{\pi}{2}$ as $m\to\infty$, which is Wallis's formula.

:::

:::

:::

:::
