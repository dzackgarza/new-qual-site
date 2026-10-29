---
schema: qual/card@1
id: P-APA22C
kind: problem
title: Simultaneous orthogonal basis for two positive definite inner products
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Inner Product Spaces
  - Diagonalization
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $V$ be a finite-dimensional inner product space and $\alpha, \beta \colon V \to V$ two positive definite, self-adjoint linear maps.
Define
$$
\langle v, w \rangle_{\alpha} := \langle \alpha(v), w \rangle,
\qquad
\langle v, w \rangle_{\beta} := \langle \beta(v), w \rangle
$$
to be the two new inner products on $V$ associated with $\alpha$ and $\beta$ respectively.

(a) If $\theta \colon V \to V$ is a linear map, and $\theta^*$ denotes its adjoint with respect to the original inner product $\langle -, - \rangle$ on $V$, prove that the adjoint of $\theta$ with respect to the new inner product $\langle -, - \rangle_{\alpha}$ is given by $\alpha^{-1} \theta^* \alpha$.

(b) Prove that the linear map $\gamma = \alpha^{-1} \beta$ is self-adjoint with respect to the new inner product $\langle -, - \rangle_{\alpha}$.

(c) By applying a spectral theorem to $\langle -, - \rangle_{\alpha}$ and $\gamma$, or otherwise, prove that there exists a basis $B = v_1, \ldots, v_n$ for $V$ that is orthogonal with respect to both $\langle -, - \rangle_{\alpha}$ and $\langle -, - \rangle_{\beta}$.
(That is, $\langle \alpha(v_i), v_j \rangle = \langle \beta(v_i), v_j \rangle = 0$ for $1 \leq i \neq j \leq n$.)
:::

::: {.solution}
Write $\theta^{*_\alpha}$ for the adjoint of $\theta$ with respect to $\langle-,-\rangle_\alpha$. Since $\alpha$ is positive definite, it is invertible.

::: pf

::: {.pf-step #adjoint}

(a) $\theta^{*_\alpha}=\alpha^{-1}\theta^*\alpha$.

::: pf-proof

For all $v,w\in V$, using $\alpha^*=\alpha$,
$$
\langle\theta v,w\rangle_\alpha=\langle\alpha\theta v,w\rangle=\langle\theta v,\alpha w\rangle=\langle v,\theta^*\alpha w\rangle=\langle\alpha v,\alpha^{-1}\theta^*\alpha w\rangle=\langle v,\alpha^{-1}\theta^*\alpha w\rangle_\alpha .
$$
The adjoint is unique because $\langle-,-\rangle_\alpha$ is nondegenerate, so $\theta^{*_\alpha}=\alpha^{-1}\theta^*\alpha$.

:::

:::

::: {.pf-step #self-adjoint}

(b) $\gamma=\alpha^{-1}\beta$ is self-adjoint with respect to $\langle-,-\rangle_\alpha$.

::: pf-proof

By step [](#adjoint){.pf-ref}, $\gamma^{*_\alpha}=\alpha^{-1}(\alpha^{-1}\beta)^*\alpha$. Since $\alpha$ and $\beta$ are self-adjoint, $(\alpha^{-1}\beta)^*=\beta^*(\alpha^{-1})^*=\beta\alpha^{-1}$, so $\gamma^{*_\alpha}=\alpha^{-1}\beta\alpha^{-1}\alpha=\gamma$.

:::

:::

::: pf-step

(c) There is a basis $v_1,\ldots,v_n$ of $V$ orthogonal for both $\langle-,-\rangle_\alpha$ and $\langle-,-\rangle_\beta$.

::: pf-proof

By step [](#self-adjoint){.pf-ref} and the spectral theorem for the inner product space $(V,\langle-,-\rangle_\alpha)$, there is a $\langle-,-\rangle_\alpha$-orthonormal basis $v_1,\ldots,v_n$ with $\gamma v_i=\lambda_iv_i$. Since $\beta=\alpha\gamma$,
$$
\langle v_i,v_j\rangle_\beta=\langle\alpha\gamma v_i,v_j\rangle=\langle\gamma v_i,v_j\rangle_\alpha=\lambda_i\langle v_i,v_j\rangle_\alpha=\lambda_i\delta_{ij},
$$
which vanishes for $i\ne j$.

:::

:::

:::
:::
