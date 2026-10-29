---
schema: qual/card@1
id: E-GNMUG
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
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
Show that if $f:X\to Y$ is continuous and $X$ is compact then $f(X)$ is compact.
:::

::: {.solution}
Let $\theset{U_\alpha}$ be a family of open subsets of $Y$ whose union contains $f(X)$.

::: pf

::: {.pf-step #s2}

$\theset{f^{-1}(U_\alpha)}$ is an open cover of $X$.

::: pf-proof

Each $f^{-1}(U_\alpha)$ is open by continuity, and for every $x \in X$, $f(x) \in U_\alpha$ for some $\alpha$, so $x \in f^{-1}(U_\alpha)$.

:::

:::

::: pf-qed

By compactness of $X$ and step [](#s2){.pf-ref}, finitely many $f^{-1}(U_{\alpha_1}), \ldots, f^{-1}(U_{\alpha_k})$ cover $X$. For $y=f(x)\in f(X)$, choose $j$ with $x\in f^{-1}(U_{\alpha_j})$; then $y\in U_{\alpha_j}$. So $U_{\alpha_1},\ldots,U_{\alpha_k}$ cover $f(X)$, and $f(X)$ is compact.

:::

:::

:::
