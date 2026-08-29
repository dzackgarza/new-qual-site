---
schema: qual/card@1
id: P-QASPQ
kind: problem
title: Characteristic subgroups are normal
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Normal Subgroups
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
(1) Prove that if $H \operatorname{char} G$ (i.e. $H$ is a characteristic subgroup of $G$), then $H \trianglelefteq G$ ($H$ is a normal subgroup of $G$).
(2) Give an example showing that normality does not imply characteristic (so "characteristic" is strictly stronger than "normal").
:::

::: solution
**Goal:** Prove that every characteristic subgroup is normal, and show the converse fails.

<1>1. Definitions:
    *Proof:*
    <2>1. A subgroup $H \le G$ is **normal** in $G$ ($H \trianglelefteq G$) if $g H g^{-1} = H$ for all $g \in G$.
    <2>2. A subgroup $H \le G$ is **characteristic** in $G$ ($H \operatorname{char} G$) if $\sigma(H) = H$ for all automorphisms $\sigma \in \operatorname{Aut}(G)$.

<1>2. Proof that $H \operatorname{char} G \implies H \trianglelefteq G$:
    *Proof:*
    <2>1. For each element $g \in G$, define the inner conjugation map $\iota_g: G \to G$ by:
        $$\iota_g(x) = g x g^{-1}.$$
    <2>2. $\iota_g$ is a bijective group homomorphism from $G$ to $G$ with inverse $\iota_{g^{-1}}$.
    <2>3. Therefore, the inner automorphism $\iota_g$ is an automorphism of $G$:
        $$\iota_g \in \operatorname{Inn}(G) \le \operatorname{Aut}(G).$$
    <2>4. Since $H \operatorname{char} G$, $H$ is invariant under every automorphism in $\operatorname{Aut}(G)$.
    <2>5. In particular, $H$ is invariant under all inner automorphisms $\iota_g$:
        $$g H g^{-1} = \iota_g(H) = H \quad \text{for every } g \in G.$$
    <2>6. Thus $H \trianglelefteq G$.

<1>3. Counterexample to the converse (Normal $\not\implies$ Characteristic):
    *Proof:*
    <2>1. Consider the Klein four-group $V_4 = \mathbb{Z}_2 \times \mathbb{Z}_2 = \{e, a, b, c\}$.
    <2>2. Since $V_4$ is abelian, every subgroup is normal.
    <2>3. In particular, the subgroup $H = \{e, a\} \cong \mathbb{Z}_2$ is normal in $V_4$: $H \trianglelefteq V_4$.
    <2>4. The automorphism group is $\operatorname{Aut}(V_4) \cong S_3$, which acts by permuting the three non-identity elements $\{a, b, c\}$.
    <2>5. There exists an automorphism $\sigma \in \operatorname{Aut}(V_4)$ that maps $a \mapsto b$.
    <2>6. Then $\sigma(H) = \{\sigma(e), \sigma(a)\} = \{e, b\} \ne H$.
    <2>7. Thus $H$ is not characteristic in $V_4$.

<1>4. Conclusion:
    Every characteristic subgroup is normal (as $\operatorname{Inn}(G) \le \operatorname{Aut}(G)$), but normal subgroups need not be characteristic. Q.E.D.
:::
