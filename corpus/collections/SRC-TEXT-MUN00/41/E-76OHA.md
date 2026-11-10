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
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    No complete published solution was located for this exercise, so the proof is checked line by line
    against the book and the search is recorded in the COMPLAINTS.md entry for §39--§42 of SRC-TEXT-MUN00.
    Searched: the sets listed in that entry --- Aleksey Zinger's MAT 530 sheets, the *Praying For Stockholm*
    posts, Moller's S38, the Riverside Math 205A solutions, Orellana, Doug's World, Whitman,
    "positron0802", "shenapse", "9beach", "kyp44", the seven further GitHub manuals, dbfin and Gardner's
    ETSU notes --- none of which solves this exercise.
    Checked against Munkres, Topology (2000), Section 41 Exercise 4, printed p. 260, with the discrete topology, the definition of paracompactness, and part (b) of Exercise 41.2 (card E-94C75) for the failure of paracompactness in the image. What was corrected: part (b) deduced the non-paracompactness of $S_\Omega=[0,\omega_1)$ from the general assertion that a paracompact countably compact Hausdorff space is compact, which the book does not prove and the card did not; the card now cites part (b) of Exercise 41.2, where the non-paracompactness of $S_\Omega$ is proved.
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
Let $Y = S_\Omega = [0, \Omega)$ be the space of countable ordinals with the order topology.
:::

::: pf-step
$Y$ is not paracompact: this is part (b) of Exercise 41.2, proved on the card of [[E-94C75]], where $S_\Omega$ is shown not to be paracompact by exhibiting $S_\Omega \times \overline{S}_\Omega$ as a non-normal product of a paracompact space with a compact one.
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
