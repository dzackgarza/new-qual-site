---
schema: qual/card@1
id: E-4WKOG
kind: problem
title: Properly discontinuous actions with compactly supported interference
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

Prove the following.

Theorem.
Let $X$ be a locally compact Hausdorff space; let $G$ be a group of homeomorphisms of $X$ such that the action of $G$ is fixed-point free.
Suppose that for each compact subspace $C$ of $X$, there are only finitely many elements $g$ of $G$ such that the intersection $C \cap g(C)$ is nonempty.
Then the action of $G$ is properly discontinuous, and $X/G$ is locally compact Hausdorff.

(a) For each compact subspace $C$ of $X$, show that the union of the sets $g(C)$, for $g \in G$, is closed in $X$.
[Hint: If $U$ is a neighborhood of $x$ with $\overline{U}$ compact, then $\overline{U} \cup C$ intersects $g(\overline{U} \cup C)$ for only finitely many $g$.]

(b) Show that $X/G$ is Hausdorff.

(c) Show that the action of $G$ is properly discontinuous.

(d) Show that $X/G$ is locally compact.
:::

::: {.solution}
**Goal:** Prove that a free, properly discontinuous group action with compact interference on a locally compact Hausdorff space $X$ yields a properly discontinuous action and a locally compact Hausdorff quotient $X/G$.

::: pf

::: pf-step

Part (a): Orbit union $G \cdot C = \bigcup_{g \in G} g(C)$ is closed in $X$ for any compact $C \subseteq X$.
    *Proof:*

::: pf-proof

::: pf-step

Let $x \in X \setminus \bigcup_{g \in G} g(C)$.

:::

::: pf-step

Since $X$ is locally compact Hausdorff, choose an open neighborhood $U$ of $x$ whose closure $K = \overline{U}$ is compact.

:::

::: pf-step

The union $K' = K \cup C$ is compact, so by hypothesis the set $F = \{g \in G \mid K' \cap g(K') \neq \varnothing\}$ is finite.

:::

::: pf-step

For any $g \in G \setminus F$, $K \cap g(C) \subseteq K' \cap g(K') = \varnothing$, which implies $U \cap g(C) = \varnothing$.

:::

::: pf-step

For each $g \in F$, $x \notin g(C)$. Because $g(C)$ is compact and $X$ is Hausdorff, $g(C)$ is closed, so $X \setminus g(C)$ is open.

:::

::: pf-step

Define $V = U \cap \bigcap_{g \in F} (X \setminus g(C))$. Then $V$ is an open neighborhood of $x$.

:::

::: pf-step

For $g \in F$, $V \cap g(C) = \varnothing$ by construction; for $g \notin F$, $V \cap g(C) \subseteq U \cap g(C) = \varnothing$.

:::

::: pf-step

Thus $V \cap (\bigcup_{g \in G} g(C)) = \varnothing$, proving $X \setminus \bigcup_{g \in G} g(C)$ is open, so $\bigcup_{g \in G} g(C)$ is closed.

:::

:::

:::

::: pf-step

Part (b): $X/G$ is Hausdorff.
    *Proof:*

::: pf-proof

::: pf-step

The quotient map $p: X \to X/G$ is open because $p^{-1}(p(W)) = \bigcup_{g \in G} g(W)$ is open for every open $W \subseteq X$.

:::

::: pf-step

Let $p(x) \neq p(y)$ in $X/G$, so $G \cdot x \cap G \cdot y = \varnothing$.

:::

::: pf-step

Choose open neighborhoods $U_x$ of $x$ and $U_y$ of $y$ with compact closures $K_x = \overline{U_x}$ and $K_y = \overline{U_y}$.

:::

::: pf-step

The compact set $K = K_x \cup K_y$ has only finitely many $g \in G$ with $K \cap g(K) \neq \varnothing$.

:::

::: pf-step

Let $F = \{g \in G \mid K_x \cap g(K_y) \neq \varnothing\}$. For each $g \in F$, since $x \neq g(y)$, choose disjoint open sets $V_g \ni x$ and $W_g \ni g(y)$.

:::

::: pf-step

Setting $U = U_x \cap \bigcap_{g \in F} V_g$ and $V = U_y \cap \bigcap_{g \in F} g^{-1}(W_g)$ gives open neighborhoods of $x$ and $y$ such that $g(U) \cap V = \varnothing$ for all $g \in G$.

:::

::: pf-step

Then $p(U)$ and $p(V)$ are disjoint open neighborhoods of $p(x)$ and $p(y)$ in $X/G$. Thus $X/G$ is Hausdorff.

:::

:::

:::

::: pf-step

Part (c): The action of $G$ is properly discontinuous.
    *Proof:*

::: pf-proof

::: pf-step

Let $x \in X$. Choose an open neighborhood $U_0$ of $x$ with $C = \overline{U_0}$ compact.

:::

::: pf-step

The set $F = \{g \in G \setminus \{e\} \mid C \cap g(C) \neq \varnothing\}$ is finite.

:::

::: pf-step

For each $g \in F$, since the action is fixed-point free, $g(x) \neq x$.

:::

::: pf-step

By Hausdorffness, choose disjoint open neighborhoods $V_g \ni x$ and $W_g \ni g(x)$.

:::

::: pf-step

Define $U = U_0 \cap \bigcap_{g \in F} (V_g \cap g^{-1}(W_g))$.

:::

::: pf-step

For each $g \in F$, $g(U) \cap U \subseteq W_g \cap V_g = \varnothing$.

:::

::: pf-step

For each $g \in G \setminus (F \cup \{e\})$, $g(U) \cap U \subseteq g(C) \cap C = \varnothing$.

:::

::: pf-step

Thus $g(U) \cap U = \varnothing$ for all $g \neq e$, so the action is properly discontinuous.

:::

:::

:::

::: pf-step

Part (d): $X/G$ is locally compact.
    *Proof:*

::: pf-proof

::: pf-step

For any point $p(x) \in X/G$, choose a compact neighborhood $K \subseteq X$ containing an open neighborhood $W \subseteq K$ of $x$.

:::

::: pf-step

Since $p$ is continuous, $p(K)$ is compact in $X/G$.

:::

::: pf-step

Since $p$ is an open map, $p(W)$ is open in $X/G$, and $p(x) \in p(W) \subseteq p(K)$.

:::

::: pf-step

Thus $p(K)$ is a compact neighborhood of $p(x)$, so $X/G$ is locally compact. Q.E.D.

:::

:::

:::

:::

:::
