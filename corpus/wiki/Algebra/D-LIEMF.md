---
schema: qual/card@1
id: D-LIEMF
kind: definition
title: Free Module
classification:
  areas:
  - algebra
  topics:
  - Free Modules
  - Modules
  - Bases
relations: []
review: draft
---

::: {.definition}
A **free** module $M$ is a module satisfying any of the following conditions:

- A universal property: There is a set \( \mathcal{B}  \) and a set map \( M \mapsvia{\iota} \mathcal{B}  \) such that every set map \( \mathcal{B} \mapsvia{N} \) lifts:

\begin{tikzcd}
	M \\
	\\
	{\mathcal{B}} && N
	\arrow["f", from=3-1, to=3-3]
	\arrow["{\tilde f}", dashed, from=1-1, to=3-3]
	\arrow["\iota", hook, from=3-1, to=1-1]
\end{tikzcd}

> [Link to Diagram](https://q.uiver.app/?q=WzAsMyxbMCwyLCJcXG1hdGhjYWx7Qn0iXSxbMCwwLCJNIl0sWzIsMiwiTiJdLFswLDIsImYiXSxbMSwyLCJcXHRpbGRlIGYiLDAseyJzdHlsZSI6eyJib2R5Ijp7Im5hbWUiOiJkYXNoZWQifX19XSxbMCwxLCJcXGlvdGEiLDAseyJzdHlsZSI6eyJ0YWlsIjp7Im5hbWUiOiJob29rIiwic2lkZSI6InRvcCJ9fX1dXQ==)

- Existence of a basis:

  There is linearly independent (so $\sum r_i \beta_i = 0 \implies r_i = 0$) spanning set (so \( m\in M \implies m = \sum r_i \beta_i \) ) of the form \( \mathcal{B} \da \ts{ \beta_i }_{i\in I} \),

- Direct sum decomposition:

  $M$ decomposes as $M \cong \bigoplus_{i\in I} \beta_i R$, a sum of cyclic submodules.
:::
