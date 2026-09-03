---
schema: qual/card@1
id: E-HAT-3.3-11
kind: problem
title: "Degree 1 maps between surfaces"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

If $M_g$ denotes the closed orientable surface of genus $g$, show that degree 1 maps $M_g \to M_h$ exist iff $g \geq h$.

::: {.solution}
<1>1. Forward direction ($f: M_g \to M_h$ of degree $1 \implies g \ge h$):
<2>1. Let $f: M_g \to M_h$ be a continuous map of degree 1.
Then the induced map on top cohomology sends the fundamental class to the fundamental class:
\[
f^*(\mu_h) = \mu_g, \quad \text{where } \mu_g \in H^2(M_g; \mathbb{R}) \cong \mathbb{R} \text{ and } \mu_h \in H^2(M_h; \mathbb{R}) \cong \mathbb{R}.
\]
::: {.proof}
definition of degree via cohomology.
:::
<2>2. We claim $f^*: H^1(M_h; \mathbb{R}) \to H^1(M_g; \mathbb{R})$ is injective:
Let $\alpha \in H^1(M_h; \mathbb{R}) \setminus \{0\}$.
By Poincaré Duality on $M_h$, the cup product pairing $H^1(M_h; \mathbb{R}) \times H^1(M_h; \mathbb{R}) \to H^2(M_h; \mathbb{R})$ is non-degenerate (skew-symmetric and non-singular).
Thus there exists $\beta \in H^1(M_h; \mathbb{R})$ such that $\alpha \smile \beta = \mu_h$.
::: {.proof}
Poincaré duality pairing on closed orientable surfaces.
:::
<2>3. Applying $f^*$ and the ring homomorphism property of cup product:
\[
f^*(\alpha) \smile f^*(\beta) = f^*(\alpha \smile \beta) = f^*(\mu_h) = \mu_g \neq 0.
\]
Because the cup product is non-zero, $f^*(\alpha) \neq 0$.
Thus $\ker(f^*) = \{0\}$, so $f^*: H^1(M_h; \mathbb{R}) \hookrightarrow H^1(M_g; \mathbb{R})$ is an injective linear map.
::: {.proof}
injectivity from non-vanishing cup product.
:::
<2>4. Comparing dimensions:
\[
\dim_\mathbb{R} H^1(M_h; \mathbb{R}) \le \dim_\mathbb{R} H^1(M_g; \mathbb{R}) \implies 2h \le 2g \implies h \le g.
\]
::: {.proof}
$\dim H^1(M_k; \mathbb{R}) = 2k$.
:::

<1>2. Reverse direction ($g \ge h \implies$ existence of degree 1 map $M_g \to M_h$):
<2>1. If $g = h$, the identity map $\operatorname{id}: M_g \to M_g$ has degree 1.
::: {.proof}
$\deg(\operatorname{id}) = 1$.
:::
<2>2. If $g > h$, decompose $M_g$ as the connected sum $M_g = M_h \# M_{g-h}$.
Let $c$ be the separating circle along which the sum is glued.
::: {.proof}
connected sum decomposition of surfaces.
:::
<2>3. Define $f: M_g \to M_h$ by collapsing the entire $M_{g-h}$ summand (the closure of one component of $M_g \setminus c$) to a single point $p \in M_h$, and mapping $M_h \setminus \operatorname{int}(D^2)$ homeomorphically onto $M_h \setminus \{p\}$.
::: {.proof}
pinch map collapsing one connected summand to a point.
:::
<2>4. Any point $y \in M_h \setminus \{p\}$ is a regular value with $f^{-1}(y) = \{x\}$ consisting of a single point where $f$ is a local orientation-preserving homeomorphism.
Thus $\deg(f) = +1$.
::: {.proof}
local degree formula for degree of smooth/continuous maps.
:::

<1>3. Conclusion:
Degree 1 maps $M_g \to M_h$ exist if and only if $g \ge h$. Q.E.D.
::: {.proof}
<1>1 and <1>2.
:::
:::
