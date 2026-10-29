---
schema: qual/card@1
id: E-VA3OK
kind: problem
title: Computing $\zeta(2)$ by integration
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Series of Numbers
  - Trigonometry
  - Riemann Zeta
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source writes the sum as starting at k >= 0, whose first term is undefined; the statement starts it at k >= 1.
---

::: {.exercise}
By computing
$$
{1\over 2\pi i}\oint {\cot(\pi z)\over z^2}\dz,
$$
say using a large rectangle, show that
$$
\zeta(2) = \sum_{k\geq 1} {1\over k^2} = {\pi^2\over 6}.
$$

:::

::: {.solution}
Let $f(z) = \frac{\cot(\pi z)}{z^2}$, and for $N\in\NN$ let $\gamma_N$ be the positively oriented boundary of the square with vertices $\pm (N + \tfrac12) \pm i(N + \tfrac12)$.
The poles of $f$ are the integers, and $\gamma_N$ encloses exactly $-N,\ldots,N$.

::: pf

::: {.pf-step #res-nonzero-k}
$\Res(f, k) = \frac{1}{\pi k^2}$ for $k \in\ZZ\setminus\theset{0}$.

::: pf-proof
$\cot(\pi z)$ has a simple pole at $z = k$ with residue $\frac{\cos(\pi k)}{\pi\cos(\pi k)}=\frac1\pi$, and $z^{-2}$ is holomorphic and equal to $k^{-2}$ there.
:::

:::

::: {.pf-step #res-zero}
$\Res(f, 0) = -\frac{\pi}{3}$.

::: pf-proof
$\cot(\pi z) = \frac{1}{\pi z} - \frac{\pi z}{3} + O(z^3)$, so $f(z) = \frac{1}{\pi z^3} - \frac{\pi}{3z} + O(z)$, and the coefficient of $z^{-1}$ is $-\pi/3$.
:::

:::

::: {.pf-step #contour-integral-value}
$\frac{1}{2\pi i}\oint_{\gamma_N} f(z)\,dz = \frac{2}{\pi}\sum_{k=1}^{N} \frac{1}{k^2} - \frac{\pi}{3}$.

::: pf-proof
By the residue theorem with steps [](#res-nonzero-k){.pf-ref} and [](#res-zero){.pf-ref}, pairing the residues at $k$ and $-k$.
:::

:::

::: {.pf-step #contour-vanishes}
$\oint_{\gamma_N} f(z)\,dz \to 0$ as $N \to \infty$.

::: pf-proof
$\abs{\cot(\pi z)}$ is bounded on $\gamma_N$ by a constant $C$ independent of $N$: on the vertical sides $\abs{\cot(\pi z)}=\abs{\tanh(\pi y)}\le1$, and on the horizontal sides $\abs{\cot(\pi z)}\le\coth(\pi(N+\tfrac12))\le\coth(\pi/2)$.
Also $\abs{z^{-2}} \le (N+\tfrac12)^{-2}$ on $\gamma_N$, and the length of $\gamma_N$ is $8(N+\tfrac12)$, so the integral is at most $8C/(N+\tfrac12)$.
:::

:::

::: pf-step
$\zeta(2) = \sum_{k=1}^{\infty} \frac{1}{k^2} = \boxed{\frac{\pi^2}{6}}$.

::: pf-proof
Letting $N\to\infty$ in step [](#contour-integral-value){.pf-ref} and using step [](#contour-vanishes){.pf-ref} gives $0 = \frac{2}{\pi}\sum_{k=1}^{\infty} \frac{1}{k^2} - \frac{\pi}{3}$.
:::

:::

:::

:::
