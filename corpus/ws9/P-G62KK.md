---
schema: qual/card@1
id: P-G62KK
kind: problem
title: Conformal automorphisms of the disk are linear fractional transformations
classification:
  areas:
  - real-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Let $D \subset \mathbb{C}$ be the unit disk.
Prove that every one-to-one conformal mapping of $D$ to $D$ is given by a linear fractional transformation.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Prove that every one-to-one conformal mapping $f: D \to D$ of the unit disk onto itself is a linear fractional transformation.

<1>1. Setup: let $a = f(0) \in D$ and define the automorphism $\psi_a(z) = \frac{a - z}{1 - \bar a z}$; set $g = \psi_a \circ f$.
Proof: $\psi_a$ is a Möbius automorphism of $D$ sending $a$ to $0$, so $g: D \to D$ is a bijective conformal map with $g(0) = 0$.

<1>2. $|g(z)| = |z|$ for all $z \in D$.
<2>1. $|g(z)| \le |z|$.
Proof: Schwarz's lemma applies to $g$ (holomorphic, $g(D) \subseteq D$, $g(0) = 0$). <2>2. $|g(z)| \ge |z|$.
Proof: apply Schwarz's lemma to $g^{-1}$ (which also maps $D$ to $D$ with $g^{-1}(0) = 0$): $|g^{-1}(w)| \le |w|$; put $w = g(z)$.
<2>3. Conclusion.
Proof: combine <2>1 and <2>2.

<1>3. $g(z) = cz$ with $|c| = 1$.
Proof: by the equality case of Schwarz's lemma applied to <1>2 (or directly: $g(z)/z$ is holomorphic, bounded by 1, and attains modulus 1, e.g. at the boundary or by the maximum principle after using $|g| = |z|$).

<1>4. $f$ is a linear fractional transformation.
Proof: $f = \psi_a^{-1} \circ g$ with $\psi_a^{-1}(w) = \frac{w + a}{1 + \bar a w}$ a Möbius map and $g(z) = cz$; a composition of Möbius maps is Möbius: $f(z) = \frac{cz + a}{1 + \bar a c z}$.

<1>5. Q.E.D. Proof: <1>1–<1>4 establish the claim (and conversely every such map is an automorphism of $D$).
:::
