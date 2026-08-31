---
schema: qual/card@1
id: P-CAF13I
kind: problem
title: "Harmonic function on the disk with prescribed boundary values and non-existence of holomorphic extension"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
(a) Does there exist a harmonic function $u$ on $\mathbb{D}$, continuous on $\overline{\mathbb{D}}$, so that $u(e^{i\theta}) = \cos^2\theta$ for $\theta \in [0, 2\pi)$?
If not, prove it.
If so, what is the value $u(0)$?

(b) Prove that there is no holomorphic function $f$ on $\mathbb{D}$, continuous on $\overline{\mathbb{D}}$, so that $f(e^{i\theta}) = e^{-i\theta}$ for $\theta \in [0, 2\pi)$.
:::

::: {.solution}
**Goal.** (a) Find a harmonic function with boundary values $\cos^2\theta$ and compute $u(0)$. (b) Show no holomorphic $f$ has boundary values $e^{-i\theta}$.

<1>1. (a) Such a harmonic function exists, and $u(0) = 1/2$.
<2>1. $\cos^2\theta = \frac{1 + \cos 2\theta}{2}$.
::: {.proof}
the double-angle identity.
:::
<2>2. The harmonic function with boundary value $\cos^2\theta$ is $u(re^{i\theta}) = \frac{1}{2} + \frac{1}{2} r^2 \cos 2\theta$.
::: {.proof}
the Poisson integral of $\cos^2\theta$; the term $\frac12$ is constant (harmonic), and $\frac12 \cos 2\theta$ extends to $\frac12 r^2 \cos 2\theta = \frac12 \Re(z^2)$ (harmonic).
:::
<2>3. $u(0) = \frac12$.
::: {.proof}
evaluate at $r = 0$: $u(0) = \frac12 + 0 = \frac12$ (equivalently, the mean value property gives $u(0) = \frac{1}{2\pi}\int_0^{2\pi}\cos^2\theta\,d\theta = \frac12$).
:::

<1>2. (b) No holomorphic $f$ has boundary values $e^{-i\theta}$.
<2>1. Suppose such $f$ exists.
::: {.proof}
assume for contradiction.
:::
<2>2. Then $\int_{|z|=1} f(z)\,dz = \int_0^{2\pi} f(e^{i\theta}) i e^{i\theta}\,d\theta = \int_0^{2\pi} e^{-i\theta} i e^{i\theta}\,d\theta = \int_0^{2\pi} i\,d\theta = 2\pi i$.
::: {.proof}
parametrize the unit circle and use the boundary values.
:::
<2>3. But $\int_{|z|=1} f(z)\,dz = 0$ by Cauchy's theorem (since $f$ is holomorphic on $\DD$ and continuous on $\overline{\DD}$).
::: {.proof}
Cauchy's integral theorem.
:::
<2>4. Contradiction: $2\pi i \neq 0$.
::: {.proof}
<1>2.2 and <1>2.3.
:::

<1>3. Q.E.D.
::: {.proof}
<1>1 answers (a); <1>2 proves (b).
:::
:::
