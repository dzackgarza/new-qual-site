---
schema: qual/card@1
id: E-4ZTVF
kind: exercise
title: "Show that a quotient of a compact space is again compact."
classification:
  areas:
  - topology
  topics:
  - compactness
  - quotient-spaces
relations: []
review: draft
solved: true
---

::: exercise
Show that a quotient of a compact space is again compact.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

Let $X$ be a compact topological space, and let $q: X \to Y$ be a quotient map (so $Y$ has the quotient topology induced by the surjective map $q$).

1. **Continuity of the quotient map:** By the definition of the quotient topology, a subset $V \subseteq Y$ is open in $Y$ if and only if $q^{-1}(V)$ is open in $X$.
   In particular, for every open set $V \subseteq Y$, the preimage $q^{-1}(V)$ is open in $X$, which means the quotient map $q: X \to Y$ is **continuous** and **surjective**.

2. **Continuous image of a compact space is compact:** Let $\mathcal{U} = \{V_\alpha\}_{\alpha \in A}$ be an open cover of $Y$:
   $$
   Y = \bigcup_{\alpha \in A} V_\alpha.
   $$
   Since $q$ is continuous, for each $\alpha \in A$, the preimage $U_\alpha = q^{-1}(V_\alpha)$ is open in $X$.
   Since $q$ is surjective, the preimages cover $X$:
   $$
   X = q^{-1}(Y) = q^{-1}\left( \bigcup_{\alpha \in A} V_\alpha \right) = \bigcup_{\alpha \in A} q^{-1}(V_\alpha) = \bigcup_{\alpha \in A} U_\alpha.
   $$
   Thus, $\{U_\alpha\}_{\alpha \in A}$ is an open cover of the compact space $X$.

3. **Extracting a finite subcover:** Since $X$ is compact, there exists a finite subcover $\{U_{\alpha_1}, U_{\alpha_2}, \ldots, U_{\alpha_k}\}$ of $X$, so:
   $$
   X = \bigcup_{i=1}^k U_{\alpha_i} = \bigcup_{i=1}^k q^{-1}(V_{\alpha_i}).
   $$
   Applying the surjective map $q$ to both sides:
   $$
   Y = q(X) = q\left( \bigcup_{i=1}^k q^{-1}(V_{\alpha_i}) \right) = \bigcup_{i=1}^k q(q^{-1}(V_{\alpha_i})) = \bigcup_{i=1}^k V_{\alpha_i}.
   $$
   Thus, $\{V_{\alpha_1}, V_{\alpha_2}, \ldots, V_{\alpha_k}\}$ is a finite subcover of $Y$.

Therefore, the quotient space $Y$ is compact.
:::
