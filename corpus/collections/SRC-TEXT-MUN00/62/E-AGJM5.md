---
schema: qual/card@1
id: E-AGJM5
kind: problem
title: Extension of homotopic maps into open euclidean sets
classification:
  areas:
  - topology
  topics:
  - Invariance of Domain
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $X$ be a space such that $X \times I$ is normal.
Let $A$ be a closed subspace of $X$; let $f: A \to Y$ be a continuous map, where $Y$ is an open subspace of $\mathbb{R}^n$.
If $f$ is homotopic to a map that is extendable to a continuous map $h: X \to Y$, then $f$ itself is extendable to a continuous map $g: X \to Y$, such that $g \simeq h$.
:::

::: {.solution}
**Goal:** Prove the Homotopy Extension Property for $(X, A)$ into an open set $Y \subseteq \mathbb{R}^n$ under the hypothesis that $X \times I$ is normal.

::: pf

::: pf-step
Setup of the cylinder extension problem:

::: pf-proof

::: pf-step
Let $H: A \times I \to Y$ be a homotopy with $H(a, 0) = f(a)$ and $H(a, 1) = h(a)$ for all $a \in A$.
:::

::: pf-step
Define the closed subspace $T \subset X \times I$:
$$T = (X \times \{1\}) \cup (A \times I).$$
:::

::: pf-step
Define $F: T \to Y \subseteq \mathbb{R}^n$ by:
$$F(x, 1) = h(x) \quad \text{for } x \in X,$$
$$F(a, t) = H(a, t) \quad \text{for } (a, t) \in A \times I.$$
:::

::: pf-step
On the intersection $(X \times \{1\}) \cap (A \times I) = A \times \{1\}$, $F(a, 1) = h(a) = H(a, 1)$, so $F$ is well-defined and continuous by the Pasting Lemma.
:::

:::

:::

::: pf-step
Extension into $\mathbb{R}^n$ via Tietze Extension Theorem:

::: pf-proof

::: pf-step
Since $X \times I$ is normal, $T$ is closed in $X \times I$, and each coordinate map of $F$ maps into $\mathbb{R}$, by the Tietze Extension Theorem there exists a continuous extension:
$$\widetilde{F}: X \times I \to \mathbb{R}^n \quad \text{such that } \widetilde{F}|_T = F.$$
:::

:::

:::

::: pf-step
Deformation into the open subset $Y$:

::: pf-proof

::: pf-step
Since $Y$ is open in $\mathbb{R}^n$, the preimage $U = \widetilde{F}^{-1}(Y)$ is an open subset of $X \times I$ containing $T$.
:::

::: pf-step
The disjoint closed sets $T$ and $(X \times I) \setminus U$ can be separated in the normal space $X \times I$.
:::

::: pf-step
By Urysohn's Lemma applied on slices (or Tube Lemma along the compact fibers), there exists a continuous function $\mu: X \to [0, 1]$ such that $\mu(A) = \{0\}$ and $\{ (x, t) \in X \times I \mid t \ge \mu(x) \} \subseteq U$.
:::

::: pf-step
Define $K: X \times I \to Y$ by:
$$K(x, t) = \widetilde{F}(x, \, (1-t)\mu(x) + t).$$
:::

::: pf-step
For every $(x, t) \in X \times I$, $(1-t)\mu(x) + t \ge \mu(x)$, so $(x, (1-t)\mu(x) + t) \in U$, meaning $K(x, t) \in Y$.
:::

::: pf-step
Thus $K: X \times I \to Y$ is continuous.
:::

:::

:::

::: pf-step
Verification of boundary values and extension:

::: pf-proof

::: pf-step
For $a \in A$, $\mu(a) = 0$, so $K(a, t) = \widetilde{F}(a, t) = H(a, t)$.
:::

::: pf-step
In particular, for $t = 0$ and $a \in A$:
$$K(a, 0) = H(a, 0) = f(a).$$
:::

::: pf-step
For $t = 1$ and all $x \in X$:
$$K(x, 1) = \widetilde{F}(x, 1) = h(x).$$
:::

::: pf-step
Define $g: X \to Y$ by $g(x) = K(x, 0)$.
:::

::: pf-step
Then $g$ is continuous, $g|_A = f$, and $K$ is a homotopy from $g$ to $h$ in $Y$.
:::

:::

:::

::: pf-step
Conclusion:
$f$ extends to a continuous map $g: X \to Y$ such that $g \simeq h$.
:::

:::
