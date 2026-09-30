---
schema: qual/card@1
id: E-3KMYL
kind: problem
title: Local compactness of products
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $\theset{X_\alpha}$ be an indexed family of nonempty spaces.

(a) Show that if $\prod X_\alpha$ is locally compact, then each $X_\alpha$ is locally compact and $X_\alpha$ is compact for all but finitely many values of $\alpha$.

(b) Prove the converse, assuming the Tychonoff theorem.
:::

::: {.solution}
**Goal:** Prove the necessary and sufficient conditions for the Cartesian product $\prod_{\alpha \in J} X_\alpha$ of non-empty topological spaces to be locally compact.

::: pf

::: pf-step
Part (a): Necessity.
If $X = \prod_{\alpha \in J} X_\alpha$ is locally compact, then each $X_\alpha$ is locally compact and all but finitely many $X_\alpha$ are compact.

::: pf-proof

::: pf-step
Let $\mathbf{x} = (x_\alpha)_{\alpha \in J} \in X$. Since $X$ is locally compact, $\mathbf{x}$ has a compact neighborhood $C \subseteq X$.
:::

::: pf-step
By definition of neighborhood, there exists an open set $U \subseteq X$ such that $\mathbf{x} \in U \subseteq C$.
:::

::: pf-step
In the product topology, $U$ contains a basic open set $V = \prod_{\alpha \in J} V_\alpha$ containing $\mathbf{x}$, where each $V_\alpha$ is open in $X_\alpha$ and $V_\alpha = X_\alpha$ for all $\alpha \in J \setminus F$, where $F \subset J$ is a finite subset.
:::

::: pf-step
For every index $\beta \in J$, the canonical coordinate projection $\pi_\beta: X \to X_\beta$ is continuous, open, and surjective.
:::

::: pf-step
The image $C_\beta := \pi_\beta(C)$ is a compact subset of $X_\beta$ because continuous maps preserve compactness.
:::

::: pf-step
Furthermore, $x_\beta \in V_\beta = \pi_\beta(V) \subseteq \pi_\beta(C) = C_\beta$, and $V_\beta$ is open in $X_\beta$, so $C_\beta$ is a compact neighborhood of $x_\beta$ in $X_\beta$.
:::

::: pf-step
Since $x_\beta$ was arbitrary, each space $X_\beta$ is locally compact.
:::

::: pf-step
For every index $\alpha \in J \setminus F$, $V_\alpha = X_\alpha$, which implies:
$$X_\alpha = V_\alpha = \pi_\alpha(V) \subseteq \pi_\alpha(C) \subseteq X_\alpha \implies X_\alpha = \pi_\alpha(C) = C_\alpha.$$
:::

::: pf-step
Thus $X_\alpha$ is compact for every $\alpha \in J \setminus F$, so all but finitely many $X_\alpha$ are compact.
:::

:::

:::

::: pf-step
Part (b): Sufficiency (Converse).
If each $X_\alpha$ is locally compact and $X_\alpha$ is compact for all $\alpha \notin \{\alpha_1, \dots, \alpha_n\}$, then $\prod_{\alpha \in J} X_\alpha$ is locally compact.

::: pf-proof

::: pf-step
Let $\mathbf{x} = (x_\alpha)_{\alpha \in J} \in X$.
:::

::: pf-step
For each $k \in \{1, \dots, n\}$, local compactness of $X_{\alpha_k}$ provides a compact neighborhood $C_{\alpha_k} \subseteq X_{\alpha_k}$ of $x_{\alpha_k}$, which contains an open neighborhood $U_{\alpha_k} \subseteq C_{\alpha_k}$ of $x_{\alpha_k}$.
:::

::: pf-step
For all indices $\alpha \notin \{\alpha_1, \dots, \alpha_n\}$, define $C_\alpha = X_\alpha$ and $U_\alpha = X_\alpha$. By hypothesis, each such $C_\alpha$ is compact and open in itself.
:::

::: pf-step
Define $C = \prod_{\alpha \in J} C_\alpha$ and $U = \prod_{\alpha \in J} U_\alpha$.
:::

::: pf-step
By the Tychonoff Theorem, the product of compact spaces $C$ is compact in $X$.
:::

::: pf-step
Since $U_\alpha = X_\alpha$ for all but finitely many $\alpha$, $U$ is a basic open set in the product topology on $X$, and $\mathbf{x} \in U \subseteq C$.
:::

::: pf-step
Thus $C$ is a compact neighborhood of $\mathbf{x}$ in $X$.
:::

::: pf-step
Therefore $X = \prod_{\alpha \in J} X_\alpha$ is locally compact. Q.E.D.
:::

:::

:::

:::

:::
