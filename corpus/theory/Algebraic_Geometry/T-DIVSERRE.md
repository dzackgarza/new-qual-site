---
schema: qual/card@1
id: T-DIVSERRE
kind: theorem
title: Serre's criterion for ampleness
slogan: 'Ample means eventual positivity: high twists globally generate every coherent sheaf, and on proper schemes they kill all higher cohomology.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ample Divisors
  - Globally Generated Sheaves
  - Cohomological Criteria
relations:
- kind: uses
  target: D-DIVAMPLE
review: draft
prompts:
- State Serre's global-generation criterion for an invertible sheaf to be ample.
- What is the cohomological characterisation of ampleness?
---

::: {.theorem}
Let $X$ be a scheme of finite type over a Noetherian ring $A$ and $\mcl$ invertible.
The following are equivalent:

- $\mcl$ is ample;

- for every coherent $\mcf$ there is $n_0$ with $\mcf \tensor \mcl\tensorpower{}{n}$ globally generated for all $n \geq n_0$.

If $X$ is proper over $A$, both are equivalent to: for every coherent $\mcf$ there is $n_0$ with $H^i(X, \mcf \tensor \mcl\tensorpower{}{n}) = 0$ for all $i > 0$ and all $n \geq n_0$ [@Har77, III.5.3].
:::

::: {.remark}
This criterion expresses ampleness as eventual global generation and, in the proper case, eventual vanishing of higher cohomology.

If $X\hookrightarrow\PP_A^N$ is a projective embedding, then the associated twisting sheaf $\OO_X(1)$ is very ample and hence ample; the cohomological implication for its powers is Serre vanishing.

Numerical criteria for ampleness, such as the Nakai--Moishezon criterion in its appropriate hypotheses, are separate results; the theorem above is the sheaf-theoretic criterion.
:::
