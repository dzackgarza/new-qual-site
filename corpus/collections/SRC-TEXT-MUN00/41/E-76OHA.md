---
schema: qual/card@1
id: E-76OHA
kind: problem
title: Discrete spaces are paracompact; images need not be
classification:
  areas:
  - topology
  topics:
  - Paracompactness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

(a) Show that if $X$ has the discrete topology, then $X$ is paracompact.

(b) Show that if $f: X \to Y$ is continuous and $X$ is paracompact, the subspace $f(X)$ of $Y$ need not be paracompact.
:::

::: {.solution}

::: pf

::: {.pf-step #discrete-spaces-paracompact}
Part (a): Discrete spaces are paracompact.

::: pf-proof

::: pf-step
In the discrete topology on $X$, every singleton $\{x\}$ is open and closed, so $X$ is Hausdorff.
:::

::: pf-step
Let $\mathcal{U} = \{U_\alpha\}_{\alpha \in J}$ be an arbitrary open cover of $X$.
:::

::: pf-step
Consider the singleton collection $\mathcal{V} = \{\{x\} \mid x \in X\}$.
:::

::: pf-step
In the discrete topology, each $\{x\}$ is open, and $\bigcup_{x \in X} \{x\} = X$, so $\mathcal{V}$ is an open cover of $X$.
:::

::: pf-step
For each $x \in X$, since $\mathcal{U}$ covers $X$, there exists an index $\alpha \in J$ such that $x \in U_\alpha$. Thus $\{x\} \subseteq U_\alpha$, so $\mathcal{V}$ refines $\mathcal{U}$.
:::

::: pf-step
For any point $p \in X$, the open neighborhood $W = \{p\}$ intersects only one member of $\mathcal{V}$ (namely $\{p\}$ itself).
:::

::: pf-step
Thus $\mathcal{V}$ is a locally finite open refinement of $\mathcal{U}$, proving $X$ is paracompact.
:::

:::

:::

::: pf-step
Part (b): Continuous images of paracompact spaces need not be paracompact.

::: pf-proof

::: pf-step
Let $Y = [0, \omega_1)$ be the space of countable ordinals equipped with the order topology.
:::

::: pf-step
The space $Y$ is Hausdorff and countably compact, but not compact (the open cover $\{[0, \alpha)\}_{\alpha < \omega_1}$ has no finite subcover).
:::

::: pf-step
Since every paracompact and countably compact Hausdorff space is compact, $Y$ is not paracompact.
:::

::: pf-step
Let $X = Y_d$ denote the set $[0, \omega_1)$ equipped with the discrete topology.
:::

::: pf-step
By step [](#discrete-spaces-paracompact){.pf-ref}, $X$ is paracompact.
:::

::: pf-step
The identity map $f: X \to Y$ defined by $f(x) = x$ is continuous because the domain $X$ is discrete, and $f(X) = Y$ is surjective.
:::

::: pf-step
Thus $f(X) = Y$ is a continuous image of the paracompact space $X$ that fails to be paracompact. Q.E.D.
:::

:::

:::

:::

:::
