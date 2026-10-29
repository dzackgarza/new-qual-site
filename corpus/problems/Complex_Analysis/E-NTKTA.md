---
schema: qual/card@1
id: E-NTKTA
kind: problem
title: $\sum 1/n^2 = \pi^2/6$ by integrating $\pi\cot(\pi z)/z^2$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Series of Numbers
  - Trigonometry
  - Meromorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}
Show
$$
\sum_{n \geq 1} \frac{1}{n^{2}}=\frac{\pi^{2}}{6}
$$
by integrating $\pi \cot(\pi z)z^{-2}$.
:::

::: {.solution}

Let $f(z) \coloneqq \pi \cot(\pi z) z^{-2}$, and for $N\geq 1$ let $\gamma_N$ be the positively oriented boundary of the square with vertices $\pm (N + \tfrac12) \pm (N + \tfrac12)i$.

::: pf

::: {.pf-step #res-nonzero-n}
For $n \in\ZZ\setminus\{0\}$, $f$ has a simple pole at $n$ with $\Res_{z=n} f = 1/n^2$.

::: pf-proof
$\sin(\pi z)$ has a simple zero at $n$ with derivative $\pi\cos(\pi n)$, so $\pi\cot(\pi z) = \pi\cos(\pi z)/\sin(\pi z)$ has a simple pole at $n$ with residue $\pi\cos(\pi n)/(\pi\cos(\pi n)) = 1$.
Since $z^{-2}$ is holomorphic and equal to $n^{-2}$ at $n$, the residue of $f$ is $n^{-2}$.
:::

:::

::: {.pf-step #res-zero}
$\Res_{z=0} f = -\pi^2/3$.

::: pf-proof
Near $0$, $\pi \cot(\pi z) = \frac{1}{z} - \frac{\pi^2 z}{3} + O(z^3)$, so $f(z) = \frac{1}{z^3} - \frac{\pi^2}{3z} + O(z)$.
:::

:::

::: {.pf-step #contour-integral-value}
$\displaystyle\int_{\gamma_N} f(z)\,dz = 2\pi i \left( 2 \sum_{n=1}^{N} \frac{1}{n^2} - \frac{\pi^2}{3} \right)$.

::: pf-proof
The poles of $f$ inside $\gamma_N$ are $-N, \ldots, N$, and none lies on $\gamma_N$.
Apply the residue theorem with steps [](#res-nonzero-n){.pf-ref} and [](#res-zero){.pf-ref}, using $1/(-n)^2 = 1/n^2$.
:::

:::

::: {.pf-step #contour-vanishes}
$\int_{\gamma_N} f(z)\,dz \to 0$ as $N \to \infty$.

::: pf-proof
$\abs{\cot(\pi z)}$ is bounded on $\gamma_N$ by a constant $C$ independent of $N$: on the vertical sides $\abs{\cot(\pi z)} = \abs{\tanh(\pi y)}\leq 1$, and on the horizontal sides $\abs{\cot(\pi z)} \leq \coth(\pi (N+\tfrac12)) \leq \coth(\pi/2)$.
On $\gamma_N$, $\abs{z^{-2}} \leq (N+\tfrac12)^{-2}$, and the length of $\gamma_N$ is $8(N+\tfrac12)$, so the integral is at most $8\pi C/(N+\tfrac12)$.
:::

:::

::: pf-step
$\displaystyle\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}$.

::: pf-proof
Let $N\to\infty$ in step [](#contour-integral-value){.pf-ref}; by step [](#contour-vanishes){.pf-ref}, $2\sum_{n\geq1} 1/n^2 - \pi^2/3 = 0$.
:::

:::

:::

:::
