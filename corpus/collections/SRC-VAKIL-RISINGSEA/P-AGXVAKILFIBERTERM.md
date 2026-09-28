---
schema: qual/card@1
id: P-AGXVAKILFIBERTERM
kind: problem
title: The fiber product over a terminal object is the cartesian product
classification:
  areas:
  - algebraic-geometry
  topics:
  - Fiber Products
  - Universal Properties
  - Terminal Objects
relations: []
review: draft
---

::: {.problem}
Show that the fiber product over the terminal object is the cartesian product.
:::

::: {.solution}
- Recall the definition: $T$ is terminal iff every object $X$ admits a unique morphism $X\to T$.

- Strategy: use both universal properties to produce an isomorphism.

- Let ${\operatorname{pr}}_X, {\operatorname{pr}}_Y$ be the cartesian product projections, and ${\operatorname{pr}}_X^T, {\operatorname{pr}}_Y^T$ the fiber product projections.

- Let $T_X, T_Y$ be the maps $X\to T$ and $Y\to T$.

- Since $X\cross Y$ is an object of this category, it admits one unique map to $T$:

\begin{tikzcd}
	X\cross Y\ar[r, "{\operatorname{pr}}_Y"]\ar[d, "{\operatorname{pr}}_X"']\ar[dr, "T_{X\cross Y}"] & Y\ar[d, "T_Y"] \\
	X\ar[r, "T_X"'] & T
\end{tikzcd}

- But $T_Y \circ {\operatorname{pr}}_Y: X\cross Y \to T$ is another such map, so it must equal $T_{X\cross Y}$.

- Similarly $T_X \circ {\operatorname{pr}}_X$ equals $T_{X\cross Y}$.

- Thus $T_Y \circ {\operatorname{pr}}_Y = T_X \circ {\operatorname{pr}}_X$, which is part of the universal property for $\fiberprod{X}{T}{Y}$.

- By the universal property of $X\cross Y$, for every $W$ admitting maps to $X$ and $Y$ we get a unique $h_0$:

\begin{tikzcd}
	W \ar[drr, bend left]\ar[rdd, bend right]\ar[dr, dotted, "\exists ! h_0"] & & \\
	& X\cross Y\ar[r, "{\operatorname{pr}}_Y"]\ar[d, "{\operatorname{pr}}_X"] & Y\ar[d, "T_Y"] \\
	& X\ar[r, "T_X"] & T
\end{tikzcd}

> Note that $T$ does not matter in this particular diagram.

- This gives the left-hand diagram below; the right-hand one comes from the universal property of $X\cross Y$:

\begin{tikzcd}
	\fiberprod{X}{T}{Y}\ar[drr, "{\operatorname{pr}}_Y^T", bend left]\ar[rdd, "{\operatorname{pr}}_X^T", bend right]\ar[dr, dotted, "\exists ! h_0"] & & \\
	& X\cross Y\ar[r, "{\operatorname{pr}}_Y"]\ar[d, "{\operatorname{pr}}_X"] & Y\ar[d, "T_Y"] \\
	& X\ar[r, "T_X"] & T
\end{tikzcd}

\begin{tikzcd}
	X\cross Y\ar[drr, "{\operatorname{pr}}_Y", bend left]\ar[rdd, "{\operatorname{pr}}_X", bend right]\ar[dr, dotted, "\exists ! h_1"] & & \\
	& \fiberprod{X}{T}{Y}\ar[r, "{\operatorname{pr}}_Y^T"]\ar[d, "{\operatorname{pr}}_X^T"] & Y\ar[d, "T_Y"] \\
	& X\ar[r, "T_X"] & T
\end{tikzcd}

- By commutativity, $h_0 \circ h_1 = \id_{X\cross Y}$ and vice versa.
:::

::: {.remark}
Erratum: the last step asserts $h_0\circ h_1 = \id_{X\cross Y}$ "by commutativity", which is not enough.
Both $h_0\circ h_1$ and $\id_{X\cross Y}$ are maps $X\cross Y \to X\cross Y$ commuting with ${\operatorname{pr}}_X$ and ${\operatorname{pr}}_Y$, so they agree by the uniqueness clause of the universal property of $X\cross Y$.
Likewise $h_1 \circ h_0$ and $\id$ commute with ${\operatorname{pr}}_X^T$ and ${\operatorname{pr}}_Y^T$, so they agree by the uniqueness clause for $\fiberprod{X}{T}{Y}$.
:::
