---
schema: qual/card@1
id: E-HAT-4.2-8
kind: problem
title: "Suspension of acyclic CW complex is contractible"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.problem}
Show the suspension of an acyclic CW complex is contractible.
:::

::: {.solution}
**Goal:** Show the suspension $\Sigma X$ is contractible when $X$ is acyclic.

::: pf

::: pf-step

Use reduced homology of suspension.

::: pf-proof

::: pf-step

For reduced homology of a suspension, $\widetilde H_n(\Sigma X)\cong \widetilde H_{n-1}(X)$ for $n\ge2$.

:::

::: pf-step

Since $X$ is acyclic, $\widetilde H_{n-1}(X)=0$ for all $n-1\ge0$, so $\widetilde H_n(\Sigma X)=0$ for all $n\ge2$.

:::

::: pf-step

The space $\Sigma X$ is nonempty and connected, hence $\widetilde H_0(\Sigma X)=0$.

:::

::: pf-step

Therefore $\widetilde H_n(\Sigma X)=0$ for every $n\ge0$.

:::

:::

:::

::: pf-step

$\Sigma X$ is simply connected.

::: pf-proof

::: pf-step

The suspension $\Sigma X = CX \cup_{X} CX$ is path-connected: any two points lie in one of the two cones, and each cone is path-connected (every point is connected to the cone vertex by a straight line).

:::

::: pf-step

Let $\gamma \colon S^1 \to \Sigma X$ be a loop. The image $\gamma(S^1)$ is compact, so the open cover $\{\mathring{C}_+, \mathring{C}_-\}$ of $\Sigma X$ by the interiors of the two cones has a finite subcover.

:::

::: pf-step

Break $\gamma$ into finitely many arcs, each lying in one cone. Since each cone $C_\pm$ is contractible (it deformation-retracts onto its vertex), any arc in $C_\pm$ is null-homotopic relative to its endpoints.

:::

::: pf-step

Concatenating these null-homotopies (along the finitely many junction points) gives a null-homotopy of $\gamma$ in $\Sigma X$.

:::

::: pf-step

Hence $\pi_1(\Sigma X) = 1$.

:::

:::

:::

::: pf-step

Apply Whitehead’s theorem for CW complexes.

::: pf-proof

::: pf-step

$\Sigma X$ is a CW complex (suspension of a CW complex).

:::

::: pf-step

A simply connected CW complex with all reduced homology zero is contractible.

:::

::: pf-step

Therefore $\Sigma X$ is contractible.

:::

:::

:::

:::

:::
