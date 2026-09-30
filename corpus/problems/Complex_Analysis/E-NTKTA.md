---
schema: qual/card@1
id: E-NTKTA
kind: problem
title: 'Sum formulas: $1/n^2$'
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
\[
\sum_{n \geq 1} \frac{1}{n^{2}}=\frac{\pi^{2}}{6}
\]
by integrating $\pi \cot(\pi z)z^{-2}$.
:::

::: {.solution}
::: pf

::: pf-step
Let $f(z) = \pi \cot(\pi z) z^{-2}$.

::: pf-proof
definition.
:::

:::

::: pf-step
$f$ has a pole of order $3$ at $z = 0$ and simple poles at each nonzero integer $z = n$.

::: pf-proof
$\cot(\pi z)$ has simple poles at the integers with residue $1/\pi$, and $z^{-2}$ adds a pole of order $2$ at $0$.
:::

:::

::: {.pf-step #res-nonzero-n}
$\operatorname{Res}(f, n) = 1/n^2$ for $n \neq 0$.

::: pf-proof
$\pi \cot(\pi z)$ has residue $1$ at $z = n$, so $f$ has residue $1 \cdot n^{-2}$.
:::

:::

::: {.pf-step #res-zero}
$\operatorname{Res}(f, 0) = -\pi^2/3$.

::: pf-proof
$\pi \cot(\pi z) = \frac{1}{z} - \frac{\pi^2 z}{3} - \frac{\pi^4 z^3}{45} - \cdots$, so $f(z) = \frac{1}{z^3} - \frac{\pi^2}{3z} - \frac{\pi^4 z}{45} - \cdots$, and the coefficient of $z^{-1}$ is $-\pi^2/3$.
:::

:::

::: pf-step
Let $\gamma_N$ be the square with vertices $(\pm (N + \tfrac12), \pm (N + \tfrac12))$.

::: pf-proof
choose a contour enclosing the poles $-N, \ldots, N$.
:::

:::

::: {.pf-step #contour-integral-value}
$\int_{\gamma_N} f(z)\,dz = 2\pi i \left( \sum_{n=-N, n \neq 0}^{N} \frac{1}{n^2} - \frac{\pi^2}{3} \right) = 2\pi i \left( 2 \sum_{n=1}^{N} \frac{1}{n^2} - \frac{\pi^2}{3} \right)$.

::: pf-proof
residue theorem, using steps [](#res-nonzero-n){.pf-ref} and [](#res-zero){.pf-ref}.
:::

:::

::: {.pf-step #contour-vanishes}
$\int_{\gamma_N} f(z)\,dz \to 0$ as $N \to \infty$.

::: pf-proof
$|\cot(\pi z)|$ is bounded on $\gamma_N$ (the contour avoids the poles), $|z^{-2}| \le C/N^2$, and the perimeter is $O(N)$, so the integral is $O(1/N)$.
:::

:::

::: {.pf-step #limit-equation}
Hence $0 = 2\pi i \left( 2 \sum_{n=1}^{\infty} \frac{1}{n^2} - \frac{\pi^2}{3} \right)$.

::: pf-proof
Steps [](#contour-integral-value){.pf-ref} and [](#contour-vanishes){.pf-ref}, taking the limit.
:::

:::

::: {.pf-step #sum-value}
Therefore $\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}$.

::: pf-proof
Step [](#limit-equation){.pf-ref}, solving for the sum.
:::

:::

::: pf-qed
Step [](#sum-value){.pf-ref}.
:::

:::

:::
