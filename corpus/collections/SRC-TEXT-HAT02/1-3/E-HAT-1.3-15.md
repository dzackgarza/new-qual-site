---
schema: qual/card@1
id: E-HAT-1.3-15
kind: problem
title: Universal cover restricted to a subspace
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $p: \tilde{X} \to X$ be a simply-connected covering space of $X$ and let $A \subset X$ be a path-connected, locally path-connected subspace, with $\tilde{A} \subset \tilde{X}$ a path-component of $p^{-1}(A)$.
Show that $p: \tilde{A} \to A$ is the covering space corresponding to the kernel of the map $\pi_1(A) \to \pi_1(X)$.
:::

::: {.solution}

::: pf

::: pf-step

$p: \tilde A \to A$ is a covering space.

::: pf-proof

the restriction of a covering map to a path-component of the preimage of a subspace is a covering map.

:::

:::

::: {.pf-step #s2}

The covering $p: \tilde A \to A$ corresponds to the subgroup $p_*(\pi_1(\tilde A)) \le \pi_1(A)$.

::: pf-proof

the fundamental theorem of covering spaces: a covering corresponds to the image of the fundamental group of the total space.

:::

:::

::: {.pf-step #s3}

$p_*(\pi_1(\tilde A)) = \ker(\pi_1(A) \to \pi_1(X))$.

::: pf-proof

::: {.pf-step #s3-1}

$p_*(\pi_1(\tilde A)) \subseteq \ker(\pi_1(A) \to \pi_1(X))$.

::: pf-proof

the composition $\pi_1(\tilde A) \xrightarrow{p_*} \pi_1(A) \to \pi_1(X)$ factors through $\pi_1(\tilde X) = 0$ (since $\tilde A \subseteq \tilde X$ and $\tilde X$ is simply connected), so its image is trivial.

:::

:::

::: {.pf-step #s3-2}

$\ker(\pi_1(A) \to \pi_1(X)) \subseteq p_*(\pi_1(\tilde A))$.

::: pf-proof

a loop $\gamma$ in $A$ whose image in $\pi_1(X)$ is trivial lifts to a loop in $\tilde X$; since $\gamma$ is based in $A$ and its lift starts in $\tilde A$, the lift lies entirely in $\tilde A$ (a path-component of $p^{-1}(A)$), so $\gamma$ is the image of a loop in $\tilde A$, i.e. $\gamma \in p_*(\pi_1(\tilde A))$.

:::

:::

::: pf-step

Hence equality holds.

::: pf-proof

Steps [](#s3-1){.pf-ref} and [](#s3-2){.pf-ref}.

:::

:::

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::
