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

::: solution
**Goal:** Prove that all discrete spaces are paracompact and show that continuous images of paracompact spaces need not be paracompact.

<1>1. Part (a): Discrete spaces are paracompact.
    *Proof:*
    <2>1. In the discrete topology on $X$, every singleton $\{x\}$ is open and closed, so $X$ is Hausdorff.
    <2>2. Let $\mathcal{U} = \{U_\alpha\}_{\alpha \in J}$ be an arbitrary open cover of $X$.
    <2>3. Consider the singleton collection $\mathcal{V} = \{\{x\} \mid x \in X\}$.
    <2>4. **Openness and Covering:** In the discrete topology, each $\{x\}$ is open, and $\bigcup_{x \in X} \{x\} = X$, so $\mathcal{V}$ is an open cover of $X$.
    <2>5. **Refinement:** For each $x \in X$, since $\mathcal{U}$ covers $X$, there exists an index $\alpha \in J$ such that $x \in U_\alpha$. Thus $\{x\} \subseteq U_\alpha$, so $\mathcal{V}$ refines $\mathcal{U}$.
    <2>6. **Local Finiteness:** For any point $p \in X$, the open neighborhood $W = \{p\}$ intersects only one member of $\mathcal{V}$ (namely $\{p\}$ itself).
    <2>7. Thus $\mathcal{V}$ is a locally finite open refinement of $\mathcal{U}$, proving $X$ is paracompact.

<1>2. Part (b): Continuous images of paracompact spaces need not be paracompact.
    *Proof:*
    <2>1. Let $Y = [0, \omega_1)$ be the space of countable ordinals equipped with the order topology.
    <2>2. The space $Y$ is Hausdorff and countably compact, but not compact (the open cover $\{[0, \alpha)\}_{\alpha < \omega_1}$ has no finite subcover).
    <2>3. Since every paracompact and countably compact Hausdorff space is compact, $Y$ is not paracompact.
    <2>4. Let $X = Y_d$ denote the set $[0, \omega_1)$ equipped with the discrete topology.
    <2>5. By <1>1, $X$ is paracompact.
    <2>6. The identity map $f: X \to Y$ defined by $f(x) = x$ is continuous because the domain $X$ is discrete, and $f(X) = Y$ is surjective.
    <2>7. Thus $f(X) = Y$ is a continuous image of the paracompact space $X$ that fails to be paracompact. Q.E.D.
:::
