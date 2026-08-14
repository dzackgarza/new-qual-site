---
schema: qual/card@1
id: P-MNWYL
kind: problem
title: "Prove that there is no sequence of polynomials that uniformly converge\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - uniform-convergence
  - cauchy-integral-formula
  - polynomials
  - counterexamples
relations: []
review: draft
---
Prove that there is no sequence of polynomials that uniformly converge to $f(z) = {1\over z}$ on $S^1$.


:::{.concept}
\envlist

- Uniform limit of holomorphic function is holomorphic

:::

:::{.solution}

- By Cauchy's integral formula, $\int_{S^1} f = 2\pi i$
- If $p_j$ is any polynomial, then $p_j$ is holomorphic in $\DD$, so $\int_{S^1} p_j = 0$.
- Contradiction: compact sets in $\CC$ are bounded, so 
  \[
  \abs{\int f - \int p_j} \leq \int \abs{p_j - f} \leq \int \norm{p_j - f}_\infty  = \norm{p_j - f}_\infty \int_{S^1} 1 \,dz = \norm{p_j-f}_\infty \cdot 2\pi \to 0
  \]
  which forces $\int f = \int p_j = 0$.
:::

