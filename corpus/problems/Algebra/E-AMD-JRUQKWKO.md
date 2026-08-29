---
schema: qual/card@1
id: E-AMD-JRUQKWKO
kind: exercise
title: $H$ characteristic in $K\trianglelefteq G$ implies $H\trianglelefteq G$
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Automorphisms
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Show that if $H \leq K \trianglelefteq G$ and $H$ is characteristic in $K$, then $H \trianglelefteq G$.
:::

::: solution
**Goal:** Prove that if $K \trianglelefteq G$ and $H \operatorname{char} K$, then $H \trianglelefteq G$.

<1>1. Conjugation by $g \in G$ restricts to an automorphism of $K$:
    *Proof:*
    <2>1. Let $g \in G$. Define the conjugation map $\varphi_g: G \to G$ by $\varphi_g(x) = g x g^{-1}$.
    <2>2. Because $K \trianglelefteq G$, for every $k \in K$ we have $g k g^{-1} \in K$.
    <2>3. Thus $\varphi_g$ restricts to a map $\varphi_g|_K: K \to K$.
    <2>4. The restriction $\varphi_g|_K$ is a group homomorphism (conjugation preserves the group operation).
    <2>5. Because $\varphi_g$ is invertible (with inverse $\varphi_{g^{-1}}$), the restriction $\varphi_g|_K$ is an automorphism of $K$.

<1>2. Characteristic subgroups are invariant under all automorphisms:
    *Proof:*
    <2>1. Because $H$ is characteristic in $K$ ($H \operatorname{char} K$), $\alpha(H) = H$ for every automorphism $\alpha \in \operatorname{Aut}(K)$.
    <2>2. In particular, $\varphi_g|_K(H) = H$ for every $g \in G$.

<1>3. Normality of $H$ in $G$:
    *Proof:*
    <2>1. For any $g \in G$:
        $$g H g^{-1} = \varphi_g(H) = \varphi_g|_K(H) = H.$$
    <2>2. Since $g H g^{-1} = H$ for every $g \in G$, $H \trianglelefteq G$.

<1>4. Conclusion:
    $H \operatorname{char} K \trianglelefteq G \implies H \trianglelefteq G$. Q.E.D.
:::
