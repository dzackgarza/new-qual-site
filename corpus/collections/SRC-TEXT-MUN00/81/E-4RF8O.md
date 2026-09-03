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

::: solution
**Goal:** Prove that every fixed-point free (free) action of a finite group $G$ of homeomorphisms on a Hausdorff space $X$ is properly discontinuous.

<1>1. Definition of proper discontinuity:
    The action of $G$ on $X$ is properly discontinuous if for every point $x \in X$, there exists an open neighborhood $U \subseteq X$ of $x$ such that:
    $$g(U) \cap U = \varnothing \quad \text{for all } g \in G \setminus \{e\}.$$

<1>2. Separation for individual group elements:
    For each $g \in G \setminus \{e\}$, there exists an open neighborhood $U_g \subseteq X$ of $x$ such that $g(U_g) \cap U_g = \varnothing$.
    *Proof:*
    <2>1. Because the action is fixed-point free, $g(x) \neq x$.
    <2>2. Since $X$ is Hausdorff, there exist disjoint open sets $V_g, W_g \subseteq X$ such that $x \in V_g$, $g(x) \in W_g$, and $V_g \cap W_g = \varnothing$.
    <2>3. Since $g: X \to X$ is continuous and $g(x) \in W_g$, the preimage $g^{-1}(W_g)$ is an open neighborhood of $x$.
    <2>4. Define $U_g = V_g \cap g^{-1}(W_g)$. Then $U_g$ is an open neighborhood of $x$.
    <2>5. If $y \in U_g$, then $y \in V_g$ and $g(y) \in W_g$.
    <2>6. Since $V_g \cap W_g = \varnothing$, $g(y) \notin V_g$, which implies $g(y) \notin U_g$.
    <2>7. Thus $g(U_g) \cap U_g = \varnothing$.

<1>3. Construction of the simultaneous neighborhood:
    *Proof:*
    <2>1. Write $G \setminus \{e\} = \{g_1, \dots, g_n\}$. Since $G$ is finite, this is a finite set of elements.
    <2>2. Define $U = \bigcap_{i=1}^n U_{g_i}$.
    <2>3. As a finite intersection of open neighborhoods containing $x$, $U$ is an open neighborhood of $x$ in $X$.
    <2>4. For every $g_k \in G \setminus \{e\}$, since $U \subseteq U_{g_k}$:
        $$g_k(U) \cap U \subseteq g_k(U_{g_k}) \cap U_{g_k} = \varnothing.$$
    <2>5. Therefore, $g(U) \cap U = \varnothing$ for all $g \neq e$.

<1>4. Conclusion:
    The action of $G$ on $X$ is properly discontinuous. Q.E.D.
:::
