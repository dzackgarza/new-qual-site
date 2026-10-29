---
schema: qual/card@1
id: P-HXOC6
kind: problem
title: Witt's cancellation and extension theorems for quadratic forms
classification:
  areas:
  - algebra
  topics:
  - Quadratic Forms
  - Bilinear Forms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
State and explain Witt's Cancellation Theorem and Witt's Extension Theorem for quadratic forms (over $\RR$ and general fields).
:::

::: {.solution}
Throughout, $k$ is a field of characteristic different from $2$, and quadratic spaces are finite-dimensional and nondegenerate unless a subspace is said otherwise.
Write $O(V,q)$ for the isometry group of a quadratic space $(V,q)$.

::: pf

::: {.pf-step #extension}
(Witt extension theorem.) Let $(V,q)$ be a nondegenerate quadratic space and let $U,U'\subseteq V$ be subspaces, possibly degenerate. Every isometry $f\colon U\xrightarrow{\sim}U'$ extends to an isometry $\widetilde f\in O(V,q)$.

::: pf-proof
This is a standard theorem; its usual proof is by induction on $\dim U$, extending the isometry one vector at a time by reflections in anisotropic vectors and, for isotropic vectors, by hyperbolic pairs.
:::

:::

::: pf-step
(Witt cancellation theorem.) If $U_1\cong U_2$ and $U_1\perp W_1\cong U_2\perp W_2$, then $W_1\cong W_2$. In particular, $U\perp W_1\cong U\perp W_2$ implies $W_1\cong W_2$.

::: pf-proof
Let $\varphi\colon U_1\perp W_1\to U_2\perp W_2$ be an isometry, and regard both $U_1$ and $\varphi^{-1}(U_2)$ as subspaces of $V=U_1\perp W_1$.
The isometry $\varphi^{-1}\circ g\colon U_1\to\varphi^{-1}(U_2)$, where $g\colon U_1\to U_2$ is the given isometry, extends by step [](#extension){.pf-ref} to some $\sigma\in O(V,q)$.
Then $\varphi\circ\sigma$ is an isometry $V\to U_2\perp W_2$ carrying $U_1$ onto $U_2$, so it carries $U_1^\perp=W_1$ onto $U_2^\perp=W_2$.
:::

:::

::: pf-step
Over $\RR$, every nondegenerate quadratic form is isometric to $x_1^2+\cdots+x_p^2-y_1^2-\cdots-y_q^2$, and the signature $(p,q)$ is a complete isometry invariant.

::: pf-proof
This is Sylvester's law of inertia. Signature is additive under orthogonal direct sum, so over $\RR$ cancellation also follows by subtracting the signature of $U$.
:::

:::

:::

:::
