---
schema: qual/card@1
id: P-MNWYL
kind: problem
title: Polynomials cannot converge uniformly to $1/z$ on $S^1$
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Cauchy Integral Formula
  - Polynomials
  - Counterexamples
relations: []
review: draft
---

::: {.problem}
Prove that there is no sequence of polynomials that uniformly converge to $f(z) = {1\over z}$ on $S^1$.
:::

::: {.hint}
Integrals over $S^1$ pass to uniform limits; compare $\int_{S^1}p\,dz$ with $\int_{S^1}\frac{dz}{z}$.
:::

::: {.solution}
Suppose polynomials $p_j$ converge uniformly to $f$ on $S^1$.

::: pf

::: {.pf-step #integral-f}
$\int_{S^1}f(z)\,dz=2\pi i$ and $\int_{S^1}p_j(z)\,dz=0$ for every $j$.

::: pf-proof
The first is the direct computation with $z=e^{i\theta}$. Each $p_j$ is entire, so its integral over a closed curve vanishes by Cauchy's theorem.
:::

:::

::: pf-step
This is a contradiction.

::: pf-proof
By step [](#integral-f){.pf-ref},
$$
2\pi=\abs{\int_{S^1}\bigl(f(z)-p_j(z)\bigr)\,dz}\le 2\pi\sup_{\abs{z}=1}\abs{f(z)-p_j(z)},
$$
and the right side tends to $0$ as $j\to\infty$.
:::

:::

:::
:::
