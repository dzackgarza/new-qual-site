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
\[
\langle v, w \rangle_{\alpha} := \langle \alpha(v), w \rangle,
\qquad
\langle v, w \rangle_{\beta} := \langle \beta(v), w \rangle
\]
to be the two new inner products on $V$ associated with $\alpha$ and $\beta$ respectively.

(a) If $\theta \colon V \to V$ is a linear map, and $\theta^*$ denotes its adjoint with respect to the original inner product $\langle -, - \rangle$ on $V$, prove that the adjoint of $\theta$ with respect to the new inner product $\langle -, - \rangle_{\alpha}$ is given by $\alpha^{-1} \theta^* \alpha$.

(b) Prove that the linear map $\gamma = \alpha^{-1} \beta$ is self-adjoint with respect to the new inner product $\langle -, - \rangle_{\alpha}$.

(c) By applying a spectral theorem to $\langle -, - \rangle_{\alpha}$ and $\gamma$, or otherwise, prove that there exists a basis $B = v_1, \ldots, v_n$ for $V$ that is orthogonal with respect to both $\langle -, - \rangle_{\alpha}$ and $\langle -, - \rangle_{\beta}$.
(That is, $\langle \alpha(v_i), v_j \rangle = \langle \beta(v_i), v_j \rangle = 0$ for $1 \leq i \neq j \leq n$.)
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Part (a): Compute the adjoint of $\theta$ with respect to $\langle -, - \rangle_\alpha$:

::: pf-proof

::: pf-step

By definition of the adjoint $\theta^{*_\alpha}$ in the inner product space $(V, \langle -, - \rangle_\alpha)$:
\[
\langle \theta(v), w \rangle_\alpha = \langle v, \theta^{*_\alpha}(w) \rangle_\alpha \quad \text{for all } v, w \in V.
\]

::: pf-proof

definition of adjoint.

:::

:::

::: pf-step

Express both sides using the original inner product $\langle -, - \rangle$:
\[
\langle \theta(v), w \rangle_\alpha = \langle \alpha(\theta(v)), w \rangle = \langle \theta(v), \alpha^*(w) \rangle = \langle \theta(v), \alpha(w) \rangle = \langle v, \theta^*(\alpha(w)) \rangle,
\]
since $\alpha$ is self-adjoint ($\alpha^* = \alpha$).

::: pf-proof

adjoint property with respect to $\langle -, - \rangle$.

:::

:::

::: pf-step

The right-hand side is:
\[
\langle v, \theta^{*_\alpha}(w) \rangle_\alpha = \langle \alpha(v), \theta^{*_\alpha}(w) \rangle = \langle v, \alpha^*(\theta^{*_\alpha}(w)) \rangle = \langle v, \alpha(\theta^{*_\alpha}(w)) \rangle.
\]

::: pf-proof

$\alpha^* = \alpha$.

:::

:::

::: pf-step

Equating the two expressions for all $v \in V$:
\[
\alpha(\theta^{*_\alpha}(w)) = \theta^*(\alpha(w)) \implies \theta^{*_\alpha}(w) = \alpha^{-1} \theta^* \alpha(w).
\]
Thus $\theta^{*_\alpha} = \alpha^{-1} \theta^* \alpha$.

::: pf-proof

non-degeneracy of inner product and invertibility of $\alpha$.

:::

:::

:::

:::

::: {.pf-step #s2}

Part (b): Show that $\gamma = \alpha^{-1}\beta$ is self-adjoint with respect to $\langle -, - \rangle_\alpha$:

::: pf-proof

::: {.pf-step #s2-1}

Apply the formula from Part (a) to $\gamma = \alpha^{-1}\beta$:
\[
\gamma^{*_\alpha} = \alpha^{-1} \gamma^* \alpha = \alpha^{-1} (\alpha^{-1}\beta)^* \alpha.
\]

::: pf-proof

Part (a).

:::

:::

::: pf-step

Using $(AB)^* = B^* A^*$ and self-adjointness of $\alpha$ and $\beta$ ($\alpha^* = \alpha, \beta^* = \beta$):
\[
(\alpha^{-1}\beta)^* = \beta^* (\alpha^{-1})^* = \beta (\alpha^*)^{-1} = \beta \alpha^{-1}.
\]

::: pf-proof

algebraic properties of adjoints.

:::

:::

::: pf-step

Substituting into step [](#s2-1){.pf-ref}:
\[
\gamma^{*_\alpha} = \alpha^{-1} (\beta \alpha^{-1}) \alpha = \alpha^{-1} \beta (\alpha^{-1} \alpha) = \alpha^{-1} \beta = \gamma.
\]
Thus $\gamma$ is self-adjoint with respect to $\langle -, - \rangle_\alpha$.

::: pf-proof

associative law and $\alpha^{-1}\alpha = I$.

:::

:::

:::

:::

::: {.pf-step #s3}

Part (c): Construct the simultaneous orthogonal basis:

::: pf-proof

::: {.pf-step #s3-1}

By the Spectral Theorem for self-adjoint operators on the finite-dimensional inner product space $(V, \langle -, - \rangle_\alpha)$, there exists an orthonormal basis $B = \{v_1, \dots, v_n\}$ of eigenvectors of $\gamma$:
\[
\langle v_i, v_j \rangle_\alpha = \delta_{ij} \quad \text{and} \quad \gamma(v_i) = \lambda_i v_i \quad (\lambda_i \in \mathbb{R}).
\]

::: pf-proof

Spectral Theorem for self-adjoint operators.

:::

:::

::: pf-step

Express $\langle v_i, v_j \rangle_\beta$ in terms of $\langle -, - \rangle_\alpha$:
\[
\langle v_i, v_j \rangle_\beta = \langle \beta(v_i), v_j \rangle = \langle \alpha(\alpha^{-1}\beta(v_i)), v_j \rangle = \langle \alpha(\gamma(v_i)), v_j \rangle = \langle \gamma(v_i), v_j \rangle_\alpha.
\]

::: pf-proof

definition of $\langle -, - \rangle_\alpha$ and $\gamma = \alpha^{-1}\beta$.

:::

:::

::: {.pf-step #s3-3}

Using $\gamma(v_i) = \lambda_i v_i$:
\[
\langle v_i, v_j \rangle_\beta = \langle \lambda_i v_i, v_j \rangle_\alpha = \lambda_i \langle v_i, v_j \rangle_\alpha = \lambda_i \delta_{ij}.
\]

::: pf-proof

linearity of inner products.

:::

:::

::: pf-step

For all $i \neq j$, $\langle v_i, v_j \rangle_\alpha = 0$ and $\langle v_i, v_j \rangle_\beta = 0$.
Thus the basis $B = \{v_1, \dots, v_n\}$ is orthogonal with respect to both $\langle -, - \rangle_\alpha$ and $\langle -, - \rangle_\beta$.

::: pf-proof

Steps [](#s3-1){.pf-ref} and [](#s3-3){.pf-ref}.

:::

:::

:::

:::

::: pf-step

Conclusion:
The basis $B$ simultaneously orthogonalizes both inner products. Q.E.D.

::: pf-proof

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::

:::
