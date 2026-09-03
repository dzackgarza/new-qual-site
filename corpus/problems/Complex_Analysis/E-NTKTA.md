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
<1>1. Let $f(z) = \pi \cot(\pi z) z^{-2}$.
::: {.proof}
definition.
:::

<1>2. $f$ has a pole of order $3$ at $z = 0$ and simple poles at each nonzero integer $z = n$.
::: {.proof}
$\cot(\pi z)$ has simple poles at the integers with residue $1/\pi$, and $z^{-2}$ adds a pole of order $2$ at $0$.
:::

<1>3. $\operatorname{Res}(f, n) = 1/n^2$ for $n \neq 0$.
::: {.proof}
$\pi \cot(\pi z)$ has residue $1$ at $z = n$, so $f$ has residue $1 \cdot n^{-2}$.
:::

<1>4. $\operatorname{Res}(f, 0) = -\pi^2/3$.
::: {.proof}
$\pi \cot(\pi z) = \frac{1}{z} - \frac{\pi^2 z}{3} - \frac{\pi^4 z^3}{45} - \cdots$, so $f(z) = \frac{1}{z^3} - \frac{\pi^2}{3z} - \frac{\pi^4 z}{45} - \cdots$, and the coefficient of $z^{-1}$ is $-\pi^2/3$.
:::

<1>5. Let $\gamma_N$ be the square with vertices $(\pm (N + \tfrac12), \pm (N + \tfrac12))$.
::: {.proof}
choose a contour enclosing the poles $-N, \ldots, N$.
:::

<1>6. $\int_{\gamma_N} f(z)\,dz = 2\pi i \left( \sum_{n=-N, n \neq 0}^{N} \frac{1}{n^2} - \frac{\pi^2}{3} \right) = 2\pi i \left( 2 \sum_{n=1}^{N} \frac{1}{n^2} - \frac{\pi^2}{3} \right)$.
::: {.proof}
residue theorem, using <1>3 and <1>4.
:::

<1>7. $\int_{\gamma_N} f(z)\,dz \to 0$ as $N \to \infty$.
::: {.proof}
$|\cot(\pi z)|$ is bounded on $\gamma_N$ (the contour avoids the poles), $|z^{-2}| \le C/N^2$, and the perimeter is $O(N)$, so the integral is $O(1/N)$.
:::

<1>8. Hence $0 = 2\pi i \left( 2 \sum_{n=1}^{\infty} \frac{1}{n^2} - \frac{\pi^2}{3} \right)$.
::: {.proof}
<1>6 and <1>7, taking the limit.
:::

<1>9. Therefore $\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}$.
::: {.proof}
<1>8, solving for the sum.
:::

<1>10. Q.E.D.
::: {.proof}
<1>9.
:::
:::
