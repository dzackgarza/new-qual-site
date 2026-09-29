---
schema: qual/card@1
id: P-IZW2T
kind: problem
title: Laurent series expansions in annuli
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Poles
  - Essential Singularities
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.problem}
Expand the following functions into Laurent series in the indicated regions:

(a) $\displaystyle f(z) = \frac{z^2 - 1}{ (z+2)(z+3)}, \; \; 2 < |z| < 3$, $3 < |z| < + \infty$.

(b) $\displaystyle f(z) = \sin \frac{z}{1-z}, \; \; 0 < |z-1| < + \infty$
:::

::: {.solution}
**Goal:** Compute the exact Laurent series expansions for each function in the specified annular domains.

::: pf

::: pf-step
Part (a): Partial fraction decomposition of $f(z)$.

::: pf-proof
Perform polynomial division on $f(z) = \frac{z^2 - 1}{z^2 + 5z + 6}$:
$$\frac{z^2 - 1}{z^2 + 5z + 6} = 1 + \frac{-5z - 7}{(z+2)(z+3)}.$$
Decompose the remainder $\frac{-5z - 7}{(z+2)(z+3)} = \frac{A}{z+2} + \frac{B}{z+3}$:
$$A = \lim_{z \to -2} (z+2) \frac{-5z - 7}{(z+2)(z+3)} = \frac{10 - 7}{1} = 3,$$
$$B = \lim_{z \to -3} (z+3) \frac{-5z - 7}{(z+2)(z+3)} = \frac{15 - 7}{-1} = -8.$$
Thus the partial fraction expansion is
$$f(z) = 1 + \frac{3}{z+2} - \frac{8}{z+3}.$$
:::

:::

::: pf-step
Part (a): Laurent series in the annulus $2 < |z| < 3$.

::: pf-proof
For $|z| > 2$, $|2/z| < 1$, so we expand $\frac{3}{z+2}$ in powers of $1/z$:
$$\frac{3}{z+2} = \frac{3}{z} \frac{1}{1 + 2/z} = \frac{3}{z} \sum_{k=0}^\infty \left(-\frac{2}{z}\right)^k = 3 \sum_{k=0}^\infty (-2)^k z^{-k-1} = \sum_{j=1}^\infty 3(-2)^{j-1} z^{-j}.$$
For $|z| < 3$, $|z/3| < 1$, so we expand $-\frac{8}{z+3}$ in positive powers of $z$:
$$-\frac{8}{z+3} = -\frac{8}{3} \frac{1}{1 + z/3} = -\frac{8}{3} \sum_{k=0}^\infty \left(-\frac{z}{3}\right)^k = -8 \sum_{k=0}^\infty \frac{(-1)^k}{3^{k+1}} z^k.$$
Combining the constant term and both series:
$$f(z) = 1 - \frac{8}{3} - 8 \sum_{k=1}^\infty \frac{(-1)^k}{3^{k+1}} z^k + 3 \sum_{j=1}^\infty (-2)^{j-1} z^{-j} = -\frac{5}{3} - 8 \sum_{k=1}^\infty \frac{(-1)^k}{3^{k+1}} z^k + \sum_{j=1}^\infty 3(-2)^{j-1} z^{-j}.$$
:::

:::

::: pf-step
Part (a): Laurent series in the exterior domain $3 < |z| < \infty$.

::: pf-proof
Since $|z| > 3 > 2$, both $|2/z| < 1$ and $|3/z| < 1$, so both fractions are expanded in negative powers of $z$:
$$\frac{3}{z+2} = 3 \sum_{k=0}^\infty (-2)^k z^{-k-1} = \sum_{j=1}^\infty 3(-2)^{j-1} z^{-j},$$
$$-\frac{8}{z+3} = -\frac{8}{z} \frac{1}{1 + 3/z} = -8 \sum_{k=0}^\infty (-3)^k z^{-k-1} = -\sum_{j=1}^\infty 8(-3)^{j-1} z^{-j}.$$
Combining these with the constant 1 gives
$$f(z) = 1 + \sum_{j=1}^\infty \left[ 3(-2)^{j-1} - 8(-3)^{j-1} \right] z^{-j}.$$
:::

:::

::: pf-step
Part (b): Laurent series for $\sin\left(\frac{z}{1-z}\right)$ in $0 < |z-1| < \infty$.

::: pf-proof
Let $w = z - 1$, so $z = 1 + w$ and $1 - z = -w$. The region becomes the punctured plane $0 < |w| < \infty$.
The argument simplifies to
$$\frac{z}{1-z} = \frac{1 + w}{-w} = -1 - \frac{1}{w}.$$
Using the angle addition formula for sine:
$$\sin\left(-1 - \frac{1}{w}\right) = -\sin\left(1 + \frac{1}{w}\right) = -\sin(1)\cos\left(\frac{1}{w}\right) - \cos(1)\sin\left(\frac{1}{w}\right).$$
Substitute the entire Taylor series for cosine and sine evaluated at $1/w$:
$$\cos\left(\frac{1}{w}\right) = \sum_{m=0}^\infty \frac{(-1)^m}{(2m)!} w^{-2m}, \qquad \sin\left(\frac{1}{w}\right) = \sum_{m=0}^\infty \frac{(-1)^m}{(2m+1)!} w^{-(2m+1)}.$$
Substituting $w = z - 1$ gives the Laurent series valid for all $0 < |z-1| < \infty$:
$$\sin\left(\frac{z}{1-z}\right) = -\sin(1) \sum_{m=0}^\infty \frac{(-1)^m}{(2m)!} (z-1)^{-2m} - \cos(1) \sum_{m=0}^\infty \frac{(-1)^m}{(2m+1)!} (z-1)^{-(2m+1)}.$$
:::

:::

::: pf-step
Conclusion:

::: pf-proof
All requested Laurent expansions are completely determined.
:::

:::

:::
:::
