---
schema: qual/card@1
id: E-AMD-F5ZHMJNK
kind: exercise
title: $C_G(H)\trianglelefteq N_G(H)$
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Normal Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Show that $C_G(H) \trianglelefteq N_G(H)$ is a normal subgroup.
:::

::: solution
**Goal:** Prove that for any subgroup $H \le G$, the centralizer $C_G(H)$ is a normal subgroup of the normalizer $N_G(H)$.

<1>1. Definition of normalizer and centralizer:
::: {.proof}
<2>1. The normalizer of $H$ in $G$ is $N_G(H) = \{g \in G \mid g H g^{-1} = H\}$.
<2>2. The centralizer of $H$ in $G$ is $C_G(H) = \{g \in G \mid g h g^{-1} = h \text{ for all } h \in H\}$.
<2>3. For any $c \in C_G(H)$, $c H c^{-1} = \{c h c^{-1} \mid h \in H\} = \{h \mid h \in H\} = H$, so $C_G(H) \subseteq N_G(H)$.
<2>4. Because $C_G(H)$ is a subgroup of $G$ contained in $N_G(H)$, $C_G(H) \le N_G(H)$.
:::

<1>2. Proof of normality via conjugation action ($N/C$ homomorphism):
::: {.proof}
<2>1. Define the conjugation mapping:
$$\phi: N_G(H) \to \operatorname{Aut}(H), \quad g \mapsto \sigma_g,$$
where $\sigma_g(h) = g h g^{-1}$ for all $h \in H$.
<2>2. For every $g \in N_G(H)$, $g H g^{-1} = H$, so $\sigma_g$ is a well-defined automorphism of $H$.
<2>3. For any $g_1, g_2 \in N_G(H)$ and $h \in H$:
$$\sigma_{g_1 g_2}(h) = (g_1 g_2) h (g_1 g_2)^{-1} = g_1 (g_2 h g_2^{-1}) g_1^{-1} = (\sigma_{g_1} \circ \sigma_{g_2})(h).$$
Thus $\phi$ is a group homomorphism.
<2>4. The kernel of $\phi$ is:
$$\ker \phi = \{g \in N_G(H) \mid \sigma_g = \operatorname{id}_H\} = \{g \in N_G(H) \mid g h g^{-1} = h \text{ for all } h \in H\} = C_G(H).$$
<2>5. Since the kernel of any group homomorphism is a normal subgroup of the domain, $C_G(H) \trianglelefteq N_G(H)$.
:::

<1>3. Direct elementwise verification of conjugation invariance:
::: {.proof}
<2>1. Let $g \in N_G(H)$ and $c \in C_G(H)$. We verify $g c g^{-1} \in C_G(H)$.
<2>2. For any $h \in H$, since $g^{-1} \in N_G(H)$, the conjugate $h' = g^{-1} h g \in H$.
<2>3. Since $c \in C_G(H)$ commutes with every element of $H$:
$$(g c g^{-1}) h (g c g^{-1})^{-1} = g c (g^{-1} h g) c^{-1} g^{-1} = g (c h' c^{-1}) g^{-1} = g h' g^{-1} = g (g^{-1} h g) g^{-1} = h.$$
<2>4. Thus $g c g^{-1} \in C_G(H)$, confirming $g C_G(H) g^{-1} \subseteq C_G(H)$ for all $g \in N_G(H)$.
:::

<1>4. Conclusion:
::: {.proof}
$C_G(H)$ is a normal subgroup of $N_G(H)$ ($C_G(H) \trianglelefteq N_G(H)$).
:::
:::
