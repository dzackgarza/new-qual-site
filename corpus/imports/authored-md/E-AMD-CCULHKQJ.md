---
schema: qual/card@1
id: E-AMD-CCULHKQJ
kind: exercise
title: Fundamental theorem of Galois theory
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Normal Subgroups
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
---

::: {.exercise}
Show that if $K/E/F$ with $K/F$ Galois then $K/E$ is always Galois with $g(K/E) \leq g(K/F)$.

- Show additionally $E/F$ is Galois $\iff g(K/E) \normal g(K/F)$.

- Show that in this case, $g(E/F) = g(K/F) / g(K/E)$.
:::

::: {.solution}
**Goal:** Let $K/F$ be a finite Galois extension, and let $E$ be an intermediate field ($F \subseteq E \subseteq K$). Let $G = \operatorname{Gal}(K/F)$ and $H = \operatorname{Gal}(K/E)$.
Prove:

1. $K/E$ is Galois and $H \le G$.

2. $E/F$ is Galois if and only if $H \trianglelefteq G$.

3. If $E/F$ is Galois, then $\operatorname{Gal}(E/F) \cong G/H$.

<1>1. Proof that $K/E$ is Galois and $H \le G$: <2>1. Since $K/F$ is finite, normal, and separable, $K$ is the splitting field over $F$ of a separable polynomial $f(x) \in F[x]$.
Proof: Standard characterization of finite Galois extensions.
<2>2. Since $F \subseteq E$, $f(x) \in E[x]$, so $K$ is also the splitting field of the separable polynomial $f(x)$ over $E$.
Proof: Polynomial coefficients in $F$ are in $E$, and roots of $f(x)$ generate $K$ over $E$.
<2>3. Therefore, $K/E$ is finite, normal, and separable, hence Galois.
Proof: Splitting field of a separable polynomial is Galois.
<2>4. Any $E$-automorphism $\sigma \in \operatorname{Gal}(K/E)$ fixes $E$ pointwise, hence fixes $F \subseteq E$ pointwise, so $\sigma \in \operatorname{Gal}(K/F) = G$.
Proof: $F \subseteq E \implies \sigma|_F = \operatorname{id}_F$.
<2>5. Thus $H = \operatorname{Gal}(K/E) \le G$.
Proof: $H$ is a subgroup of $G$.

<1>2. The Restriction Homomorphism: <2>1. Define the map $\Phi: \operatorname{Gal}(K/F) \to \operatorname{Hom}_F(E, K)$ by $\Phi(\sigma) = \sigma|_E$.
Proof: For each $\sigma \in G$, $\sigma|_E$ is an $F$-algebra embedding of $E$ into $K$.
<2>2. The kernel of $\Phi$ (elements $\sigma \in G$ such that $\sigma|_E = \operatorname{id}_E$) is by definition $H = \operatorname{Gal}(K/E)$.
Proof: $\sigma \in \ker(\Phi) \iff \sigma(e) = e$ for all $e \in E \iff \sigma \in \operatorname{Gal}(K/E)$.
<2>3. For any $\sigma \in G$, the intermediate field corresponding to the subgroup $\sigma H \sigma^{-1}$ is $\sigma(E)$.
<3>1. Let $x \in K$.
$x \in \operatorname{Fix}(\sigma H \sigma^{-1}) \iff (\sigma \tau \sigma^{-1})(x) = x$ for all $\tau \in H \iff \tau(\sigma^{-1}(x)) = \sigma^{-1}(x)$ for all $\tau \in H$.
Proof: Group action algebraic rearrangement.
<3>2. $\tau(\sigma^{-1}(x)) = \sigma^{-1}(x)$ for all $\tau \in H \iff \sigma^{-1}(x) \in \operatorname{Fix}(H) = E \iff x \in \sigma(E)$.
Proof: By Galois correspondence, $\operatorname{Fix}(\operatorname{Gal}(K/E)) = E$.
<3>3. Q.E.D. Proof: $\operatorname{Gal}(K/\sigma(E)) = \sigma H \sigma^{-1}$.

<1>3. Proof of Part 2 ($E/F$ is Galois $\iff H \trianglelefteq G$): <2>1. $E/F$ is Galois if and only if $E/F$ is normal (since separability of $K/F$ implies separability of $E/F$). Proof: Subextensions of separable extensions are separable.
<2>2. An algebraic extension $E/F$ inside normal $K/F$ is normal if and only if every $F$-embedding of $E$ into $K$ has image $E$, i.e., $\sigma(E) = E$ for all $\sigma \in \operatorname{Gal}(K/F)$.
Proof: Standard characterization of normal subextensions.
<2>3. By <1>2.<2>3, $\sigma(E) = E$ for all $\sigma \in G$ if and only if $\sigma H \sigma^{-1} = H$ for all $\sigma \in G$.
Proof: The Galois correspondence is a bijection between intermediate subfields and subgroups.
<2>4. $\sigma H \sigma^{-1} = H$ for all $\sigma \in G$ is the definition of $H \trianglelefteq G$.
Proof: Definition of normal subgroup.
<2>5. Therefore, $E/F$ is Galois if and only if $H = \operatorname{Gal}(K/E) \trianglelefteq G = \operatorname{Gal}(K/F)$.
Proof: Follows from <2>1 through <2>4.

<1>4. Proof of Part 3 ($\operatorname{Gal}(E/F) \cong G / H$): <2>1. Assume $E/F$ is Galois (so $H \trianglelefteq G$). Proof: Setting for Part 3. <2>2. Since $\sigma(E) = E$ for all $\sigma \in G$, restriction defines a group homomorphism $\rho: G \to \operatorname{Gal}(E/F)$ by $\rho(\sigma) = \sigma|_E$.
Proof: Composition of restrictions is restriction of compositions: $(\sigma \circ \tau)|_E = \sigma|_E \circ \tau|_E$.
<2>3. The kernel of $\rho$ is $\ker(\rho) = \{\sigma \in G \mid \sigma|_E = \operatorname{id}_E\} = \operatorname{Gal}(K/E) = H$.
Proof: By <1>2.<2>2. <2>4. The homomorphism $\rho$ is surjective.
Proof: Any $F$-automorphism $\tau \in \operatorname{Gal}(E/F)$ extends to an automorphism of the splitting field $K$ over $F$ by the Isomorphism Extension Theorem.
<2>5. By the First Isomorphism Theorem for groups: $$\operatorname{Gal}(E/F) \cong G / \ker(\rho) = \operatorname{Gal}(K/F) / \operatorname{Gal}(K/E) = G / H.$$ Proof: Direct application of the First Isomorphism Theorem to the surjective homomorphism $\rho$.

<1>5. Conclusion: All parts of the Fundamental Theorem of Galois Theory for intermediate fields are proven.
Proof: By <1>1, <1>3, and <1>4.
:::
