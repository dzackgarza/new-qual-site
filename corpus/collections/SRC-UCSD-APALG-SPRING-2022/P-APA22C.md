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

::: problem
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
<1>1. Part (a): Compute the adjoint of $\theta$ with respect to $\langle -, - \rangle_\alpha$:
<2>1. By definition of the adjoint $\theta^{*_\alpha}$ in the inner product space $(V, \langle -, - \rangle_\alpha)$:
\[
\langle \theta(v), w \rangle_\alpha = \langle v, \theta^{*_\alpha}(w) \rangle_\alpha \quad \text{for all } v, w \in V.
\]
Proof: definition of adjoint.
<2>2. Express both sides using the original inner product $\langle -, - \rangle$:
\[
\langle \theta(v), w \rangle_\alpha = \langle \alpha(\theta(v)), w \rangle = \langle \theta(v), \alpha^*(w) \rangle = \langle \theta(v), \alpha(w) \rangle = \langle v, \theta^*(\alpha(w)) \rangle,
\]
since $\alpha$ is self-adjoint ($\alpha^* = \alpha$).
Proof: adjoint property with respect to $\langle -, - \rangle$.
<2>3. The right-hand side is:
\[
\langle v, \theta^{*_\alpha}(w) \rangle_\alpha = \langle \alpha(v), \theta^{*_\alpha}(w) \rangle = \langle v, \alpha^*(\theta^{*_\alpha}(w)) \rangle = \langle v, \alpha(\theta^{*_\alpha}(w)) \rangle.
\]
Proof: $\alpha^* = \alpha$.
<2>4. Equating the two expressions for all $v \in V$:
\[
\alpha(\theta^{*_\alpha}(w)) = \theta^*(\alpha(w)) \implies \theta^{*_\alpha}(w) = \alpha^{-1} \theta^* \alpha(w).
\]
Thus $\theta^{*_\alpha} = \alpha^{-1} \theta^* \alpha$.
Proof: non-degeneracy of inner product and invertibility of $\alpha$.

<1>2. Part (b): Show that $\gamma = \alpha^{-1}\beta$ is self-adjoint with respect to $\langle -, - \rangle_\alpha$:
<2>1. Apply the formula from Part (a) to $\gamma = \alpha^{-1}\beta$:
\[
\gamma^{*_\alpha} = \alpha^{-1} \gamma^* \alpha = \alpha^{-1} (\alpha^{-1}\beta)^* \alpha.
\]
Proof: Part (a).
<2>2. Using $(AB)^* = B^* A^*$ and self-adjointness of $\alpha$ and $\beta$ ($\alpha^* = \alpha, \beta^* = \beta$):
\[
(\alpha^{-1}\beta)^* = \beta^* (\alpha^{-1})^* = \beta (\alpha^*)^{-1} = \beta \alpha^{-1}.
\]
Proof: algebraic properties of adjoints.
<2>3. Substituting into <2>1:
\[
\gamma^{*_\alpha} = \alpha^{-1} (\beta \alpha^{-1}) \alpha = \alpha^{-1} \beta (\alpha^{-1} \alpha) = \alpha^{-1} \beta = \gamma.
\]
Thus $\gamma$ is self-adjoint with respect to $\langle -, - \rangle_\alpha$.
Proof: associative law and $\alpha^{-1}\alpha = I$.

<1>3. Part (c): Construct the simultaneous orthogonal basis:
<2>1. By the Spectral Theorem for self-adjoint operators on the finite-dimensional inner product space $(V, \langle -, - \rangle_\alpha)$, there exists an orthonormal basis $B = \{v_1, \dots, v_n\}$ of eigenvectors of $\gamma$:
\[
\langle v_i, v_j \rangle_\alpha = \delta_{ij} \quad \text{and} \quad \gamma(v_i) = \lambda_i v_i \quad (\lambda_i \in \mathbb{R}).
\]
Proof: Spectral Theorem for self-adjoint operators.
<2>2. Express $\langle v_i, v_j \rangle_\beta$ in terms of $\langle -, - \rangle_\alpha$:
\[
\langle v_i, v_j \rangle_\beta = \langle \beta(v_i), v_j \rangle = \langle \alpha(\alpha^{-1}\beta(v_i)), v_j \rangle = \langle \alpha(\gamma(v_i)), v_j \rangle = \langle \gamma(v_i), v_j \rangle_\alpha.
\]
Proof: definition of $\langle -, - \rangle_\alpha$ and $\gamma = \alpha^{-1}\beta$.
<2>3. Using $\gamma(v_i) = \lambda_i v_i$:
\[
\langle v_i, v_j \rangle_\beta = \langle \lambda_i v_i, v_j \rangle_\alpha = \lambda_i \langle v_i, v_j \rangle_\alpha = \lambda_i \delta_{ij}.
\]
Proof: linearity of inner products.
<2>4. For all $i \neq j$, $\langle v_i, v_j \rangle_\alpha = 0$ and $\langle v_i, v_j \rangle_\beta = 0$.
Thus the basis $B = \{v_1, \dots, v_n\}$ is orthogonal with respect to both $\langle -, - \rangle_\alpha$ and $\langle -, - \rangle_\beta$.
Proof: <2>1 and <2>3.

<1>4. Conclusion:
The basis $B$ simultaneously orthogonalizes both inner products. Q.E.D.
Proof: <1>1, <1>2, and <1>3.
:::
