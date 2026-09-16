---
schema: qual/card@1
id: P-TOPS22D
kind: problem
title: "True or False: ten statements in algebraic topology"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cohomology
  - Covering Spaces
  - Manifolds
  - Projective Spaces
  - Homotopy Groups
  - Surfaces
relations: []
review: draft
---

::: {.problem}
Write down "True" or "False" for each of the following statements.
No justification needed.

(a) For any CW complex $X$, $H_*(X)$ is a finitely generated abelian group.

(b) There exist two connected simply connected CW complexes $X$ and $Y$ such that they have isomorphic homotopy groups but non-isomorphic homology groups.

(c) Denote by $\Sigma_g$ the orientable surface with genus $g$.
Then $\Sigma_n$ is a covering space of $\Sigma_2$ for all $n \geq 3$.

(d) Let $M$ be a connected closed $n$-dimensional manifold.
Then $H_{n-1}(M; \mathbb{Z})$ is free.

(e) Let $R$ be a PID, and $M, N$ be $R$-modules.
Then $\operatorname{Ext}^n_R(M, N) = 0$ for $n \geq 1$.

(f) As a ring, $H^*(\mathbb{CP}^n; \mathbb{Z}) = \mathbb{Z}[\alpha]/(\alpha^{n+1})$, where $\alpha$ has degree $2$.

(g) The Klein bottle and the torus are covering spaces of each other.

(h) For positive $n$ and $m$, $\mathbb{RP}^n \times \mathbb{RP}^m$ is orientable if and only if $n \cdot m$ is odd.

(i) For any CW structure of $\mathbb{RP}^n$, there is at least one cell in each dimension $i$ for $0 \leq i \leq n$.

(j) For any spaces $X$ and $Y$ and any field $k$, we have an isomorphism of rings: $H^*(X \times Y; k) \cong H^*(X; k) \otimes_k H^*(Y; k)$.
:::

::: {.solution}
<1>1. The answers are
$$\boxed{\text{(a) F, (b) T, (c) T, (d) F, (e) F, (f) T, (g) F, (h) T, (i) T, (j) F.}}$$
::: {.proof}
No justification was requested. Brief checks: (a) infinite CW complexes can have infinitely generated homology; (b) abstract homotopy groups do not determine Postnikov $k$-invariants and hence need not determine homology; (c) an $(n-1)$-sheeted cover of $\Sigma_2$ has genus $n$, and such cyclic covers exist; (d) $H_1(\mathbb{RP}^2)=\mathbb Z/2$; (e) over a PID only Ext in degrees at least $2$ vanishes universally, while $\operatorname{Ext}^1(\mathbb Z/2,\mathbb Z)\ne0$; (f) is the standard ring computation; (g) the torus double-covers the Klein bottle but a nonabelian Klein-bottle group cannot inject into $\mathbb Z^2$; (h) a product is orientable exactly when both factors are, and $\mathbb{RP}^r$ is orientable exactly when $r$ is odd; (i) $H_i(\mathbb{RP}^n;\mathbb F_2)\ne0$ in every degree $0\le i\le n$, forcing at least one $i$-cell in any CW structure; (j) the unrestricted cohomological Künneth tensor formula can fail for spaces with infinite-dimensional homology, so finite-type hypotheses are needed for this form.
:::
:::
