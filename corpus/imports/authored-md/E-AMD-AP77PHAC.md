---
schema: qual/card@1
id: E-AMD-AP77PHAC
kind: exercise
title: $Z(G)\subseteq C_G(H)\subseteq N_G(H)$
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Subgroups
relations: []
review: draft
---

::: {.exercise}
Show that $Z(G) \subseteq C_G(H) \subseteq N_G(H)$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $G$ be a group and $H \le G$ a subgroup.
Prove that $Z(G) \subseteq C_G(H) \subseteq N_G(H)$, where $Z(G)$ is the center of $G$, $C_G(H)$ is the centralizer of $H$ in $G$, and $N_G(H)$ is the normalizer of $H$ in $G$.

<1>1. Definitions: <2>1. $Z(G) = \{g \in G \mid g x = x g \text{ for all } x \in G\}$.
Proof: Standard definition of the center of a group.
<2>2. $C_G(H) = \{g \in G \mid g h = h g \text{ for all } h \in H\}$.
Proof: Standard definition of the centralizer of a subgroup.
<2>3. $N_G(H) = \{g \in G \mid g H g^{-1} = H\} = \{g \in G \mid g H = H g\}$.
Proof: Standard definition of the normalizer of a subgroup.

<1>2. Proof that $Z(G) \subseteq C_G(H)$: <2>1. Let $g \in Z(G)$ be an arbitrary element.
Proof: Setting an element to prove subset inclusion.
<2>2. For every $x \in G$, $g x = x g$.
Proof: By <1>1.<2>1 and $g \in Z(G)$.
<2>3. Since $H \subseteq G$, for every $h \in H$, $g h = h g$.
Proof: Specialization of <2>2 to the subset $H \subseteq G$.
<2>4. Therefore, $g \in C_G(H)$.
Proof: By definition of $C_G(H)$ in <1>1.<2>2. <2>5. Since $g \in Z(G)$ was arbitrary, $Z(G) \subseteq C_G(H)$.
Proof: Standard subset verification.

<1>3. Proof that $C_G(H) \subseteq N_G(H)$: <2>1. Let $g \in C_G(H)$ be an arbitrary element.
Proof: Setting an element to prove subset inclusion.
<2>2. For every $h \in H$, $g h = h g$.
Proof: By definition of $C_G(H)$ in <1>1.<2>2. <2>3. For every $h \in H$, $g h g^{-1} = h g g^{-1} = h$.
Proof: Post-multiplying both sides of $g h = h g$ by $g^{-1}$.
<2>4. Conjugation by $g$ acts as the identity on $H$, so $g H g^{-1} = \{g h g^{-1} \mid h \in H\} = \{h \mid h \in H\} = H$.
Proof: Follows directly from <2>3. <2>5. Therefore, $g \in N_G(H)$.
Proof: By definition of $N_G(H)$ in <1>1.<2>3. <2>6. Since $g \in C_G(H)$ was arbitrary, $C_G(H) \subseteq N_G(H)$.
Proof: Standard subset verification.

<1>4. Conclusion: $Z(G) \subseteq C_G(H) \subseteq N_G(H)$.
Proof: By <1>2 and <1>3.
:::
