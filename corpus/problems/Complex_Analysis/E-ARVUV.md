---
schema: qual/card@1
id: E-ARVUV
kind: exercise
title: 'Sum formulas: $1/n^2+a^2$'
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Series of Numbers
  - Hyperbolic Functions
  - Meromorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

:::{.exercise}
Show that
\[
\sum_{k\in \ZZ} {1\over k^2 + a^2} = {\pi \coth(\pi a) \over a} \qquad\text{for } a>0
.\]

:::

::: {.solution}
<1>1. Let $f(z) = \frac{\pi \cot(\pi z)}{z^2 + a^2}$.
Proof: definition.

<1>2. $f$ has simple poles at each integer $z = k$ and at $z = \pm i a$.
Proof: $\cot(\pi z)$ has simple poles at the integers, and $z^2 + a^2 = (z - ia)(z + ia)$ gives simple poles at $\pm ia$.

<1>3. $\operatorname{Res}(f, k) = \frac{1}{k^2 + a^2}$ for each integer $k$.
Proof: $\pi \cot(\pi z)$ has residue $1$ at $z = k$, so $f$ has residue $\frac{1}{k^2 + a^2}$.

<1>4. $\operatorname{Res}(f, ia) = \frac{\pi \cot(\pi i a)}{2ia} = -\frac{\pi \coth(\pi a)}{2a}$.
Proof: $\cot(i\pi a) = -i\coth(\pi a)$, so $\pi \cot(\pi i a) = -i\pi \coth(\pi a)$, and dividing by $2ia$ gives $-\frac{\pi \coth(\pi a)}{2a}$.

<1>5. $\operatorname{Res}(f, -ia) = \frac{\pi \cot(-\pi i a)}{-2ia} = -\frac{\pi \coth(\pi a)}{2a}$.
Proof: symmetric computation; $\cot(-\pi i a) = i\coth(\pi a)$, so $\pi \cot(-\pi i a) = i\pi \coth(\pi a)$, and dividing by $-2ia$ gives $-\frac{\pi \coth(\pi a)}{2a}$.

<1>6. Let $\gamma_N$ be the rectangle with vertices $(\pm (N + \tfrac12), \pm (N + \tfrac12))$, enclosing the poles $-N, \ldots, N$ and $\pm ia$ (for $N$ large).
Proof: choose a contour.

<1>7. $\oint_{\gamma_N} f(z)\,dz = 2\pi i \left( \sum_{k=-N}^{N} \frac{1}{k^2 + a^2} - \frac{\pi \coth(\pi a)}{a} \right)$.
Proof: residue theorem, using <1>3–<1>5.

<1>8. $\oint_{\gamma_N} f(z)\,dz \to 0$ as $N \to \infty$.
Proof: $|\cot(\pi z)|$ is bounded on $\gamma_N$, and $|f(z)| \le C/N^2$ on the contour (since $|z^2 + a^2| \sim N^2$), while the perimeter is $O(N)$, so the integral is $O(1/N)$.

<1>9. Hence $0 = \sum_{k=-\infty}^{\infty} \frac{1}{k^2 + a^2} - \frac{\pi \coth(\pi a)}{a}$.
Proof: <1>7 and <1>8, taking the limit.

<1>10. Therefore $\sum_{k \in \ZZ} \frac{1}{k^2 + a^2} = \frac{\pi \coth(\pi a)}{a}$.
Proof: <1>9.

<1>11. Q.E.D.
Proof: <1>10.
:::

