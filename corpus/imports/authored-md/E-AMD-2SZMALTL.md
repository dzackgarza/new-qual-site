---
schema: qual/card@1
id: E-AMD-2SZMALTL
kind: exercise
title: Finite $p$-groups are nilpotent
classification:
  areas:
  - algebra
  topics:
  - p-groups
  - nilpotent-groups
relations: []
review: draft
solved: true
---

::: {.exercise}
Show that every finite $p\dash$group is nilpotent.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

Let $G$ be a finite $p$-group of order $|G| = p^n$ where $n \geq 1$.
We proceed by induction on $n$.

1. **Lemma (Non-triviality of the center of a finite $p$-group):** Consider the class equation for $G$:
   $$
   |G| = |Z(G)| + \sum_{i=1}^k [G : C_G(x_i)],
   $$
   where $x_1, \ldots, x_k$ are representatives of the conjugacy classes of size strictly greater than 1.

   - For each $i$, $[G : C_G(x_i)] > 1$ divides $|G| = p^n$, so $p$ divides $[G : C_G(x_i)]$.

   - Since $p$ divides $|G|$ and $p$ divides every term in the sum $\sum_{i=1}^k [G : C_G(x_i)]$, it follows that $p$ must divide $|Z(G)|$.

   - Since $e \in Z(G)$, $|Z(G)| \geq 1$.
     Because $p \mid |Z(G)|$, we have:
     $$
     |Z(G)| \geq p > 1.
     $$
   Thus the center $Z(G)$ is non-trivial.

2. **Induction Step using the Upper Central Series:** Define the upper central series $\{Z_i(G)\}$ of $G$ inductively by:
   $$
   Z_0(G) = 1, \qquad Z_1(G) = Z(G), \qquad Z_{i+1}(G) / Z_i(G) = Z(G / Z_i(G)).
   $$

   - **Base Case:** For $|G| = p^1$, $G \cong \ZZ_p$ is abelian, so $Z_1(G) = Z(G) = G$, and $G$ is nilpotent of class 1.

   - **Inductive Step:** Assume that all $p$-groups of order $p^k$ (with $k < n$) are nilpotent.
     Since $|Z(G)| \geq p$, the quotient group $\bar{G} = G / Z(G)$ is a $p$-group of strictly smaller order:
     $$
     |\bar{G}| = \frac{|G|}{|Z(G)|} \leq p^{n-1}.
     $$
     By the induction hypothesis, $\bar{G} = G / Z_1(G)$ is nilpotent.
     Therefore, the upper central series of $\bar{G}$ reaches $\bar{G}$ in finitely many steps, say $c$ steps:
     $$
     Z_c(G / Z_1(G)) = G / Z_1(G).
     $$
     By the correspondence theorem for the upper central series, this implies:
     $$
     Z_{c+1}(G) = G.
     $$

Hence, the upper central series of $G$ terminates at $G$ in at most $n$ steps ($Z_n(G) = G$). Therefore, every finite $p$-group is nilpotent.
:::
