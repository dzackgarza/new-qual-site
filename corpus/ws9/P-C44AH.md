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
solved: true
---

::: {.problem title="?"}
Let $\mu$ be Lebesgue measure on $\mathbb{D}$.
Let $H$ be the subspace of $L^2(\mathbb{D},\mu)$ consisting of holomorphic functions.
Show that $H$ is complete.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Let $\mu$ be Lebesgue measure on $\DD$ and let $H$ be the subspace of $L^2(\DD, \mu)$ consisting of holomorphic functions.
Show that $H$ is complete.

<1>1. $H$ is a subspace of the Hilbert space $L^2(\DD, \mu)$; it suffices to show $H$ is closed in $L^2$.
Proof: a closed subspace of a complete metric space is complete, and the inner product on $H$ is the restriction of the $L^2$ inner product.

<1>2. Let $(f_n) \subset H$ with $f_n \to f$ in $L^2$; we show $f \in H$ (after modification on a null set).
<2>1. $(f_n)$ is Cauchy in $\sup$ on compacta.
Proof: for any compact $K \subset \DD$, the mean-value estimate gives $\sup_K |f_n - f_m| \le C_K \|f_n - f_m\|_{L^2} \to 0$ as $n, m \to \infty$ (by part (i) of the companion mean-value inequality applied to the holomorphic function $f_n - f_m$). <2>2. $f_n \to g$ locally uniformly for some holomorphic $g$ on $\DD$.
Proof: by <2>1, $(f_n)$ is locally uniformly Cauchy, hence converges locally uniformly on $\DD$; the limit $g$ is holomorphic (locally uniform limit of holomorphic functions).
<2>3. $f = g$ a.e. Proof: $f_n \to f$ in $L^2$ implies $f_n \to f$ in measure along a subsequence, and a.e. along a further subsequence; also $f_n \to g$ pointwise everywhere by <2>2. Hence $f = g$ a.e. <2>4. $f \in H$.
Proof: by <2>2–<2>3, $f$ equals a.e. the holomorphic function $g$, and $\int_\DD |g|^2\, d\mu = \int_\DD |f|^2\, d\mu < \infty$; so the class of $f$ in $L^2$ is represented by the holomorphic function $g$, i.e. $f \in H$.

<1>3. $H$ is complete.
Proof: <1>2 shows $H$ is closed in the complete space $L^2(\DD, \mu)$; by <1>1, $H$ is a Hilbert space.

<1>4. Q.E.D. Proof: <1>1–<1>3 prove the claim.
:::
