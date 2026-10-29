---
schema: qual/card@1
id: E-MGS22
kind: problem
title: The continuous image of a compact space is compact
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Continuity
relations: []
review: draft
---

::: {.problem}
Let $f : X \to Y$ be a continuous function, with $X$ compact.
Show that $f(X)$ is compact.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Let $\theset{U_\alpha}$ be a cover of $f(X)$ by open subsets of $Y$. Then $\theset{\inverseof{f}(U_\alpha)}$ is an open cover of $X$.

::: pf-proof

Each $\inverseof{f}(U_\alpha)$ is open by continuity. For $x\in X$, the point $f(x)\in f(X)$ lies in some $U_\alpha$, so $x\in \inverseof{f}(U_\alpha)$.

:::

:::

::: pf-step

$f(X)$ is compact.

::: pf-proof

By compactness of $X$, the cover of step [](#s1){.pf-ref} has a finite subcover $\inverseof{f}(U_{\alpha_1}), \ldots, \inverseof{f}(U_{\alpha_N})$. If $y = f(x)\in f(X)$, then $x\in \inverseof{f}(U_{\alpha_j})$ for some $j$, so $y\in U_{\alpha_j}$. Thus $U_{\alpha_1}, \ldots, U_{\alpha_N}$ cover $f(X)$.

:::

:::

:::

:::
