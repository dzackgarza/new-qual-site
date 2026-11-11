---
schema: qual/card@1
id: E-J8QUX
kind: problem
title: Two-dimensional CW complexes with finitely many cells are metrizable
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Metrization
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Munkres §73 Exercise 4, printed p. 445. No complete published solution located; the searches are listed in
    the COMPLAINTS.md entry for §61--§73 of SRC-TEXT-MUN00. The hint's perfect map
    is used in the form "a closed surjection with compact fibres from a second-countable space has a
    second-countable image", which is proved on the card: the countable family got by pushing a countable base
    through the closed map. Metrizability then follows from Theorem 34.1 (printed p. 215), the space being
    compact Hausdorff hence regular. Checked against Exercise 2 of this section (printed p. 445) for
    compactness and Hausdorffness.
---

::: {.exercise}

Show that the space constructed in [[E-VYYH3]] is in fact metrizable.
[Hint: The quotient map is a perfect map.]
:::

::: {.solution}

Let $E=A\sqcup B_1\sqcup\cdots\sqcup B_m$ and $q:E\to X$ be as in the construction of Exercise 2, and let $d$ be a metric for $E$, which is compact metrizable.

::: pf

::: pf-step

$q$ is a closed map with compact fibres.

::: pf-proof

Closedness is step 1 of Exercise 2's card (the saturation of a closed set is closed, since $S^1$ is compact). The fibre $q^{-1}(x)$ is a closed subset of the compact space $E$, hence compact (Theorem 26.2, printed p. 165). So $q$ is perfect.

:::

:::

::: pf-step

$E$ is second-countable and $X$ has a countable base.

::: pf-proof

$E$ is the topological sum of the second-countable spaces $A$ (a compact subspace of $\RR^2$, and $\RR^2$ is second-countable by Example 1, printed p. 190, with Theorem 30.2, printed p. 191) and the finitely many disks $B_i$ (subspaces of $\RR^2$); a finite sum of second-countable spaces is second-countable. Let $\mathcal{B}$ be a countable base for $E$. Claim: the countable family $\mathcal{C}=\theset{X\setminus q(E\setminus U):U\in\mathcal{B}}$ is a base for $X$. Let $x\in W$ with $W$ open in $X$; the compact set $F=q^{-1}(x)$ is contained in the open set $q^{-1}(W)$, so finitely many $U_1,\dots,U_r\in\mathcal{B}$ cover $F$ with $\bigcup U_i\subseteq q^{-1}(W)$. Put $U=\bigcup U_i$; then $x\in X\setminus q(E\setminus U)$ and $X\setminus q(E\setminus U)\subseteq W$: indeed $U\subseteq q^{-1}(W)$ gives $E\setminus U\supseteq E\setminus q^{-1}(W)$, hence $q(E\setminus U)\supseteq X\setminus W$.

:::

:::

::: pf-step

$X$ is metrizable.

::: pf-proof

$X$ is compact Hausdorff by Exercise 2(a), hence normal (Theorem 32.3, printed p. 202) and so regular (the definition, printed p. 195, gives regularity from normality). With the countable base of step 2, Theorem 34.1 (printed p. 215) gives a metric for $X$.

:::

:::

::: pf-qed

$X$ is a compact Hausdorff space with a countable base, hence metrizable.

:::

:::
:::
