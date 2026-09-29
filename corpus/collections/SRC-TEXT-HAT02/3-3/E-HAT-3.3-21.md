---
schema: qual/card@1
id: E-HAT-3.3-21
kind: problem
title: Compactly supported cohomology and one-point compactification
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
For a space $X$, let $X^+$ be the one-point compactification.
If the added point, denoted $\infty$, has a neighborhood in $X^+$ that is a cone with $\infty$ the cone point, show that the evident map $H_c^n(X; G) \to H^n(X^+, \infty; G)$ is an isomorphism for all $n$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

$H_c^n(X; G) = \varinjlim_K H^n(X, X - K; G)$, the direct limit over compact subsets $K \subseteq X$.

::: pf-proof

definition of compactly supported cohomology.

:::

:::

::: {.pf-step #s2}

$H^n(X^+, \infty; G) \cong H^n(X^+, X^+ - U; G)$ for any neighborhood $U$ of $\infty$ (by excision).

::: pf-proof

excision (removing the complement of a neighborhood of $\infty$).

:::

:::

::: {.pf-step #s3}

The neighborhoods $U$ of $\infty$ correspond to complements of compact sets $K \subseteq X$ (since $X^+$ is the one-point compactification).

::: pf-proof

a neighborhood of $\infty$ is the complement of a compact set in $X$.

:::

:::

::: {.pf-step #s4}

Hence $H^n(X^+, \infty; G) \cong \varinjlim_K H^n(X^+, X^+ - K; G) \cong \varinjlim_K H^n(X, X - K; G)$.

::: pf-proof

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} (the direct limit over neighborhoods of $\infty$ is the direct limit over compact $K$).

:::

:::

::: pf-step

The cone condition ensures the direct limit is well-behaved (the map from the direct limit to $H^n(X^+, \infty)$ is an isomorphism).

::: pf-proof

Step [](#s4){.pf-ref} and the hypothesis (the cone neighborhood of $\infty$ makes the direct limit stabilize).

:::

:::

::: {.pf-step #s6}

Hence $H_c^n(X; G) \cong H^n(X^+, \infty; G)$.

::: pf-proof

Steps [](#s1){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref}.

:::

:::

:::
