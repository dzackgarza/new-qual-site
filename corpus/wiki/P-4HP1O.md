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
solved: true
---

::: {.problem title="?"}
Prove that there is no sequence of polynomials that uniformly converge to $f(z) = {1\over z}$ on $S^1$.
:::

::: {.solution}

- By Cauchy's integral formula, $\int_{S^1} f = 2\pi i$

- If $p_j$ is any polynomial, then $p_j$ is holomorphic in $\DD$, so $\int_{S^1} p_j = 0$.

- Contradiction: compact sets in $\CC$ are bounded, so
  \[
  \abs{\int f - \int p_j} 
  &\leq \int \abs{p_j - f} \\
  &\leq \int \norm{p_j - f}_\infty  \\
  &= \norm{p_j - f}_\infty \int_{S^1} 1 \,dz \\
  &= \norm{p_j-f}_\infty \cdot 2\pi \\
  &\to 0
  \]
  which forces $\int f = \int p_j = 0$.
:::
