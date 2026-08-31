---
schema: qual/card@1
id: E-HAT-3.3-21
kind: exercise
title: "Compactly supported cohomology and one-point compactification"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

For a space $X$, let $X^+$ be the one-point compactification.
If the added point, denoted $\infty$, has a neighborhood in $X^+$ that is a cone with $\infty$ the cone point, show that the evident map $H_c^n(X; G) \to H^n(X^+, \infty; G)$ is an isomorphism for all $n$.

::: {.solution}
<1>1. $H_c^n(X; G) = \varinjlim_K H^n(X, X - K; G)$, the direct limit over compact subsets $K \subseteq X$.
::: {.proof}
definition of compactly supported cohomology.
:::

<1>2. $H^n(X^+, \infty; G) \cong H^n(X^+, X^+ - U; G)$ for any neighborhood $U$ of $\infty$ (by excision).
::: {.proof}
excision (removing the complement of a neighborhood of $\infty$).
:::

<1>3. The neighborhoods $U$ of $\infty$ correspond to complements of compact sets $K \subseteq X$ (since $X^+$ is the one-point compactification).
::: {.proof}
a neighborhood of $\infty$ is the complement of a compact set in $X$.
:::

<1>4. Hence $H^n(X^+, \infty; G) \cong \varinjlim_K H^n(X^+, X^+ - K; G) \cong \varinjlim_K H^n(X, X - K; G)$.
::: {.proof}
<1>2 and <1>3 (the direct limit over neighborhoods of $\infty$ is the direct limit over compact $K$).
:::

<1>5. The cone condition ensures the direct limit is well-behaved (the map from the direct limit to $H^n(X^+, \infty)$ is an isomorphism).
::: {.proof}
<1>4 and the hypothesis (the cone neighborhood of $\infty$ makes the direct limit stabilize).
:::

<1>6. Hence $H_c^n(X; G) \cong H^n(X^+, \infty; G)$.
::: {.proof}
<1>1 and <1>4.
:::

<1>7. Q.E.D.
::: {.proof}
<1>6.
:::
:::
