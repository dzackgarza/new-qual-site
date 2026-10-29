---
schema: qual/card@1
id: P-56AFO
kind: problem
title: Integrability of a radial power
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Euclidean Spaces
relations: []
review: draft
---

::: {.problem}
Let $n\geq 1$ and $p\in\RR$. Show that
$$
\begin{aligned}
\int_{\bB^n} {1 \over \abs{x}^p } \dx &< \infty \iff p < n, \\
\int_{\RR^n\sm \bB^n} {1 \over \abs{x}^p } \dx &< \infty \iff p > n.
\end{aligned}
$$
:::

::: {.solution}
Let $\omega_{n-1}$ be the surface measure of the unit sphere.

::: pf

::: {.pf-step #polar}

$\int_{\bB^n}\abs{x}^{-p}\,\dx = \omega_{n-1}\int_0^1 r^{n-1-p}\,\dr$ and $\int_{\RR^n\sm\bB^n}\abs{x}^{-p}\,\dx = \omega_{n-1}\int_1^\infty r^{n-1-p}\,\dr$.

::: pf-proof

This is integration in polar coordinates, $\dx = r^{n-1}\,\dr\,d\sigma$, applied to the radial function $\abs{x}^{-p}$.

:::

:::

::: pf-step

$\int_0^1 r^{n-1-p}\,\dr < \infty$ exactly when $p<n$, and $\int_1^\infty r^{n-1-p}\,\dr < \infty$ exactly when $p>n$.

::: pf-proof

The first is finite exactly when $n-1-p>-1$, and the second exactly when $n-1-p<-1$. At $p=n$ both are $\int r^{-1}\,\dr$ over an interval with endpoint $0$ or $\infty$, and both diverge. With step [](#polar){.pf-ref} this gives both equivalences.

:::

:::

:::

:::
