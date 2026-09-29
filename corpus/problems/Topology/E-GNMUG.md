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
**Goal:** Show that if $f: X \to Y$ is continuous and $X$ is compact, then $f(X)$ is compact.

::: pf

::: {.pf-step #s1}

Let $\theset{U_\alpha}$ be an open cover of $f(X)$.

::: pf-proof

Arbitrary open cover in $Y$ (intersect with $f(X)$ if needed).

:::

:::

::: {.pf-step #s2}

$\theset{f^{-1}(U_\alpha)}$ is an open cover of $X$.

::: pf-proof

Each $f^{-1}(U_\alpha)$ is open (continuity), and for every $x \in X$, $f(x) \in U_\alpha$ for some $\alpha$, so $x \in f^{-1}(U_\alpha)$.

:::

:::

::: {.pf-step #s3}

There is a finite subcover $\theset{f^{-1}(U_{\alpha_1}), \ldots, f^{-1}(U_{\alpha_k})}$ of $X$.

::: pf-proof

$X$ is compact and step [](#s2){.pf-ref} gives an open cover.

:::

:::

::: {.pf-step #s4}

$\theset{U_{\alpha_1}, \ldots, U_{\alpha_k}}$ covers $f(X)$.

::: pf-proof

For $y \in f(X)$, $y = f(x)$ with $x \in f^{-1}(U_{\alpha_j})$ for some $j$ (step [](#s3){.pf-ref}); then $y = f(x) \in U_{\alpha_j}$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} show every open cover of $f(X)$ has a finite subcover, i.e. $f(X)$ is compact.

:::

:::

:::
