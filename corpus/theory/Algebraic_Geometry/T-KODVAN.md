---
schema: qual/card@1
id: T-KODVAN
kind: theorem
title: Kodaira vanishing
classification:
  areas:
  - algebraic-geometry
  topics:
  - Vanishing Theorems
  - Ample Line Bundles
  - Sheaf Cohomology
relations:
- kind: related-to
  target: T-COHSD
review: draft
prompts:
- What is Kodaira vanishing?
---

::: {.theorem title="Kodaira vanishing"}
Let $X$ be a smooth projective variety of dimension $n$ over a field of characteristic zero, and let $L$ be an ample line bundle on $X$.
Then
\[
H^i(X, \omega_X \otimes L) = 0 \quad \text{for } i > 0 .
\]
Equivalently, by Serre duality, $H^i(X, L^{-1}) = 0$ for $i < n$.
:::

::: {.example}
On a smooth projective curve of genus $g$, an ample line bundle is one of positive degree, and $H^1(C, \omega_C \otimes L) \cong H^0(C, L^{-1})^\dual = 0$ because $L^{-1}$ has negative degree.
On $\PP^n$, with $\omega = \OO(-n-1)$ and $L = \OO(m)$ for $m > 0$, the theorem says $H^i(\PP^n, \OO(m-n-1)) = 0$ for $i > 0$, which agrees with the Čech computation of the cohomology of projective space.
:::

::: {.remark}
The characteristic-zero hypothesis is necessary: Raynaud constructed smooth projective surfaces in characteristic $p$ with an ample line bundle $L$ and $H^1(X, L^{-1}) \neq 0$.
:::
