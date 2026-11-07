---
schema: qual/card@1
id: E-HAT-3.3-11
kind: problem
title: Degree 1 maps between surfaces
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 11; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read both directions: a degree 1 map makes $f^*$ injective on $H^1$ because the pairing on
    $M_h$ is nondegenerate and $f^*\mu_h=\mu_g\ne0$, giving $2h\le2g$; conversely the pinch map
    collapsing one connected-summand of $M_g=M_h\#M_{g-h}$ has degree 1.
- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    The card stated "iff", but p.258 prints "degree 1 maps $M_g\to M_h$ exist if $g\ge h$"; the
    card's own note had called the stored statement a match. The printed sentence is restored, and
    the converse is kept and labelled as an addition, since Exercises 12 and 13 need the
    impossibility for $j<k$ and the print does not ask for it. Both arguments rechecked: $f^*\mu_h
    =\mu_g$ from $\deg f=1$ by evaluation on the fundamental class, nondegeneracy of the cup product
    pairing on $H^1$ of a closed orientable surface, and the pinch map on $M_h\#M_{g-h}$ which is a
    local orientation-preserving homeomorphism off the collapsed point.
---

::: {.problem}
If $M_g$ denotes the closed orientable surface of genus $g$, show that degree 1 maps $M_g \to M_h$ exist if $g \geq h$.
:::

::: {.solution}
The printed exercise asks for the direction $g\ge h$; step [](#s1){.pf-ref} proves in addition the converse, that a degree 1 map $M_g\to M_h$ forces $g\ge h$, because Exercises 12 and 13 use that direction and it is not printed there.

::: pf

::: {.pf-step #s1}

Converse, proved here although the print does not ask for it, and used by Exercises 12 and 13 ($f: M_g \to M_h$ of degree $1 \implies g \ge h$):

::: pf-proof

::: pf-step

Let $f: M_g \to M_h$ be a continuous map of degree 1.
Then the induced map on top cohomology sends the fundamental class to the fundamental class:
$$
f^*(\mu_h) = \mu_g, \quad \text{where } \mu_g \in H^2(M_g; \RR) \cong \RR \text{ and } \mu_h \in H^2(M_h; \RR) \cong \RR.
$$

::: pf-proof

definition of degree via cohomology.

:::

:::

::: pf-step

We claim $f^*: H^1(M_h; \RR) \to H^1(M_g; \RR)$ is injective:
Let $\alpha \in H^1(M_h; \RR) \setminus \{0\}$.
By Poincaré Duality on $M_h$, the cup product pairing $H^1(M_h; \RR) \times H^1(M_h; \RR) \to H^2(M_h; \RR)$ is non-degenerate (skew-symmetric and non-singular).
Thus there exists $\beta \in H^1(M_h; \RR)$ such that $\alpha \smile \beta = \mu_h$.

::: pf-proof

Poincaré duality pairing on closed orientable surfaces.

:::

:::

::: pf-step

Applying $f^*$ and the ring homomorphism property of cup product:
$$
f^*(\alpha) \smile f^*(\beta) = f^*(\alpha \smile \beta) = f^*(\mu_h) = \mu_g \neq 0.
$$
Because the cup product is non-zero, $f^*(\alpha) \neq 0$.
Thus $\ker(f^*) = \{0\}$, so $f^*: H^1(M_h; \RR) \hookrightarrow H^1(M_g; \RR)$ is an injective linear map.

::: pf-proof

injectivity from non-vanishing cup product.

:::

:::

::: pf-step

Comparing dimensions:
$$
\dim_\RR H^1(M_h; \RR) \le \dim_\RR H^1(M_g; \RR) \implies 2h \le 2g \implies h \le g.
$$

::: pf-proof

$\dim H^1(M_k; \RR) = 2k$.

:::

:::

:::

:::

::: {.pf-step #s2}

Reverse direction, the one the exercise asks for ($g \ge h \implies$ existence of a degree 1 map $M_g \to M_h$):

::: pf-proof

::: pf-step

If $g = h$, the identity map $\operatorname{id}: M_g \to M_g$ has degree 1.

::: pf-proof

$\deg(\operatorname{id}) = 1$.

:::

:::

::: pf-step

If $g > h$, decompose $M_g$ as the connected sum $M_g = M_h \# M_{g-h}$.
Let $c$ be the separating circle along which the sum is glued.

::: pf-proof

connected sum decomposition of surfaces.

:::

:::

::: pf-step

Collapse the punctured $M_{g-h}$ summand, including the separating circle $c$, to one point. The resulting quotient is the punctured $M_h$ summand with its boundary circle collapsed to a point, which is homeomorphic to $M_h$. Let $f:M_g\to M_h$ be this quotient map, choosing the homeomorphism to preserve orientation on the interior of the punctured $M_h$ summand.

::: pf-proof

pinch map collapsing one connected summand to a point.

:::

:::

::: pf-step

Any point $y \in M_h \setminus \{p\}$ has $f^{-1}(y) = \{x\}$ consisting of a single point where $f$ is a local orientation-preserving homeomorphism.
Thus $\deg(f) = +1$.

::: pf-proof

local degree formula for degree of smooth/continuous maps.

:::

:::

:::

:::

::: pf-step

Conclusion:
Degree 1 maps $M_g \to M_h$ exist if and only if $g \ge h$. Q.E.D.

::: pf-proof

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref}.

:::

:::

:::

:::
