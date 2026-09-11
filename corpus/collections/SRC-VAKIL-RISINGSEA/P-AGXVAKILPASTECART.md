---
schema: qual/card@1
id: P-AGXVAKILPASTECART
kind: problem
title: Pasting two cartesian squares gives a cartesian outer square
classification:
  areas:
  - algebraic-geometry
  topics:
  - Fiber Products
  - Pasting Lemma
  - Universal Properties
relations: []
review: draft
---

::: problem
Show that if the two squares in this diagram are cartesian, then the outer square is also cartesian:

\begin{tikzcd}
	U \ar[r]\ar[d] & V\ar[d] \\
	W \ar[r]\ar[d] & X\ar[d] \\
	Y \ar[r] & Z
\end{tikzcd}
:::

::: solution
- We must show that given two maps $R\to V$ and $R\to Y$ such that $(V\to Z) \circ (R\to V) = (Y\to Z) \circ (R\to Y)$, there is a unique map $R\to U$ giving a commuting diagram:

\begin{tikzcd}
	U\ar[drr, bend left] \ar[rdd, bend right] & & \\
	& R\ar[ul, dotted, "\exists !\, ?"] \ar[r]\ar[d] & V\ar[d] \\
	& Y \ar[r] & Z
\end{tikzcd}

- Applying the bottom square:
  - We need maps $R\to X$ and $R\to Y$.
  - We are given a map $R\to Y$ by assumption.
  - We build a map $R\to X$ as $(V\to X) \circ (R\to V)$.
  - We then get a map $R\to W$:

\begin{tikzcd}
	W\ar[drr, bend left] \ar[rdd, bend right] & & \\
	& R\ar[ul, dotted, "\exists !"] \ar[r]\ar[d] & X\ar[d] \\
	& Y \ar[r] & Z
\end{tikzcd}

- Applying the top square:
  - We have a map $R\to V$ by assumption.
  - We have a map $R\to W$ from the previous step.
  - We have maps $V\to X$ and $W\to X$ from the top square.
  - We thus obtain

\begin{tikzcd}
	U\ar[drr, bend left] \ar[rdd, bend right] & & \\
	& R\ar[ul, dotted, "\exists !"] \ar[r]\ar[d] & V\ar[d] \\
	& W \ar[r] & X
\end{tikzcd}
:::
