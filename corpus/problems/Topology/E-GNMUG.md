---
schema: qual/card@1
id: E-GNMUG
kind: exercise
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

::: exercise
Show that if $f:X\to Y$ is continuous and $X$ is compact then $f(X)$ is compact.
:::

::: {.solution}
**Goal:** Show that if $f: X \to Y$ is continuous and $X$ is compact, then $f(X)$ is compact.

<1>1. Let $\theset{U_\alpha}$ be an open cover of $f(X)$.
::: {.proof}
Arbitrary open cover in $Y$ (intersect with $f(X)$ if needed).
:::

<1>2. $\theset{f^{-1}(U_\alpha)}$ is an open cover of $X$.
::: {.proof}
Each $f^{-1}(U_\alpha)$ is open (continuity), and for every $x \in X$, $f(x) \in U_\alpha$ for some $\alpha$, so $x \in f^{-1}(U_\alpha)$.
:::

<1>3. There is a finite subcover $\theset{f^{-1}(U_{\alpha_1}), \ldots, f^{-1}(U_{\alpha_k})}$ of $X$.
::: {.proof}
$X$ is compact and <1>2 gives an open cover.
:::

<1>4. $\theset{U_{\alpha_1}, \ldots, U_{\alpha_k}}$ covers $f(X)$.
::: {.proof}
For $y \in f(X)$, $y = f(x)$ with $x \in f^{-1}(U_{\alpha_j})$ for some $j$ (<1>3); then $y = f(x) \in U_{\alpha_j}$.
:::

<1>5. Q.E.D.
::: {.proof}
<1>1--<1>4 show every open cover of $f(X)$ has a finite subcover, i.e. $f(X)$ is compact.
:::
:::
