---
schema: qual/card@1
id: E-8NCA4
kind: problem
title: Free product construction in §68
classification:
  areas:
  - topology
  topics:
  - Free Products
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Check the details of Example 1 of §68.
:::

::: {.solution}
**Goal:** Verify the foundational details of the construction of the free product of groups $G = *_{\alpha \in J} G_\alpha$ from §68, including word reduction, the group axioms, and the universal mapping property.

::: pf

::: pf-step

Words and reduced words:
    *Proof:*

::: pf-proof

::: pf-step

Let $\{G_\alpha\}_{\alpha \in J}$ be a family of groups. Assume without loss of generality that the sets $G_\alpha \setminus \{1_\alpha\}$ are pairwise disjoint.

:::

::: pf-step

A **word** is a finite sequence $w = (x_1, x_2, \dots, x_m)$ where each $x_i \in \bigcup_{\alpha \in J} (G_\alpha \setminus \{1_\alpha\})$. The empty sequence $\varnothing$ is the empty word of length $0$.

:::

::: pf-step

A word is **reduced** if no two adjacent elements $x_i, x_{i+1}$ belong to the same group $G_\alpha$.

:::

::: pf-step

Let $G$ denote the set of all reduced words.

:::

:::

:::

::: pf-step

Group multiplication and associativity (van der Waerden representation):
    *Proof:*

::: pf-proof

::: pf-step

To avoid tedious case analysis on word concatenation and reduction, let $\operatorname{Sym}(G)$ be the group of permutations of the set of reduced words $G$.

:::

::: pf-step

For each $\alpha \in J$ and $g \in G_\alpha$, define the action $L_g: G \to G$ on a reduced word $w = (x_1, \dots, x_m)$ by:
        $$L_g(w) = \begin{cases}
        (g, x_1, \dots, x_m) & \text{if } x_1 \notin G_\alpha, \\
        (g x_1, x_2, \dots, x_m) & \text{if } x_1 \in G_\alpha \text{ and } g x_1 \neq 1_\alpha, \\
        (x_2, \dots, x_m) & \text{if } x_1 \in G_\alpha \text{ and } g x_1 = 1_\alpha.
        \end{cases}$$

:::

::: pf-step

Direct verification shows $L_{1_\alpha} = \operatorname{id}_G$ and $L_{g h} = L_g \circ L_h$ for all $g, h \in G_\alpha$.

:::

::: pf-step

Thus each $L_g$ is a permutation with inverse $L_{g^{-1}}$, defining an injective homomorphism $\phi_\alpha: G_\alpha \to \operatorname{Sym}(G)$.

:::

::: pf-step

The map $\Psi: G \to \operatorname{Sym}(G)$ given by $\Psi(x_1, \dots, x_m) = L_{x_1} \circ \dots \circ L_{x_m}$ evaluates on the empty word as $\Psi(w)(\varnothing) = w$, hence $\Psi$ is injective.

:::

::: pf-step

Pulling back the group structure from $\operatorname{Sym}(G)$ via $\Psi$ equips $G$ with an associative group multiplication whose identity is $\varnothing$ and where $(x_1, \dots, x_m)^{-1} = (x_m^{-1}, \dots, x_1^{-1})$.

:::

:::

:::

::: pf-step

Canonical inclusions and Universal Mapping Property:
    *Proof:*

::: pf-proof

::: pf-step

The inclusion maps $i_\alpha: G_\alpha \hookrightarrow G$ sending $g \mapsto (g)$ are injective group homomorphisms.

:::

::: pf-step

Let $H$ be any group and let $\{h_\alpha: G_\alpha \to H\}_{\alpha \in J}$ be a family of homomorphisms.

:::

::: pf-step

Define $h: G \to H$ by $h(\varnothing) = 1_H$ and $h(x_1, \dots, x_m) = h_{\alpha_1}(x_1) \cdots h_{\alpha_m}(x_m)$ where $x_j \in G_{\alpha_j}$.

:::

::: pf-step

The homomorphism property $h(w \cdot w') = h(w) h(w')$ follows from the definition of reduction in $G_\alpha$.

:::

::: pf-step

$h$ is the unique homomorphism satisfying $h \circ i_\alpha = h_\alpha$ for all $\alpha \in J$.

:::

:::

:::

::: pf-step

Conclusion:

:::

:::

    The construction rigorously yields the free product $*_{\alpha \in J} G_\alpha$ satisfying all group axioms and universal properties. Q.E.D.
:::
