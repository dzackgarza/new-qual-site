---
schema: qual/card@1
id: P-4HP1O
kind: problem
title: Polynomials do not converge uniformly to $1/z$ on $S^1$
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

::: {.solution}

Orient $S^1$ counterclockwise, and suppose polynomials $p_j$ converge uniformly to $1/z$ on $S^1$.

::: pf

::: {.pf-step #integrals}
$\int_{S^1}\frac{dz}{z}=2\pi i$ and $\int_{S^1}p_j(z)\,dz=0$ for every $j$.

::: pf-proof
The first is the direct computation with $z=e^{it}$.
The second is Cauchy's theorem, since $p_j$ is entire.
:::

:::

::: pf-step
This is a contradiction.

::: pf-proof
By the standard estimate,
$$
\abs{\int_{S^1}\frac{dz}{z}-\int_{S^1}p_j(z)\,dz}\leq2\pi\sup_{\abs{z}=1}\abs{\frac1z-p_j(z)}\to0,
$$
while by step [](#integrals){.pf-ref} the left side is $2\pi$ for every $j$.
:::

:::

:::

:::
