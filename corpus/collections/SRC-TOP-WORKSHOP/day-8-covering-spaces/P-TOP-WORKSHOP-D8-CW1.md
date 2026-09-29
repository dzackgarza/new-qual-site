---
schema: qual/card@1
id: P-TOP-WORKSHOP-D8-CW1
kind: problem
title: The real line is the universal cover of the circle
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Explicitly prove that $\mathbb R$ is that universal cover of $S^1$.
:::

::: {.solution}
View $S^1$ as $\{z \in \mathbb{C} : |z| = 1\}$ and let $p\colon \mathbb{R} \to S^1$, $p(t) = e^{2\pi i t}$. The map $p$ is continuous and surjective, and $p(t) = p(s)$ if and only if $t - s \in \mathbb{Z}$.

::: pf

::: {.pf-step #s1}

Every $z_0 \in S^1$ has an evenly covered open neighborhood.

::: pf-proof

Write $z_0 = e^{2\pi i t_0}$ and let $U = S^1 \setminus \{-z_0\} = \{e^{2\pi i t} : t_0 - \tfrac12 < t < t_0 + \tfrac12\}$, an open arc. Then
$$
p^{-1}(U) = \bigsqcup_{k \in \mathbb{Z}} V_k,
\qquad
V_k = \left(t_0 - \tfrac{1}{2} + k,\ t_0 + \tfrac{1}{2} + k\right),
$$
because $p(t) = -z_0$ exactly when $t \in t_0 + \tfrac12 + \mathbb{Z}$; the $V_k$ are pairwise disjoint open intervals. Let $\operatorname{Arg}\colon \mathbb{C} \setminus (-\infty, 0] \to (-\pi, \pi)$ be the principal argument, which is continuous. For $z \in U$, $z e^{-2\pi i t_0} \neq -1$, so
$$
\sigma_k(z) = t_0 + k + \frac{1}{2\pi} \operatorname{Arg}\left(z e^{-2\pi i t_0}\right)
$$
is a continuous map $U \to V_k$ with $p \circ \sigma_k = \operatorname{id}_U$ and $\sigma_k \circ p|_{V_k} = \operatorname{id}_{V_k}$. Hence each $p|_{V_k}\colon V_k \to U$ is a homeomorphism.

:::

:::

::: {.pf-step #s2}

$\mathbb{R}$ is simply connected.

::: pf-proof

$H(t, s) = (1 - s)t$ is a homotopy from $\operatorname{id}_{\mathbb{R}}$ to the constant map $0$, so $\mathbb{R}$ is contractible, hence path-connected with $\pi_1(\mathbb{R}, 0) = 0$.

:::

:::

::: pf-qed

By step [](#s1){.pf-ref}, $p$ is a covering map. By step [](#s2){.pf-ref}, its total space is simply connected, and $S^1$ is connected and locally path-connected, so $p$ is the universal cover of $S^1$, unique up to isomorphism of covering spaces.

:::

:::

:::
