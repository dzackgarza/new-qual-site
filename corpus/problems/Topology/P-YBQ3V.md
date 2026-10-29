---
schema: qual/card@1
id: P-YBQ3V
kind: problem
title: When compact sets are closed, and $\overline{A\times B}=\overline{A}\times\overline{B}$
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
  - Homeomorphisms
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: "Part (d) was an image of the source text, which opens with the locator '(May 2016)'; it is transcribed from that image, without the locator."
---

::: {.problem}
(a) What property on a space guarantees that compact sets are closed?

(b) What property on a space guarantees that closed sets are compact?

(c) Show that a continuous bijection from a compact space to a Hausdorff space is necessarily a homeomorphism.

(d) Given any topological space $Z$ and subset $D \subseteq Z$, let $\operatorname{Cl}_Z(D)$ denote the closure of $D$ in $Z$. Show that if $X$ and $Y$ are topological spaces and $A \subseteq X$, $B \subseteq Y$, then $\operatorname{Cl}_{X\times Y}(A \times B) = \operatorname{Cl}_X(A) \times \operatorname{Cl}_Y(B)$.
:::

::: {.solution}

::: pf

::: pf-step

(a) In a Hausdorff space every compact subset is closed.

::: pf-proof

For a compact $K$ and $x\notin K$, separate $x$ from each point of $K$ and use compactness to obtain one neighborhood of $x$ disjoint from $K$.

:::

:::

::: pf-step

(b) In a compact space every closed subset is compact.

::: pf-proof

If $F$ is closed and $\mathcal U$ covers $F$, then $\mathcal U\cup\{X\setminus F\}$ covers $X$; a finite subcover restricts to one of $F$.

:::

:::

::: pf-step

(c) A continuous bijection $f:X\to Y$ from compact $X$ to Hausdorff $Y$ is a homeomorphism.

::: pf-proof

For closed $F\subseteq X$, $F$ is compact, so $f(F)$ is compact and therefore closed in $Y$. Thus $f$ is a closed bijection, hence $f^{-1}$ is continuous.

:::

:::

::: pf-step

(d) For arbitrary subsets $A\subseteq X$ and $B\subseteq Y$, $\operatorname{Cl}_{X\times Y}(A\times B)=\operatorname{Cl}_X(A)\times\operatorname{Cl}_Y(B)$.

::: pf-proof

If $(x,y)$ is in the left closure, continuity of the projections, which map the closure of a set into the closure of its image, gives $x\in\operatorname{Cl}_X(A)$ and $y\in\operatorname{Cl}_Y(B)$. Conversely, if $x\in\operatorname{Cl}_X(A)$ and $y\in\operatorname{Cl}_Y(B)$, every basic neighborhood $U\times V$ of $(x,y)$ meets $A\times B$ because $U\cap A$ and $V\cap B$ are both nonempty.

:::

:::

:::

:::
