---
schema: qual/card@1
id: P-APA22C
kind: problem
title: Simultaneous orthogonal basis for two positive definite inner products
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
solved: false
---

::: problem
Let $V$ be a finite-dimensional inner product space and $\alpha, \beta \colon V \to V$ two positive definite, self-adjoint linear maps. Define
\[
\langle v, w \rangle_{\alpha} := \langle \alpha(v), w \rangle,
\qquad
\langle v, w \rangle_{\beta} := \langle \beta(v), w \rangle
\]
to be the two new inner products on $V$ associated with $\alpha$ and $\beta$ respectively.

(a) If $\theta \colon V \to V$ is a linear map, and $\theta^*$ denotes its adjoint with respect to the original inner product $\langle -, - \rangle$ on $V$, prove that the adjoint of $\theta$ with respect to the new inner product $\langle -, - \rangle_{\alpha}$ is given by $\alpha^{-1} \theta^* \alpha$.

(b) Prove that the linear map $\gamma = \alpha^{-1} \beta$ is self-adjoint with respect to the new inner product $\langle -, - \rangle_{\alpha}$.

(c) By applying a spectral theorem to $\langle -, - \rangle_{\alpha}$ and $\gamma$, or otherwise, prove that there exists a basis $B = v_1, \ldots, v_n$ for $V$ that is orthogonal with respect to both $\langle -, - \rangle_{\alpha}$ and $\langle -, - \rangle_{\beta}$. (That is, $\langle \alpha(v_i), v_j \rangle = \langle \beta(v_i), v_j \rangle = 0$ for $1 \leq i \neq j \leq n$.)
:::
