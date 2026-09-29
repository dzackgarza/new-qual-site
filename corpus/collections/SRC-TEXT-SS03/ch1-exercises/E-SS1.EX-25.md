---
schema: qual/card@1
id: E-SS1.EX-25
kind: problem
title: Integrals of $z^n$ and $1/((z-a)(z-b))$ over circles
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Numbers
  - Power Series
  - Cauchy-Riemann
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-09-28
  note: Restored part (c), which the source prints after a page break and the card had dropped; text from the Stein-Shakarchi extraction in Zotero.
---

::: {.exercise}
25. The next three calculations provide some insight into Cauchy’s theorem, which we treat in the next chapter.

(a) Evaluate the integrals

$$
\int_ {\gamma} z ^ {n} d z
$$

for all integers $n .$ . Here $\gamma$ is any circle centered at the origin with the positive (counterclockwise) orientation.

(b) Same question as before, but with $\gamma$ any circle not containing the origin.

(c) Show that if $\vert a \vert < r < \vert b \vert$ , then

$$
\int_ {\gamma} \frac {1}{(z - a) (z - b)} d z = \frac {2 \pi i}{a - b},
$$

where $\gamma$ denotes the circle centered at the origin, of radius $r ,$ with the positive orientation.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

(a) If $\gamma$ is the positively oriented circle of radius $R$ centered at $0$, then $\int_\gamma z^n\,dz = \boxed{0}$ for $n \neq -1$ and $\int_\gamma z^{-1}\,dz=\boxed{2\pi i}$.

::: pf-proof

Parametrize $\gamma$ by $z = R e^{i\theta}$, $0 \le \theta \le 2\pi$, so $dz = i R e^{i\theta}\,d\theta$ and
$$\int_\gamma z^n\,dz = i R^{n+1} \int_0^{2\pi} e^{i(n+1)\theta}\,d\theta.$$
If $n \neq -1$, the integrand has the $2\pi$-periodic antiderivative $e^{i(n+1)\theta}/(i(n+1))$, so the integral is $0$. If $n = -1$, the integrand is $1$, and the integral is $iR^0\cdot 2\pi = 2\pi i$.

:::

:::

::: pf-step

(b) If the origin lies outside the closed disc bounded by $\gamma$, then $\int_\gamma z^n\,dz = \boxed{0}$ for every integer $n$.

::: pf-proof

The closed disc bounded by $\gamma$ is a compact set not containing $0$, so it lies in a slightly larger open disc $D$ with $0\notin D$. The function $z^n$ is holomorphic on $D$ for every integer $n$, and Cauchy's theorem in the disc $D$ gives $\int_\gamma z^n\,dz=0$.

:::

:::

::: pf-step

(c) If $\abs a<r<\abs b$ and $\gamma$ is the positively oriented circle $\abs z=r$, then $\int_\gamma\frac{dz}{(z-a)(z-b)}=\frac{2\pi i}{a-b}$.

::: pf-proof

Partial fractions give $\frac{1}{(z-a)(z-b)}=\frac{1}{a-b}\qty{\frac{1}{z-a}-\frac{1}{z-b}}$. On $\gamma$, $\abs{a/z}=\abs a/r<1$ and $\abs{z/b}=r/\abs b<1$, so the geometric series
$$\frac{1}{z-a}=\sum_{k\ge0}\frac{a^k}{z^{k+1}},\qquad \frac{1}{z-b}=-\sum_{k\ge0}\frac{z^k}{b^{k+1}}$$
converge uniformly on $\gamma$ and may be integrated term by term. By step [](#s1){.pf-ref}, only the term $a^0z^{-1}$ has a nonzero integral, namely $2\pi i$, so $\int_\gamma\frac{dz}{z-a}=2\pi i$ and $\int_\gamma\frac{dz}{z-b}=0$. Hence the integral is $\frac{2\pi i}{a-b}$.

:::

:::

:::

:::
