---
schema: qual/card@1
id: P-C44AH
kind: problem
title: The subspace of holomorphic functions in $L^2(\mathbb{D})$ is complete
classification:
  areas:
  - real-analysis
  topics:
  - Holomorphic Functions
  - L²
  - Completeness
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $\mu$ be Lebesgue measure on $\mathbb{D}$.
Let $H$ be the subspace of $L^2(\mathbb{D},\mu)$ consisting of holomorphic functions.
Show that $H$ is complete.
:::

::: {.solution}
**Goal:** Let $\mu$ be Lebesgue measure on $\DD$ and let $H$ be the subspace of $L^2(\DD, \mu)$ consisting of holomorphic functions.
Show that $H$ is complete.

::: pf

::: {.pf-step #s1}
$H$ is a subspace of the Hilbert space $L^2(\DD, \mu)$; it suffices to show $H$ is closed in $L^2$.

::: pf-proof
a closed subspace of a complete metric space is complete, and the inner product on $H$ is the restriction of the $L^2$ inner product.
:::

:::

::: {.pf-step #s2}
Let $(f_n) \subset H$ with $f_n \to f$ in $L^2$; we show $f \in H$ (after modification on a null set).

::: pf-proof

::: {.pf-step #s2-1}
$(f_n)$ is Cauchy in $\sup$ on compacta.

::: pf-proof
for any compact $K \subset \DD$, the mean-value estimate gives $\sup_K |f_n - f_m| \le C_K \|f_n - f_m\|_{L^2} \to 0$ as $n, m \to \infty$ (by part (i) of the companion mean-value inequality applied to the holomorphic function $f_n - f_m$).
:::

:::

::: {.pf-step #s2-2}
$f_n \to g$ locally uniformly for some holomorphic $g$ on $\DD$.

::: pf-proof
by step [](#s2-1){.pf-ref}, $(f_n)$ is locally uniformly Cauchy, hence converges locally uniformly on $\DD$; the limit $g$ is holomorphic (locally uniform limit of holomorphic functions).
:::

:::

::: {.pf-step #s2-3}
$f = g$ a.e.

::: pf-proof
$f_n \to f$ in $L^2$ implies $f_n \to f$ in measure along a subsequence, and a.e. along a further subsequence; also $f_n \to g$ pointwise everywhere by step [](#s2-2){.pf-ref}. Hence $f = g$ a.e.
:::

:::

::: pf-step
$f \in H$.

::: pf-proof
by step [](#s2-2){.pf-ref} and step [](#s2-3){.pf-ref}, $f$ equals a.e. the holomorphic function $g$, and $\int_\DD |g|^2\, d\mu = \int_\DD |f|^2\, d\mu < \infty$; so the class of $f$ in $L^2$ is represented by the holomorphic function $g$, i.e. $f \in H$.
:::

:::

:::

:::

::: {.pf-step #s3}
$H$ is complete.

::: pf-proof
Step [](#s2){.pf-ref} shows $H$ is closed in the complete space $L^2(\DD, \mu)$; by step [](#s1){.pf-ref}, $H$ is a Hilbert space.
:::

:::

::: pf-qed
Step [](#s1){.pf-ref}, step [](#s2){.pf-ref}, and step [](#s3){.pf-ref} prove the claim.
:::

:::
:::
