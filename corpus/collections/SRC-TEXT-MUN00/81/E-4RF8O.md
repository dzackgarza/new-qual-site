---
schema: qual/card@1
id: E-4RF8O
kind: problem
title: Finite fixed-point-free actions are properly discontinuous
classification:
  areas:
  - topology
  topics:
  - Covering Transformations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $G$ be a group of homeomorphisms of $X$.
The action of $G$ on $X$ is said to be fixed-point free if no element of $G$ other than the identity $e$ has a fixed point.
Show that if $X$ is Hausdorff, and if $G$ is a finite group of homeomorphisms of $X$ whose action is fixed-point free, then the action of $G$ is properly discontinuous.
:::

::: {.solution}
**Goal:** Prove that every fixed-point free (free) action of a finite group $G$ of homeomorphisms on a Hausdorff space $X$ is properly discontinuous.

::: pf

::: pf-step

Definition of proper discontinuity:
    The action of $G$ on $X$ is properly discontinuous if for every point $x \in X$, there exists an open neighborhood $U \subseteq X$ of $x$ such that:
    $$g(U) \cap U = \varnothing \quad \text{for all } g \in G \setminus \{e\}.$$

:::

::: pf-step

Separation for individual group elements:
    For each $g \in G \setminus \{e\}$, there exists an open neighborhood $U_g \subseteq X$ of $x$ such that $g(U_g) \cap U_g = \varnothing$.
    *Proof:*

::: pf-proof

::: pf-step

Because the action is fixed-point free, $g(x) \neq x$.

:::

::: pf-step

Since $X$ is Hausdorff, there exist disjoint open sets $V_g, W_g \subseteq X$ such that $x \in V_g$, $g(x) \in W_g$, and $V_g \cap W_g = \varnothing$.

:::

::: pf-step

Since $g: X \to X$ is continuous and $g(x) \in W_g$, the preimage $g^{-1}(W_g)$ is an open neighborhood of $x$.

:::

::: pf-step

Define $U_g = V_g \cap g^{-1}(W_g)$. Then $U_g$ is an open neighborhood of $x$.

:::

::: pf-step

If $y \in U_g$, then $y \in V_g$ and $g(y) \in W_g$.

:::

::: pf-step

Since $V_g \cap W_g = \varnothing$, $g(y) \notin V_g$, which implies $g(y) \notin U_g$.

:::

::: pf-step

Thus $g(U_g) \cap U_g = \varnothing$.

:::

:::

:::

::: pf-step

Construction of the simultaneous neighborhood:
    *Proof:*

::: pf-proof

::: pf-step

Write $G \setminus \{e\} = \{g_1, \dots, g_n\}$. Since $G$ is finite, this is a finite set of elements.

:::

::: pf-step

Define $U = \bigcap_{i=1}^n U_{g_i}$.

:::

::: pf-step

As a finite intersection of open neighborhoods containing $x$, $U$ is an open neighborhood of $x$ in $X$.

:::

::: pf-step

For every $g_k \in G \setminus \{e\}$, since $U \subseteq U_{g_k}$:
        $$g_k(U) \cap U \subseteq g_k(U_{g_k}) \cap U_{g_k} = \varnothing.$$

:::

::: pf-step

Therefore, $g(U) \cap U = \varnothing$ for all $g \neq e$.

:::

:::

:::

::: pf-step

Conclusion:

:::

:::

    The action of $G$ on $X$ is properly discontinuous. Q.E.D.
:::
