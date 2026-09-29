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

::: pf

::: pf-step
$f$ has simple poles at each integer $z = k$ and at $z = \pm i a$.

::: pf-proof
$\cot(\pi z)$ has simple poles at the integers, and $z^2 + a^2 = (z - ia)(z + ia)$ gives simple poles at $\pm ia$.
:::

:::

::: {.pf-step #res-integer}
$\operatorname{Res}(f, k) = \frac{1}{k^2 + a^2}$ for each integer $k$.

::: pf-proof
$\pi \cot(\pi z)$ has residue $1$ at $z = k$, so $f$ has residue $\frac{1}{k^2 + a^2}$.
:::

:::

::: {.pf-step #res-ia}
$\operatorname{Res}(f, ia) = \frac{\pi \cot(\pi i a)}{2ia} = -\frac{\pi \coth(\pi a)}{2a}$.

::: pf-proof
$\cot(i\pi a) = -i\coth(\pi a)$, so $\pi \cot(\pi i a) = -i\pi \coth(\pi a)$, and dividing by $2ia$ gives $-\frac{\pi \coth(\pi a)}{2a}$.
:::

:::

::: {.pf-step #res-neg-ia}
$\operatorname{Res}(f, -ia) = \frac{\pi \cot(-\pi i a)}{-2ia} = -\frac{\pi \coth(\pi a)}{2a}$.

::: pf-proof
$\cot(-\pi i a) = i\coth(\pi a)$, so $\pi \cot(-\pi i a) = i\pi \coth(\pi a)$, and dividing by $-2ia$ gives $-\frac{\pi \coth(\pi a)}{2a}$.
:::

:::

::: {.pf-step #residue-theorem-sum}
$\oint_{\gamma_N} f(z)\,dz = 2\pi i \left( \sum_{k=-N}^{N} \frac{1}{k^2 + a^2} - \frac{\pi \coth(\pi a)}{a} \right)$.

::: pf-proof
This is the residue theorem with the residues of steps [](#res-integer){.pf-ref}, [](#res-ia){.pf-ref} and [](#res-neg-ia){.pf-ref}.
:::

:::

::: {.pf-step #integral-vanishes}
$\oint_{\gamma_N} f(z)\,dz \to 0$ as $N \to \infty$.

::: pf-proof
$|\cot(\pi z)|$ is bounded on $\gamma_N$ independently of $N$, and $|z^2 + a^2| \ge (N+\tfrac12)^2-a^2$ there, so $|f(z)| \le C/N^2$ on $\gamma_N$. The perimeter is $O(N)$, so the integral is $O(1/N)$.
:::

:::

::: pf-qed
Letting $N\to\infty$ in step [](#residue-theorem-sum){.pf-ref} and using step [](#integral-vanishes){.pf-ref} gives $\sum_{k \in \ZZ} \frac{1}{k^2 + a^2} = \frac{\pi \coth(\pi a)}{a}$.
:::

:::
:::

