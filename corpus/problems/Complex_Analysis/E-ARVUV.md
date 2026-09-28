---
schema: qual/card@1
id: E-ARVUV
kind: problem
title: $\sum_{k\in\ZZ}\frac{1}{k^2+a^2}=\frac{\pi\coth(\pi a)}{a}$ for $a>0$
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

::: {.exercise}
Show that
\[
\sum_{k\in \ZZ} {1\over k^2 + a^2} = {\pi \coth(\pi a) \over a} \qquad\text{for } a>0
.\]

:::

::: {.solution}
Let $f(z) = \frac{\pi \cot(\pi z)}{z^2 + a^2}$, and for $N>a$ let $\gamma_N$ be the positively oriented square with vertices $(\pm (N + \tfrac12), \pm (N + \tfrac12))$. It encloses the poles $-N, \ldots, N$ and $\pm ia$.

<1>1. $f$ has simple poles at each integer $z = k$ and at $z = \pm i a$.

::: {.proof}
$\cot(\pi z)$ has simple poles at the integers, and $z^2 + a^2 = (z - ia)(z + ia)$ gives simple poles at $\pm ia$.
:::

<1>2. $\operatorname{Res}(f, k) = \frac{1}{k^2 + a^2}$ for each integer $k$.

::: {.proof}
$\pi \cot(\pi z)$ has residue $1$ at $z = k$, so $f$ has residue $\frac{1}{k^2 + a^2}$.
:::

<1>3. $\operatorname{Res}(f, ia) = \frac{\pi \cot(\pi i a)}{2ia} = -\frac{\pi \coth(\pi a)}{2a}$.

::: {.proof}
$\cot(i\pi a) = -i\coth(\pi a)$, so $\pi \cot(\pi i a) = -i\pi \coth(\pi a)$, and dividing by $2ia$ gives $-\frac{\pi \coth(\pi a)}{2a}$.
:::

<1>4. $\operatorname{Res}(f, -ia) = \frac{\pi \cot(-\pi i a)}{-2ia} = -\frac{\pi \coth(\pi a)}{2a}$.

::: {.proof}
$\cot(-\pi i a) = i\coth(\pi a)$, so $\pi \cot(-\pi i a) = i\pi \coth(\pi a)$, and dividing by $-2ia$ gives $-\frac{\pi \coth(\pi a)}{2a}$.
:::

<1>5. $\oint_{\gamma_N} f(z)\,dz = 2\pi i \left( \sum_{k=-N}^{N} \frac{1}{k^2 + a^2} - \frac{\pi \coth(\pi a)}{a} \right)$.

::: {.proof}
This is the residue theorem with the residues of steps <1>2 to <1>4.
:::

<1>6. $\oint_{\gamma_N} f(z)\,dz \to 0$ as $N \to \infty$.

::: {.proof}
$|\cot(\pi z)|$ is bounded on $\gamma_N$ independently of $N$, and $|z^2 + a^2| \ge (N+\tfrac12)^2-a^2$ there, so $|f(z)| \le C/N^2$ on $\gamma_N$. The perimeter is $O(N)$, so the integral is $O(1/N)$.
:::

<1>7. Q.E.D.

::: {.proof}
Letting $N\to\infty$ in step <1>5 and using step <1>6 gives $\sum_{k \in \ZZ} \frac{1}{k^2 + a^2} = \frac{\pi \coth(\pi a)}{a}$.
:::
:::

