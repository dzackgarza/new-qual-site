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

::: problem
Let $f : S^{2n+1} \to S^{2n+1}$ be a map satisfying $f(-x) = -f(x)$.
Show that the degree of $f$ must be odd.
:::

::: {.solution}
<1>1. Descent to real projective space $\mathbb{RP}^{2n+1}$: <2>1. Let $k = 2n+1$.
The antipodal identification $x \sim -x$ gives the 2-fold covering projection $p: S^k \to \mathbb{RP}^k$.
Proof: definition of real projective space.
<2>2. Since $f(-x) = -f(x)$, $f$ preserves antipodal fibers: $p(f(x)) = p(f(-x))$.
Proof: hypothesis $f(-x) = -f(x)$.
<2>3. Thus $f$ induces a well-defined continuous map $\bar{f}: \mathbb{RP}^k \to \mathbb{RP}^k$ such that $p \circ f = \bar{f} \circ p$.
Proof: universal property of quotient spaces.

<1>2. Show that $\bar{f}^*$ acts non-trivially on $H^1(\mathbb{RP}^k; \mathbb{Z}_2)$: <2>1. Let $\gamma: [0, 1] \to S^k$ be a path from a point $x_0 \in S^k$ to its antipode $-x_0$.
Proof: $S^k$ is path-connected for $k \ge 1$.
<2>2. The projection $p \circ \gamma$ is a closed loop in $\mathbb{RP}^k$ representing the unique non-trivial element of $\pi_1(\mathbb{RP}^k) \cong \mathbb{Z}_2$.
Proof: paths connecting antipodal points project to generators of $\pi_1(\mathbb{RP}^k)$.
<2>3. The image loop $\bar{f} \circ (p \circ \gamma) = p \circ (f \circ \gamma)$ is the projection of the path $f \circ \gamma$ in $S^k$, which starts at $f(x_0)$ and ends at $f(-x_0) = -f(x_0)$.
Proof: $p \circ f = \bar{f} \circ p$ and $f(-x_0) = -f(x_0)$.
<2>4. Since $f \circ \gamma$ connects antipodal points in $S^k$, its projection $p \circ (f \circ \gamma)$ is non-trivial in $\pi_1(\mathbb{RP}^k)$.
Proof: covering homotopy property.
<2>5. Thus $\bar{f}_*: \pi_1(\mathbb{RP}^k) \to \pi_1(\mathbb{RP}^k)$ is the identity isomorphism.
Proof: the only non-trivial endomorphism of $\mathbb{Z}_2$ is the identity.
<2>6. By the Universal Coefficient Theorem, $H^1(\mathbb{RP}^k; \mathbb{Z}_2) \cong \operatorname{Hom}(\pi_1(\mathbb{RP}^k), \mathbb{Z}_2) \cong \mathbb{Z}_2$.
Proof: Hurewicz theorem and UCT. <2>7. Thus $\bar{f}^*(\alpha) = \alpha$, where $\alpha \in H^1(\mathbb{RP}^k; \mathbb{Z}_2)$ is the non-zero generator.
Proof: <2>5 and <2>6.

<1>3. Compute the mod 2 degree of $\bar{f}$ and $f$: <2>1. The cohomology ring of $\mathbb{RP}^k$ with $\mathbb{Z}_2$ coefficients is:
\[
H^*(\mathbb{RP}^k; \mathbb{Z}_2) \cong \mathbb{Z}_2[\alpha] / (\alpha^{k+1}).
\]
Proof: standard cell structure and cup product structure of $\mathbb{RP}^k$.
<2>2. The top cohomology generator is $\alpha^k \in H^k(\mathbb{RP}^k; \mathbb{Z}_2) \cong \mathbb{Z}_2$.
Proof: $k = 2n+1$.
<2>3. By the ring homomorphism property of induced maps in cohomology:
\[
\bar{f}^*(\alpha^k) = (\bar{f}^*(\alpha))^k = \alpha^k \neq 0.
\]
Proof: <2>7 and cup product preservation.
<2>4. Thus the mod 2 degree of $\bar{f}$ is $\deg_2(\bar{f}) = 1$.
Proof: $\bar{f}^*(\alpha^k) = \deg_2(\bar{f}) \alpha^k$.
<2>5. Since $p: S^k \to \mathbb{RP}^k$ is a 2-fold cover and $p \circ f = \bar{f} \circ p$, the degree of $f$ modulo 2 equals $\deg_2(\bar{f})$:
\[
\deg(f) \equiv \deg_2(\bar{f}) \equiv 1 \pmod 2.
\]
Proof: covering transfer and mod 2 degree reduction.

<1>4. Conclusion: $\deg(f)$ is an odd integer.
Q.E.D. Proof: <1>3.
:::
