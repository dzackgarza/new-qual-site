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
Let $X$ be an acyclic CW complex, so $\widetilde H_n(X) = 0$ for all $n$. Write $\Sigma X = X \times I / {\sim}$, with $X \times \{0\}$ and $X \times \{1\}$ each collapsed to a point.

::: pf

::: {.pf-step #homology}
$\widetilde H_n(\Sigma X) = 0$ for every $n \ge 0$.

::: pf-proof

::: pf-step
$\widetilde H_n(\Sigma X) \cong \widetilde H_{n-1}(X) = 0$ for $n \ge 1$.

::: pf-proof
This is the suspension isomorphism for reduced homology, which holds for all $n \ge 1$.
:::

:::

::: pf-step
$\widetilde H_0(\Sigma X) = 0$.

::: pf-proof
Every point of $\Sigma X$ is joined by a path to a cone point, and the two cone points are joined through any point of $X$; $X$ is nonempty because $\widetilde H_0$ of the empty space is $\ZZ$ in degree $-1$, which acyclicity excludes. So $\Sigma X$ is path-connected.
:::

:::

:::

:::

::: {.pf-step #pi1}
$\pi_1(\Sigma X) = 1$.

::: pf-proof

::: pf-step
$U = X \times [0, 2/3) / {\sim}$ and $V = X \times (1/3, 1] / {\sim}$ are open, contractible, and cover $\Sigma X$.

::: pf-proof
Each is an open cone on $X$, which deformation retracts to its cone point.
:::

:::

::: pf-step
$U \cap V = X \times (1/3, 2/3)$ is path-connected.

::: pf-proof
$U \cap V \simeq X$, and $\widetilde H_0(X) = 0$ says $X$ is path-connected.
:::

:::

::: pf-step
$\pi_1(\Sigma X) = 1$.

::: pf-proof
By van Kampen, $\pi_1(\Sigma X)$ is a quotient of $\pi_1(U) * \pi_1(V) = 1$.
:::

:::

:::

:::

::: pf-step
$\Sigma X$ is contractible.

::: pf-proof
$\Sigma X$ is a CW complex. By step [](#pi1){.pf-ref} it is simply connected, and by step [](#homology){.pf-ref} it has trivial reduced homology. By the Hurewicz theorem, $\pi_n(\Sigma X) = 0$ for all $n$, so the map $\Sigma X \to \mathrm{pt}$ is a weak homotopy equivalence. By Whitehead's theorem, it is a homotopy equivalence.
:::

:::

:::

:::
