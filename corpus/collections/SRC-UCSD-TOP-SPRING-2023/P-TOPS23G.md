---
schema: qual/card@1
id: P-TOPS23G
kind: problem
title: "Antipodal-preserving map of S^{2n+1} has odd degree"
classification:
  areas:
  - topology
  topics:
  - Degree
  - Antipodal Map
  - Spheres
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $f : S^{2n+1} \to S^{2n+1}$ be a map satisfying $f(-x) = -f(x)$.
Show that the degree of $f$ must be odd.
:::

::: {.solution}

::: pf

::: pf-step
Descent to real projective space $\mathbb{RP}^{2n+1}$:

::: pf-proof

::: pf-step
Let $k = 2n+1$.
The antipodal identification $x \sim -x$ gives the 2-fold covering projection $p: S^k \to \mathbb{RP}^k$.

::: pf-proof
definition of real projective space.
:::

:::

::: pf-step
Since $f(-x) = -f(x)$, $f$ preserves antipodal fibers: $p(f(x)) = p(f(-x))$.

::: pf-proof
hypothesis $f(-x) = -f(x)$.
:::

:::

::: pf-step
Thus $f$ induces a well-defined continuous map $\bar{f}: \mathbb{RP}^k \to \mathbb{RP}^k$ such that $p \circ f = \bar{f} \circ p$.

::: pf-proof
universal property of quotient spaces.
:::

:::

:::

:::

::: pf-step
Show that $\bar{f}^*$ acts non-trivially on $H^1(\mathbb{RP}^k; \mathbb{Z}_2)$:

::: pf-proof

::: pf-step
Let $\gamma: [0, 1] \to S^k$ be a path from a point $x_0 \in S^k$ to its antipode $-x_0$.

::: pf-proof
$S^k$ is path-connected for $k \ge 1$.
:::

:::

::: pf-step
The projection $p \circ \gamma$ is a closed loop in $\mathbb{RP}^k$ representing the unique non-trivial element of $\pi_1(\mathbb{RP}^k) \cong \mathbb{Z}_2$.

::: pf-proof
paths connecting antipodal points project to generators of $\pi_1(\mathbb{RP}^k)$.
:::

:::

::: pf-step
The image loop $\bar{f} \circ (p \circ \gamma) = p \circ (f \circ \gamma)$ is the projection of the path $f \circ \gamma$ in $S^k$, which starts at $f(x_0)$ and ends at $f(-x_0) = -f(x_0)$.

::: pf-proof
$p \circ f = \bar{f} \circ p$ and $f(-x_0) = -f(x_0)$.
:::

:::

::: pf-step
Since $f \circ \gamma$ connects antipodal points in $S^k$, its projection $p \circ (f \circ \gamma)$ is non-trivial in $\pi_1(\mathbb{RP}^k)$.

::: pf-proof
covering homotopy property.
:::

:::

::: {.pf-step #s2-5}
Thus $\bar{f}_*: \pi_1(\mathbb{RP}^k) \to \pi_1(\mathbb{RP}^k)$ is the identity isomorphism.

::: pf-proof
the only non-trivial endomorphism of $\mathbb{Z}_2$ is the identity.
:::

:::

::: {.pf-step #s2-6}
By the Universal Coefficient Theorem, $H^1(\mathbb{RP}^k; \mathbb{Z}_2) \cong \operatorname{Hom}(\pi_1(\mathbb{RP}^k), \mathbb{Z}_2) \cong \mathbb{Z}_2$.

::: pf-proof
Hurewicz theorem and UCT.
:::

:::

::: {.pf-step #s2-7}
Thus $\bar{f}^*(\alpha) = \alpha$, where $\alpha \in H^1(\mathbb{RP}^k; \mathbb{Z}_2)$ is the non-zero generator.

::: pf-proof
Step [](#s2-5){.pf-ref} and step [](#s2-6){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #s3}
Compute the mod 2 degree of $\bar{f}$ and $f$:

::: pf-proof

::: pf-step
The cohomology ring of $\mathbb{RP}^k$ with $\mathbb{Z}_2$ coefficients is:
\[
H^*(\mathbb{RP}^k; \mathbb{Z}_2) \cong \mathbb{Z}_2[\alpha] / (\alpha^{k+1}).
\]

::: pf-proof
standard cell structure and cup product structure of $\mathbb{RP}^k$.
:::

:::

::: pf-step
The top cohomology generator is $\alpha^k \in H^k(\mathbb{RP}^k; \mathbb{Z}_2) \cong \mathbb{Z}_2$.

::: pf-proof
$k = 2n+1$.
:::

:::

::: pf-step
By the ring homomorphism property of induced maps in cohomology:
\[
\bar{f}^*(\alpha^k) = (\bar{f}^*(\alpha))^k = \alpha^k \neq 0.
\]

::: pf-proof
Step [](#s2-7){.pf-ref} and cup product preservation.
:::

:::

::: pf-step
Thus the mod 2 degree of $\bar{f}$ is $\deg_2(\bar{f}) = 1$.

::: pf-proof
$\bar{f}^*(\alpha^k) = \deg_2(\bar{f}) \alpha^k$.
:::

:::

::: pf-step
Since $p: S^k \to \mathbb{RP}^k$ is a 2-fold cover and $p \circ f = \bar{f} \circ p$, the degree of $f$ modulo 2 equals $\deg_2(\bar{f})$:
\[
\deg(f) \equiv \deg_2(\bar{f}) \equiv 1 \pmod 2.
\]

::: pf-proof
covering transfer and mod 2 degree reduction.
:::

:::

:::

:::

::: pf-step
Conclusion: $\deg(f)$ is an odd integer.

::: pf-proof
Step [](#s3){.pf-ref}.
:::

:::

:::
:::
