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
---

:::{.exercise}
By computing
\[
{1\over 2\pi i}\oint {\cot(\pi z)\over z^2}\dz
,\]
say using a large rectangle, show that
\[
\zeta(2) = \sum_{k\geq 0} {1\over k^2} = {\pi^2\over 6}
.\]

:::

::: {.solution}
<1>1. Let $f(z) = \frac{\cot(\pi z)}{z^2}$.
::: {.proof}
definition.
:::

<1>2. $f$ has a pole of order $3$ at $z = 0$ and simple poles at each nonzero integer $z = k$.
::: {.proof}
$\cot(\pi z)$ has simple poles at the integers with residue $1/\pi$, and $z^{-2}$ adds a pole of order $2$ at $0$.
:::

<1>3. $\operatorname{Res}(f, k) = \frac{1}{\pi k^2}$ for $k \neq 0$.
::: {.proof}
$\cot(\pi z)$ has residue $1/\pi$ at $z = k$, so $f$ has residue $\frac{1}{\pi} \cdot k^{-2}$.
:::

<1>4. $\operatorname{Res}(f, 0) = -\frac{\pi}{3}$.
::: {.proof}
$\cot(\pi z) = \frac{1}{\pi z} - \frac{\pi z}{3} - \frac{\pi^3 z^3}{45} - \cdots$, so $f(z) = \frac{1}{\pi z^3} - \frac{\pi}{3z} - \frac{\pi^3 z}{45} - \cdots$, and the coefficient of $z^{-1}$ is $-\pi/3$.
:::

<1>5. Let $\gamma_N$ be the rectangle with vertices $(\pm (N + \tfrac12), \pm (N + \tfrac12))$.
::: {.proof}
choose a contour enclosing the poles $-N, \ldots, N$.
:::

<1>6. $\frac{1}{2\pi i}\oint_{\gamma_N} f(z)\,dz = \sum_{k=-N, k \neq 0}^{N} \frac{1}{\pi k^2} - \frac{\pi}{3} = \frac{2}{\pi}\sum_{k=1}^{N} \frac{1}{k^2} - \frac{\pi}{3}$.
::: {.proof}
residue theorem, using <1>3 and <1>4.
:::

<1>7. $\oint_{\gamma_N} f(z)\,dz \to 0$ as $N \to \infty$.
::: {.proof}
$|\cot(\pi z)|$ is bounded on $\gamma_N$ (the contour avoids the poles), $|z^{-2}| \le C/N^2$, and the perimeter is $O(N)$, so the integral is $O(1/N)$.
:::

<1>8. Hence $0 = \frac{2}{\pi}\sum_{k=1}^{\infty} \frac{1}{k^2} - \frac{\pi}{3}$.
::: {.proof}
<1>6 and <1>7, taking the limit.
:::

<1>9. Therefore $\zeta(2) = \sum_{k=1}^{\infty} \frac{1}{k^2} = \frac{\pi^2}{6}$.
::: {.proof}
<1>8, solving for the sum.
:::

<1>10. Q.E.D.
::: {.proof}
<1>9.
:::
:::
