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
Choose $a_0\in A$ and $\widetilde a_0\in\widetilde A$ above it. Write $i:A\hookrightarrow X$ for inclusion.

::: pf

::: pf-step
The restriction $p:\widetilde A\to A$ is a connected covering space.

::: pf-proof
By [[E-HAT-1.3-1|Exercise 1.3.1]], $p:p^{-1}(A)\to A$ is a covering. For $a\in A$, choose an evenly covered neighborhood that is path connected, using local path connectedness of $A$. Each sheet over this neighborhood is path connected. It is therefore either contained in the path component $\widetilde A$ or disjoint from it. The sheets contained in $\widetilde A$ evenly cover the neighborhood for the restricted map. Every $a\in A$ has a lift in $\widetilde A$: lift a path in $A$ from $a_0$ to $a$ starting at $\widetilde a_0$. Thus the restriction is a connected covering of all of $A$.
:::

:::

::: pf-step
The subgroup of $\pi_1(A,a_0)$ corresponding to this cover is contained in $\ker i_*$.

::: pf-proof
A loop in $\widetilde A$ maps to a loop in $\widetilde X$. Since $\widetilde X$ is simply connected, its image under $p$ is nullhomotopic in $X$. Hence $i_*p_*\pi_1(\widetilde A,\widetilde a_0)=1$.
:::

:::

::: pf-step
The subgroup $\ker i_*$ is contained in $p_*\pi_1(\widetilde A,\widetilde a_0)$.

::: pf-proof
Let $\gamma$ be a loop in $A$ based at $a_0$ whose class is trivial in $\pi_1(X,a_0)$. Lift it through $p:\widetilde X\to X$ starting at $\widetilde a_0$. A nullhomotopic loop has a closed lift, by homotopy lifting. The lifted loop lies in $p^{-1}(A)$ and begins in $\widetilde A$, so its whole image lies in $\widetilde A$. Its class maps to $[\gamma]$.
:::

:::

::: pf-step
The covering $p:\widetilde A\to A$ corresponds to $\ker i_*$.

::: pf-proof
The two inclusions above give $p_*\pi_1(\widetilde A,\widetilde a_0)=\ker i_*$. This image is the subgroup assigned to the connected based covering.
:::

:::

:::

:::
