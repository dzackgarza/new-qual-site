---
schema: qual/card@1
id: E-AMD-4M7MSCEI
kind: exercise
title: "Show that $H ~\\text{char}~ K ~\\text{char}~G \\Rightarrow H ~\\text{char}~ G$"
classification:
  areas:
  - algebra
  topics:
  - automorphisms
  - subgroups
  - normal-subgroups
relations: []
review: draft
solved: true
---

::: {.exercise}
Show that $H \operatorname{char} K \operatorname{char} G \implies H \operatorname{char} G$.

> So "characteristic" is a transitive relation for subgroups.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

Recall the definition of a characteristic subgroup:
A subgroup $S \leq M$ is **characteristic in $M$** (denoted $S \operatorname{char} M$) if for every automorphism $\psi \in \Aut(M)$, we have $\psi(S) = S$.

We are given:
1. $H \operatorname{char} K$, where $K \leq G$.
2. $K \operatorname{char} G$.

Let $\phi \in \Aut(G)$ be an arbitrary automorphism of $G$.
- Since $K \operatorname{char} G$, the automorphism $\phi$ maps $K$ onto itself:
  $$
  \phi(K) = K.
  $$
- Therefore, the restriction of $\phi$ to $K$, denoted $\restrictionof{\phi}{K} : K \to K$, is an automorphism of the group $K$:
  $$
  \restrictionof{\phi}{K} \in \Aut(K).
  $$
- Since $H \operatorname{char} K$, every automorphism of $K$ maps $H$ onto itself.
  In particular, for the automorphism $\restrictionof{\phi}{K} \in \Aut(K)$:
  $$
  \phi(H) = (\restrictionof{\phi}{K})(H) = H.
  $$

Since $\phi(H) = H$ for all $\phi \in \Aut(G)$, it follows by definition that:
$$
H \operatorname{char} G.
$$
Thus, the property of being a characteristic subgroup is **transitive**.

*(Note: In contrast, normality is not transitive in general: $H \normal K \normal G \centernot\implies H \normal G$. However, if $H \operatorname{char} K \normal G$, then $H \normal G$.)*
:::
