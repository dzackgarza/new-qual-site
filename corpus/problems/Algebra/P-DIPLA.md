---
schema: qual/card@1
id: P-DIPLA
kind: problem
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
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $K/F$ be a finite Galois extension and let $E$ be an intermediate field ($F \subseteq E \subseteq K$).
(1) Prove that $K/E$ is always Galois with $\operatorname{Gal}(K/E) \le \operatorname{Gal}(K/F)$.
(2) Prove that $E/F$ is Galois if and only if $\operatorname{Gal}(K/E) \trianglelefteq \operatorname{Gal}(K/F)$.
(3) Prove that when $E/F$ is Galois, $\operatorname{Gal}(E/F) \cong \operatorname{Gal}(K/F) / \operatorname{Gal}(K/E)$.
:::

::: solution
**Goal:** Prove the Fundamental Theorem of Galois Theory for intermediate extensions and normal subgroups.

<1>1. Part (1): $K/E$ is always Galois:
::: {.proof}
<2>1. Since $K/F$ is a finite Galois extension, $K/F$ is finite, normal, and separable.
<2>2. **Separability:** Every element in $K$ is separable over $F$. Since the minimal polynomial of $\alpha \in K$ over $E$ divides its minimal polynomial over $F$, every element in $K$ is separable over $E$.
<2>3. **Normality:** $K$ is the splitting field over $F$ of a separable polynomial $f(x) \in F[x]$. Since $F[x] \subseteq E[x]$, $K$ is also the splitting field of $f(x)$ viewed as a polynomial over $E$.
<2>4. Thus $K/E$ is finite, normal, and separable, hence **Galois**.
<2>5. Any automorphism $\sigma \in \operatorname{Gal}(K/E)$ fixes $E$ pointwise, and since $F \subseteq E$, $\sigma$ fixes $F$ pointwise. Thus $\operatorname{Gal}(K/E)$ is a subgroup of $\operatorname{Gal}(K/F)$.
:::

<1>2. Part (2) and (3): $E/F$ is Galois $\iff \operatorname{Gal}(K/E) \trianglelefteq \operatorname{Gal}(K/F)$, with $\operatorname{Gal}(E/F) \cong \operatorname{Gal}(K/F)/\operatorname{Gal}(K/E)$:
::: {.proof}
<2>1. Consider the restriction mapping:
$$\Phi: \operatorname{Gal}(K/F) \to \operatorname{Aut}(E/F), \qquad \Phi(\sigma) = \sigma|_E.$$
<2>2. For any $\sigma \in \operatorname{Gal}(K/F)$, $\sigma(E)$ is an $F$-isomorphic subfield of $K$.
<2>3. **Normality of $E/F$:** $E/F$ is normal $\iff \sigma(E) = E$ for all $F$-embeddings $\sigma: E \hookrightarrow \overline{F}$. Since every $F$-embedding extends to an automorphism of $K$, $E/F$ is normal $\iff \sigma(E) = E$ for all $\sigma \in \operatorname{Gal}(K/F)$.
<2>4. **Characterizing $\sigma(E) = E$ in terms of subgroups:**
- Under the Galois correspondence, the fixed field of the subgroup $\sigma H \sigma^{-1}$ (where $H = \operatorname{Gal}(K/E)$) is $\sigma(E)$.
- Thus $\sigma(E) = E \iff \sigma H \sigma^{-1} = H$.
- Therefore, $E/F$ is normal (hence Galois, since $E/F$ is already separable) if and only if $H \trianglelefteq \operatorname{Gal}(K/F)$.
<2>5. **Restriction Homomorphism:**
- When $H \trianglelefteq \operatorname{Gal}(K/F)$, every $\sigma \in \operatorname{Gal}(K/F)$ maps $E$ to $E$, so $\sigma|_E \in \operatorname{Gal}(E/F)$.
- $\Phi: \operatorname{Gal}(K/F) \to \operatorname{Gal}(E/F)$ is a group homomorphism.
- **Kernel of $\Phi$:** $$\ker\Phi = \{\sigma \in \operatorname{Gal}(K/F) \mid \sigma|_E = \operatorname{id}_E\} = \operatorname{Gal}(K/E) = H.$$
- **Surjectivity of $\Phi$:** Every $\tau \in \operatorname{Gal}(E/F)$ extends to an automorphism $\tilde{\tau} \in \operatorname{Gal}(K/F)$ by the Isomorphism Extension Theorem for splitting fields. Thus $\Phi$ is surjective.
<2>6. By the First Isomorphism Theorem for groups:
$$\operatorname{Gal}(E/F) = \operatorname{im}(\Phi) \cong \operatorname{Gal}(K/F) / \ker\Phi = \operatorname{Gal}(K/F) / \operatorname{Gal}(K/E).$$
:::

<1>3. Conclusion:
::: {.proof}
$K/E$ is always Galois, $E/F$ is Galois iff $\operatorname{Gal}(K/E) \trianglelefteq \operatorname{Gal}(K/F)$, and $\operatorname{Gal}(E/F) \cong \operatorname{Gal}(K/F)/\operatorname{Gal}(K/E)$.
:::
:::
