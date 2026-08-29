---
schema: qual/card@1
id: P-HPSTB
kind: problem
title: Inner automorphisms preserve conjugacy of subgroups
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Conjugacy
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Show that any automorphism (and in particular, every inner automorphism) sends conjugate subgroups to conjugate subgroups.
:::

::: solution
**Goal:** Prove that if $H_1, H_2 \le G$ are conjugate subgroups and $\varphi \in \operatorname{Aut}(G)$ is an automorphism, then $\varphi(H_1)$ and $\varphi(H_2)$ are conjugate in $G$.

<1>1. Setting up conjugacy of subgroups:
    *Proof:*
    <2>1. By definition, $H_1$ and $H_2$ are conjugate in $G$ if and only if there exists some element $g \in G$ such that:
        $$H_2 = g H_1 g^{-1} = \{g h g^{-1} \mid h \in H_1\}.$$

<1>2. Applying the automorphism $\varphi$:
    *Proof:*
    <2>1. Let $\varphi: G \to G$ be an automorphism.
    <2>2. Applying $\varphi$ to both sides of $H_2 = g H_1 g^{-1}$:
        $$\varphi(H_2) = \varphi(g H_1 g^{-1}) = \{\varphi(g h g^{-1}) \mid h \in H_1\}.$$
    <2>3. Because $\varphi$ is a group homomorphism:
        $$\varphi(g h g^{-1}) = \varphi(g) \varphi(h) \varphi(g^{-1}) = \varphi(g) \varphi(h) (\varphi(g))^{-1}.$$
    <2>4. Therefore:
        $$\varphi(H_2) = \{\varphi(g) \varphi(h) (\varphi(g))^{-1} \mid h \in H_1\} = \varphi(g) \{\varphi(h) \mid h \in H_1\} (\varphi(g))^{-1} = \varphi(g) \varphi(H_1) (\varphi(g))^{-1}.$$

<1>3. Verification of conjugacy in $G$:
    *Proof:*
    <2>1. The element $g' = \varphi(g)$ belongs to $G$ (since $\varphi \in \operatorname{Aut}(G)$).
    <2>2. Thus $\varphi(H_2) = g' \varphi(H_1) (g')^{-1}$, which proves that $\varphi(H_1)$ and $\varphi(H_2)$ are conjugate in $G$ via the conjugating element $\varphi(g)$.

<1>4. Special case of inner automorphisms $\varphi = \operatorname{Inn}_x$:
    *Proof:*
    <2>1. If $\varphi(y) = x y x^{-1}$ for some $x \in G$, then $\varphi \in \operatorname{Aut}(G)$, so the general result applies.
    <2>2. Explicitly: $\varphi(H_2) = x (g H_1 g^{-1}) x^{-1} = (xgx^{-1}) (x H_1 x^{-1}) (xgx^{-1})^{-1} = \varphi(g) \varphi(H_1) \varphi(g)^{-1}$.

<1>5. Conclusion:
    Every automorphism (and hence every inner automorphism) maps conjugate subgroups to conjugate subgroups. Q.E.D.
:::
