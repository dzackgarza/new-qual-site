---
schema: qual/card@1
id: P-XW3UP
kind: problem
title: Stabilizer of a point in the unit disk under conformal automorphisms
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Orbit-Stabilizer
  - Geometry
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
What is the stabilizer of a point $z_0 \in \mathbb{D}$ in the open unit disk under the group of conformal automorphisms $\operatorname{Aut}(\mathbb{D})$?
Describe the group structure and express the automorphisms explicitly.
:::

::: solution
**Goal:** Determine the stabilizer $\operatorname{Stab}_{\operatorname{Aut}(\mathbb{D})}(z_0)$ for any $z_0 \in \mathbb{D}$ and prove it is isomorphic to the circle group $\operatorname{U}(1) \cong \operatorname{SO}(2) \cong S^1$.

<1>1. Group of Conformal Automorphisms of the Unit Disk:
    *Proof:*
    <2>1. By the Schwarz Lemma and the classification of holomorphic automorphisms of $\mathbb{D} = \{z \in \mathbb{C} \mid |z| < 1\}$:
        $$\operatorname{Aut}(\mathbb{D}) = \left\{ f(z) = e^{i\theta} \frac{z - a}{1 - \bar{a} z} \;\middle|\; \theta \in [0, 2\pi), \; a \in \mathbb{D} \right\} \cong \operatorname{PSU}(1, 1) \cong \operatorname{PSL}_2(\mathbb{R}).$$

<1>2. Stabilizer of the Origin $z_0 = 0$:
    *Proof:*
    <2>1. Let $f \in \operatorname{Aut}(\mathbb{D})$ fix the origin $0$: $f(0) = 0$.
    <2>2. Setting $f(0) = 0$ in the general formula:
        $$f(0) = e^{i\theta} \frac{0 - a}{1 - 0} = -a e^{i\theta} = 0 \implies a = 0.$$
    <2>3. Thus, every automorphism fixing the origin is a pure rotation:
        $$f(z) = e^{i\theta} z \quad (\theta \in \mathbb{R}).$$
    <2>4. The stabilizer of the origin is therefore the circle group of rotations:
        $$\operatorname{Stab}_{\operatorname{Aut}(\mathbb{D})}(0) = \{z \mapsto e^{i\theta} z \mid \theta \in \mathbb{R}\} \cong S^1 \cong \operatorname{U}(1) \cong \operatorname{SO}(2).$$

<1>3. Stabilizer of an Arbitrary Point $z_0 \in \mathbb{D}$:
    *Proof:*
    <2>1. Let $\phi_{z_0}(z) = \frac{z - z_0}{1 - \bar{z}_0 z}$ be the standard Blaschke factor automorphism mapping $z_0 \mapsto 0$.
    <2>2. $\phi_{z_0} \in \operatorname{Aut}(\mathbb{D})$ is an involution up to sign: $\phi_{z_0}^{-1}(w) = \frac{w + z_0}{1 + \bar{z}_0 w} = \phi_{-z_0}(w)$.
    <2>3. Conjugating the stabilizer of the origin by $\phi_{z_0}$ gives the stabilizer of $z_0$:
        $$\begin{aligned}
        g \in \operatorname{Stab}(z_0) &\iff g(z_0) = z_0 \\
        &\iff (\phi_{z_0} \circ g \circ \phi_{z_0}^{-1})(0) = \phi_{z_0}(g(z_0)) = \phi_{z_0}(z_0) = 0 \\
        &\iff \phi_{z_0} \circ g \circ \phi_{z_0}^{-1} \in \operatorname{Stab}(0) = \operatorname{U}(1).
        \end{aligned}$$
    <2>4. Thus, $\operatorname{Stab}_{\operatorname{Aut}(\mathbb{D})}(z_0) = \phi_{z_0}^{-1} \circ \operatorname{Stab}(0) \circ \phi_{z_0} \cong \operatorname{U}(1) \cong S^1$.
    <2>5. Explicitly, every element in $\operatorname{Stab}(z_0)$ is parametrized by $\theta \in [0, 2\pi)$ as:
        $$f_\theta(z) = \phi_{-z_0}\left( e^{i\theta} \phi_{z_0}(z) \right) = \frac{e^{i\theta} \left(\frac{z - z_0}{1 - \bar{z}_0 z}\right) + z_0}{1 + \bar{z}_0 e^{i\theta} \left(\frac{z - z_0}{1 - \bar{z}_0 z}\right)}.$$

<1>4. Geometric Interpretation (Hyperbolic Geometry):
    *Proof:*
    <2>1. In the Poincaré disk model of hyperbolic geometry, $\operatorname{Aut}(\mathbb{D})$ is the group of orientation-preserving hyperbolic isometries $\operatorname{Isom}^+(\mathbb{H}^2)$.
    <2>2. The stabilizer of any point $z_0 \in \mathbb{D}$ is the maximal compact subgroup of elliptic isometries (hyperbolic rotations fixing $z_0$), which is isomorphic to $\operatorname{SO}(2) \cong S^1$.

<1>5. Conclusion:
    The stabilizer of any point $z_0 \in \mathbb{D}$ is isomorphic to the circle group $S^1 \cong \operatorname{U}(1) \cong \operatorname{SO}(2)$ of rotations around $z_0$. Q.E.D.
:::
